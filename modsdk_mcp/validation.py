# -*- coding: utf-8 -*-
"""ModSDK 生成物的统一、可扩展校验管线。"""

from __future__ import annotations

import ast
import io
import json
import re
import tokenize
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, FrozenSet, Iterable, List, Mapping, Optional, Sequence, Tuple, Union


from .standards import get_version_profile


CURRENT_TARGET_VERSION = get_version_profile()["version"]
SEVERITY_CRITICAL = "critical"
SEVERITY_ERROR = "error"
SEVERITY_WARNING = "warning"
SEVERITY_INFO = "info"


# 仓库内官方快照不可用时使用的后备子集。ModSDK 路径也必须精确匹配。
DEFAULT_IMPORT_WHITELIST: FrozenSet[str] = frozenset({
    "__future__",
    "_md5",
    "_random",
    "abc",
    "ast",
    "base64",
    "binascii",
    "bisect",
    "builtin_modules._inspect",
    "builtin_modules._operator",
    "calendar",
    "collections",
    "contextlib",
    "copy",
    "cStringIO",
    "datetime",
    "fnmatch",
    "functools",
    "gzip",
    "hashlib",
    "heapq",
    "io",
    "itertools",
    "json",
    "keyword",
    "logging",
    "math",
    "mod.builtin_modules._inspect",
    "mod.builtin_modules._operator",
    "mod.client.extraClientApi",
    "mod.common.mod",
    "mod.server.extraServerApi",
    "mod_log",
    "posixpath",
    "Queue",
    "random",
    "re",
    "singleton",
    "string",
    "struct",
    "threading",
    "time",
    "traceback",
    "types",
    "uuid",
    "warnings",
    "weakref",
    "zlib",
})


BLOCK_FORMAT_PROFILES: Mapping[str, str] = {
    "legacy_1_10": "1.10.0",
    "scalar_1_16": "1.16.0",
    "modern_1_19_20": "1.19.20",
}


# 这里只收录文档能够明确判定的字段错配，不猜测自定义事件载荷。
EVENT_FIELD_CORRECTIONS: Mapping[str, Mapping[str, str]] = {
    "AddServerPlayerEvent": {"playerId": "id"},
    "DelServerPlayerEvent": {"playerId": "id"},
    "ServerItemUseOnEvent": {"playerId": "entityId", "cancel": "ret"},
    "PlayerDieEvent": {"playerId": "id"},
    "EntityDeathEvent": {"entityId": "id", "playerId": "id"},
    "ClientItemUseOnEvent": {"entityId": "playerId", "cancel": "ret"},
}


TextValue = Union[str, bytes]


@dataclass(frozen=True)
class Artifact:
    """待校验生成物及其显式上下文。"""

    content: TextValue
    filename: str = "unknown"
    artifact_type: str = "auto"
    side: str = "auto"
    target_version: str = "current"
    format_profile: Optional[str] = None
    project_modules: Tuple[str, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "project_modules", tuple(self.project_modules or ()))

    @property
    def kind(self) -> str:
        artifact_type = (self.artifact_type or "auto").lower()
        if artifact_type in {"python", "py"}:
            return "python"
        if artifact_type in {"json", "json_ui", "item", "block"}:
            return "json"
        if artifact_type != "auto":
            return artifact_type
        lowered = self.filename.lower()
        if lowered.endswith((".py", ".pyw")):
            return "python"
        if lowered.endswith(".json"):
            return "json"
        return "text"


@dataclass(frozen=True)
class ValidationIssue:
    """单条可定位、可序列化的校验结论。"""

    code: str
    message: str
    filename: str
    line: int = 1
    column: int = 1
    severity: str = SEVERITY_CRITICAL
    detector: str = ""
    suggestion: str = ""
    details: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result = {
            "code": self.code,
            "severity": self.severity,
            "message": self.message,
            "filename": self.filename,
            "line": self.line,
            "column": self.column,
            "detector": self.detector,
        }
        if self.suggestion:
            result["suggestion"] = self.suggestion
        if self.details:
            result["details"] = dict(self.details)
        return result


@dataclass(frozen=True)
class ValidationReport:
    """统一校验报告；error/critical 会阻断生成物交付。"""

    artifacts: Tuple[Artifact, ...]
    issues: Tuple[ValidationIssue, ...] = ()

    @property
    def blocked(self) -> bool:
        return any(issue.severity in {SEVERITY_ERROR, SEVERITY_CRITICAL} for issue in self.issues)

    @property
    def has_warnings(self) -> bool:
        return any(issue.severity == SEVERITY_WARNING for issue in self.issues)

    @property
    def errors(self) -> Tuple[ValidationIssue, ...]:
        return tuple(issue for issue in self.issues if issue.severity in {SEVERITY_ERROR, SEVERITY_CRITICAL})

    @property
    def warnings(self) -> Tuple[ValidationIssue, ...]:
        return tuple(issue for issue in self.issues if issue.severity == SEVERITY_WARNING)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "blocked": self.blocked,
            "has_warnings": self.has_warnings,
            "artifact_count": len(self.artifacts),
            "issue_count": len(self.issues),
            "artifacts": [
                {
                    "filename": artifact.filename,
                    "artifact_type": artifact.artifact_type,
                    "kind": artifact.kind,
                }
                for artifact in self.artifacts
            ],
            "issues": [issue.to_dict() for issue in self.issues],
        }


@dataclass(frozen=True)
class _ImportRef:
    module: str
    line: int
    column: int


@dataclass
class _PythonAnalysis:
    text: str
    lines: List[str]
    tokens: List[tokenize.TokenInfo]
    tree: Optional[ast.AST]
    imports: List[_ImportRef]
    token_error: Optional[BaseException] = None
    tokenized_until: Tuple[int, int] = (0, 0)


@dataclass
class ValidationContext:
    """Detector 共享上下文和解析缓存。"""

    whitelist: FrozenSet[str] = DEFAULT_IMPORT_WHITELIST
    _text_cache: Dict[int, str] = field(default_factory=dict)
    _python_cache: Dict[int, _PythonAnalysis] = field(default_factory=dict)
    _json_cache: Dict[int, Any] = field(default_factory=dict)

    def text(self, artifact: Artifact) -> str:
        key = id(artifact)
        if key not in self._text_cache:
            content = artifact.content
            if isinstance(content, bytes):
                encoding = "utf-8-sig" if content.startswith(b"\xef\xbb\xbf") else "utf-8"
                self._text_cache[key] = content.decode(encoding)
            else:
                self._text_cache[key] = content.lstrip("\ufeff")
        return self._text_cache[key]

    def python(self, artifact: Artifact) -> _PythonAnalysis:
        key = id(artifact)
        if key not in self._python_cache:
            self._python_cache[key] = _analyze_python(self.text(artifact), artifact.filename)
        return self._python_cache[key]

    def json_value(self, artifact: Artifact) -> Any:
        key = id(artifact)
        if key not in self._json_cache:
            text = self.text(artifact)

            def reject_constant(value: str) -> None:
                position = text.find(value)
                raise json.JSONDecodeError("JSON 不允许非标准数值 {}".format(value), text, max(0, position))

            self._json_cache[key] = json.loads(text, parse_constant=reject_constant)
        return self._json_cache[key]


