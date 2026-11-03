"""Build deterministic guidance documents from the standards registry."""

from __future__ import annotations

import json
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from .standards import find_local_coupling_markers, get_registry


GUIDANCE_SCHEMA_VERSION = "1.0"
GUIDANCE_TOP_LEVEL_FIELDS = (
    "schema_version",
    "request",
    "target",
    "strategy",
    "rules",
    "source_boundaries",
    "verify_next",
)
RULE_PROJECTION_FIELDS = (
    "id",
    "title",
    "severity",
    "enforcement",
    "authority",
    "applies_when",
    "do",
    "avoid",
    "source_ids",
)

_SEVERITY_ORDER = {"critical": 0, "error": 1, "warning": 2, "info": 3}
_ENFORCEMENT_ORDER = {"block": 0, "warn": 1, "guide": 2, "manual": 3}
_MAX_RULES = 12
_VERIFY_TOOLS = frozenset(
    ("search_api", "get_api_detail", "search_docs", "get_document_section")
)


def _normalize_values(value: Optional[Iterable[str]]) -> Optional[Tuple[str, ...]]:
    if value is None:
        return None
    if isinstance(value, str):
        values = (value,)
    else:
        values = tuple(str(item) for item in value)
    return tuple(sorted(set(item.strip() for item in values if item.strip())))


def _target_filter(
    target: Mapping[str, Any],
    explicit: Optional[Iterable[str]],
    key: str,
) -> Optional[Tuple[str, ...]]:
    if explicit is not None:
        return _normalize_values(explicit)
    return _normalize_values(target.get(key))


def _validate_filter(name: str, values: Optional[Sequence[str]], allowed: Sequence[str]) -> None:
    if values is None:
        return
    unknown = sorted(set(values) - set(allowed))
    if unknown:
        raise ValueError(
            "Unknown {} filter values: {}".format(name, ", ".join(unknown))
        )


def _rule_relevance(rule: Mapping[str, Any], request_text: str) -> int:
    text = request_text.casefold()
    if not text:
        return 0
    score = 0
    title = str(rule["title"]).casefold()
    if title in text or text in title:
        score += 12
    for keyword in rule["keywords"]:
        folded = str(keyword).casefold()
        if folded in text:
            score += 5
    for condition in rule["conditions"]:
        folded = str(condition).casefold()
        if folded in text or text in folded:
            score += 2
    if str(rule["domain"]).casefold() in text:
        score += 1
    return score


def _project_rule(rule: Mapping[str, Any]) -> Dict[str, Any]:
    projected = {
        "id": rule["id"],
        "title": rule["title"],
        "severity": rule["severity"],
        "enforcement": rule["enforcement"],
        "authority": rule["authority"],
        "applies_when": list(rule["conditions"]),
        "do": list(rule["do"]),
        "avoid": list(rule["avoid"]),
        "source_ids": list(rule["source_ids"]),
        "domain": rule["domain"],
        "sides": list(rule["sides"]),
        "artifact_types": list(rule["artifact_types"]),
        "versions": list(rule["versions"]),
        "detector": rule["detector"],
    }
    return projected


def _selected_sources(
    registry: Any,
    rules: Sequence[Mapping[str, Any]],
    version_profile: Mapping[str, Any],
) -> List[Dict[str, Any]]:
    source_ids = set(version_profile["source_ids"])
    for rule in rules:
        source_ids.update(rule["source_ids"])
    fields = (
        "id",
        "title",
        "authority",
        "url",
        "last_modified",
        "retrieved_at",
        "notes",
    )
    selected = []
    for source_id in sorted(source_ids):
        source = registry.get_source(source_id)
        selected.append({field: source[field] for field in fields})
    return selected


def _verify_next(
    rules: Sequence[Mapping[str, Any]],
    request_text: str,
) -> List[Dict[str, Any]]:
    query = request_text.strip() or "ModSDK 开发规则"
    steps: List[Dict[str, Any]] = []
    api_domains = {"architecture", "api_event", "json_ui", "performance", "multiplayer"}
    if any(rule["domain"] in api_domains for rule in rules):
        steps.extend(
            [
                {
                    "tool": "search_api",
                    "arguments": {"query": query, "entry_type": "all", "limit": 5},
                    "purpose": "定位目标 API 或事件的精确名称。",
                },
                {
                    "tool": "get_api_detail",
                    "arguments": {"name": "<search_api 返回的精确名称>"},
                    "purpose": "复核端侧、参数、返回值和事件字段。",
                },
            ]
        )
    steps.extend(
        [
            {
                "tool": "search_docs",
                "arguments": {"query": query, "limit": 10, "fuzzy": True},
                "purpose": "定位规则对应的官方说明、备注和 JSON 文档。",
            },
            {
                "tool": "get_document_section",
                "arguments": {
                    "filepath": "<search_docs 返回的文档路径>",
                    "section_title": "<需要复核的章节标题>",
                },
                "purpose": "读取目标章节并确认适用条件与版本边界。",
            },
        ]
    )
    if any(step["tool"] not in _VERIFY_TOOLS for step in steps):
        raise AssertionError("verify_next contains an unknown MCP tool")
    return steps


