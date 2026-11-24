# -*- coding: utf-8 -*-
"""官方文档全量同步、白名单规范化与事务性落盘契约测试。"""

import io
import json
import os
import tempfile
import unittest
import urllib.parse
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

from modsdk_mcp.docs_reader import DocsReader, _find_guide_root
from tools.sync_official_docs import (
    BASE_URL,
    PYTHON_WHITELIST_URL,
    build_sync_plan,
    freeze_snapshot,
    official_url,
    OfficialSnapshot,
    write_files_atomically,
)


LAST_MODIFIED = "Wed, 28 Oct 2026 10:10:37 GMT"

API_DOCS = {
    "RemovePlayerAnimationFromState": ("接口/玩家/渲染", "客户端"),
    "GetBlockCollision": ("接口/世界/方块管理", "服务端"),
}

EVENT_DOCS = {
    "PlayerSleepServerEvent": ("事件/玩家", "服务端"),
    "PhysXPostSimulateServerEvent": ("事件/物理", "服务端"),
}

PARAMS = {
    "RemovePlayerAnimationFromState": [
        "animationControllerName", "stateName", "animationName",
    ],
    "GetBlockCollision:服务端": ["pos", "dimensionId", "getAll"],
    "GetBlockCollision:客户端": ["pos", "getAll"],
    "PlayerSleepServerEvent": ["playerId", "fullName", "auxData", "dimensionid", "x", "y", "z"],
    "PhysXPostSimulateServerEvent": ["dimensionId", "deltaTime"],
}


def wrap_html(body):
    return '<html><main><div class="theme-default-content content__default">{}</div><footer></footer></main></html>'.format(body)


def href_for(doc_path, name=""):
    encoded = "/".join(urllib.parse.quote(part, safe="") for part in doc_path.split("/"))
    href = "/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/{}.html".format(encoded)
    return href + ("#" + name.lower() if name else "")


def params_table(names):
    rows = "".join(
        "<tr><td>{0}</td><td>str</td><td>{0} 参数</td></tr>".format(name)
        for name in names
    )
    return (
        "<p>参数</p><table><thead><tr><th>参数名</th><th>数据类型</th><th>说明</th></tr></thead>"
        "<tbody>{}</tbody></table>"
    ).format(rows)


def entry_body(name, side, params, class_path=""):
    method = "<p>method in {}</p>".format(class_path) if class_path else ""
    return (
        "{method}<ul><li><p>描述</p><p>{name} 的官方描述</p></li>"
        "<li>{params}</li><li><p>返回值</p><p>无</p></li>"
        "<li><p>备注</p><ul><li>{name} 的官方备注</li></ul></li>"
        "<li><p>示例</p></li></ul>"
        "<pre class=\"language-python\"><code>result = comp.{name}()</code></pre>"
    ).format(method=method, name=name, params=params_table(params))


def api_section(name, side, params):
    class_side = "server" if side == "服务端" else "client"
    class_path = "mod.{}.component.fixture.{}Component{}".format(
        class_side,
        name,
        "Server" if side == "服务端" else "Client",
    )
    return '<h2 id="{anchor}">{name}</h2><p><span>{side}</span></p>{body}'.format(
        anchor=name.lower(),
        name=name,
        side=side,
        body=entry_body(name, side, params, class_path),
    )


def event_section(name, side, params):
    return '<h2 id="{anchor}">{name}</h2><p><span>{side}</span></p>{body}'.format(
        anchor=name.lower(),
        name=name,
        side=side,
        body=entry_body(name, side, params),
    )


def get_block_collision_section():
    server_body = entry_body(
        "GetBlockCollision",
        "服务端",
        PARAMS["GetBlockCollision:服务端"],
        "mod.server.component.blockInfoCompServer.BlockInfoComponentServer",
    )
    client_body = entry_body(
        "GetBlockCollision",
        "客户端",
        PARAMS["GetBlockCollision:客户端"],
        "mod.client.component.blockInfoCompClient.BlockInfoComponentClient",
    )
    return (
        '<h2 id="getblockcollision">GetBlockCollision</h2>'
        '<p><span>服务端</span><span>客户端</span></p>'
        '<h3 id="server">服务端接口</h3>{}'
        '<h3 id="client">客户端接口</h3>{}'
    ).format(server_body, client_body)


