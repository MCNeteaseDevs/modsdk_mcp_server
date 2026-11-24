# -*- coding: utf-8 -*-
"""MCP 工具、Resource 与生成器的本地契约测试。"""

import asyncio
import json
import unittest

from modsdk_mcp.server import (
    _health_payload,
    call_tool,
    list_resources,
    list_tools,
    read_resource,
)


LEGACY_TOOL_NAMES = {
    "search_docs",
    "search_api",
    "get_api_detail",
    "get_document",
    "get_document_section",
    "list_documents",
    "get_document_structure",
    "reload_documents",
    "generate_mod_project",
    "generate_server_system",
    "generate_client_system",
    "generate_event_listener",
    "generate_custom_command",
    "generate_custom_item",
    "generate_custom_block",
    "generate_item_json",
    "generate_block_json",
    "generate_recipe_json",
    "generate_entity_json",
    "generate_loot_table_json",
    "generate_spawn_rules_json",
    "generate_sword_json",
    "generate_pickaxe_json",
    "generate_axe_json",
    "generate_shovel_json",
    "generate_hoe_json",
    "generate_food_json",
    "generate_armor_json",
    "generate_bow_json",
    "generate_throwable_json",
    "review_code",
    "search_components",
    "get_component_details",
    "list_components",
    "get_best_practices",
    "get_architecture_pattern",
    "browse_api_category",
}


def run(coro):
    return asyncio.run(coro)