Detector = Callable[[Artifact, ValidationContext], Iterable[ValidationIssue]]


@dataclass(frozen=True)
class DetectorSpec:
    name: str
    artifact_types: Tuple[str, ...]
    detector: Detector


DETECTOR_REGISTRY: "OrderedDict[str, DetectorSpec]" = OrderedDict()


def register_detector(name: str, artifact_types: Sequence[str]) -> Callable[[Detector], Detector]:
    """注册 detector；名称重复时立即失败，避免规则被静默覆盖。"""

    def decorator(detector: Detector) -> Detector:
        if name in DETECTOR_REGISTRY:
            raise ValueError("detector already registered: {}".format(name))
        DETECTOR_REGISTRY[name] = DetectorSpec(name, tuple(artifact_types), detector)
        return detector

    return decorator


def get_registered_detectors() -> Tuple[DetectorSpec, ...]:
    return tuple(DETECTOR_REGISTRY.values())


def _issue(
    artifact: Artifact,
    code: str,
    message: str,
    detector: str,
    line: int = 1,
    column: int = 1,
    severity: str = SEVERITY_CRITICAL,
    suggestion: str = "",
    details: Optional[Mapping[str, Any]] = None,
) -> ValidationIssue:
    return ValidationIssue(
        code=code,
        message=message,
        filename=artifact.filename,
        line=max(1, int(line or 1)),
        column=max(1, int(column or 1)),
        severity=severity,
        detector=detector,
        suggestion=suggestion,
        details=details or {},
    )


def _analyze_python(text: str, filename: str) -> _PythonAnalysis:
    tokens: List[tokenize.TokenInfo] = []
    token_error: Optional[BaseException] = None
    token_text = re.sub(
        r"(?i)(?<![A-Za-z0-9_])(?:ur|ru)(?='''|\"\"\"|'|\")",
        lambda match: " " * len(match.group(0)),
        text,
    )
    generator = tokenize.generate_tokens(io.StringIO(token_text).readline)
    try:
        while True:
            tokens.append(next(generator))
    except StopIteration:
        pass
    except (IndentationError, tokenize.TokenError) as exc:
        token_error = exc

    tree: Optional[ast.AST]
    try:
        tree = ast.parse(text, filename=filename)
    except (SyntaxError, ValueError, TypeError):
        try:
            tree = ast.parse(_normalize_python2_print_statements(text, tokens), filename=filename)
        except (SyntaxError, ValueError, TypeError):
            # Python 3 的 ast 无法解析全部 Python 2 合法源码，不能据此误报。
            tree = None

    imports = _imports_from_ast(tree) if tree is not None else _imports_from_tokens(tokens)
    tokenized_until = tokens[-1].end if tokens else (0, 0)
    return _PythonAnalysis(text, text.splitlines(), tokens, tree, imports, token_error, tokenized_until)


def _normalize_python2_print_statements(text: str, tokens: Sequence[tokenize.TokenInfo]) -> str:
    """仅为结构分析改写 Python 2 print 语句，不改变对外源码和定位。"""

    line_offsets = [0]
    for match in re.finditer(r"\n", text):
        line_offsets.append(match.end())

    def absolute(position: Tuple[int, int]) -> int:
        line, column = position
        return line_offsets[min(max(line - 1, 0), len(line_offsets) - 1)] + column

    ignored = {tokenize.COMMENT, tokenize.NL}
    significant_indexes = [index for index, token in enumerate(tokens) if token.type not in ignored]
    replacements: List[Tuple[int, int, str]] = []
    for position, token_index in enumerate(significant_indexes):
        token = tokens[token_index]
        if token.type != tokenize.NAME or token.string != "print":
            continue
        previous = tokens[significant_indexes[position - 1]] if position else None
        following = tokens[significant_indexes[position + 1]] if position + 1 < len(significant_indexes) else None
        if following is not None and following.string == "(":
            continue
        if previous is not None and previous.type not in {
            tokenize.NEWLINE,
            tokenize.INDENT,
            tokenize.DEDENT,
        } and previous.string not in {":", ";"}:
            continue

        depth = 0
        end_index = len(text)
        redirect = False
        for candidate in tokens[token_index + 1:]:
            if candidate.type == tokenize.COMMENT and depth == 0:
                end_index = absolute(candidate.start)
                break
            if candidate.type in {tokenize.NEWLINE, tokenize.ENDMARKER} and depth == 0:
                end_index = absolute(candidate.start)
                break
            if candidate.type == tokenize.OP:
                if candidate.string in {"(", "[", "{"}:
                    depth += 1
                elif candidate.string in {")", "]", "}"}:
                    depth = max(0, depth - 1)
                elif candidate.string == ";" and depth == 0:
                    end_index = absolute(candidate.start)
                    break
                elif candidate.string == ">>" and depth == 0:
                    redirect = True

        start_index = absolute(token.start)
        if redirect:
            replacements.append((start_index, end_index, "pass"))
        else:
            replacements.append((absolute(token.end), absolute(token.end), "("))
            replacements.append((end_index, end_index, ")"))

    normalized = text
    for start, end, replacement in sorted(replacements, reverse=True):
        normalized = normalized[:start] + replacement + normalized[end:]
    return normalized


def _imports_from_ast(tree: ast.AST) -> List[_ImportRef]:
    imports: List[_ImportRef] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(_ImportRef(alias.name, node.lineno, node.col_offset + 1))
        elif isinstance(node, ast.ImportFrom):
            prefix = "." * int(node.level or 0)
            imports.append(_ImportRef(prefix + (node.module or ""), node.lineno, node.col_offset + 1))
    return imports


def _imports_from_tokens(tokens: Sequence[tokenize.TokenInfo]) -> List[_ImportRef]:
    imports: List[_ImportRef] = []
    statement: List[tokenize.TokenInfo] = []

    def flush(parts: Sequence[tokenize.TokenInfo]) -> None:
        segments: List[List[tokenize.TokenInfo]] = [[]]
        for token in parts:
            if token.type == tokenize.OP and token.string == ";":
                segments.append([])
            else:
                segments[-1].append(token)
        for segment in segments:
            significant = [
                token for token in segment
                if token.type not in {tokenize.INDENT, tokenize.DEDENT, tokenize.NL, tokenize.COMMENT}
            ]
            if not significant:
                continue
            words = [token.string for token in significant]
            if "from" in words and "import" in words:
                start = words.index("from") + 1
                end = words.index("import", start)
                module_tokens = significant[start:end]
                module = "".join(
                    token.string for token in module_tokens
                    if token.type == tokenize.NAME or token.string == "."
                )
                if module:
                    imports.append(_ImportRef(module, module_tokens[0].start[0], module_tokens[0].start[1] + 1))
                continue
            if "import" not in words:
                continue
            start = words.index("import") + 1
            clauses: List[List[tokenize.TokenInfo]] = [[]]
            for token in significant[start:]:
                if token.string == ",":
                    clauses.append([])
                else:
                    clauses[-1].append(token)
            for clause in clauses:
                alias_index = next(
                    (index for index, token in enumerate(clause) if token.string == "as"),
                    len(clause),
                )
                module_tokens = clause[:alias_index]
                module = "".join(
                    token.string for token in module_tokens
                    if token.type == tokenize.NAME or token.string == "."
                )
                if module and module_tokens:
                    imports.append(_ImportRef(module, module_tokens[0].start[0], module_tokens[0].start[1] + 1))

    for token in tokens:
        if token.type in {tokenize.NEWLINE, tokenize.ENDMARKER}:
            flush(statement)
            statement = []
        else:
            statement.append(token)
    return imports


