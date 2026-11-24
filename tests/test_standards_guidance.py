# -*- coding: utf-8 -*-

import hashlib
import json
import unittest
from pathlib import Path

from pydantic import ValidationError

from modsdk_mcp.guidance import (
    GUIDANCE_TOP_LEVEL_FIELDS,
    RULE_PROJECTION_FIELDS,
    build_guidance,
    render_guidance_json,
)
from modsdk_mcp.standards import (
    Rule,
    Source,
    StandardsRegistry,
    VersionProfile,
    find_local_coupling_markers,
    get_python_module_whitelist,
    get_python_module_whitelist_snapshot,
    get_standard_rule,
    get_version_profile,
    is_python_module_allowed,
    list_standard_rules,
    validate_registry,
)
from modsdk_mcp.validation import get_registered_detectors


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_ROOT = ROOT / "standard" / "registry"


def local_coupling_markers():
    return (
        "E:" + chr(92) + "JJU",
        "np-mod-" + "work-space",
        "Nir" + "vana",
        chr(0x6D85) + chr(0x69C3),
    )


class StandardsRegistryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = StandardsRegistry(REGISTRY_ROOT)
        cls.manifest = cls.registry.manifest

    def test_registry_schema_and_references_are_valid(self):
        summary = validate_registry()
        self.assertEqual(summary["schema_version"], "1.0")
        self.assertEqual(summary["rule_count"], 61)
        self.assertEqual(summary["source_count"], 6)
        self.assertEqual(summary["version_count"], 2)
        self.assertEqual(summary["python_module_count"], 456)

        required = set(self.manifest["required_rule_fields"])
        detectors = set(self.manifest["detectors"])
        registered_detectors = {spec.name for spec in get_registered_detectors()}
        self.assertEqual(detectors, registered_detectors)
        source_ids = {source["id"] for source in self.registry.sources}
        for rule in self.registry.rules:
            self.assertTrue(required.issubset(rule), rule["id"])
            self.assertTrue(set(rule["source_ids"]).issubset(source_ids), rule["id"])
            if rule["detector"] is not None:
                self.assertIn(rule["detector"], detectors, rule["id"])

    def test_source_and_version_required_fields(self):
        source_fields = set(self.manifest["required_source_fields"])
        version_fields = set(self.manifest["required_version_profile_fields"])
        for source in self.registry.sources:
            self.assertTrue(source_fields.issubset(source), source["id"])
        for profile in self.registry.versions:
            self.assertTrue(version_fields.issubset(profile), profile["version"])

        profile = get_version_profile("V3.9")
        self.assertEqual(profile["version"], "3.9")
        self.assertEqual(profile["bedrock_version"], "1.21.120")
        self.assertEqual(profile["released_at"], "2026-07-22")
        self.assertEqual(profile["runtime_evidence_status"], "unreviewed")
        self.assertIn("3.9", profile["aliases"])
        self.assertEqual(
            profile["source_boundary"],
            "尚无可读的 ModSDK 3.9 Python 运行时源码复核",
        )
        current_profile = get_version_profile("current")
        self.assertEqual(current_profile["version"], "3.10")
        self.assertEqual(current_profile["bedrock_version"], "1.21.130")
        self.assertEqual(current_profile["status"], "stable")
        self.assertEqual(current_profile["released_at"], "2026-10-28")
        self.assertEqual(current_profile["runtime_evidence_status"], "unreviewed")

    def test_python_whitelist_is_exact_immutable_snapshot(self):
        whitelist = get_python_module_whitelist()
        self.assertIsInstance(whitelist, frozenset)
        self.assertEqual(len(whitelist), 456)
        for module in (
            "__future__",
            "ast",
            "json",
            "mod.client.extraClientApi",
            "mod.server.extraServerApi",
            "client.component.itemCompClient",
            "server.component.itemCompServer",
        ):
            self.assertIn(module, whitelist)
        for module in ("os", "sys", "requests", "numpy", "yaml", "PIL"):
            self.assertNotIn(module, whitelist)
            self.assertFalse(is_python_module_allowed(module))
        self.assertFalse(is_python_module_allowed("mod.client.notListed"))

        snapshot = get_python_module_whitelist_snapshot()
        module_text = "\n".join(snapshot["modules"]) + "\n"
        digest = hashlib.sha256(module_text.encode("utf-8")).hexdigest()
        self.assertEqual(digest, snapshot["modules_sha256"])
        self.assertEqual(snapshot["module_count"], 456)
        self.assertEqual(len(snapshot["entries"]), 456)
        self.assertEqual(
            [entry["normalized_name"] for entry in snapshot["entries"]],
            snapshot["modules"],
        )
        ast_entry = next(
            entry for entry in snapshot["entries"] if entry["normalized_name"] == "ast"
        )
        self.assertEqual(ast_entry["raw_display"], "ast（3.3新增）")

    def test_local_module_roots_are_explicit_and_segment_aware(self):
        self.assertTrue(is_python_module_allowed("demo", ["demo"]))
        self.assertTrue(is_python_module_allowed("demo.client.system", ["demo"]))
        self.assertFalse(is_python_module_allowed("demo_extra", ["demo"]))
        self.assertFalse(is_python_module_allowed("demo-client", ["demo"]))

    def test_version_domain_side_and_artifact_filters(self):
        rules = list_standard_rules(
            version="BE1.21.120",
            domains=["json_ui"],
            sides=["client"],
            artifact_types=["ui_python"],
        )
        self.assertTrue(rules)
        self.assertTrue(all(rule["domain"] == "json_ui" for rule in rules))
        self.assertTrue(all("client" in rule["sides"] for rule in rules))
        self.assertTrue(all("ui_python" in rule["artifact_types"] for rule in rules))
        self.assertEqual(
            list_standard_rules(version="3.9", domains=["json_ui"], sides=["server"]),
            [],
        )

        python_rules = list_standard_rules(
            version="3.9",
            domains="python",
            authorities="official_doc",
        )
        self.assertTrue(python_rules)
        self.assertTrue(
            all(rule["authority"] == "official_doc" for rule in python_rules)
        )
        for domain in ("api_event", "performance", "multiplayer"):
            self.assertTrue(
                list_standard_rules(version="current", domains=[domain]),
                domain,
            )
        self.assertTrue(
            list_standard_rules(version="3.9", domains=["json_content"], sides=["common"])
        )

    def test_authority_grades_and_representative_rules(self):
        authorities = self.manifest["authorities"]
        ranks = [row["rank"] for row in authorities]
        self.assertEqual(ranks, sorted(ranks, reverse=True))
        self.assertEqual(
            {row["id"] for row in authorities},
            {
                "official_runtime",
                "official_doc",
                "curated_policy",
                "runtime_evidence",
                "bedrock_reference",
                "community_reference",
            },
        )
        self.assertEqual(
            set(self.manifest["enforcements"]),
            {"block", "warn", "guide", "manual"},
        )
        self.assertEqual(get_standard_rule("UI-PATH-001")["authority"], "official_doc")
        self.assertEqual(get_standard_rule("UI-PERCENT-001")["authority"], "runtime_evidence")
        self.assertEqual(get_standard_rule("UI-ARCH-001")["authority"], "curated_policy")
        self.assertEqual(get_standard_rule("UI-VISUAL-001")["enforcement"], "manual")
        self.assertEqual(get_standard_rule("PY-ENCODING-001")["enforcement"], "block")
        self.assertEqual(get_standard_rule("PY-ENCODING-001")["detector"], "python.encoding")
        self.assertEqual(get_standard_rule("JSON-ID-001")["enforcement"], "block")
        self.assertEqual(get_standard_rule("JSON-BIOME-001")["detector"], "json.biome_namespace")

    def test_strict_models_reject_extra_fields_and_invalid_enums(self):
        rule = get_standard_rule("PY-STRING-001")
        source = self.registry.sources[0]
        profile = get_version_profile("3.9")

        for model, payload in (
            (Rule, rule),
            (Source, source),
            (VersionProfile, profile),
        ):
            self.assertTrue(model.model_config["strict"])
            self.assertTrue(model.model_config["frozen"])
            self.assertEqual(model.model_config["extra"], "forbid")
            invalid = dict(payload)
            invalid["unexpected"] = True
            with self.subTest(model=model.__name__), self.assertRaises(ValidationError):
                model.model_validate(invalid, strict=True)

        invalid_rule = dict(rule, authority="unverified")
        with self.assertRaises(ValidationError):
            Rule.model_validate(invalid_rule, strict=True)
        invalid_rule = dict(rule, enforcement="invalid_enforcement")
        with self.assertRaises(ValidationError):
            Rule.model_validate(invalid_rule, strict=True)
        invalid_source = dict(source, authority="unverified")
        with self.assertRaises(ValidationError):
            Source.model_validate(invalid_source, strict=True)
        invalid_profile = dict(profile, status="current")
        with self.assertRaises(ValidationError):
            VersionProfile.model_validate(invalid_profile, strict=True)

    def test_runtime_evidence_and_advisory_domains_cannot_block(self):
        for rule in self.registry.rules:
            if rule["authority"] == "runtime_evidence":
                self.assertIn(rule["enforcement"], {"warn", "manual"}, rule["id"])
            if rule["domain"] in {"json_ui", "performance"}:
                self.assertNotEqual(rule["enforcement"], "block", rule["id"])
            if "LIFE" in rule["id"]:
                self.assertNotEqual(rule["enforcement"], "block", rule["id"])

        runtime_rule = get_standard_rule("UI-PERCENT-001")
        runtime_rule["enforcement"] = "block"
        with self.assertRaises(ValidationError):
            Rule.model_validate(runtime_rule, strict=True)

    def test_portability_block_is_enforced_at_registry_boundary(self):
        rule = get_standard_rule("ARCH-PORTABILITY-001")
        self.assertEqual(rule["enforcement"], "block")
        self.assertIsNone(rule["detector"])
        self.assertTrue(
            any("registry 与 guidance 边界" in condition for condition in rule["conditions"])
        )
        self.assertTrue(find_local_coupling_markers(local_coupling_markers()[0]))

    def test_product_files_reject_local_coupling(self):
        product_files = [
            ROOT / "README.md",
            ROOT / "tests" / "test_standards_guidance.py",
        ]
        product_files += sorted((ROOT / "modsdk_mcp").glob("*.py"))
        product_files += sorted((ROOT / "skills").glob("*.md"))
        product_files += sorted(REGISTRY_ROOT.rglob("*.json"))
        for path in product_files:
            text = path.read_text(encoding="utf-8")
            for marker in local_coupling_markers():
                self.assertNotIn(marker, text, str(path))