def index_html(rows, version="3.10"):
    nav = '<a href="{}">{}</a>'.format(href_for("更新信息/" + version), version)
    body = [nav, "<h1>索引</h1><table><tr><th>名称</th><th>端</th><th>描述</th></tr>"]
    for name, doc_path, side in rows:
        body.append(
            '<tr><td><a href="{}">{}</a></td><td>{}</td><td>fixture 描述</td></tr>'.format(
                href_for(doc_path, name), name, side,
            )
        )
    body.append("</table>")
    return wrap_html("".join(body))


def build_fixture_pages():
    pages = {}
    release_body = (
        "<h1>3.10</h1>"
        "<p>- 新增PhysXPostSimulateServerEvent(服务端)，物理模拟后事件</p>"
        '<p><a href="{}">EnchantType</a></p>'
    ).format(href_for("枚举值/EnchantType"))
    pages[official_url("更新信息/3.10", BASE_URL)] = wrap_html(release_body)

    api_rows = []
    api_pages = {}
    for name, (doc_path, side) in API_DOCS.items():
        if name == "GetBlockCollision":
            api_rows.append((name, doc_path, "服务端"))
            api_rows.append((name, doc_path, "客户端"))
            api_pages.setdefault(doc_path, []).append(get_block_collision_section())
            continue
        api_rows.append((name, doc_path, side))
        api_pages.setdefault(doc_path, []).append(api_section(name, side, PARAMS.get(name, ["value"])))
    pages[official_url("接口/Api索引表", BASE_URL)] = index_html(api_rows)
    for doc_path, sections in api_pages.items():
        pages[official_url(doc_path, BASE_URL)] = wrap_html("".join(sections))

    event_rows = []
    event_pages = {}
    for name, (doc_path, side) in EVENT_DOCS.items():
        event_rows.append((name, doc_path, side))
        event_pages.setdefault(doc_path, []).append(event_section(name, side, PARAMS.get(name, ["entityId"])))
    pages[official_url("事件/事件索引表", BASE_URL)] = index_html(event_rows)
    for doc_path, sections in event_pages.items():
        pages[official_url(doc_path, BASE_URL)] = wrap_html("".join(sections))

    pages[official_url("枚举值/EnchantType", BASE_URL)] = wrap_html(
        '<h1>EnchantType</h1><pre class="language-python"><code>class EnchantType(object):\n    Lunge = 41\n    NumEnchantments = 42</code></pre>'
    )

    modules = ["__future__", "ast（3.3新增）", "json", "mod.client.extraClientApi", "mod.server.extraServerApi"]
    modules.extend("allowed.module{:03d}".format(index) for index in range(456 - len(modules)))
    cells = "".join("<td>{}</td>".format(module) for module in modules)
    pages[PYTHON_WHITELIST_URL] = wrap_html("<h1>Python模块白名单</h1><table><tr>{}</tr></table>".format(cells))
    return pages


class FixtureFetcher:
    def __init__(self, pages):
        self.pages = pages
        self.requests = []

    def __call__(self, url):
        self.requests.append(url)
        if url not in self.pages:
            raise AssertionError("测试禁止联网且不存在 fixture URL: {}".format(url))
        return self.pages[url], {"Last-Modified": LAST_MODIFIED}