def _token_contains(token: tokenize.TokenInfo, line: int, column: int) -> bool:
    start_line, start_col = token.start
    end_line, end_col = token.end
    if line < start_line or line > end_line:
        return False
    if start_line == end_line:
        return start_col <= column < end_col
    if line == start_line:
        return column >= start_col
    if line == end_line:
        return column < end_col
    return True


def _literal_prefix_occurrences(
    analysis: _PythonAnalysis,
    prefixes: Sequence[str],
) -> List[Tuple[str, int, int]]:
    prefix_pattern = "|".join(re.escape(prefix) for prefix in sorted(prefixes, key=len, reverse=True))
    pattern = re.compile(
        r"(?i)(?<![A-Za-z0-9_])(?P<prefix>{})(?P<quote>'''|\"\"\"|'|\")".format(prefix_pattern)
    )
    ignored_types = {tokenize.COMMENT, tokenize.STRING}
    fstring_middle = getattr(tokenize, "FSTRING_MIDDLE", None)
    fstring_end = getattr(tokenize, "FSTRING_END", None)
    ignored_types.update(token_type for token_type in (fstring_middle, fstring_end) if token_type is not None)
    occurrences: List[Tuple[str, int, int]] = []
    for line_number, line in enumerate(analysis.text.splitlines(), 1):
        for match in pattern.finditer(line):
            column = match.start("prefix")
            if analysis.token_error is not None and (line_number, column) >= analysis.tokenized_until:
                continue
            ignored = False
            for token in analysis.tokens:
                if token.type not in ignored_types or not _token_contains(token, line_number, column):
                    continue
                if token.type == tokenize.STRING and token.start == (line_number, column):
                    continue
                ignored = True
                break
            if not ignored:
                occurrences.append((match.group("prefix"), line_number, column + 1))
    return occurrences


def _dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = _dotted_name(node.value)
        return "{}.{}".format(parent, node.attr) if parent else node.attr
    return ""


def _constant_string(node: Optional[ast.AST]) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _module_is_allowed(module: str, whitelist: FrozenSet[str], project_modules: Sequence[str]) -> bool:
    if module.startswith("."):
        return True
    if module in whitelist:
        return True
    return any(module == project or module.startswith(project + ".") for project in project_modules if project)


def _infer_side(artifact: Artifact, imports: Sequence[_ImportRef], tree: Optional[ast.AST]) -> str:
    requested = (artifact.side or "auto").lower()
    if requested in {"server", "client", "common", "cross_side"}:
        return requested

    lowered = artifact.filename.replace("\\", "/").lower()
    has_server_name = re.search(r"(^|[/_.-])server([/_.-]|$)", lowered) is not None or "serversystem" in lowered
    has_client_name = re.search(r"(^|[/_.-])client([/_.-]|$)", lowered) is not None or "clientsystem" in lowered
    if has_server_name != has_client_name:
        return "server" if has_server_name else "client"

    has_server_import = any(ref.module.startswith("mod.server.") for ref in imports)
    has_client_import = any(ref.module.startswith("mod.client.") for ref in imports)
    if has_server_import != has_client_import:
        return "server" if has_server_import else "client"

    if tree is not None:
        names = {_dotted_name(node.func) for node in ast.walk(tree) if isinstance(node, ast.Call)}
        has_server_base = any(name.endswith("GetServerSystemCls") for name in names)
        has_client_base = any(name.endswith("GetClientSystemCls") for name in names)
        if has_server_base != has_client_base:
            return "server" if has_server_base else "client"
    return "auto"


def _version_tuple(version: str) -> Tuple[int, ...]:
    value = CURRENT_TARGET_VERSION if not version or version == "current" else str(version)
    numbers = re.findall(r"\d+", value)
    return tuple(int(number) for number in numbers) if numbers else ()


def _json_location(text: str, key: str, value: Optional[str] = None) -> Tuple[int, int]:
    key_pattern = re.escape(json.dumps(key, ensure_ascii=False))
    pattern = key_pattern
    if value is not None:
        pattern += r"\s*:\s*" + re.escape(json.dumps(value, ensure_ascii=False))
    match = re.search(pattern, text)
    if not match:
        return 1, 1
    line = text.count("\n", 0, match.start()) + 1
    last_newline = text.rfind("\n", 0, match.start())
    return line, match.start() - last_newline


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


