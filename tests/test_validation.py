# -*- coding: utf-8 -*-

import json
import unittest

from modsdk_mcp.validation import (
    Artifact,
    DETECTOR_REGISTRY,
    ValidationIssue,
    ValidationReport,
    get_registered_detectors,
    register_detector,
    validate_artifact,
    validate_artifacts,
    validate_json,
    validate_python,
)


UTF8_HEADER = "# -*- coding: utf-8 -*-\n"


def issue_codes(report):
    return [issue.code for issue in report.issues]


def python_source(body):
    return UTF8_HEADER + body


def block_source(format_version, components):
    return json.dumps(
        {
            "format_version": format_version,
            "minecraft:block": {
                "description": {"identifier": "demo:test_block"},
                "components": components,
            },
        },
        ensure_ascii=False,
    )


class ValidationModelTest(unittest.TestCase):
    def test_report_properties_and_serialization(self):
        artifact = Artifact("value", filename="demo.txt")
        critical = ValidationIssue("DEMO", "broken", artifact.filename)
        warning = ValidationIssue("WARN", "careful", artifact.filename, severity="warning")
        report = ValidationReport((artifact,), (critical, warning))

        self.assertTrue(report.blocked)
        self.assertTrue(report.has_warnings)
        self.assertEqual([critical], list(report.errors))
        self.assertEqual([warning], list(report.warnings))
        result = report.to_dict()
        self.assertEqual("critical", result["issues"][0]["severity"])
        self.assertEqual(1, result["artifact_count"])
        self.assertEqual(2, result["issue_count"])

    def test_report_accepts_legacy_error_as_blocking(self):
        artifact = Artifact("value")
        issue = ValidationIssue("OLD", "legacy", artifact.filename, severity="error")
        self.assertTrue(ValidationReport((artifact,), (issue,)).blocked)

    def test_detector_registry_is_extensible_and_rejects_duplicates(self):
        name = "test.temporary_detector"

        try:
            @register_detector(name, ("text",))
            def detector(artifact, context):
                del context
                return [ValidationIssue("TEMP", "temporary", artifact.filename, severity="warning")]

            self.assertIs(detector, DETECTOR_REGISTRY[name].detector)
            self.assertIn(name, [spec.name for spec in get_registered_detectors()])
            report = validate_artifact(Artifact("value", artifact_type="text"))
            self.assertEqual(["TEMP"], issue_codes(report))
            with self.assertRaises(ValueError):
                register_detector(name, ("text",))(lambda artifact, context: [])
        finally:
            DETECTOR_REGISTRY.pop(name, None)

    def test_json_ui_uses_json_detectors(self):
        artifact = Artifact("{", filename="ui.json", artifact_type="json_ui")
        self.assertEqual("json", artifact.kind)
        report = validate_artifact(artifact)
        self.assertIn("JSON_PARSE_ERROR", issue_codes(report))
        self.assertEqual("critical", report.issues[0].severity)

    def test_non_text_artifact_content_returns_a_stable_issue(self):
        report = validate_artifact(Artifact({"value": 1}, artifact_type="json"))

        self.assertEqual(["ARTIFACT_CONTENT_TYPE"], issue_codes(report))
        self.assertTrue(report.blocked)

    def test_batch_validation_materializes_whitelist_iterables_once(self):
        artifacts = (
            Artifact(python_source("import approved.module\n"), "first.py", "python"),
            Artifact(python_source("import approved.module\n"), "second.py", "python"),
        )
        whitelist = (module for module in ("approved.module",))
        report = validate_artifacts(artifacts, whitelist=whitelist)

        self.assertNotIn("PY_IMPORT_NOT_WHITELISTED", issue_codes(report))