def write_repo_seed(repo_root):
    docs = repo_root / "docs"
    for sub in ("接口", "事件", "枚举值", "更新信息"):
        (docs / sub).mkdir(parents=True, exist_ok=True)
    (docs / "接口" / "旧遗留页.md").write_text("# 旧页\n", encoding="utf-8")

    registry = repo_root / "standard" / "registry"
    (registry / "versions").mkdir(parents=True, exist_ok=True)
    (registry / "snapshots").mkdir(parents=True, exist_ok=True)
    (registry / "rules").mkdir(parents=True, exist_ok=True)

    manifest = {
        "schema_version": "1.0",
        "default_version": "3.10",
        "version_files": {
            "3.9": "versions/3.9.json",
            "3.10": "versions/3.10.json",
        },
    }
    profile_39 = {
        "version": "3.9",
        "bedrock_version": "1.21.120",
        "status": "stable",
        "released_at": "2026-07-22",
        "docs_base_url": BASE_URL,
    }
    profile_310 = {
        "version": "3.10",
        "bedrock_version": "1.21.130",
        "status": "stable",
        "released_at": "2026-10-28",
        "previous_version": "3.9",
        "docs_base_url": BASE_URL,
    }
    (registry / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    (registry / "versions" / "3.9.json").write_text(json.dumps(profile_39, ensure_ascii=False), encoding="utf-8")
    (registry / "versions" / "3.10.json").write_text(json.dumps(profile_310, ensure_ascii=False), encoding="utf-8")
    (registry / "rules" / "modsdk-3.10.json").write_text(
        json.dumps({"schema_version": "1.0", "rules": []}, ensure_ascii=False),
        encoding="utf-8",
    )

    baseline = OfficialSnapshot(
        profile=profile_39,
        pages={
            "更新信息/3.9": {
                "url": official_url("更新信息/3.9", BASE_URL),
                "html": wrap_html("<h1>3.9</h1>"),
                "headers": {"Last-Modified": LAST_MODIFIED},
                "markdown": "# 3.9",
            },
            "枚举值/EnchantType": {
                "url": official_url("枚举值/EnchantType", BASE_URL),
                "html": wrap_html("<h1>EnchantType</h1>"),
                "headers": {"Last-Modified": LAST_MODIFIED},
                "markdown": "```python\nclass EnchantType(object):\n    NumEnchantments = 41\n```",
            },
        },
        api_entries=[],
        event_entries=[],
        tutorials={},
    )
    (registry / "snapshots" / "modsdk-3.9-baseline.json").write_text(
        json.dumps(freeze_snapshot(baseline), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def tree_snapshot(root):
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }


class OfficialDocSyncContractTest(unittest.TestCase):
    def make_repo(self):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        write_repo_seed(root)
        return temporary, root

    def test_default_guide_root_is_local_and_diagnostics_use_stderr(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with mock.patch.dict(os.environ, {}, clear=True):
            with redirect_stdout(stdout), redirect_stderr(stderr):
                guide_root = _find_guide_root()

        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(Path(guide_root), Path(__file__).resolve().parents[1] / "input")
        self.assertIn("官方教程文档", stderr.getvalue())
        self.assertNotIn(str(Path(__file__).resolve().parents[1]), stderr.getvalue())

    def test_offline_sync_plan_discovers_entries_and_normalizes_whitelist(self):
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        before = tree_snapshot(root)
        pages = build_fixture_pages()
        fetcher = FixtureFetcher(pages)

        plan = build_sync_plan(
            root,
            version="current",
            include_python_whitelist=True,
            workers=2,
            fetcher=fetcher,
        )
        # build_sync_plan 本身无磁盘副作用
        self.assertEqual(tree_snapshot(root), before)
        self.assertEqual(plan.version, "3.10")
        self.assertEqual(len(plan.api_entries), 3)
        self.assertEqual(len(plan.event_entries), 2)
        self.assertIsNone(plan.files[root / "docs" / "接口" / "旧遗留页.md"])

        whitelist_path = root / "standard" / "registry" / "snapshots" / "python-module-whitelist.json"
        whitelist = json.loads(plan.files[whitelist_path])
        self.assertEqual(whitelist["module_count"], 456)
        ast_entry = next(item for item in whitelist["entries"] if item["normalized_name"] == "ast")
        self.assertEqual(ast_entry["raw_display"], "ast（3.3新增）")

        write_files_atomically(root, plan.files)
        self.assertFalse((root / "docs" / "接口" / "旧遗留页.md").exists())

        reader = DocsReader(str(root / "docs"))
        reader.load_all_docs()
        detail = reader.get_api_detail("RemovePlayerAnimationFromState")
        self.assertEqual(detail["source_last_modified"], LAST_MODIFIED)
        self.assertTrue(detail["source_url"].endswith("#removeplayeranimationfromstate"))
        self.assertIn("Lunge", reader.get_enum_inline("EnchantType"))

    def test_atomic_replace_rolls_back_after_mid_commit_failure(self):
        temporary, root = self.make_repo()
        self.addCleanup(temporary.cleanup)
        plan = build_sync_plan(
            root,
            version="current",
            include_python_whitelist=True,
            workers=2,
            fetcher=FixtureFetcher(build_fixture_pages()),
        )
        before = tree_snapshot(root)
        real_replace = os.replace
        calls = {"count": 0}

        def flaky_replace(source, target):
            calls["count"] += 1
            if calls["count"] == 3:
                raise OSError("fixture replacement failure")
            return real_replace(source, target)

        with mock.patch("tools.sync_official_docs.os.replace", side_effect=flaky_replace):
            with self.assertRaisesRegex(OSError, "fixture replacement failure"):
                write_files_atomically(root, plan.files)

        self.assertEqual(tree_snapshot(root), before)


if __name__ == "__main__":
    unittest.main()