class GuidanceTest(unittest.TestCase):
    def test_guidance_has_fixed_top_level_and_rule_projection(self):
        guidance = build_guidance(
            "检查 JSON UI 的 ScrollView 和 Button",
            version="3.9",
            domains=["json_ui"],
            sides=["client"],
            artifact_types=["ui_json", "ui_python"],
        )
        self.assertEqual(tuple(guidance), GUIDANCE_TOP_LEVEL_FIELDS)
        self.assertTrue(guidance["rules"])
        self.assertTrue(
            all(
                set(RULE_PROJECTION_FIELDS).issubset(projected)
                for projected in guidance["rules"]
            )
        )
        self.assertTrue(
            all(projected["domain"] == "json_ui" for projected in guidance["rules"])
        )
        self.assertEqual(
            guidance["source_boundaries"]["runtime_boundary"],
            "尚无可读的 ModSDK 3.9 Python 运行时源码复核",
        )

    def test_guidance_json_is_stable_and_utf8_preserving(self):
        arguments = {
            "request": "检查 import 白名单",
            "version": "3.9.x",
            "domains": ["python"],
            "sides": ["client"],
            "artifact_types": ["python"],
            "limit": 3,
        }
        first = render_guidance_json(**arguments)
        second = render_guidance_json(**arguments)
        self.assertEqual(first, second)
        self.assertTrue(first.endswith("\n"))
        self.assertIn("模块白名单", first)
        self.assertEqual(json.loads(first), build_guidance(**arguments))

    def test_guidance_rejects_unknown_filters(self):
        with self.assertRaisesRegex(ValueError, "Unknown ModSDK version"):
            build_guidance("检查", version="9.9")
        for invalid_limit in (0, 13, True, 1.5):
            with self.subTest(limit=invalid_limit), self.assertRaisesRegex(
                ValueError, "between 1 and 12"
            ):
                build_guidance("检查", limit=invalid_limit)
        with self.assertRaisesRegex(ValueError, "between 1 and 12"):
            render_guidance_json("检查", limit=13)
        with self.assertRaises(ValueError):
            build_guidance("检查", domains=["unknown_domain"])
        with self.assertRaises(ValueError):
            build_guidance("检查", sides=["unknown_side"])
        with self.assertRaises(ValueError):
            build_guidance("检查", artifact_types=["unknown_artifact"])

    def test_guidance_rejects_local_coupling_inputs(self):
        local_path = local_coupling_markers()[0]
        with self.assertRaises(ValueError):
            build_guidance("检查 " + local_path)
        with self.assertRaises(ValueError):
            build_guidance("检查", target={"label": local_path})

    def test_runtime_boundary_is_not_upgraded_to_runtime_confirmation(self):
        guidance = build_guidance("生成服务端 Python", domains=["python"])
        boundaries = guidance["source_boundaries"]
        self.assertEqual(boundaries["runtime_evidence_status"], "unreviewed")
        self.assertEqual(
            {step["tool"] for step in guidance["verify_next"]},
            {"search_docs", "get_document_section"},
        )

    def test_verify_next_uses_only_real_mcp_tools_and_structured_arguments(self):
        guidance = build_guidance(
            "核验客户端 UI API",
            domains=["json_ui"],
            sides=["client"],
        )
        allowed_tools = {
            "search_api",
            "get_api_detail",
            "search_docs",
            "get_document_section",
        }
        self.assertTrue(guidance["verify_next"])
        for step in guidance["verify_next"]:
            self.assertEqual(set(step), {"tool", "arguments", "purpose"})
            self.assertIn(step["tool"], allowed_tools)
            self.assertIsInstance(step["arguments"], dict)
            self.assertIsInstance(step["purpose"], str)
            self.assertTrue(step["purpose"])

    def test_new_addon_package_guidance_hits_package_and_manifest_rules(self):
        guidance = build_guidance(
            "新建组件包目录结构与 manifest.json 清单配置",
            version="current",
            limit=8,
        )
        hit_ids = {rule["id"] for rule in guidance["rules"]}
        self.assertIn("ARCH-PACKAGE-001", hit_ids)
        self.assertIn("JSON-MANIFEST-001", hit_ids)


if __name__ == "__main__":
    unittest.main()
