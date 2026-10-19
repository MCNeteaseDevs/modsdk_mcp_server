"""Load and query the repository-backed ModSDK standards registry."""

from __future__ import annotations

import hashlib
import json
import re
from copy import deepcopy
from functools import lru_cache
from pathlib import Path
from typing import (
    Any,
    Dict,
    FrozenSet,
    Iterable,
    List,
    Literal,
    Mapping,
    Optional,
    Tuple,
    Type,
    TypeVar,
    get_args,
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)


REGISTRY_ROOT = Path(__file__).resolve().parents[1] / "standard" / "registry"

Authority = Literal[
    "official_runtime",
    "official_doc",
    "curated_policy",
    "runtime_evidence",
    "bedrock_reference",
    "community_reference",
]
Enforcement = Literal["block", "warn", "guide", "manual"]
Severity = Literal["critical", "error", "warning", "info"]
Domain = Literal[
    "python",
    "architecture",
    "api_event",
    "json_content",
    "json_ui",
    "performance",
    "multiplayer",
]
Side = Literal["client", "server", "common", "cross_side"]
ArtifactType = Literal[
    "python",
    "behavior_json",
    "resource_json",
    "manifest_json",
    "ui_json",
    "ui_python",
    "ui_defs_json",
    "mixed",
]
VersionStatus = Literal["stable", "beta", "preview", "deprecated"]
RuntimeEvidenceStatus = Literal["reviewed", "partial", "unreviewed"]

_MODULE_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*$")
_RULE_ID_PATTERN = r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$"
_LOCAL_PATH_RE = re.compile(
    r"(?:(?<![A-Za-z0-9])[A-Za-z]:[\\/][^\s\"'<>]+|\\\\[^\\/\s]+[\\/][^\s\"'<>]+|(?<![A-Za-z0-9:/])/(?:home|Users)/[^\s\"'<>]+)",
    re.IGNORECASE,
)


class StandardsRegistryError(ValueError):
    """Raised when a registry file is missing, malformed, or inconsistent."""


class _StrictRegistryModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)


class Rule(_StrictRegistryModel):
    """Strict schema for one versioned development rule."""

    id: str = Field(min_length=3, pattern=_RULE_ID_PATTERN)
    title: str = Field(min_length=1)
    domain: Domain
    sides: Tuple[Side, ...]
    artifact_types: Tuple[ArtifactType, ...]
    versions: Tuple[str, ...]
    severity: Severity
    enforcement: Enforcement
    authority: Authority
    conditions: Tuple[str, ...]
    do: Tuple[str, ...]
    avoid: Tuple[str, ...]
    positive_examples: Tuple[str, ...]
    negative_examples: Tuple[str, ...]
    keywords: Tuple[str, ...]
    source_ids: Tuple[str, ...]
    detector: Optional[str]

    @field_validator(
        "sides",
        "artifact_types",
        "versions",
        "conditions",
        "do",
        "avoid",
        "positive_examples",
        "negative_examples",
        "keywords",
        "source_ids",
        mode="before",
    )
    @classmethod
    def _convert_json_arrays(cls, value: Any) -> Any:
        if isinstance(value, list):
            return tuple(value)
        return value

    @field_validator(
        "sides",
        "artifact_types",
        "versions",
        "conditions",
        "do",
        "avoid",
        "positive_examples",
        "negative_examples",
        "keywords",
        "source_ids",
    )
    @classmethod
    def _require_unique_non_empty_values(cls, value: Tuple[Any, ...]) -> Tuple[Any, ...]:
        if not value:
            raise ValueError("rule arrays must not be empty")
        if any(not isinstance(item, str) or not item.strip() for item in value):
            raise ValueError("rule arrays must contain non-empty strings")
        if len(value) != len(set(value)):
            raise ValueError("rule arrays must not contain duplicates")
        return value

    @model_validator(mode="after")
    def _limit_runtime_evidence_enforcement(self) -> "Rule":
        if self.authority == "runtime_evidence" and self.enforcement not in {
            "warn",
            "manual",
        }:
            raise ValueError("runtime_evidence rules may only warn or require manual verification")
        return self