def assert_array_items(testcase, value, path="schema"):
    if isinstance(value, dict):
        if value.get("type") == "array":
            testcase.assertIn("items", value, path)
        for key, child in value.items():
            assert_array_items(testcase, child, "{}.{}".format(path, key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            assert_array_items(testcase, child, "{}[{}]".format(path, index))


def first_payload(contents):
    try:
        return json.loads(contents[0].text)
    except (TypeError, ValueError):
        return None


class McpContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tools = run(list_tools())

    def test_all_41_tools_are_registered(self):
        names = {tool.name for tool in self.tools}
        expected_extra = {
            "get_development_guidance",
            "get_version_changes",
            "generate_manifest_json",
            "generate_ui_json",
        }
        self.assertEqual(41, len(names))
        self.assertEqual(LEGACY_TOOL_NAMES, names - expected_extra)

    def test_every_array_schema_has_items(self):
        for tool in self.tools:
            assert_array_items(self, tool.inputSchema, tool.name)

    def test_health_payload_reports_current_offline_snapshot(self):
        payload = _health_payload()
        self.assertEqual("ok", payload["status"])
        self.assertEqual("3.10", payload["modsdk_version"])
        self.assertEqual("1.21.130", payload["bedrock_version"])
        self.assertEqual(61, payload["rule_count"])
        self.assertGreater(payload["detector_count"], 0)
        self.assertGreater(payload["document_count"], 0)
        self.assertTrue(payload["snapshot_time"])
        self.assertEqual("unreviewed", payload["runtime_evidence_status"])

    def test_guidance_schema_version_error_and_rule_limit(self):
        result = run(call_tool("get_development_guidance", {
            "goal": "生成服务端 Python 事件监听器",
            "domain": "python",
            "side": "server",
            "target_version": "current",
            "max_rules": 3,
        }))
        payload = json.loads(result[0].text)
        self.assertEqual(
            ["schema_version", "request", "target", "strategy", "rules", "source_boundaries", "verify_next"],
            list(payload),
        )
        self.assertLessEqual(len(payload["rules"]), 3)
        self.assertEqual("3.10", payload["target"]["version"])

        unknown = first_payload(run(call_tool("get_development_guidance", {
            "goal": "测试",
            "target_version": "9.9",
        })))
        self.assertEqual("blocked", unknown["status"])
        self.assertIn("GUIDANCE_REQUEST_INVALID", {item["code"] for item in unknown["issues"]})

    def test_guidance_resources_are_listed_and_readable(self):
        resources = run(list_resources())
        uris = {str(resource.uri) for resource in resources}
        for uri in (
            "modsdk-guidance://versions",
            "modsdk-guidance://index",
            "modsdk-guidance://sources",
        ):
            self.assertIn(uri, uris)
            payload = json.loads(run(read_resource(uri)))
            self.assertEqual("1.0", payload["schema_version"])

        rule_uri = next(uri for uri in uris if uri.startswith("modsdk-guidance://rules/"))
        rule = json.loads(run(read_resource(rule_uri)))
        self.assertIn("id", rule)
        self.assertIn("source_ids", rule)

    def test_guide_resources_are_listed_and_readable(self):
        resources = run(list_resources())
        guide_uris = {
            str(resource.uri)
            for resource in resources
            if str(resource.uri).startswith("guide://")
        }
        self.assertEqual({
            "guide://json-ui",
            "guide://custom-dimension",
            "guide://custom-block",
            "guide://custom-entity",
            "guide://custom-item",
            "guide://particle-effect",
        }, guide_uris)

        for uri in guide_uris:
            with self.subTest(uri=uri):
                content = run(read_resource(uri))
                self.assertTrue(content.strip())
                self.assertNotIn("路径不存在", content)
                self.assertNotIn("未找到网易官方教程文档目录", content)

    def test_search_api_renders_parameter_comments(self):
        contents = run(call_tool("search_api", {
            "query": "RemovePlayerAnimationFromState",
        }))
        self.assertIn("动画控制器名称", contents[0].text)
        self.assertIn("动画状态名称", contents[0].text)
        self.assertIn("要移除的动画名称", contents[0].text)

    def test_api_index_resource_description_uses_current_total(self):
        from modsdk_mcp.docs_reader import get_docs_reader

        expected_total = get_docs_reader().get_api_entry_count()
        resource = next(
            item for item in run(list_resources())
            if str(item.uri) == "api-index://full"
        )
        self.assertIn("{}个API/事件".format(expected_total), resource.description)
        self.assertNotIn("1879个API/事件", resource.description)

    def test_review_code_success_warning_and_blocked(self):
        clean_code = "# -*- coding: utf-8 -*-\nimport mod.server.extraServerApi as serverApi\n"
        clean = first_payload(run(call_tool("review_code", {
            "code": clean_code,
            "filename": "server.py",
            "side": "server",
        })))
        self.assertEqual("ok", clean["status"])

        noisy_code = (
            "# -*- coding: utf-8 -*-\n"
            "from __future__ import print_function\n"
            "def OnTickServer(self):\n"
            "    print('[Demo] tick')\n"
        )
        warning = first_payload(run(call_tool("review_code", {
            "code": noisy_code,
            "filename": "server.py",
            "side": "server",
        })))
        self.assertEqual("warning", warning["status"])

        forbidden_line = 'value = u"blocked"'
        blocked_code = "# -*- coding: utf-8 -*-\n{}\n".format(forbidden_line)
        result = run(call_tool("review_code", {"code": blocked_code, "filename": "sample.py"}))
        blocked = first_payload(result)
        self.assertEqual("blocked", blocked["status"])
        self.assertIn("critical", {item["severity"] for item in blocked["issues"]})
        self.assertNotIn(forbidden_line, result[0].text)

        alias = first_payload(run(call_tool("review_code", {
            "code": clean_code,
            "filename": "server.py",
            "side": "server",
            "target_version": "BE1.21.120",
        })))
        self.assertEqual("ok", alias["status"])

        unsupported = first_payload(run(call_tool("review_code", {
            "code": clean_code,
            "filename": "server.py",
            "target_version": "9.9",
        })))
        self.assertEqual("blocked", unsupported["status"])
        self.assertIn("TARGET_VERSION_UNSUPPORTED", {item["code"] for item in unsupported["issues"]})

        invalid_side = first_payload(run(call_tool("review_code", {
            "code": clean_code,
            "filename": "server.py",
            "side": "invalid",
        })))
        self.assertIn("SIDE_INVALID", {item["code"] for item in invalid_side["issues"]})

    def test_event_generator_requires_verified_or_explicit_contract(self):
        official = run(call_tool("generate_event_listener", {
            "event_name": "ServerItemUseOnEvent",
            "event_kind": "official",
            "side": "server",
        }))
        self.assertIn('args: 事件参数', official[0].text)
        self.assertIn('entityId', official[0].text)

        unknown = first_payload(run(call_tool("generate_event_listener", {
            "event_name": "UnknownOfficialEvent",
            "event_kind": "official",
            "side": "server",
        })))
        self.assertEqual("blocked", unknown["status"])

        custom_missing = first_payload(run(call_tool("generate_event_listener", {
            "event_name": "MyEvent",
            "event_kind": "custom",
            "side": "server",
        })))
        self.assertEqual("blocked", custom_missing["status"])

        custom = run(call_tool("generate_event_listener", {
            "event_name": "MyEvent",
            "event_kind": "custom",
            "side": "server",
            "params": {"playerId": "玩家实体 ID"},
        }))
        self.assertIn("playerId", custom[0].text)

    def test_all_generators_return_non_blocked_representative_output(self):
        samples = {
            "generate_mod_project": {"mod_name": "Demo", "mod_id": "demo"},
            "generate_manifest_json": {"pack_name": "Demo Pack"},
            "generate_ui_json": {"ui_namespace": "demo_panel", "mod_id": "demo"},
            "generate_server_system": {"mod_name": "Demo", "class_name": "Demo"},
            "generate_client_system": {"mod_name": "Demo", "class_name": "Demo"},
            "generate_event_listener": {"event_name": "ServerItemUseOnEvent", "side": "server"},
            "generate_custom_command": {"command_name": "demo"},
            "generate_custom_item": {"item_id": "demo_item", "namespace": "demo"},
            "generate_custom_block": {"block_id": "demo_block", "namespace": "demo"},
            "generate_item_json": {"namespace": "demo", "item_id": "demo_item"},
            "generate_block_json": {"namespace": "demo", "block_id": "demo_block"},
            "generate_recipe_json": {"recipe_type": "shaped", "namespace": "demo", "recipe_id": "demo_recipe"},
            "generate_entity_json": {"namespace": "demo", "entity_id": "demo_entity"},
            "generate_loot_table_json": {"pools": []},
            "generate_spawn_rules_json": {"namespace": "demo", "entity_id": "demo_entity"},
            "generate_sword_json": {"namespace": "demo", "item_id": "demo_sword"},
            "generate_pickaxe_json": {"namespace": "demo", "item_id": "demo_pickaxe"},
            "generate_axe_json": {"namespace": "demo", "item_id": "demo_axe"},
            "generate_shovel_json": {"namespace": "demo", "item_id": "demo_shovel"},
            "generate_hoe_json": {"namespace": "demo", "item_id": "demo_hoe"},
            "generate_food_json": {"namespace": "demo", "item_id": "demo_food"},
            "generate_armor_json": {"namespace": "demo", "item_id": "demo_armor"},
            "generate_bow_json": {"namespace": "demo", "item_id": "demo_bow"},
            "generate_throwable_json": {
                "namespace": "demo",
                "item_id": "demo_throwable",
                "projectile_entity": "demo:projectile",
            },
        }
        for tool_name, arguments in samples.items():
            with self.subTest(tool=tool_name):
                contents = run(call_tool(tool_name, arguments))
                payload = first_payload(contents)
                self.assertFalse(payload and payload.get("status") == "blocked", contents[0].text)
                self.assertTrue(contents[0].text.strip())

    def test_block_profiles_and_critical_non_leakage(self):
        for profile in ("legacy_1_10", "scalar_1_16", "modern_1_19_20"):
            contents = run(call_tool("generate_block_json", {
                "namespace": "demo",
                "block_id": "profile_block",
                "format_profile": profile,
            }))
            payload = first_payload(contents)
            self.assertFalse(payload and payload.get("status") == "blocked", profile)

        blocked = run(call_tool("generate_block_json", {
            "namespace": "demo",
            "block_id": "bad_block",
            "format_profile": "legacy_1_10",
            "components": {
                "minecraft:destructible_by_mining": {"seconds_to_destroy": 1.0},
            },
        }))
        self.assertEqual(1, len(blocked))
        payload = json.loads(blocked[0].text)
        self.assertEqual("blocked", payload["status"])
        self.assertNotIn('```json', blocked[0].text)

    def test_architecture_examples_pass_unified_validation(self):
        listing = run(call_tool("get_architecture_pattern", {}))
        self.assertIn("可用架构模式", listing[0].text)
        for name in ("跨端通信", "组件使用", "UI开发流程", "实体创建与管理", "定时任务", "物品掉落与生成"):
            with self.subTest(pattern=name):
                contents = run(call_tool("get_architecture_pattern", {"pattern_name": name}))
                payload = first_payload(contents)
                self.assertFalse(payload and payload.get("status") == "blocked", contents[0].text)

    def test_best_practices_are_registry_compatibility_projections(self):
        expected_rule_ids = {
            "python27_compatibility": "PY-COMPAT-001",
            "client_server_separation": "ARCH-SIDE-001",
            "performance": "ARCH-TICK-001",
            "ui_development": "UI-LIFE-001",
            "modsdk_39_migration": "ARCH-API-001",
        }
        for category, rule_id in expected_rule_ids.items():
            with self.subTest(category=category):
                contents = run(call_tool("get_best_practices", {"category": category}))
                self.assertIn("standard/registry", contents[0].text)
                self.assertIn(rule_id, contents[0].text)

        legacy = run(call_tool("get_best_practices", {"category": "modsdk_38_migration"}))
        self.assertIn("3.8 历史迁移入口", legacy[0].text)

    def test_mod_project_generates_complete_dual_pack_and_rejects_bad_mod_id(self):
        contents = run(call_tool("generate_mod_project", {
            "mod_name": "星辉组件",
            "mod_id": "starlight_mod",
            "version": "1.2.3",
        }))
        text = contents[0].text
        for required_path in (
            "behavior_pack/manifest.json",
            "behavior_pack/entities/.gitkeep",
            "behavior_pack/starlight_mod_Script/__init__.py",
            "behavior_pack/starlight_mod_Script/modConfig.py",
            "behavior_pack/starlight_mod_Script/modMain.py",
            "behavior_pack/starlight_mod_Script/serverSystem.py",
            "behavior_pack/starlight_mod_Script/clientSystem.py",
            "resource_pack/manifest.json",
            "resource_pack/textures/item_texture.json",
            "resource_pack/textures/terrain_texture.json",
            "resource_pack/texts/languages.json",
            "resource_pack/texts/zh_CN.lang",
        ):
            self.assertIn(required_path, text)
        self.assertNotIn("pack_manifest.json", text)

        custom_dirs = run(call_tool("generate_mod_project", {
            "mod_name": "StudioMod",
            "mod_id": "studio_mod",
            "behavior_pack_dir": "behavior_pack_abc123",
            "resource_pack_dir": "resource_pack_def456",
        }))[0].text
        self.assertIn("behavior_pack_abc123/manifest.json", custom_dirs)
        self.assertIn("resource_pack_def456/manifest.json", custom_dirs)

        bad_mod_id = first_payload(run(call_tool("generate_mod_project", {
            "mod_name": "Bad",
            "mod_id": "bad-hyphen-id",
        })))
        self.assertEqual("blocked", bad_mod_id["status"])

    def test_advanced_items_and_blocks_emit_complete_netease_bundles(self):
        axe_text = run(call_tool("generate_axe_json", {
            "namespace": "demo",
            "item_id": "ruby_axe",
            "damage": 7,
            "mining_speed": 8,
            "durability": 500,
        }))[0].text
        self.assertIn('"custom_item_type": "weapon"', axe_text)
        self.assertIn('"type": "hatchet"', axe_text)
        self.assertIn("resource_pack/textures/item_texture.json", axe_text)
        self.assertNotIn('"minecraft:durability":', axe_text)
        self.assertNotIn('"minecraft:stacked_by_data":', axe_text)

        armor_text = run(call_tool("generate_armor_json", {
            "namespace": "demo",
            "item_id": "ruby_helmet",
            "slot": "slot.armor.head",
            "protection": 4,
        }))[0].text
        self.assertIn('"netease:armor"', armor_text)
        self.assertIn('"armor_slot": 0', armor_text)
        self.assertIn("resource_pack/attachables/demo_ruby_helmet.json", armor_text)

        default_block = run(call_tool("generate_block_json", {
            "namespace": "demo",
            "block_id": "glow_stone_ex",
            "light_emission": 12,
        }))[0].text
        self.assertIn('"format_version": "1.19.20"', default_block)
        self.assertIn('"minecraft:light_emission": 12', default_block)
        self.assertIn("resource_pack/blocks.json", default_block)
        self.assertIn("resource_pack/textures/terrain_texture.json", default_block)

        legacy_lit_block = run(call_tool("generate_block_json", {
            "namespace": "demo",
            "block_id": "legacy_glow",
            "light_emission": 12,
            "format_profile": "legacy_1_10",
        }))
        self.assertFalse(first_payload(legacy_lit_block) and first_payload(legacy_lit_block).get("status") == "blocked")
        self.assertIn('"emission": 0.8', legacy_lit_block[0].text)

        entity_text = run(call_tool("generate_entity_json", {
            "namespace": "demo",
            "entity_id": "spirit_fox",
        }))[0].text
        self.assertIn("resource_pack/models/entity/demo_spirit_fox.geo.json", entity_text)
        self.assertIn('"runtime_identifier": "minecraft:pig"', entity_text)


if __name__ == "__main__":
    unittest.main()