@register_detector("python.encoding", ("python",))
def _detect_python_encoding(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    text = context.text(artifact)
    cookie = re.compile(r"^[ \t\f]*\#.*?coding[:=][ \t]*([-_.A-Za-z0-9]+)")
    encoding: Optional[str] = None
    encoding_line = 1
    for index, line in enumerate(text.splitlines()[:2], 1):
        match = cookie.match(line)
        if match:
            encoding = match.group(1)
            encoding_line = index
            break
    if encoding is None:
        return [
            _issue(
                artifact,
                "PY_ENCODING_MISSING",
                "Python 2.7 源文件前两行缺少 UTF-8 编码声明",
                "python.encoding",
                suggestion="# -*- coding: utf-8 -*-",
            )
        ]
    normalized = encoding.lower().replace("_", "-")
    if normalized not in {"utf-8", "utf8"}:
        return [
            _issue(
                artifact,
                "PY_ENCODING_NOT_UTF8",
                "Python 源文件编码声明不是 UTF-8：{}".format(encoding),
                "python.encoding",
                line=encoding_line,
                suggestion="统一使用 # -*- coding: utf-8 -*-",
            )
        ]
    return []


@register_detector("python.tokenize", ("python",))
def _detect_python_tokenize_error(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    analysis = context.python(artifact)
    if analysis.token_error is None:
        return []
    error = analysis.token_error
    line = getattr(error, "lineno", None)
    offset = getattr(error, "offset", None)
    if isinstance(line, int):
        column = offset if isinstance(offset, int) else 1
    else:
        line = 1
        column = 1
        location = getattr(error, "args", (None, (1, 0)))
        if len(location) > 1 and isinstance(location[1], tuple):
            position = location[1]
            if len(position) >= 2 and all(isinstance(value, int) for value in position[:2]):
                line = position[0] or 1
                column = (position[1] or 0) + 1
    return [
        _issue(
            artifact,
            "PY_TOKENIZE_ERROR",
            "Python 源码无法完成词法分析：{}".format(error),
            "python.tokenize",
            line=line,
            column=column,
        )
    ]


@register_detector("python.unicode_prefix", ("python",))
def _detect_unicode_prefix(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    analysis = context.python(artifact)
    return [
        _issue(
            artifact,
            "PY_UNICODE_PREFIX",
            "字符串字面量使用了禁止的 {} 前缀".format(prefix),
            "python.unicode_prefix",
            line=line,
            column=column,
            suggestion="移除 u/U/ur/ru 前缀并保持源文件为 UTF-8",
            details={"prefix": prefix},
        )
        for prefix, line, column in _literal_prefix_occurrences(analysis, ("ur", "ru", "u"))
    ]


@register_detector("python.python3_syntax", ("python",))
def _detect_python3_syntax(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    analysis = context.python(artifact)
    issues: List[ValidationIssue] = []
    seen: set = set()

    def add(code: str, message: str, line: int, column: int, suggestion: str = "") -> None:
        key = (code, line, column)
        if key in seen:
            return
        seen.add(key)
        issues.append(_issue(
            artifact,
            code,
            message,
            "python.python3_syntax",
            line=line,
            column=column,
            suggestion=suggestion,
        ))

    for _, line, column in _literal_prefix_occurrences(analysis, ("rf", "fr", "f")):
        add("PY3_FSTRING", "使用了 Python 3 专属 f-string", line, column, "改用 .format() 或 % 格式化")

    for token in analysis.tokens:
        if token.type == tokenize.OP and token.string == ":=":
            add("PY3_WALRUS", "使用了 Python 3.8 专属海象运算符", token.start[0], token.start[1] + 1)
        elif token.type == tokenize.NUMBER and "_" in token.string:
            add("PY3_NUMERIC_SEPARATOR", "数字字面量使用了 Python 3 数字分隔符", token.start[0], token.start[1] + 1)

    semantic_tokens = [
        token for token in analysis.tokens
        if token.type not in {
            tokenize.COMMENT,
            tokenize.NL,
            tokenize.NEWLINE,
            tokenize.INDENT,
            tokenize.DEDENT,
            tokenize.ENDMARKER,
        }
    ]
    for index, token in enumerate(semantic_tokens):
        following = semantic_tokens[index + 1:index + 3]
        if token.string == "except" and following and following[0].string == "*":
            add("PY3_EXCEPTION_GROUP", "使用了 Python 3.11 专属 except*", token.start[0], token.start[1] + 1)
        if (
            token.type == tokenize.NAME
            and token.string == "type"
            and len(following) == 2
            and following[0].type == tokenize.NAME
            and following[1].string == "="
        ):
            add("PY3_TYPE_ALIAS", "使用了 Python 3.12 专属 type 类型别名", token.start[0], token.start[1] + 1)
        if (
            token.string in {"def", "class"}
            and len(following) == 2
            and following[0].type == tokenize.NAME
            and following[1].string == "["
        ):
            add("PY3_TYPE_PARAMETERS", "使用了 Python 3.12 专属泛型类型参数", token.start[0], token.start[1] + 1)

    tree = analysis.tree
    if tree is None:
        significant = [token for token in analysis.tokens if token.type not in {tokenize.COMMENT, tokenize.NL}]
        for index, token in enumerate(significant):
            previous_word = significant[index - 1].string if index > 0 else ""
            next_word = significant[index + 1].string if index + 1 < len(significant) else ""
            if token.type == tokenize.NAME and token.string == "async":
                if next_word in {"def", "for", "with"}:
                    add("PY3_ASYNC", "使用了 Python 3 专属 async 语法", token.start[0], token.start[1] + 1)
            if token.type == tokenize.NAME and token.string == "nonlocal":
                if previous_word != "." and index + 1 < len(significant) and significant[index + 1].type == tokenize.NAME:
                    add("PY3_NONLOCAL", "使用了 Python 3 专属 nonlocal", token.start[0], token.start[1] + 1)
            if token.type == tokenize.OP and token.string == "->":
                add("PY3_TYPE_ANNOTATION", "函数使用了 Python 3 类型注解", token.start[0], token.start[1] + 1)
        return issues

    for node in ast.walk(tree):
        line = getattr(node, "lineno", 1)
        column = getattr(node, "col_offset", 0) + 1
        if isinstance(node, ast.JoinedStr):
            add("PY3_FSTRING", "使用了 Python 3 专属 f-string", line, column, "改用 .format() 或 % 格式化")
        elif isinstance(node, (ast.AsyncFunctionDef, ast.AsyncFor, ast.AsyncWith)):
            add("PY3_ASYNC", "使用了 Python 3 专属 async 语法", line, column)
        elif isinstance(node, ast.Await):
            add("PY3_AWAIT", "使用了 Python 3 专属 await", line, column)
        elif isinstance(node, ast.comprehension) and node.is_async:
            add("PY3_ASYNC", "推导式使用了 Python 3 专属 async for", line, column)
        elif isinstance(node, ast.AnnAssign):
            add("PY3_TYPE_ANNOTATION", "变量使用了 Python 3 类型注解", line, column)
        elif isinstance(node, ast.NamedExpr):
            add("PY3_WALRUS", "使用了 Python 3.8 专属海象运算符", line, column)
        elif isinstance(node, ast.Nonlocal):
            add("PY3_NONLOCAL", "使用了 Python 3 专属 nonlocal", line, column)
        elif isinstance(node, ast.YieldFrom):
            add("PY3_YIELD_FROM", "使用了 Python 3 专属 yield from", line, column)
        elif isinstance(node, ast.Raise) and node.cause is not None:
            add("PY3_RAISE_FROM", "使用了 Python 3 专属 raise ... from ...", line, column)
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.MatMult):
            add("PY3_MATRIX_OPERATOR", "使用了 Python 3 专属 @ 运算符", line, column)
        elif hasattr(ast, "Match") and isinstance(node, ast.Match):
            add("PY3_MATCH", "使用了 Python 3.10 专属 match/case", line, column)
        elif isinstance(node, ast.Dict) and any(key is None for key in node.keys):
            add("PY3_DICT_UNPACK", "字典字面量使用了 Python 3 专属 ** 解包", line, column)
        elif isinstance(node, ast.ClassDef) and node.keywords:
            add("PY3_CLASS_KEYWORD", "类定义使用了 Python 3 专属关键字参数", line, column)
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "super" and not node.args:
            add("PY3_ZERO_ARG_SUPER", "使用了 Python 3 零参数 super()", line, column)

        if isinstance(node, ast.ImportFrom) and node.module == "__future__":
            supported = {
                "absolute_import",
                "division",
                "generators",
                "nested_scopes",
                "print_function",
                "unicode_literals",
                "with_statement",
            }
            for alias in node.names:
                if alias.name not in supported:
                    add(
                        "PY3_FUTURE_FEATURE",
                        "__future__ 特性不受 Python 2.7 支持：{}".format(alias.name),
                        line,
                        column,
                    )

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            annotations: List[ast.AST] = []
            args = node.args
            annotations.extend(arg.annotation for arg in list(args.args) + list(args.kwonlyargs) if arg.annotation is not None)
            annotations.extend(arg.annotation for arg in getattr(args, "posonlyargs", []) if arg.annotation is not None)
            if args.vararg is not None and args.vararg.annotation is not None:
                annotations.append(args.vararg.annotation)
            if args.kwarg is not None and args.kwarg.annotation is not None:
                annotations.append(args.kwarg.annotation)
            if node.returns is not None:
                annotations.append(node.returns)
            for annotation in annotations:
                add(
                    "PY3_TYPE_ANNOTATION",
                    "函数使用了 Python 3 类型注解",
                    getattr(annotation, "lineno", line),
                    getattr(annotation, "col_offset", column - 1) + 1,
                )
            if args.kwonlyargs:
                add("PY3_KEYWORD_ONLY_ARGS", "函数使用了 Python 3 关键字专用参数", line, column)
            if getattr(args, "posonlyargs", []):
                add("PY3_POSITIONAL_ONLY_ARGS", "函数使用了 Python 3.8 位置专用参数", line, column)
    return issues


@register_detector("python.import_whitelist", ("python",))
def _detect_import_whitelist(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    analysis = context.python(artifact)
    issues: List[ValidationIssue] = []
    for imported in analysis.imports:
        if _module_is_allowed(imported.module, context.whitelist, artifact.project_modules):
            continue
        issues.append(_issue(
            artifact,
            "PY_IMPORT_NOT_WHITELISTED",
            "导入路径不在网易精确白名单中：{}".format(imported.module),
            "python.import_whitelist",
            line=imported.line,
            column=imported.column,
            suggestion="删除该导入，或仅通过 project_modules 显式声明组件自身模块",
            details={"module": imported.module},
        ))
    return issues


@register_detector("python.cross_side_import", ("python",))
def _detect_cross_side_import(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    analysis = context.python(artifact)
    side = _infer_side(artifact, analysis.imports, analysis.tree)
    server_imports = [ref for ref in analysis.imports if ref.module.startswith("mod.server.")]
    client_imports = [ref for ref in analysis.imports if ref.module.startswith("mod.client.")]
    issues: List[ValidationIssue] = []

    if side == "server":
        invalid = client_imports
    elif side == "client":
        invalid = server_imports
    elif side == "common":
        invalid = server_imports + client_imports
    elif side == "cross_side":
        invalid = []
    elif server_imports and client_imports:
        invalid = server_imports + client_imports
    else:
        invalid = []

    for imported in invalid:
        issues.append(_issue(
            artifact,
            "PY_CROSS_SIDE_IMPORT",
            "{} 文件导入了跨端模块 {}".format(side, imported.module),
            "python.cross_side_import",
            line=imported.line,
            column=imported.column,
            suggestion="客户端与服务端仅通过事件通信",
            details={"side": side, "module": imported.module},
        ))
    return issues


class _DynamicImportVisitor(ast.NodeVisitor):
    def __init__(self, dynamic_calls: FrozenSet[str]) -> None:
        self.dynamic_calls = dynamic_calls
        self.aliases: List[Dict[str, Optional[str]]] = [{}]
        self.calls: List[Tuple[str, ast.Call]] = []

    def _resolve(self, node: ast.AST) -> Optional[str]:
        direct = _dotted_name(node)
        if direct in self.dynamic_calls:
            return direct
        if isinstance(node, ast.Name):
            return self.aliases[-1].get(node.id)
        return None

    def _bind_target(self, target: ast.AST, dynamic_name: Optional[str]) -> None:
        if isinstance(target, ast.Name):
            self.aliases[-1][target.id] = dynamic_name
        else:
            self.visit(target)

    def _visit_function_scope(self, node: Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> None:
        for decorator in node.decorator_list:
            self.visit(decorator)
        for default in list(node.args.defaults) + [item for item in node.args.kw_defaults if item is not None]:
            self.visit(default)
        if node.returns is not None:
            self.visit(node.returns)

        shadowed = {
            argument.arg: None
            for argument in (
                list(node.args.args)
                + list(node.args.kwonlyargs)
                + list(getattr(node.args, "posonlyargs", []))
            )
        }
        if node.args.vararg is not None:
            shadowed[node.args.vararg.arg] = None
        if node.args.kwarg is not None:
            shadowed[node.args.kwarg.arg] = None
        self.aliases.append(shadowed)
        for statement in node.body:
            self.visit(statement)
        self.aliases.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._visit_function_scope(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._visit_function_scope(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        for expression in list(node.decorator_list) + list(node.bases):
            self.visit(expression)
        for keyword_node in node.keywords:
            self.visit(keyword_node.value)
        self.aliases.append({})
        for statement in node.body:
            self.visit(statement)
        self.aliases.pop()

    def visit_Lambda(self, node: ast.Lambda) -> None:
        for default in list(node.args.defaults) + [item for item in node.args.kw_defaults if item is not None]:
            self.visit(default)
        shadowed = {argument.arg: None for argument in list(node.args.args) + list(node.args.kwonlyargs)}
        self.aliases.append(shadowed)
        self.visit(node.body)
        self.aliases.pop()

    def visit_Assign(self, node: ast.Assign) -> None:
        self.visit(node.value)
        dynamic_name = self._resolve(node.value)
        for target in node.targets:
            self._bind_target(target, dynamic_name)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if node.value is not None:
            self.visit(node.value)
        self._bind_target(node.target, self._resolve(node.value) if node.value is not None else None)

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.visit(node.value)
        self._bind_target(node.target, self._resolve(node.value))

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        self.visit(node.value)
        self._bind_target(node.target, None)

    def visit_Call(self, node: ast.Call) -> None:
        dynamic_name = self._resolve(node.func)
        if dynamic_name is not None:
            self.calls.append((dynamic_name, node))
        self.generic_visit(node)


@register_detector("python.dynamic_import", ("python",))
def _detect_dynamic_import(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    analysis = context.python(artifact)
    dynamic_calls = frozenset({
        "__import__",
        "importlib.import_module",
        "imp.load_compiled",
        "imp.load_module",
        "imp.load_package",
        "imp.load_source",
    })
    issues: List[ValidationIssue] = []
    if analysis.tree is not None:
        visitor = _DynamicImportVisitor(dynamic_calls)
        visitor.visit(analysis.tree)
        for call_name, node in visitor.calls:
            issues.append(_issue(
                artifact,
                "PY_DYNAMIC_IMPORT",
                "禁止使用动态导入：{}".format(call_name),
                "python.dynamic_import",
                line=node.lineno,
                column=node.col_offset + 1,
                suggestion="组件模块使用静态导入；字符串模块仅使用对应端 extraApi.ImportModule",
                details={"call": call_name},
            ))
        return issues

    significant = [
        token for token in analysis.tokens
        if token.type not in {tokenize.COMMENT, tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT}
    ]
    for index, token in enumerate(significant):
        if token.string != "(":
            continue
        name_index = index - 1
        if name_index < 0 or significant[name_index].type != tokenize.NAME:
            continue
        name_parts = [significant[name_index].string]
        start_token = significant[name_index]
        name_index -= 1
        while (
            name_index >= 1
            and significant[name_index].string == "."
            and significant[name_index - 1].type == tokenize.NAME
        ):
            start_token = significant[name_index - 1]
            name_parts[:0] = [start_token.string, "."]
            name_index -= 2
        call_name = "".join(name_parts)
        if call_name not in dynamic_calls:
            continue
        previous = significant[name_index].string if name_index >= 0 else ""
        if previous in {"def", "class"}:
            continue
        issues.append(_issue(
            artifact,
            "PY_DYNAMIC_IMPORT",
            "禁止使用动态导入：{}".format(call_name),
            "python.dynamic_import",
            line=start_token.start[0],
            column=start_token.start[1] + 1,
            details={"call": call_name},
        ))
    return issues


_ScopePart = Tuple[str, str, int]
_ScopeKey = Tuple[_ScopePart, ...]


@dataclass(frozen=True)
class _EventCallRef:
    scope: _ScopeKey
    event_name: str
    callback: ast.AST


class _EventStructureVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.scope: List[_ScopePart] = []
        self.functions: Dict[Tuple[_ScopeKey, str], Union[ast.FunctionDef, ast.AsyncFunctionDef]] = {}
        self.event_calls: List[_EventCallRef] = []

    def _visit_scope(self, kind: str, node: Union[ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef]) -> None:
        part = (kind, node.name, node.lineno)
        self.scope.append(part)
        for statement in node.body:
            self.visit(statement)
        self.scope.pop()

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self._visit_scope("class", node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.functions[(tuple(self.scope), node.name)] = node
        self._visit_scope("function", node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.functions[(tuple(self.scope), node.name)] = node
        self._visit_scope("function", node)

    def visit_Call(self, node: ast.Call) -> None:
        call_name = _dotted_name(node.func)
        if call_name.rsplit(".", 1)[-1] == "ListenForEvent":
            event_node = node.args[2] if len(node.args) > 2 else None
            callback_node = node.args[4] if len(node.args) > 4 else None
            for keyword_node in node.keywords:
                if keyword_node.arg in {"eventName", "event_name"}:
                    event_node = keyword_node.value
                elif keyword_node.arg in {"callback", "func", "handler"}:
                    callback_node = keyword_node.value
            event_name = _constant_string(event_node)
            if event_name in EVENT_FIELD_CORRECTIONS and callback_node is not None:
                self.event_calls.append(_EventCallRef(tuple(self.scope), event_name, callback_node))
        self.generic_visit(node)


def _resolve_event_callback(
    reference: _EventCallRef,
    functions: Mapping[Tuple[_ScopeKey, str], Union[ast.FunctionDef, ast.AsyncFunctionDef]],
) -> Optional[Union[ast.FunctionDef, ast.AsyncFunctionDef]]:
    callback = reference.callback
    if isinstance(callback, ast.Attribute) and isinstance(callback.value, ast.Name):
        if callback.value.id not in {"self", "cls"}:
            return None
        for index in range(len(reference.scope) - 1, -1, -1):
            if reference.scope[index][0] == "class":
                return functions.get((reference.scope[:index + 1], callback.attr))
        return None
    if not isinstance(callback, ast.Name):
        return None
    for length in range(len(reference.scope), -1, -1):
        parent_scope = reference.scope[:length]
        if parent_scope and parent_scope[-1][0] == "class" and length != len(reference.scope):
            continue
        function = functions.get((parent_scope, callback.id))
        if function is not None:
            return function
    return None


def _field_accesses(function: Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> List[Tuple[str, int, int]]:
    parameters = [arg.arg for arg in function.args.args]
    if parameters and parameters[0] in {"self", "cls"}:
        parameters = parameters[1:]
    if not parameters:
        return []
    payload = parameters[0]

    class FieldAccessVisitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.accesses: List[Tuple[str, int, int]] = []

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            return

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
            return

        def visit_Lambda(self, node: ast.Lambda) -> None:
            return

        def visit_ClassDef(self, node: ast.ClassDef) -> None:
            return

        def visit_Subscript(self, node: ast.Subscript) -> None:
            if isinstance(node.value, ast.Name) and node.value.id == payload:
                field_name = _constant_string(node.slice)
                if field_name:
                    self.accesses.append((field_name, node.lineno, node.col_offset + 1))
            self.generic_visit(node)

        def visit_Call(self, node: ast.Call) -> None:
            if isinstance(node.func, ast.Attribute):
                payload_call = isinstance(node.func.value, ast.Name) and node.func.value.id == payload
                if payload_call and node.func.attr in {"get", "has_key", "pop", "setdefault"} and node.args:
                    field_name = _constant_string(node.args[0])
                    if field_name:
                        self.accesses.append((field_name, node.lineno, node.col_offset + 1))
            self.generic_visit(node)

    visitor = FieldAccessVisitor()
    for statement in function.body:
        visitor.visit(statement)
    return visitor.accesses


@register_detector("python.event_fields", ("python",))
def _detect_event_fields(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    tree = context.python(artifact).tree
    if tree is None:
        return []
    structure = _EventStructureVisitor()
    structure.visit(tree)
    bindings: Dict[Union[ast.FunctionDef, ast.AsyncFunctionDef], List[str]] = {}
    for reference in structure.event_calls:
        function = _resolve_event_callback(reference, structure.functions)
        if function is not None:
            bindings.setdefault(function, []).append(reference.event_name)

    issues: List[ValidationIssue] = []
    seen: set = set()
    for function, event_names in bindings.items():
        for field_name, line, column in _field_accesses(function):
            for event_name in event_names:
                replacement = EVENT_FIELD_CORRECTIONS[event_name].get(field_name)
                key = (event_name, field_name, line, column)
                if not replacement or key in seen:
                    continue
                seen.add(key)
                issues.append(_issue(
                    artifact,
                    "PY_EVENT_FIELD_MISMATCH",
                    "{} 使用字段 {}，该事件应使用 {}".format(event_name, field_name, replacement),
                    "python.event_fields",
                    line=line,
                    column=column,
                    suggestion="将 {} 改为 {}".format(field_name, replacement),
                    details={"event": event_name, "field": field_name, "replacement": replacement},
                ))
    return issues


def _is_high_frequency_name(name: str) -> bool:
    normalized = re.sub(r"[^a-z0-9]", "", name.lower())
    return any(marker in normalized for marker in ("tick", "frame", "onupdate", "onrender"))


class _PrintVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.high_frequency_depth = 0
        self.loop_depth = 0
        self.calls: List[ast.Call] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        high_frequency = _is_high_frequency_name(node.name)
        self.high_frequency_depth += int(high_frequency)
        self.generic_visit(node)
        self.high_frequency_depth -= int(high_frequency)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.visit_FunctionDef(node)  # type: ignore[arg-type]

    def visit_For(self, node: ast.For) -> None:
        self.loop_depth += 1
        self.generic_visit(node)
        self.loop_depth -= 1

    def visit_While(self, node: ast.While) -> None:
        self.loop_depth += 1
        self.generic_visit(node)
        self.loop_depth -= 1

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Name) and node.func.id == "print":
            if self.high_frequency_depth or self.loop_depth:
                self.calls.append(node)
        self.generic_visit(node)


@register_detector("python.high_frequency_print", ("python",))
def _detect_high_frequency_print(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    tree = context.python(artifact).tree
    if tree is None:
        return []
    visitor = _PrintVisitor()
    visitor.visit(tree)
    return [
        _issue(
            artifact,
            "PY_PRINT_HIGH_FREQUENCY",
            "高频回调或循环中使用 print，可能造成日志刷屏",
            "python.high_frequency_print",
            line=node.lineno,
            column=node.col_offset + 1,
            severity=SEVERITY_WARNING,
            suggestion="删除逐帧日志，或仅在状态变化/采样帧输出稳定前缀日志",
        )
        for node in visitor.calls
    ]


@register_detector("json.parse", ("json",))
def _detect_json_parse(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    try:
        context.json_value(artifact)
    except json.JSONDecodeError as exc:
        return [
            _issue(
                artifact,
                "JSON_PARSE_ERROR",
                "JSON 解析失败：{}".format(exc.msg),
                "json.parse",
                line=exc.lineno,
                column=exc.colno,
            )
        ]
    return []


def _json_root_type(data: Any, artifact: Artifact) -> str:
    requested = (artifact.artifact_type or "auto").lower()
    if requested in {"item", "block"}:
        return requested
    if not isinstance(data, dict):
        return "json"
    if "minecraft:item" in data:
        return "item"
    if "minecraft:block" in data:
        return "block"
    return "json"


@register_detector("json.identifier", ("json",))
def _detect_json_identifier(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    try:
        data = context.json_value(artifact)
    except json.JSONDecodeError:
        return []
    if not isinstance(data, dict):
        return [
            _issue(
                artifact,
                "JSON_ROOT_NOT_OBJECT",
                "JSON 根节点必须是对象",
                "json.identifier",
            )
        ]

    requested = _json_root_type(data, artifact)
    roots: List[Tuple[str, Any]] = []
    if requested == "item":
        roots.append(("minecraft:item", data.get("minecraft:item")))
    elif requested == "block":
        roots.append(("minecraft:block", data.get("minecraft:block")))
    else:
        roots.extend((key, value) for key, value in data.items() if key.startswith("minecraft:") and isinstance(value, dict))

    issues: List[ValidationIssue] = []
    identifier_pattern = re.compile(r"^[a-z0-9][a-z0-9_.-]*:[a-z0-9][a-z0-9_./-]*$")
    for root_name, root in roots:
        if not isinstance(root, dict):
            if requested in {"item", "block"}:
                issues.append(_issue(
                    artifact,
                    "JSON_ROOT_MISSING",
                    "缺少或错误的 {} 根对象".format(root_name),
                    "json.identifier",
                ))
            continue
        description = root.get("description")
        identifier = description.get("identifier") if isinstance(description, dict) else None
        if not isinstance(identifier, str) or not identifier:
            line, column = _json_location(context.text(artifact), "description")
            issues.append(_issue(
                artifact,
                "JSON_IDENTIFIER_MISSING",
                "{} 缺少 description.identifier".format(root_name),
                "json.identifier",
                line=line,
                column=column,
            ))
        elif not identifier_pattern.fullmatch(identifier):
            line, column = _json_location(context.text(artifact), "identifier", identifier)
            issues.append(_issue(
                artifact,
                "JSON_IDENTIFIER_INVALID",
                "identifier 必须是小写 namespace:id：{}".format(identifier),
                "json.identifier",
                line=line,
                column=column,
                details={"identifier": identifier},
            ))
    return issues


@register_detector("json.item_format", ("json",))
def _detect_item_format(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    try:
        data = context.json_value(artifact)
    except json.JSONDecodeError:
        return []
    if _json_root_type(data, artifact) != "item" or not isinstance(data, dict):
        return []
    version = data.get("format_version")
    if version == "1.10":
        return []
    line, column = _json_location(context.text(artifact), "format_version")
    return [
        _issue(
            artifact,
            "JSON_ITEM_FORMAT_VERSION",
            "网易物品 JSON 必须使用 format_version \"1.10\"，当前为 {!r}".format(version),
            "json.item_format",
            line=line,
            column=column,
            suggestion='设置 "format_version": "1.10"',
        )
    ]


def _walk_json_values(value: Any) -> Iterable[Tuple[str, Any]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield key, child
            yield from _walk_json_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_json_values(child)


@register_detector("json.biome_namespace", ("json",))
def _detect_biome_namespace(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    if _version_tuple(artifact.target_version) < (3, 9):
        return []
    try:
        data = context.json_value(artifact)
    except json.JSONDecodeError:
        return []
    issues: List[ValidationIssue] = []
    identifier_pattern = re.compile(r"^[a-z0-9][a-z0-9_.-]*:[a-z0-9][a-z0-9_./-]*$")
    for key, value in _walk_json_values(data):
        if key != "biome_type":
            continue
        if isinstance(value, str) and identifier_pattern.fullmatch(value):
            continue
        line, column = _json_location(
            context.text(artifact),
            key,
            value if isinstance(value, str) else None,
        )
        issues.append(_issue(
            artifact,
            "JSON_BIOME_TYPE_NAMESPACE",
            "ModSDK 3.9 起 biome_type 必须使用完整 namespace:id：{!r}".format(value),
            "json.biome_namespace",
            line=line,
            column=column,
            details={"biome_type": value},
        ))
    return issues


def _block_profile(artifact: Artifact, format_version: Any) -> Optional[str]:
    if artifact.format_profile:
        return artifact.format_profile
    for profile, version in BLOCK_FORMAT_PROFILES.items():
        if format_version == version:
            return profile
    return None


@register_detector("json.block_profile", ("json",))
def _detect_block_profile(artifact: Artifact, context: ValidationContext) -> Iterable[ValidationIssue]:
    try:
        data = context.json_value(artifact)
    except json.JSONDecodeError:
        return []
    if _json_root_type(data, artifact) != "block" or not isinstance(data, dict):
        return []

    text = context.text(artifact)
    format_version = data.get("format_version")
    profile = _block_profile(artifact, format_version)
    issues: List[ValidationIssue] = []
    if artifact.format_profile and artifact.format_profile not in BLOCK_FORMAT_PROFILES:
        line, column = _json_location(text, "format_version")
        return [
            _issue(
                artifact,
                "JSON_BLOCK_PROFILE_UNKNOWN",
                "未知方块格式 profile：{}".format(artifact.format_profile),
                "json.block_profile",
                line=line,
                column=column,
            )
        ]
    if artifact.format_profile:
        expected_version = BLOCK_FORMAT_PROFILES[artifact.format_profile]
        if format_version != expected_version:
            line, column = _json_location(text, "format_version")
            issues.append(_issue(
                artifact,
                "JSON_BLOCK_PROFILE_VERSION_CONFLICT",
                "profile {} 要求 format_version {}，当前为 {!r}".format(
                    artifact.format_profile, expected_version, format_version
                ),
                "json.block_profile",
                line=line,
                column=column,
            ))

    block = data.get("minecraft:block")
    components = block.get("components") if isinstance(block, dict) else None
    if components is None or profile is None:
        return issues
    if not isinstance(components, dict):
        line, column = _json_location(text, "components")
        issues.append(_issue(
            artifact,
            "JSON_BLOCK_COMPONENTS_SHAPE",
            "minecraft:block.components 必须是对象",
            "json.block_profile",
            line=line,
            column=column,
        ))
        return issues

    legacy_shapes = {
        "minecraft:destroy_time": "value",
        "minecraft:explosion_resistance": "value",
        "minecraft:block_light_emission": "emission",
        "minecraft:block_light_absorption": "value",
    }
    modern_shapes = {
        "minecraft:destructible_by_mining": "seconds_to_destroy",
        "minecraft:destructible_by_explosion": "explosion_resistance",
    }
    modern_scalar_shapes = (
        "minecraft:light_emission",
        "minecraft:light_dampening",
    )
    modern_components = tuple(modern_shapes) + tuple(modern_scalar_shapes)

    def add_shape(component: str, message: str) -> None:
        line, column = _json_location(text, component)
        issues.append(_issue(
            artifact,
            "JSON_BLOCK_COMPONENT_SHAPE_CONFLICT",
            message,
            "json.block_profile",
            line=line,
            column=column,
            details={"profile": profile, "component": component},
        ))

    if profile == "legacy_1_10":
        for component, value_key in legacy_shapes.items():
            if component not in components:
                continue
            value = components[component]
            if not isinstance(value, dict) or not _is_number(value.get(value_key)):
                add_shape(component, "{} 在 legacy_1_10 中必须是包含数值 {} 的对象".format(component, value_key))
        for component in modern_components:
            if component in components:
                add_shape(component, "{} 属于 modern_1_19_20，不能用于 legacy_1_10".format(component))
    elif profile == "scalar_1_16":
        for component in legacy_shapes:
            if component in components and not _is_number(components[component]):
                add_shape(component, "{} 在 scalar_1_16 中必须是数值".format(component))
        for component in modern_components:
            if component in components:
                add_shape(component, "{} 属于 modern_1_19_20，不能用于 scalar_1_16".format(component))
    elif profile == "modern_1_19_20":
        for component in legacy_shapes:
            if component in components:
                add_shape(component, "{} 是旧 profile 组件，不能用于 modern_1_19_20".format(component))
        for component, value_key in modern_shapes.items():
            if component not in components:
                continue
            value = components[component]
            valid = isinstance(value, bool) or (isinstance(value, dict) and _is_number(value.get(value_key)))
            if not valid:
                add_shape(
                    component,
                    "{} 在 modern_1_19_20 中必须是布尔值或包含数值 {} 的对象".format(component, value_key),
                )
        for component in modern_scalar_shapes:
            if component in components and not _is_number(components[component]):
                add_shape(component, "{} 在 modern_1_19_20 中必须是数值".format(component))
    return issues


def validate_artifact(
    artifact: Artifact,
    whitelist: Optional[Iterable[str]] = None,
) -> ValidationReport:
    """按注册顺序运行适用于该生成物的全部 detector。"""

    if not isinstance(artifact.content, (str, bytes)):
        issue = _issue(
            artifact,
            "ARTIFACT_CONTENT_TYPE",
            "生成物内容必须是 str 或 UTF-8 bytes",
            "pipeline.input",
            details={"content_type": type(artifact.content).__name__},
        )
        return ValidationReport((artifact,), (issue,))

    effective_whitelist = DEFAULT_IMPORT_WHITELIST if whitelist is None else frozenset(whitelist)
    context = ValidationContext(whitelist=effective_whitelist)
    try:
        if isinstance(artifact.content, str):
            artifact.content.encode("utf-8")
        context.text(artifact)
    except (UnicodeDecodeError, UnicodeEncodeError) as exc:
        line = 1
        column = exc.start + 1
        if isinstance(artifact.content, str):
            prefix = artifact.content[:exc.start]
            line = prefix.count("\n") + 1
            column = exc.start - prefix.rfind("\n")
        issue = _issue(
            artifact,
            "ARTIFACT_NOT_UTF8",
            "生成物不是有效 UTF-8：{}".format(exc),
            "pipeline.encoding",
            line=line,
            column=column,
        )
        return ValidationReport((artifact,), (issue,))

    issues: List[ValidationIssue] = []
    for spec in DETECTOR_REGISTRY.values():
        if artifact.kind not in spec.artifact_types and "*" not in spec.artifact_types:
            continue
        try:
            issues.extend(spec.detector(artifact, context))
        except Exception as exc:  # pragma: no cover - 保护 MCP 进程，测试会覆盖各内置 detector
            issues.append(_issue(
                artifact,
                "VALIDATOR_INTERNAL_ERROR",
                "校验器 {} 执行失败：{}".format(spec.name, exc),
                spec.name,
            ))

    unique: Dict[Tuple[str, str, int, int, str], ValidationIssue] = OrderedDict()
    for issue in issues:
        key = (issue.filename, issue.code, issue.line, issue.column, issue.message)
        unique.setdefault(key, issue)
    return ValidationReport((artifact,), tuple(unique.values()))


def validate_artifacts(
    artifacts: Iterable[Artifact],
    whitelist: Optional[Iterable[str]] = None,
) -> ValidationReport:
    """批量校验并合并为一个报告。"""

    artifact_tuple = tuple(artifacts)
    effective_whitelist = None if whitelist is None else frozenset(whitelist)
    issues: List[ValidationIssue] = []
    for artifact in artifact_tuple:
        issues.extend(validate_artifact(artifact, whitelist=effective_whitelist).issues)
    return ValidationReport(artifact_tuple, tuple(issues))


def validate_python(
    code: TextValue,
    filename: str = "unknown.py",
    side: str = "auto",
    target_version: str = "current",
    project_modules: Optional[Iterable[str]] = None,
    whitelist: Optional[Iterable[str]] = None,
) -> ValidationReport:
    """校验一份 ModSDK Python 源码。"""

    artifact = Artifact(
        content=code,
        filename=filename,
        artifact_type="python",
        side=side,
        target_version=target_version,
        project_modules=tuple(project_modules or ()),
    )
    return validate_artifact(artifact, whitelist=whitelist)


def validate_json(
    text: TextValue,
    filename: str = "unknown.json",
    artifact_type: str = "json",
    target_version: str = "current",
    format_profile: Optional[str] = None,
) -> ValidationReport:
    """校验一份 ModSDK JSON 生成物。"""

    artifact = Artifact(
        content=text,
        filename=filename,
        artifact_type=artifact_type,
        target_version=target_version,
        format_profile=format_profile,
    )
    return validate_artifact(artifact)


__all__ = [
    "Artifact",
    "BLOCK_FORMAT_PROFILES",
    "CURRENT_TARGET_VERSION",
    "DEFAULT_IMPORT_WHITELIST",
    "DETECTOR_REGISTRY",
    "DetectorSpec",
    "SEVERITY_CRITICAL",
    "SEVERITY_ERROR",
    "SEVERITY_INFO",
    "SEVERITY_WARNING",
    "ValidationContext",
    "ValidationIssue",
    "ValidationReport",
    "get_registered_detectors",
    "register_detector",
    "validate_artifact",
    "validate_artifacts",
    "validate_json",
    "validate_python",
]