class PythonValidationTest(unittest.TestCase):
    def test_encoding_declaration_is_required_and_must_be_utf8(self):
        missing = validate_python("value = 1\n")
        wrong = validate_python("# coding: gbk\nvalue = 1\n")
        valid = validate_python("#!/usr/bin/env python\n# coding=utf8\nvalue = 1\n")

        self.assertIn("PY_ENCODING_MISSING", issue_codes(missing))
        self.assertIn("PY_ENCODING_NOT_UTF8", issue_codes(wrong))
        self.assertNotIn("PY_ENCODING_MISSING", issue_codes(valid))
        self.assertNotIn("PY_ENCODING_NOT_UTF8", issue_codes(valid))
        self.assertTrue(all(issue.severity == "critical" for issue in missing.issues))

    def test_non_utf8_bytes_are_rejected_before_detectors(self):
        report = validate_python(b"# coding: utf-8\nname = '\xff'\n")
        self.assertEqual(["ARTIFACT_NOT_UTF8"], issue_codes(report))
        self.assertTrue(report.blocked)

    def test_unpaired_surrogate_string_is_reported_as_not_utf8(self):
        report = validate_python(UTF8_HEADER + "# " + chr(0xDCFF) + "\n")

        self.assertEqual(["ARTIFACT_NOT_UTF8"], issue_codes(report))
        self.assertEqual("critical", report.issues[0].severity)

    def test_tokenize_error_is_reported_without_internal_failure(self):
        report = validate_python(
            python_source("if True:\n    value = 1\n  invalid_indent = 2\n")
        )

        self.assertIn("PY_TOKENIZE_ERROR", issue_codes(report))
        self.assertNotIn("VALIDATOR_INTERNAL_ERROR", issue_codes(report))
        issue = next(issue for issue in report.issues if issue.code == "PY_TOKENIZE_ERROR")
        self.assertEqual(4, issue.line)

    def test_tokenize_error_does_not_scan_uncovered_comment_or_string_tail(self):
        report = validate_python(
            python_source(
                "if True:\n"
                "    value = 1\n"
                "  invalid_indent = 2\n"
                '# u"comment only"\n'
                'text = \'ur"ordinary string only"\'\n'
            )
        )

        self.assertIn("PY_TOKENIZE_ERROR", issue_codes(report))
        self.assertNotIn("PY_UNICODE_PREFIX", issue_codes(report))

    def test_real_unicode_prefixes_are_detected(self):
        report = validate_python(
            python_source(
                "first = u'one'\n"
                'second = U"two"\n'
                "third = ur'three'\n"
                'fourth = ru"four"\n'
            )
        )
        issues = [issue for issue in report.issues if issue.code == "PY_UNICODE_PREFIX"]

        self.assertEqual(4, len(issues))
        self.assertEqual({"u", "U", "ur", "ru"}, {issue.details["prefix"] for issue in issues})
        self.assertTrue(all(issue.severity == "critical" for issue in issues))

    def test_unicode_prefix_mentions_in_comments_and_strings_are_ignored(self):
        report = validate_python(
            python_source(
                '# u"comment" and ur"comment"\n'
                'text = \'mentions u"one" and ru"two"\'\n'
                'formatted = f\'u"inside f-string text"\'\n'
            )
        )

        self.assertNotIn("PY_UNICODE_PREFIX", issue_codes(report))
        self.assertIn("PY3_FSTRING", issue_codes(report))

    def test_python3_only_syntax_is_detected(self):
        cases = {
            "PY3_FSTRING": "value = f'{name}'\n",
            "PY3_TYPE_ANNOTATION": "def convert(value: int) -> str:\n    return str(value)\n",
            "PY3_ASYNC": "async def work():\n    await task()\n",
            "PY3_WALRUS": "if (value := fetch()):\n    pass\n",
            "PY3_MATCH": "match value:\n    case 1:\n        pass\n",
            "PY3_YIELD_FROM": "def values():\n    yield from source\n",
            "PY3_RAISE_FROM": "raise RuntimeError() from cause\n",
            "PY3_ZERO_ARG_SUPER": "class Child(Base):\n    def run(self):\n        return super().run()\n",
            "PY3_EXCEPTION_GROUP": "try:\n    work()\nexcept* ValueError:\n    pass\n",
            "PY3_TYPE_ALIAS": "type Identifier = str\n",
            "PY3_TYPE_PARAMETERS": "def identity[T](value: T):\n    return value\n",
            "PY3_FUTURE_FEATURE": "from __future__ import annotations\n",
        }

        for expected, body in cases.items():
            with self.subTest(expected=expected):
                report = validate_python(python_source(body))
                self.assertIn(expected, issue_codes(report))

    def test_python3_syntax_mentions_are_ignored(self):
        report = validate_python(
            python_source(
                '# async def work() and f"value"\n'
                'text = \'match value; x: int; await task(); f"value"\'\n'
            )
        )
        self.assertFalse(any(code.startswith("PY3_") for code in issue_codes(report)))

    def test_python2_identifiers_named_await_or_nonlocal_are_not_keywords(self):
        report = validate_python(
            python_source(
                "await = 1\n"
                "nonlocal = 2\n"
                "obj.await()\n"
                "obj.nonlocal = 3\n"
            )
        )

        self.assertNotIn("PY3_AWAIT", issue_codes(report))
        self.assertNotIn("PY3_NONLOCAL", issue_codes(report))

    def test_python2_supported_future_features_are_accepted(self):
        report = validate_python(
            python_source("from __future__ import absolute_import, print_function\n")
        )

        self.assertNotIn("PY3_FUTURE_FEATURE", issue_codes(report))

    def test_exact_whitelist_does_not_allow_prefixed_fake_modules(self):
        allowed = validate_python(python_source("import mod.server.extraServerApi as serverApi\n"))
        rejected = validate_python(python_source("import mod.server.extraServerApi.fake\n"))

        self.assertNotIn("PY_IMPORT_NOT_WHITELISTED", issue_codes(allowed))
        issue = next(issue for issue in rejected.issues if issue.code == "PY_IMPORT_NOT_WHITELISTED")
        self.assertEqual("mod.server.extraServerApi.fake", issue.details["module"])

    def test_project_module_exception_is_anchored(self):
        report = validate_python(
            python_source("import game.sub\nimport gameplay\n"),
            project_modules=("game",),
        )
        rejected = [
            issue.details["module"]
            for issue in report.issues
            if issue.code == "PY_IMPORT_NOT_WHITELISTED"
        ]

        self.assertEqual(["gameplay"], rejected)

    def test_import_fallback_after_python2_print_keeps_all_aliases(self):
        report = validate_python(
            python_source(
                'print "python two"\n'
                "marker = ur'forces token fallback'\n"
                "import mod.server.extraServerApi as serverApi, os\n"
                "import game.sub as local_game, gameplay\n"
            ),
            project_modules=("game",),
        )
        rejected = {
            issue.details["module"]
            for issue in report.issues
            if issue.code == "PY_IMPORT_NOT_WHITELISTED"
        }

        self.assertEqual({"os", "gameplay"}, rejected)

    def test_explicit_side_rejects_cross_side_import(self):
        server = validate_python(
            python_source("import mod.client.extraClientApi as clientApi\n"),
            side="server",
        )
        client = validate_python(
            python_source("import mod.server.extraServerApi as serverApi\n"),
            side="client",
        )

        self.assertIn("PY_CROSS_SIDE_IMPORT", issue_codes(server))
        self.assertIn("PY_CROSS_SIDE_IMPORT", issue_codes(client))

    def test_cross_side_entry_allows_both_official_apis_only_when_explicit(self):
        code = python_source(
            "import mod.server.extraServerApi as serverApi\n"
            "import mod.client.extraClientApi as clientApi\n"
        )
        cross_side = validate_python(code, side="cross_side")
        automatic = validate_python(code, side="auto")
        common = validate_python(code, side="common")

        self.assertNotIn("PY_CROSS_SIDE_IMPORT", issue_codes(cross_side))
        self.assertIn("PY_CROSS_SIDE_IMPORT", issue_codes(automatic))
        self.assertIn("PY_CROSS_SIDE_IMPORT", issue_codes(common))

    def test_dynamic_imports_are_rejected_but_extra_api_import_module_is_allowed(self):
        report = validate_python(
            python_source(
                "first = __import__('game')\n"
                "second = importlib.import_module('game')\n"
                "third = imp.load_source('game', 'game.py')\n"
                "allowed = clientApi.ImportModule('game.client')\n"
            )
        )
        calls = {
            issue.details["call"]
            for issue in report.issues
            if issue.code == "PY_DYNAMIC_IMPORT"
        }

        self.assertEqual({"__import__", "importlib.import_module", "imp.load_source"}, calls)

    def test_dynamic_import_simple_aliases_are_rejected_in_the_same_scope(self):
        report = validate_python(
            python_source(
                "builtin_loader = __import__\n"
                "first = builtin_loader('game')\n"
                "module_loader = importlib.import_module\n"
                "second = module_loader('game')\n"
            )
        )
        calls = [
            issue.details["call"]
            for issue in report.issues
            if issue.code == "PY_DYNAMIC_IMPORT"
        ]

        self.assertEqual(["__import__", "importlib.import_module"], calls)

    def test_dynamic_import_fallback_works_with_python2_print(self):
        report = validate_python(
            python_source(
                'print "python two"\n'
                "marker = ur'forces token fallback'\n"
                "module = importlib.import_module('game')\n"
                "other = imp.load_module('game', file_obj, path, desc)\n"
            )
        )
        calls = {
            issue.details["call"]
            for issue in report.issues
            if issue.code == "PY_DYNAMIC_IMPORT"
        }

        self.assertEqual({"importlib.import_module", "imp.load_module"}, calls)

    def test_event_callback_rejects_documented_wrong_fields(self):
        report = validate_python(
            python_source(
                "class System(object):\n"
                "    def setup(self):\n"
                "        print 'registering event'\n"
                "        self.ListenForEvent('ns', 'sys', 'ServerItemUseOnEvent', self, self.on_item)\n"
                "    def on_item(self, args):\n"
                "        return args['playerId'], args.get('cancel')\n"
            )
        )
        replacements = {
            (issue.details["field"], issue.details["replacement"])
            for issue in report.issues
            if issue.code == "PY_EVENT_FIELD_MISMATCH"
        }

        self.assertEqual({("playerId", "entityId"), ("cancel", "ret")}, replacements)

    def test_event_callback_accepts_documented_fields(self):
        report = validate_python(
            python_source(
                "class System(object):\n"
                "    def setup(self):\n"
                "        self.ListenForEvent('ns', 'sys', 'ServerItemUseOnEvent', self, self.on_item)\n"
                "    def on_item(self, args):\n"
                "        return args['entityId'], args.get('ret')\n"
            )
        )

        self.assertNotIn("PY_EVENT_FIELD_MISMATCH", issue_codes(report))

    def test_event_like_function_name_without_registration_is_ignored(self):
        report = validate_python(
            python_source(
                "def ServerItemUseOnEvent(args):\n"
                "    return args['playerId']\n"
            )
        )

        self.assertNotIn("PY_EVENT_FIELD_MISMATCH", issue_codes(report))

    def test_same_callback_name_in_different_classes_does_not_cross_bind(self):
        report = validate_python(
            python_source(
                "class ServerSystem(object):\n"
                "    def setup(self):\n"
                "        self.ListenForEvent('ns', 'sys', 'ServerItemUseOnEvent', self, self.on_item)\n"
                "    def on_item(self, args):\n"
                "        return args['entityId']\n"
                "class ClientSystem(object):\n"
                "    def setup(self):\n"
                "        self.ListenForEvent('ns', 'sys', 'ClientItemUseOnEvent', self, self.on_item)\n"
                "    def on_item(self, args):\n"
                "        return args['playerId']\n"
            )
        )

        self.assertNotIn("PY_EVENT_FIELD_MISMATCH", issue_codes(report))

    def test_nested_scope_payload_shadow_is_not_an_event_access(self):
        report = validate_python(
            python_source(
                "class System(object):\n"
                "    def setup(self):\n"
                "        self.ListenForEvent('ns', 'sys', 'ServerItemUseOnEvent', self, self.on_item)\n"
                "    def on_item(self, args):\n"
                "        def nested(args):\n"
                "            return args['playerId']\n"
                "        return args['entityId']\n"
            )
        )

        self.assertNotIn("PY_EVENT_FIELD_MISMATCH", issue_codes(report))

    def test_client_item_event_uses_player_id_and_ret(self):
        report = validate_python(
            python_source(
                "class System(object):\n"
                "    def setup(self):\n"
                "        self.ListenForEvent('ns', 'sys', 'ClientItemUseOnEvent', self, self.on_item)\n"
                "    def on_item(self, args):\n"
                "        return args['entityId'], args.get('cancel')\n"
            )
        )
        replacements = {
            (issue.details["field"], issue.details["replacement"])
            for issue in report.issues
            if issue.code == "PY_EVENT_FIELD_MISMATCH"
        }

        self.assertEqual({("entityId", "playerId"), ("cancel", "ret")}, replacements)

    def test_print_warns_only_in_high_frequency_contexts(self):
        ordinary = validate_python(
            python_source("def save():\n    print('saved')\n")
        )
        frequent = validate_python(
            python_source(
                "def OnTick():\n"
                "    print('tick')\n"
                "def batch(values):\n"
                "    for value in values:\n"
                "        print(value)\n"
            )
        )

        self.assertNotIn("PY_PRINT_HIGH_FREQUENCY", issue_codes(ordinary))
        warnings = [issue for issue in frequent.issues if issue.code == "PY_PRINT_HIGH_FREQUENCY"]
        self.assertEqual(2, len(warnings))
        self.assertTrue(all(issue.severity == "warning" for issue in warnings))
        self.assertTrue(frequent.has_warnings)
        self.assertFalse(frequent.blocked)

    def test_python2_print_statement_warns_in_tick_callback(self):
        report = validate_python(
            python_source("def OnTick():\n    print 'tick'\n")
        )

        issue = next(issue for issue in report.issues if issue.code == "PY_PRINT_HIGH_FREQUENCY")
        self.assertEqual("warning", issue.severity)
        self.assertFalse(report.blocked)


