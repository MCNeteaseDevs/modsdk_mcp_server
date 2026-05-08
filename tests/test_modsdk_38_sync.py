# -*- coding: utf-8 -*-

import unittest
from pathlib import Path

from modsdk_mcp.docs_reader import DocsReader
from modsdk_mcp.knowledge_base import get_component_info, search_component


ROOT = Path(__file__).resolve().parents[1]


class ModSdk38SyncTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reader = DocsReader(str(ROOT / "docs"))
        cls.reader.load_all_docs()

    def assert_api_detail_contains(self, name, expected):
        detail = self.reader.get_api_detail(name)
        self.assertIsNotNone(detail, name)
        details = detail if isinstance(detail, list) else [detail]
        joined = "\n".join(
            "{} {} {} {}".format(
                item.get("name", ""),
                item.get("side", ""),
                item.get("category", ""),
                item.get("desc", ""),
            )
            for item in details
        )
        self.assertIn(expected, joined)

    def assert_search_hits(self, query, name, entry_type="all"):
        results = self.reader.search_api(query, limit=10, entry_type=entry_type)
        names = [item["name"] for item in results]
        self.assertIn(name, names, "query={!r} names={!r}".format(query, names))

    def get_doc(self, doc_path):
        return self.reader.get_document(doc_path) or self.reader.get_document(doc_path.replace("/", "\\"))

    def test_new_api_details(self):
        self.assert_api_detail_contains("AddModifier", "属性修饰符")
        self.assert_api_detail_contains("BindItemToMinecraftModel", "附作物")
        self.assert_api_detail_contains("UseItemToPos", "方块使用指定物品")

    def test_new_search_queries(self):
        self.assert_search_hits("钓鱼线颜色", "SetFishingLineColor", "api")
        self.assert_search_hits("自定义容器添加物品事件", "PlayerAddCustomContainerItemServerEvent", "event")
        self.assert_search_hits("属性修饰符", "AddModifier", "api")

    def test_synced_documents_are_readable(self):
        for doc_path in [
            "更新信息/3.8.md",
            "接口/物品/钓鱼线.md",
            "枚举值/AttributeModifierOperation.md",
        ]:
            doc = self.get_doc(doc_path)
            self.assertIsNotNone(doc, doc_path)
            self.assertIn("source_url", doc.metadata)
            self.assertGreater(len(doc.content), 100)

    def test_deprecated_aliases_remain_searchable(self):
        detail = self.reader.get_api_detail("PlayerDestoryBlock")
        self.assertIsNotNone(detail)
        self.assertIn("PlayerDestroyBlock", detail["desc"])

        detail = self.reader.get_api_detail("EntityUseItemToPos")
        self.assertIsNotNone(detail)
        self.assertIn("UseItemToPos", detail["desc"])

    def test_38_component_knowledge(self):
        detail = get_component_info("netease:liquid_clipped")
        self.assertEqual(detail["name"], "流体点击检测")
        results = search_component("流体", "netease")
        self.assertTrue(any(item["id"] == "netease:liquid_clipped" for item in results))


if __name__ == "__main__":
    unittest.main()