class Source(_StrictRegistryModel):
    """Strict provenance record for rules and version profiles."""

    id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    authority: Authority
    url: str = Field(min_length=1)
    last_modified: str = Field(min_length=1)
    retrieved_at: str = Field(min_length=1)
    notes: str = Field(min_length=1)
    snapshot_path: Optional[str] = None


class VersionProfile(_StrictRegistryModel):
    """Strict schema for one supported ModSDK release profile."""

    version: str = Field(min_length=1)
    bedrock_version: str = Field(min_length=1)
    status: VersionStatus
    released_at: str = Field(min_length=1)
    docs_base_url: str = Field(min_length=1)
    scheduled_stable_at: Optional[str] = None
    scheduled_rollout_at: Optional[str] = None
    previous_version: Optional[str] = None
    runtime_evidence_status: RuntimeEvidenceStatus
    source_ids: Tuple[str, ...]
    aliases: Tuple[str, ...]
    source_boundary: Optional[str] = None

    @field_validator("source_ids", "aliases", mode="before")
    @classmethod
    def _convert_json_arrays(cls, value: Any) -> Any:
        if isinstance(value, list):
            return tuple(value)
        return value

    @field_validator("source_ids", "aliases")
    @classmethod
    def _require_unique_non_empty_values(cls, value: Tuple[str, ...]) -> Tuple[str, ...]:
        if not value or any(not item.strip() for item in value):
            raise ValueError("version arrays must contain non-empty strings")
        if len(value) != len(set(value)):
            raise ValueError("version arrays must not contain duplicates")
        return value

    @model_validator(mode="after")
    def _require_runtime_boundary(self) -> "VersionProfile":
        if self.runtime_evidence_status == "unreviewed" and not self.source_boundary:
            raise ValueError("未经运行时复核的版本必须声明证据边界")
        if not re.fullmatch(r"https://mc\.163\.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI(?:-beta)?", self.docs_base_url):
            raise ValueError("版本文档必须指向网易官方稳定版或 Beta 版频道")
        return self


RegistryModel = TypeVar("RegistryModel", bound=_StrictRegistryModel)


def _as_values(value: Optional[Iterable[str]]) -> Optional[FrozenSet[str]]:
    if value is None:
        return None
    if isinstance(value, str):
        return frozenset((value,))
    return frozenset(str(item) for item in value)


def _model_dict(model: _StrictRegistryModel) -> Dict[str, Any]:
    return model.model_dump(mode="json")


def find_local_coupling_markers(value: Any) -> Tuple[str, ...]:
    """Return machine-local absolute paths found in a nested value."""

    def strings(item: Any) -> Iterable[str]:
        if isinstance(item, str):
            yield item
        elif isinstance(item, BaseModel):
            yield from strings(item.model_dump(mode="json"))
        elif isinstance(item, Mapping):
            for key, nested in item.items():
                yield from strings(key)
                yield from strings(nested)
        elif isinstance(item, (list, tuple, set, frozenset)):
            for nested in item:
                yield from strings(nested)

    matches: List[str] = []
    for item in strings(value):
        for match in _LOCAL_PATH_RE.finditer(item):
            path = match.group(0)
            if path not in matches:
                matches.append(path)
    return tuple(matches)