class JsonValidationTest(unittest.TestCase):
    def test_json_parse_error_is_located_and_critical(self):
        report = validate_json('{"value": }')
        issue = next(issue for issue in report.issues if issue.code == "JSON_PARSE_ERROR")

        self.assertEqual("critical", issue.severity)
        self.assertEqual(1, issue.line)
        self.assertGreater(issue.column, 1)

    def test_non_standard_json_numbers_are_rejected(self):
        for constant in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(constant=constant):
                report = validate_json('{"value": ' + constant + "}")
                self.assertIn("JSON_PARSE_ERROR", issue_codes(report))

    def test_json_root_must_be_an_object(self):
        report = validate_json("[]")

        self.assertEqual(["JSON_ROOT_NOT_OBJECT"], issue_codes(report))
        self.assertTrue(report.blocked)

    def test_item_requires_root_identifier_and_format(self):
        missing_root = validate_json("{}", artifact_type="item")
        missing_identifier = validate_json(
            json.dumps({"format_version": "1.10", "minecraft:item": {}}),
            artifact_type="item",
        )
        wrong_format = validate_json(
            json.dumps(
                {
                    "format_version": "1.16.0",
                    "minecraft:item": {"description": {"identifier": "demo:item"}},
                }
            ),
            artifact_type="item",
        )

        self.assertIn("JSON_ROOT_MISSING", issue_codes(missing_root))
        self.assertIn("JSON_IDENTIFIER_MISSING", issue_codes(missing_identifier))
        self.assertIn("JSON_ITEM_FORMAT_VERSION", issue_codes(wrong_format))

    def test_valid_item_uses_lowercase_namespaced_identifier(self):
        valid = validate_json(
            json.dumps(
                {
                    "format_version": "1.10",
                    "minecraft:item": {"description": {"identifier": "demo:test_item"}},
                }
            ),
            artifact_type="item",
        )
        invalid = validate_json(
            json.dumps(
                {
                    "format_version": "1.10",
                    "minecraft:item": {"description": {"identifier": "Demo:Item"}},
                }
            ),
            artifact_type="item",
        )

        self.assertFalse(valid.blocked)
        self.assertIn("JSON_IDENTIFIER_INVALID", issue_codes(invalid))

    def test_modsdk39_biome_type_requires_namespace(self):
        incomplete = validate_json('{"biome_type": "forest"}', target_version="3.9")
        complete = validate_json('{"biome_type": "minecraft:forest"}', target_version="3.9")
        non_string = validate_json('{"biome_type": 3}', target_version="3.9")
        old_target = validate_json('{"biome_type": "forest"}', target_version="3.8")

        self.assertIn("JSON_BIOME_TYPE_NAMESPACE", issue_codes(incomplete))
        self.assertNotIn("JSON_BIOME_TYPE_NAMESPACE", issue_codes(complete))
        self.assertIn("JSON_BIOME_TYPE_NAMESPACE", issue_codes(non_string))
        self.assertNotIn("JSON_BIOME_TYPE_NAMESPACE", issue_codes(old_target))

    def test_legacy_block_profile_uses_object_components(self):
        valid = validate_json(
            block_source(
                "1.10.0",
                {
                    "minecraft:destroy_time": {"value": 2.0},
                    "minecraft:explosion_resistance": {"value": 5.0},
                },
            ),
            artifact_type="block",
        )
        invalid = validate_json(
            block_source("1.10.0", {"minecraft:destroy_time": 2.0}),
            artifact_type="block",
        )

        self.assertFalse(valid.blocked)
        self.assertIn("JSON_BLOCK_COMPONENT_SHAPE_CONFLICT", issue_codes(invalid))

    def test_scalar_block_profile_uses_number_components(self):
        valid = validate_json(
            block_source(
                "1.16.0",
                {
                    "minecraft:destroy_time": 2.0,
                    "minecraft:block_light_emission": 0.5,
                },
            ),
            artifact_type="block",
        )
        invalid = validate_json(
            block_source("1.16.0", {"minecraft:destroy_time": {"value": 2.0}}),
            artifact_type="block",
        )

        self.assertFalse(valid.blocked)
        self.assertIn("JSON_BLOCK_COMPONENT_SHAPE_CONFLICT", issue_codes(invalid))

    def test_modern_block_profile_uses_destructible_components(self):
        valid = validate_json(
            block_source(
                "1.19.20",
                {
                    "minecraft:destructible_by_mining": {"seconds_to_destroy": 2.0},
                    "minecraft:destructible_by_explosion": True,
                    "minecraft:light_emission": 0.5,
                    "minecraft:light_dampening": 1.0,
                },
            ),
            artifact_type="block",
        )
        invalid = validate_json(
            block_source("1.19.20", {"minecraft:destroy_time": 2.0}),
            artifact_type="block",
        )

        self.assertFalse(valid.blocked)
        self.assertIn("JSON_BLOCK_COMPONENT_SHAPE_CONFLICT", issue_codes(invalid))

    def test_modern_block_profile_strictly_checks_light_components(self):
        wrong_shape = validate_json(
            block_source("1.19.20", {"minecraft:light_emission": "bright"}),
            artifact_type="block",
        )
        legacy_name = validate_json(
            block_source("1.19.20", {"minecraft:block_light_emission": {"emission": 1.0}}),
            artifact_type="block",
        )
        modern_name_in_legacy = validate_json(
            block_source("1.10.0", {"minecraft:light_emission": 1.0}),
            artifact_type="block",
        )

        self.assertIn("JSON_BLOCK_COMPONENT_SHAPE_CONFLICT", issue_codes(wrong_shape))
        self.assertIn("JSON_BLOCK_COMPONENT_SHAPE_CONFLICT", issue_codes(legacy_name))
        self.assertIn("JSON_BLOCK_COMPONENT_SHAPE_CONFLICT", issue_codes(modern_name_in_legacy))

    def test_explicit_profile_version_conflict_is_blocking(self):
        report = validate_json(
            block_source("1.16.0", {"minecraft:destroy_time": 2.0}),
            artifact_type="block",
            format_profile="legacy_1_10",
        )

        self.assertIn("JSON_BLOCK_PROFILE_VERSION_CONFLICT", issue_codes(report))
        self.assertTrue(report.blocked)

    def test_unknown_block_version_without_profile_is_not_guessed(self):
        report = validate_json(
            block_source("9.9.9", {"minecraft:destroy_time": "custom-shape"}),
            artifact_type="block",
        )

        self.assertNotIn("JSON_BLOCK_COMPONENT_SHAPE_CONFLICT", issue_codes(report))
        self.assertFalse(report.blocked)

    def test_duplicate_json_keys_are_blocked(self):
        raw_dup = (
            '{\n'
            '  "format_version": "1.10",\n'
            '  "minecraft:item": {\n'
            '    "description": {"identifier": "demo:dup_item"},\n'
            '    "components": {\n'
            '      "minecraft:max_stack_size": 64,\n'
            '      "minecraft:max_stack_size": 1\n'
            '    }\n'
            '  }\n'
            '}'
        )
        report = validate_json(raw_dup, artifact_type="item")
        self.assertIn("JSON_DUPLICATE_KEY", issue_codes(report))
        self.assertTrue(report.blocked)

    def test_languages_json_accepts_non_empty_string_array(self):
        valid = validate_json('["zh_CN", "en_US"]', filename="resource_pack/texts/languages.json")
        invalid_empty = validate_json("[]", filename="resource_pack/texts/languages.json")

        self.assertFalse(valid.blocked)
        self.assertEqual([], issue_codes(valid))
        self.assertIn("JSON_LANGUAGES_INVALID", issue_codes(invalid_empty))

    def test_manifest_json_enforces_format_version_2_and_unique_uuids(self):
        valid_manifest = json.dumps({
            "format_version": 2,
            "header": {
                "name": "Demo Pack",
                "description": "Demo",
                "uuid": "54bdabed-493c-49fa-b7fe-c2b6a026226b",
                "version": [1, 0, 0],
                "min_engine_version": [1, 18, 0],
            },
            "modules": [
                {
                    "type": "data",
                    "uuid": "d5a4a945-948a-4b48-81a8-f1341ff29f73",
                    "version": [1, 0, 0],
                }
            ],
        })
        self.assertFalse(validate_json(valid_manifest, filename="behavior_pack/manifest.json").blocked)

        legacy_name = validate_json(valid_manifest, filename="behavior_pack/pack_manifest.json")
        self.assertFalse(legacy_name.blocked)
        self.assertIn("JSON_MANIFEST_LEGACY_FILENAME", issue_codes(legacy_name))

        old_fv = json.loads(valid_manifest)
        old_fv["format_version"] = 1
        self.assertIn(
            "JSON_MANIFEST_FORMAT_VERSION",
            issue_codes(validate_json(json.dumps(old_fv), filename="manifest.json")),
        )

        dup_uuid = json.loads(valid_manifest)
        dup_uuid["modules"][0]["uuid"] = dup_uuid["header"]["uuid"]
        self.assertIn(
            "JSON_MANIFEST_UUID_DUPLICATE",
            issue_codes(validate_json(json.dumps(dup_uuid), filename="manifest.json")),
        )

    def test_item_110_rejects_bedrock_116_components_and_side_conflicts(self):
        bad_116 = json.dumps({
            "format_version": "1.10",
            "minecraft:item": {
                "description": {"identifier": "demo:bad_sword"},
                "components": {
                    "minecraft:durability": {"max_durability": 200},
                    "minecraft:digger": {"use_efficiency": True},
                },
            },
        })
        self.assertIn("JSON_ITEM_UNSUPPORTED_COMPONENT", issue_codes(validate_json(bad_116, artifact_type="item")))

        stack_conflict = json.dumps({
            "format_version": "1.10",
            "minecraft:item": {
                "description": {"identifier": "demo:conflict_sword"},
                "components": {
                    "minecraft:max_damage": 250,
                    "minecraft:stacked_by_data": True,
                },
            },
        })
        self.assertIn("JSON_ITEM_DAMAGE_STACKED_CONFLICT", issue_codes(validate_json(stack_conflict, artifact_type="item")))

        client_in_beh = json.dumps({
            "format_version": "1.10",
            "minecraft:item": {
                "description": {"identifier": "demo:bad_food"},
                "components": {
                    "minecraft:food": {"nutrition": 4, "saturation_modifier": "normal"},
                    "minecraft:use_animation": "eat",
                    "minecraft:use_duration": 1.6,
                },
            },
        })
        beh_codes = issue_codes(validate_json(client_in_beh, filename="behavior_pack/netease_items_beh/demo_bad_food.json", artifact_type="item"))
        self.assertIn("JSON_ITEM_CLIENT_COMPONENT_IN_BEHAVIOR", beh_codes)
        self.assertIn("JSON_ITEM_USE_DURATION_TICKS", beh_codes)

        bad_axe_type = json.dumps({
            "format_version": "1.10",
            "minecraft:item": {
                "description": {"identifier": "demo:bad_axe", "custom_item_type": "weapon"},
                "components": {
                    "netease:weapon": {"type": "axe", "level": 2, "speed": 6, "attack_damage": 4, "enchantment": 10},
                },
            },
        })
        self.assertIn("JSON_ITEM_WEAPON_CONTRACT", issue_codes(validate_json(bad_axe_type, artifact_type="item")))

    def test_legacy_block_light_emission_above_one_is_blocked(self):
        legacy_overflow = validate_json(
            block_source("1.10.0", {"minecraft:block_light_emission": {"emission": 12}}),
            artifact_type="block",
        )
        scalar_overflow = validate_json(
            block_source("1.16.0", {"minecraft:block_light_emission": 15}),
            artifact_type="block",
        )

        self.assertIn("JSON_BLOCK_LIGHT_EMISSION_RANGE", issue_codes(legacy_overflow))
        self.assertIn("JSON_BLOCK_LIGHT_EMISSION_RANGE", issue_codes(scalar_overflow))


if __name__ == "__main__":
    unittest.main()