def build_guidance(
    request: str,
    target: Optional[Mapping[str, Any]] = None,
    version: str = "current",
    domains: Optional[Iterable[str]] = None,
    sides: Optional[Iterable[str]] = None,
    artifact_types: Optional[Iterable[str]] = None,
    severities: Optional[Iterable[str]] = None,
    authorities: Optional[Iterable[str]] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """Return a stable guidance object with explicit source and version boundaries."""

    if not isinstance(request, str):
        raise TypeError("request must be a string")
    target_input: Mapping[str, Any] = target or {}
    if not isinstance(target_input, Mapping):
        raise TypeError("target must be a mapping")
    if find_local_coupling_markers(request) or find_local_coupling_markers(target_input):
        raise ValueError("Guidance input contains forbidden local coupling markers")
    if limit is not None and (
        not isinstance(limit, int)
        or isinstance(limit, bool)
        or not 1 <= limit <= _MAX_RULES
    ):
        raise ValueError("limit must be an integer between 1 and {}".format(_MAX_RULES))

    registry = get_registry()
    manifest = registry.manifest
    try:
        version_profile = registry.get_version_profile(version)
    except KeyError as exc:
        raise ValueError("Unknown ModSDK version: {}".format(version)) from exc
    domain_filter = _target_filter(target_input, domains, "domains")
    side_filter = _target_filter(target_input, sides, "sides")
    artifact_filter = _target_filter(target_input, artifact_types, "artifact_types")
    severity_filter = _target_filter(target_input, severities, "severities")
    authority_filter = _target_filter(target_input, authorities, "authorities")

    _validate_filter("domain", domain_filter, manifest["domains"])
    _validate_filter("side", side_filter, manifest["sides"])
    _validate_filter("artifact type", artifact_filter, manifest["artifact_types"])
    _validate_filter("severity", severity_filter, manifest["severities"])
    authority_ids = [row["id"] for row in manifest["authorities"]]
    _validate_filter("authority", authority_filter, authority_ids)

    candidates = registry.list_rules(
        version=version_profile["version"],
        domains=domain_filter,
        sides=side_filter,
        artifact_types=artifact_filter,
        severities=severity_filter,
        authorities=authority_filter,
    )
    scored = [(rule, _rule_relevance(rule, request)) for rule in candidates]
    relevant = [(rule, score) for rule, score in scored if score > 0]
    explicit_scope = any(
        value is not None
        for value in (
            domain_filter,
            side_filter,
            artifact_filter,
            severity_filter,
            authority_filter,
        )
    )
    if explicit_scope:
        selected_scored = scored
        selection_mode = "explicit_filters"
    elif relevant:
        selected_scored = relevant
        selection_mode = "keyword_relevance"
    elif not request.strip():
        selected_scored = scored
        selection_mode = "version_default"
    else:
        selected_scored = scored
        selection_mode = "version_fallback"

    authority_rank = {row["id"]: row["rank"] for row in manifest["authorities"]}
    selected_scored.sort(
        key=lambda item: (
            -item[1],
            _SEVERITY_ORDER[item[0]["severity"]],
            _ENFORCEMENT_ORDER[item[0]["enforcement"]],
            -authority_rank[item[0]["authority"]],
            item[0]["id"],
        )
    )
    if limit is not None:
        selected_scored = selected_scored[:limit]
    selected_rules = [rule for rule, _score in selected_scored]

    normalized_target = {
        "version": version_profile["version"],
        "bedrock_version": version_profile["bedrock_version"],
        "domains": list(domain_filter or ()),
        "sides": list(side_filter or ()),
        "artifact_types": list(artifact_filter or ()),
        "severities": list(severity_filter or ()),
        "authorities": list(authority_filter or ()),
    }
    strategy = {
        "selection_mode": selection_mode,
        "selected_rule_count": len(selected_rules),
        "default_import_policy": manifest["content_policy"]["default_import_policy"],
        "blocking_enforcements": ["block"],
        "authority_order": [
            row["id"]
            for row in sorted(
                manifest["authorities"], key=lambda item: item["rank"], reverse=True
            )
        ],
    }
    source_boundaries = {
        "api_reference_version": manifest["default_version"],
        "version_status": version_profile["status"],
        "runtime_evidence_status": version_profile["runtime_evidence_status"],
        "runtime_boundary": version_profile["source_boundary"],
        "sources": _selected_sources(registry, selected_rules, version_profile),
    }
    guidance = {
        "schema_version": GUIDANCE_SCHEMA_VERSION,
        "request": {"text": request.strip()},
        "target": normalized_target,
        "strategy": strategy,
        "rules": [_project_rule(rule) for rule in selected_rules],
        "source_boundaries": source_boundaries,
        "verify_next": _verify_next(selected_rules, request),
    }
    if tuple(guidance) != GUIDANCE_TOP_LEVEL_FIELDS:
        raise AssertionError("Guidance top-level schema order changed")
    if find_local_coupling_markers(guidance):
        raise ValueError("Generated guidance contains forbidden local coupling markers")
    return guidance


def render_guidance_json(
    request: str,
    target: Optional[Mapping[str, Any]] = None,
    version: str = "current",
    domains: Optional[Iterable[str]] = None,
    sides: Optional[Iterable[str]] = None,
    artifact_types: Optional[Iterable[str]] = None,
    severities: Optional[Iterable[str]] = None,
    authorities: Optional[Iterable[str]] = None,
    limit: Optional[int] = None,
) -> str:
    """Serialize guidance deterministically without network or environment access."""

    guidance = build_guidance(
        request=request,
        target=target,
        version=version,
        domains=domains,
        sides=sides,
        artifact_types=artifact_types,
        severities=severities,
        authorities=authorities,
        limit=limit,
    )
    return json.dumps(guidance, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


__all__ = [
    "GUIDANCE_SCHEMA_VERSION",
    "GUIDANCE_TOP_LEVEL_FIELDS",
    "RULE_PROJECTION_FIELDS",
    "build_guidance",
    "render_guidance_json",
]