class StandardsRegistry:
    """Validated, repository-only view over ``standard/registry`` JSON files."""

    def __init__(self, registry_root: Optional[Path] = None) -> None:
        self.root = Path(registry_root or REGISTRY_ROOT).resolve()
        self._manifest = self._read_json("manifest.json")
        self._sources = self._load_sources()
        self._versions = self._load_versions()
        self._rules = self._load_rules()
        self._whitelist_snapshot = self._load_whitelist_snapshot()
        self._validation_summary = self._validate()
        self._rules_by_id = {rule.id: rule for rule in self._rules}
        self._sources_by_id = {source.id: source for source in self._sources}
        self._versions_by_name = self._build_version_index()

    def _resolve(self, relative_path: str) -> Path:
        path = (self.root / relative_path).resolve()
        try:
            path.relative_to(self.root)
        except ValueError as exc:
            raise StandardsRegistryError(
                "Registry path escapes its root: {!r}".format(relative_path)
            ) from exc
        return path

    def _read_json(self, relative_path: str) -> Dict[str, Any]:
        path = self._resolve(relative_path)
        try:
            with path.open("r", encoding="utf-8") as handle:
                payload = json.load(handle)
        except FileNotFoundError as exc:
            raise StandardsRegistryError(
                "Registry file does not exist: {}".format(relative_path)
            ) from exc
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise StandardsRegistryError(
                "Cannot read registry file {}: {}".format(relative_path, exc)
            ) from exc
        if not isinstance(payload, dict):
            raise StandardsRegistryError(
                "Registry file must contain a JSON object: {}".format(relative_path)
            )
        return payload

    @staticmethod
    def _parse_model(
        model_type: Type[RegistryModel], value: Any, location: str
    ) -> RegistryModel:
        try:
            return model_type.model_validate(value, strict=True)
        except ValidationError as exc:
            raise StandardsRegistryError(
                "Invalid {} schema:\n{}".format(location, exc)
            ) from exc

    def _load_sources(self) -> Tuple[Source, ...]:
        relative_path = self._manifest.get("source_file")
        if not isinstance(relative_path, str):
            raise StandardsRegistryError("manifest.source_file must be a string")
        payload = self._read_json(relative_path)
        rows = payload.get("sources")
        if not isinstance(rows, list):
            raise StandardsRegistryError("sources.json must contain a sources array")
        return tuple(
            self._parse_model(Source, row, "source #{}".format(index))
            for index, row in enumerate(rows)
        )

    def _load_versions(self) -> Tuple[VersionProfile, ...]:
        version_files = self._manifest.get("version_files")
        if not isinstance(version_files, dict) or not version_files:
            raise StandardsRegistryError("manifest.version_files must be a non-empty object")
        profiles = []
        for declared_version, relative_path in sorted(version_files.items()):
            if not isinstance(relative_path, str):
                raise StandardsRegistryError("Every version file path must be a string")
            profile = self._parse_model(
                VersionProfile,
                self._read_json(relative_path),
                "version {}".format(declared_version),
            )
            if profile.version != declared_version:
                raise StandardsRegistryError(
                    "Version file {!r} declares {!r}".format(
                        declared_version, profile.version
                    )
                )
            profiles.append(profile)
        return tuple(profiles)

    def _load_rules(self) -> Tuple[Rule, ...]:
        rule_files = self._manifest.get("rule_files")
        if not isinstance(rule_files, list) or not rule_files:
            raise StandardsRegistryError("manifest.rule_files must be a non-empty array")
        rules = []
        for relative_path in rule_files:
            if not isinstance(relative_path, str):
                raise StandardsRegistryError("Every rule file path must be a string")
            rows = self._read_json(relative_path).get("rules")
            if not isinstance(rows, list):
                raise StandardsRegistryError(
                    "Rule file must contain a rules array: {}".format(relative_path)
                )
            rules.extend(
                self._parse_model(
                    Rule, row, "{} rule #{}".format(relative_path, index)
                )
                for index, row in enumerate(rows)
            )
        return tuple(rules)

    def _load_whitelist_snapshot(self) -> Dict[str, Any]:
        snapshot_files = self._manifest.get("snapshot_files")
        if not isinstance(snapshot_files, dict):
            raise StandardsRegistryError("manifest.snapshot_files must be an object")
        relative_path = snapshot_files.get("python_module_whitelist")
        if not isinstance(relative_path, str):
            raise StandardsRegistryError(
                "manifest.snapshot_files.python_module_whitelist must be a string"
            )
        return self._read_json(relative_path)

    def _build_version_index(self) -> Dict[str, VersionProfile]:
        index: Dict[str, VersionProfile] = {}
        for profile in self._versions:
            for name in (profile.version,) + profile.aliases:
                index[name.strip().casefold()] = profile
        return index

    @staticmethod
    def _required_model_fields(model_type: Type[BaseModel]) -> set:
        return {
            name for name, field in model_type.model_fields.items() if field.is_required()
        }

    def _validate_manifest(self, errors: List[str]) -> None:
        required = {
            "schema_version",
            "registry_version",
            "default_version",
            "source_file",
            "version_files",
            "rule_files",
            "snapshot_files",
            "required_rule_fields",
            "required_source_fields",
            "required_version_profile_fields",
            "domains",
            "sides",
            "artifact_types",
            "severities",
            "enforcements",
            "authorities",
            "detectors",
            "content_policy",
        }
        missing = sorted(required - set(self._manifest))
        if missing:
            errors.append("manifest missing fields: {}".format(", ".join(missing)))
            return

        exact_enums = {
            "domains": set(get_args(Domain)),
            "sides": set(get_args(Side)),
            "artifact_types": set(get_args(ArtifactType)),
            "severities": set(get_args(Severity)),
            "enforcements": set(get_args(Enforcement)),
        }
        for field, expected in exact_enums.items():
            actual = self._manifest.get(field)
            if not isinstance(actual, list) or set(actual) != expected:
                errors.append("manifest.{} must exactly match its schema enum".format(field))

        authority_rows = self._manifest.get("authorities")
        if not isinstance(authority_rows, list):
            errors.append("manifest.authorities must be an array")
        else:
            ids = [row.get("id") for row in authority_rows if isinstance(row, dict)]
            ranks = [row.get("rank") for row in authority_rows if isinstance(row, dict)]
            if set(ids) != set(get_args(Authority)) or len(ids) != len(set(ids)):
                errors.append("manifest.authorities must exactly match the authority enum")
            if any(not isinstance(rank, int) for rank in ranks) or len(ranks) != len(
                set(ranks)
            ):
                errors.append("manifest authority ranks must be unique integers")
            for row in authority_rows:
                if not isinstance(row, dict) or not isinstance(
                    row.get("blocking_eligible"), bool
                ):
                    errors.append("Every authority requires blocking_eligible")

        required_models = {
            "required_rule_fields": self._required_model_fields(Rule),
            "required_source_fields": self._required_model_fields(Source),
            "required_version_profile_fields": self._required_model_fields(
                VersionProfile
            ),
        }
        for field, expected in required_models.items():
            actual = self._manifest.get(field)
            if not isinstance(actual, list) or set(actual) != expected:
                errors.append("manifest.{} does not match the Pydantic model".format(field))

        detectors = self._manifest.get("detectors")
        if not isinstance(detectors, list) or not all(
            isinstance(item, str) and item for item in detectors
        ):
            errors.append("manifest.detectors must be an array of strings")
        elif len(detectors) != len(set(detectors)):
            errors.append("manifest.detectors contains duplicates")

    def _validate_cross_references(self, errors: List[str]) -> None:
        source_ids = [source.id for source in self._sources]
        if len(source_ids) != len(set(source_ids)):
            errors.append("Duplicate source id")
        known_sources = set(source_ids)

        version_ids = [profile.version for profile in self._versions]
        if len(version_ids) != len(set(version_ids)):
            errors.append("Duplicate version profile")
        known_versions = set(version_ids)
        alias_owners: Dict[str, str] = {}
        for profile in self._versions:
            unknown = sorted(set(profile.source_ids) - known_sources)
            if unknown:
                errors.append(
                    "Version {} references unknown sources: {}".format(
                        profile.version, ", ".join(unknown)
                    )
                )
            for name in (profile.version,) + profile.aliases:
                alias = name.strip().casefold()
                owner = alias_owners.get(alias)
                if owner is not None and owner != profile.version:
                    errors.append(
                        "Version alias {!r} belongs to both {} and {}".format(
                            name, owner, profile.version
                        )
                    )
                alias_owners[alias] = profile.version
        if self._manifest.get("default_version") not in known_versions:
            errors.append("manifest.default_version has no profile")

        rule_ids = [rule.id for rule in self._rules]
        if len(rule_ids) != len(set(rule_ids)):
            errors.append("Duplicate rule id")
        known_detectors = set(self._manifest.get("detectors", []))
        for rule in self._rules:
            unknown_sources = sorted(set(rule.source_ids) - known_sources)
            if unknown_sources:
                errors.append(
                    "Rule {} references unknown sources: {}".format(
                        rule.id, ", ".join(unknown_sources)
                    )
                )
            unknown_versions = sorted(set(rule.versions) - known_versions)
            if unknown_versions:
                errors.append(
                    "Rule {} references unknown versions: {}".format(
                        rule.id, ", ".join(unknown_versions)
                    )
                )
            if rule.detector is not None and rule.detector not in known_detectors:
                errors.append(
                    "Rule {} uses undeclared detector {}".format(
                        rule.id, rule.detector
                    )
                )

    def _validate_whitelist(self, errors: List[str]) -> None:
        snapshot = self._whitelist_snapshot
        modules = snapshot.get("modules")
        if not isinstance(modules, list) or not all(
            isinstance(module, str) and _MODULE_NAME_RE.fullmatch(module)
            for module in modules or []
        ):
            errors.append("Python module whitelist contains an invalid module path")
            return
        if snapshot.get("module_count") != len(modules) or not modules:
            errors.append("Python module whitelist count must match its non-empty snapshot")
        if len(modules) != len(set(modules)):
            errors.append("Python module whitelist contains duplicates")
        entries = snapshot.get("entries")
        if not isinstance(entries, list) or len(entries) != len(modules):
            errors.append("Python module whitelist entries must align with modules")
        else:
            normalized_names = []
            for entry in entries:
                if not isinstance(entry, dict):
                    errors.append("Python module whitelist entry must be an object")
                    break
                raw_display = entry.get("raw_display")
                normalized_name = entry.get("normalized_name")
                if not isinstance(raw_display, str) or not raw_display.strip():
                    errors.append("Python module whitelist entry lacks raw display text")
                    break
                if not isinstance(normalized_name, str) or not _MODULE_NAME_RE.fullmatch(normalized_name):
                    errors.append("Python module whitelist entry has an invalid normalized name")
                    break
                normalized_names.append(normalized_name)
            if normalized_names and normalized_names != modules:
                errors.append("Python module whitelist entry order does not match modules")
        if snapshot.get("source_id") not in {source.id for source in self._sources}:
            errors.append("Python module whitelist references an unknown source")
        for field in ("source_url", "last_modified", "retrieved_at"):
            if not isinstance(snapshot.get(field), str) or not snapshot[field].strip():
                errors.append("Python module whitelist lacks {} metadata".format(field))
        module_text = "\n".join(modules) + "\n"
        digest = hashlib.sha256(module_text.encode("utf-8")).hexdigest()
        if digest != snapshot.get("modules_sha256"):
            errors.append("Python module whitelist hash does not match its modules")

    def _validate(self) -> Dict[str, Any]:
        errors: List[str] = []
        self._validate_manifest(errors)
        self._validate_cross_references(errors)
        self._validate_whitelist(errors)
        if find_local_coupling_markers(
            {
                "manifest": self._manifest,
                "sources": self._sources,
                "versions": self._versions,
                "rules": self._rules,
                "whitelist": self._whitelist_snapshot,
            }
        ):
            errors.append("Registry contains forbidden local coupling markers")
        if errors:
            raise StandardsRegistryError("\n".join(errors))
        return {
            "schema_version": self._manifest["schema_version"],
            "registry_version": self._manifest["registry_version"],
            "rule_count": len(self._rules),
            "source_count": len(self._sources),
            "version_count": len(self._versions),
            "python_module_count": len(self._whitelist_snapshot["modules"]),
        }

    @property
    def manifest(self) -> Dict[str, Any]:
        return deepcopy(self._manifest)

    @property
    def sources(self) -> Tuple[Dict[str, Any], ...]:
        return tuple(_model_dict(source) for source in self._sources)

    @property
    def versions(self) -> Tuple[Dict[str, Any], ...]:
        return tuple(_model_dict(profile) for profile in self._versions)

    @property
    def rules(self) -> Tuple[Dict[str, Any], ...]:
        return tuple(_model_dict(rule) for rule in self._rules)

    @property
    def validation_summary(self) -> Dict[str, Any]:
        return dict(self._validation_summary)

    def get_source(self, source_id: str) -> Dict[str, Any]:
        try:
            return _model_dict(self._sources_by_id[source_id])
        except KeyError as exc:
            raise KeyError("Unknown standards source: {}".format(source_id)) from exc

    def get_version_profile(self, version: str = "current") -> Dict[str, Any]:
        key = str(version).strip().casefold()
        if key in {"current", "latest"}:
            key = self._manifest["default_version"].casefold()
        try:
            return _model_dict(self._versions_by_name[key])
        except KeyError as exc:
            raise KeyError("Unknown ModSDK version: {}".format(version)) from exc

    def get_version_changes(self) -> Dict[str, Any]:
        """读取完整官方版本比较快照，运行时不重新抓取或推断版本变更。"""
        return self._read_json(self._manifest["snapshot_files"]["version_changes"])

    def get_rule(self, rule_id: str) -> Dict[str, Any]:
        try:
            return _model_dict(self._rules_by_id[rule_id])
        except KeyError as exc:
            raise KeyError("Unknown standards rule: {}".format(rule_id)) from exc

    @staticmethod
    def _validate_filter(
        name: str, values: Optional[FrozenSet[str]], allowed: Iterable[str]
    ) -> None:
        if values is None:
            return
        unknown = sorted(values - set(allowed))
        if unknown:
            raise ValueError(
                "Unknown {} filter values: {}".format(name, ", ".join(unknown))
            )

    def list_rules(
        self,
        version: Optional[str] = None,
        domains: Optional[Iterable[str]] = None,
        sides: Optional[Iterable[str]] = None,
        artifact_types: Optional[Iterable[str]] = None,
        severities: Optional[Iterable[str]] = None,
        authorities: Optional[Iterable[str]] = None,
        rule_ids: Optional[Iterable[str]] = None,
        query: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        domain_filter = _as_values(domains)
        side_filter = _as_values(sides)
        artifact_filter = _as_values(artifact_types)
        severity_filter = _as_values(severities)
        authority_filter = _as_values(authorities)
        id_filter = _as_values(rule_ids)
        self._validate_filter("domain", domain_filter, get_args(Domain))
        self._validate_filter("side", side_filter, get_args(Side))
        self._validate_filter("artifact type", artifact_filter, get_args(ArtifactType))
        self._validate_filter("severity", severity_filter, get_args(Severity))
        self._validate_filter("authority", authority_filter, get_args(Authority))
        self._validate_filter("rule id", id_filter, self._rules_by_id)

        canonical_version = None
        if version is not None:
            canonical_version = self.get_version_profile(version)["version"]
        query_text = str(query).strip().casefold() if query is not None else ""

        selected = []
        for rule in self._rules:
            if canonical_version is not None and canonical_version not in rule.versions:
                continue
            if domain_filter is not None and rule.domain not in domain_filter:
                continue
            if side_filter is not None and not side_filter.intersection(rule.sides):
                continue
            if artifact_filter is not None and not artifact_filter.intersection(
                rule.artifact_types
            ):
                continue
            if severity_filter is not None and rule.severity not in severity_filter:
                continue
            if authority_filter is not None and rule.authority not in authority_filter:
                continue
            if id_filter is not None and rule.id not in id_filter:
                continue
            if query_text:
                searchable = "\n".join(
                    (rule.id, rule.title)
                    + rule.keywords
                    + rule.conditions
                    + rule.do
                    + rule.avoid
                ).casefold()
                if query_text not in searchable:
                    continue
            selected.append(_model_dict(rule))
        return sorted(selected, key=lambda item: item["id"])

    def python_module_whitelist(self) -> FrozenSet[str]:
        return frozenset(self._whitelist_snapshot["modules"])

    def python_module_whitelist_snapshot(self) -> Dict[str, Any]:
        return deepcopy(self._whitelist_snapshot)

    def is_python_module_allowed(
        self,
        module_name: str,
        local_module_roots: Optional[Iterable[str]] = None,
    ) -> bool:
        if not isinstance(module_name, str) or not _MODULE_NAME_RE.fullmatch(module_name):
            return False
        if module_name in self.python_module_whitelist():
            return True
        for root in local_module_roots or ():
            if not isinstance(root, str) or not _MODULE_NAME_RE.fullmatch(root):
                continue
            if module_name == root or module_name.startswith(root + "."):
                return True
        return False


@lru_cache(maxsize=1)
def get_registry() -> StandardsRegistry:
    """Return the process-wide validated standards registry."""

    return StandardsRegistry()


def validate_registry() -> Dict[str, Any]:
    """Validate every registry file and return stable content counts."""

    return get_registry().validation_summary


def list_standard_rules(
    version: Optional[str] = None,
    domains: Optional[Iterable[str]] = None,
    sides: Optional[Iterable[str]] = None,
    artifact_types: Optional[Iterable[str]] = None,
    severities: Optional[Iterable[str]] = None,
    authorities: Optional[Iterable[str]] = None,
    rule_ids: Optional[Iterable[str]] = None,
    query: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """List rules using exact version, domain, side, and artifact filters."""

    return get_registry().list_rules(
        version=version,
        domains=domains,
        sides=sides,
        artifact_types=artifact_types,
        severities=severities,
        authorities=authorities,
        rule_ids=rule_ids,
        query=query,
    )


def get_standard_rule(rule_id: str) -> Dict[str, Any]:
    return get_registry().get_rule(rule_id)


def get_version_profile(version: str = "current") -> Dict[str, Any]:
    return get_registry().get_version_profile(version)


def get_python_module_whitelist() -> FrozenSet[str]:
    """Return the immutable set of 456 exact, repository-snapshotted paths."""

    return get_registry().python_module_whitelist()


def get_python_module_whitelist_snapshot() -> Dict[str, Any]:
    return get_registry().python_module_whitelist_snapshot()


def is_python_module_allowed(
    module_name: str,
    local_module_roots: Optional[Iterable[str]] = None,
) -> bool:
    return get_registry().is_python_module_allowed(module_name, local_module_roots)


__all__ = [
    "ArtifactType",
    "Authority",
    "Domain",
    "Enforcement",
    "REGISTRY_ROOT",
    "Rule",
    "RuntimeEvidenceStatus",
    "Severity",
    "Side",
    "Source",
    "StandardsRegistry",
    "StandardsRegistryError",
    "VersionProfile",
    "VersionStatus",
    "find_local_coupling_markers",
    "get_python_module_whitelist",
    "get_python_module_whitelist_snapshot",
    "get_registry",
    "get_standard_rule",
    "get_version_profile",
    "is_python_module_allowed",
    "list_standard_rules",
    "validate_registry",
]
