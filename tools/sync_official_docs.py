#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sync selected NetEase ModSDK official docs into this MCP repository.

The script intentionally depends only on the Python standard library so it can
be reviewed and run in constrained MCP environments. It fetches public pages
from the NetEase developer website, converts the page body to Markdown, and
merges official 3.8 API/event entries into docs/interface.json and
docs/events.json.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


BASE_URL = "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI"
CHANGELOG_PATH = "更新信息/3.8"
USER_AGENT = "Mozilla/5.0 (compatible; modsdk-mcp-doc-sync/1.0)"

DOC_PATHS = [
    "更新信息/3.8",
    "接口/Api索引表",
    "事件/事件索引表",
    "接口/实体/属性",
    "接口/物品",
    "接口/物品/钓鱼线",
    "接口/世界/行为",
    "接口/玩家/行为",
    "接口/玩家/背包",
    "接口/物理",
    "接口/实体/渲染",
    "接口/玩家/摄像机",
    "接口/游戏设置",
    "接口/自定义UI/通用设置",
    "接口/原生UI",
    "接口/世界/时间",
    "接口/实体/背包",
    "接口/方块/容器",
    "事件/物品",
    "事件/物理",
    "事件/玩家",
    "枚举值/AttrType",
    "枚举值/AttributeModifierOperation",
    "枚举值/AttributeOperands",
    "枚举值/EntityType",
    "枚举值/RenderLayer",
]

ALWAYS_API_NAMES = {
    "AddModifier",
    "UpdateModifier",
    "RemoveModifier",
    "HasModifier",
    "GetAllModifiers",
    "SetFishingLineMax",
    "GetFishingLineMax",
    "SetFishingLineColor",
    "GetFishingLineColor",
    "UseItemToPos",
    "GetPlayerFishHookEntity",
    "GetPlayerFishItem",
    "GetPlayerIsFishing",
    "AddCapsuleGeometry",
    "AddSphereGeometry",
    "AddBoxTrigger",
    "AddForceAtPosLocal",
    "AddForceAtPos",
    "GetQueryableBoneOrientation",
    "ResetEntityExtraSkin",
    "ResetCameraPos",
    "BindItemToMinecraftModel",
    "BindItemToSkeletonModel",
    "SetBindBoneForBindItem",
    "GetBindBoneForBindItem",
    "SetBindItemRotation",
    "SetBindItemOffset",
    "SetBindItemScale",
    "GetBindItemRotation",
    "GetBindItemOffset",
    "GetBindItemScale",
    "PlayerDestroyBlock",
    "SetShearsDestroyBlockSpeed",
    "CancelShearsDestroyBlockSpeed",
    "CancelShearsDestroyBlockSpeedAll",
    "SetCameraPos",
    "SetToggleOption",
    "GetCarriedItem",
    "GetPlayerItem",
    "GetPlayerAllItems",
    "GetEntityItem",
    "GetContainerItem",
    "GetEnderChestItem",
    "SetUseLocalTime",
    "UseItemToEntity",
    "HideNeteaseStoreGui",
    "OpenNeteaseStoreGui",
}

ALWAYS_EVENT_NAMES = {
    "PlayerRemoveCustomContainerItemServerEvent",
    "PlayerAddCustomContainerItemServerEvent",
    "LiquidClippedServerEvent",
    "PhysxTriggerServerEvent",
    "PlayerFishingServerEvent",
    "PlayerFishingAfterServerEvent",
    "PlayerStartFishingServerEvent",
    "LiquidClippedClientEvent",
    "PlayerAddCustomContainerItemClientEvent",
    "PlayerRemoveCustomContainerItemClientEvent",
    "PhysxTriggerClientEvent",
}

MIGRATION_ALIASES = {
    "PlayerDestoryBlock": ("PlayerDestroyBlock", "拼写错误，请使用 PlayerDestroyBlock。"),
    "EntityUseItemToPos": ("UseItemToPos", "接口已废弃，请使用 UseItemToPos。"),
    "SetShearsDestoryBlockSpeed": (
        "SetShearsDestroyBlockSpeed",
        "拼写错误，请使用 SetShearsDestroyBlockSpeed。",
    ),
    "CancelShearsDestoryBlockSpeed": (
        "CancelShearsDestroyBlockSpeed",
        "拼写错误，请使用 CancelShearsDestroyBlockSpeed。",
    ),
    "CancelShearsDestoryBlockSpeedAll": (
        "CancelShearsDestroyBlockSpeedAll",
        "拼写错误，请使用 CancelShearsDestroyBlockSpeedAll。",
    ),
}


class MarkdownConverter(HTMLParser):
    """Small official-doc HTML to Markdown converter."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: List[str] = []
        self.list_stack: List[str] = []
        self.in_pre = False
        self.in_code = False
        self.in_table = False
        self.in_cell = False
        self.in_header_cell = False
        self.current_row: List[str] = []
        self.current_cell: List[str] = []
        self.table_header_written = False
        self.skip_anchor_depth = 0

    def handle_starttag(self, tag: str, attrs: Sequence[Tuple[str, Optional[str]]]) -> None:
        attrs_map = dict(attrs)
        cls = attrs_map.get("class", "") or ""
        if tag == "a" and "header-anchor" in cls:
            self.skip_anchor_depth += 1
            return
        if self.skip_anchor_depth:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._blank()
            self.out.append("#" * int(tag[1]) + " ")
        elif tag == "p":
            self._blank()
        elif tag in ("ul", "ol"):
            self.list_stack.append(tag)
            self._blank()
        elif tag == "li":
            self._blank()
            marker = "1. " if self.list_stack and self.list_stack[-1] == "ol" else "- "
            self.out.append(marker)
        elif tag == "br":
            self.out.append("\n")
        elif tag == "strong":
            self.out.append("**")
        elif tag == "em":
            self.out.append("*")
        elif tag == "pre":
            self.in_pre = True
            lang = "python" if "language-python" in cls else ""
            self._blank()
            self.out.append("```{}\n".format(lang))
        elif tag == "code" and not self.in_pre:
            self.in_code = True
            self.out.append("`")
        elif tag == "table":
            self.in_table = True
            self.table_header_written = False
            self._blank()
        elif tag == "tr" and self.in_table:
            self.current_row = []
        elif tag in ("td", "th") and self.in_table:
            self.in_cell = True
            self.in_header_cell = tag == "th"
            self.current_cell = []

    def handle_endtag(self, tag: str) -> None:
        if self.skip_anchor_depth:
            if tag == "a":
                self.skip_anchor_depth -= 1
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._blank()
        elif tag == "p":
            self._blank()
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            self._blank()
        elif tag == "li":
            self._blank()
        elif tag == "strong":
            self.out.append("**")
        elif tag == "em":
            self.out.append("*")
        elif tag == "pre":
            self.out.append("\n```\n")
            self.in_pre = False
        elif tag == "code" and self.in_code and not self.in_pre:
            self.out.append("`")
            self.in_code = False
        elif tag in ("td", "th") and self.in_table:
            text = normalize_text("".join(self.current_cell))
            self.current_row.append(text)
            self.in_cell = False
            self.in_header_cell = False
            self.current_cell = []
        elif tag == "tr" and self.in_table and self.current_row:
            row = "| " + " | ".join(cell.replace("|", "\\|") for cell in self.current_row) + " |\n"
            self.out.append(row)
            if not self.table_header_written:
                self.out.append("| " + " | ".join("---" for _ in self.current_row) + " |\n")
                self.table_header_written = True
            self.current_row = []
        elif tag == "table":
            self.in_table = False
            self._blank()

    def handle_data(self, data: str) -> None:
        if self.skip_anchor_depth:
            return
        if self.in_cell:
            self.current_cell.append(data)
        elif self.in_pre:
            self.out.append(data)
        else:
            self.out.append(data)

    def _blank(self) -> None:
        if not self.out:
            return
        text = "".join(self.out)
        if text.endswith("\n\n"):
            return
        if text.endswith("\n"):
            self.out.append("\n")
        else:
            self.out.append("\n\n")

    def markdown(self) -> str:
        text = "".join(self.out)
        text = unescape(text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def normalize_text(value: str) -> str:
    value = unescape(re.sub(r"<[^>]+>", " ", value))
    value = value.replace("\xa0", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def official_url(doc_path: str) -> str:
    encoded = "/".join(urllib.parse.quote(part) for part in doc_path.split("/"))
    return "{}/{}.html".format(BASE_URL, encoded)


def fetch(url: str) -> Tuple[str, Dict[str, str]]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=45) as resp:
        html = resp.read().decode("utf-8", "replace")
        headers = {k: v for k, v in resp.headers.items()}
        return html, headers


def extract_main_html(html: str) -> str:
    marker = '<div class="theme-default-content content__default">'
    start = html.find(marker)
    if start == -1:
        raise ValueError("cannot find official doc content container")
    start += len(marker)
    candidates = [idx for idx in (html.find('<div class="page-info-hide"', start), html.find("<footer", start)) if idx != -1]
    end = min(candidates) if candidates else html.find("</main>", start)
    if end == -1:
        end = len(html)
    return html[start:end]


def html_to_markdown(main_html: str) -> str:
    parser = MarkdownConverter()
    parser.feed(main_html)
    parser.close()
    return parser.markdown()


def write_doc(repo_root: Path, doc_path: str, markdown: str, url: str, last_modified: str) -> None:
    output_path = repo_root / "docs" / (doc_path + ".md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    body = (
        "---\n"
        "source_url: \"{}\"\n"
        "last_modified: \"{}\"\n"
        "synced_from: \"NetEase developer official website\"\n"
        "---\n\n"
        "{}"
    ).format(url, last_modified, markdown)
    output_path.write_text(body, encoding="utf-8")


def extract_official_links(changelog_html: str) -> Dict[str, str]:
    main = extract_main_html(changelog_html)
    links: Dict[str, str] = {}
    for href, label_html in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', main):
        label = normalize_text(label_html)
        if not label or "/1-ModAPI/" not in href:
            continue
        links[label] = href
    return links


def parse_index_rows(index_html: str) -> Dict[str, List[Dict[str, str]]]:
    main = extract_main_html(index_html)
    rows: Dict[str, List[Dict[str, str]]] = {}
    row_re = re.compile(
        r"<tr><td><a href=\"([^\"]+)\">([^<]+)</a></td>\s*"
        r"<td>(.*?)</td>\s*<td>(.*?)</td></tr>",
        re.S,
    )
    for href, name, side_html, desc_html in row_re.findall(main):
        entry = {
            "name": normalize_text(name),
            "href": href,
            "side": normalize_text(side_html),
            "desc": normalize_text(desc_html),
        }
        rows.setdefault(entry["name"], []).append(entry)
    return rows


def href_to_doc_path(href: str) -> str:
    path = href.split("#", 1)[0].split("?", 1)[0]
    prefix = "/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/"
    if path.startswith(prefix):
        path = path[len(prefix):]
    path = urllib.parse.unquote(path)
    if path.endswith(".html"):
        path = path[:-5]
    return path


def href_to_anchor(href: str, name: str) -> str:
    if "#" in href:
        return href.rsplit("#", 1)[-1].split("?", 1)[0]
    return name.lower()


def doc_class_path_from_href(href: str) -> List[str]:
    doc_path = href_to_doc_path(href)
    if doc_path.startswith("接口/"):
        return [doc_path[len("接口/"):]]
    if doc_path.startswith("事件/"):
        return [doc_path[len("事件/"):]]
    return [doc_path]


def strip_span_side(section_html: str) -> List[str]:
    return [normalize_text(m) for m in re.findall(r"<span[^>]*>(服务端|客户端)</span>", section_html)]


def section_for_anchor(page_html: str, anchor: str) -> str:
    start = page_html.find('<h2 id="{}"'.format(anchor))
    if start == -1:
        start = page_html.find("<h2 id='{}'".format(anchor))
    if start == -1:
        return ""
    end = page_html.find("<h2 id=", start + 1)
    if end == -1:
        end = page_html.find("<footer", start)
    if end == -1:
        end = len(page_html)
    return page_html[start:end]


def parse_table(table_html: str) -> List[List[str]]:
    rows: List[List[str]] = []
    for row_html in re.findall(r"<tr>(.*?)</tr>", table_html, re.S):
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row_html, re.S)
        if cells:
            rows.append([normalize_text(cell) for cell in cells])
    return rows


def parse_params(section_html: str) -> List[Dict[str, str]]:
    match = re.search(r"参数</p>\s*<table.*?</table>", section_html, re.S)
    if not match:
        return []
    table_match = re.search(r"<table.*?</table>", match.group(0), re.S)
    if not table_match:
        return []
    rows = parse_table(table_match.group(0))
    params = []
    for row in rows[1:]:
        if len(row) >= 3:
            params.append({
                "param_name": row[0],
                "param_type": row[1],
                "param_comment": row[2],
            })
    return params


def parse_return(section_html: str) -> Dict[str, str]:
    match = re.search(r"返回值</p>\s*<table.*?</table>", section_html, re.S)
    if match:
        table_match = re.search(r"<table.*?</table>", match.group(0), re.S)
        rows = parse_table(table_match.group(0)) if table_match else []
        if len(rows) > 1 and len(rows[1]) >= 2:
            return {"return_type": rows[1][0], "return_comment": rows[1][1]}
    if re.search(r"返回值</p>\s*<p>\s*无\s*</p>", section_html):
        return {"return_type": "", "return_comment": "无"}
    return {"return_type": "", "return_comment": ""}


def parse_desc(section_html: str, fallback: str) -> str:
    match = re.search(r"描述</p>\s*<p>(.*?)</p>", section_html, re.S)
    if match:
        return normalize_text(match.group(1))
    return fallback


def choose_method_path(section_html: str, side: str, fallback: str) -> str:
    paths = re.findall(r"method in ([A-Za-z0-9_.]+)", section_html)
    if not paths:
        return fallback
    if side == "服务端":
        for path in paths:
            if ".server." in path or path.endswith("Server"):
                return path
    if side == "客户端":
        for path in paths:
            if ".client." in path or path.endswith("Client"):
                return path
    return paths[0]


def load_json(path: Path) -> Dict[str, List[Dict[str, object]]]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: Dict[str, List[Dict[str, object]]]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")


def remove_existing_entry(data: Dict[str, List[Dict[str, object]]], name: str, side: str) -> None:
    empty_keys = []
    for class_path, entries in data.items():
        kept = [
            entry for entry in entries
            if not (entry.get("name") == name and (not side or entry.get("side") == side))
        ]
        if kept:
            data[class_path] = kept
        else:
            empty_keys.append(class_path)
    for key in empty_keys:
        del data[key]


def merge_entry(data: Dict[str, List[Dict[str, object]]], entry: Dict[str, object]) -> None:
    name = str(entry.get("name", ""))
    side = str(entry.get("side", ""))
    class_path = str(entry.get("path", ""))
    remove_existing_entry(data, name, side)
    data.setdefault(class_path, []).append(entry)


def page_html_for_href(href: str, html_by_doc: Dict[str, str]) -> str:
    doc_path = href_to_doc_path(href)
    return html_by_doc.get(doc_path, "")


def build_structured_entries(
    target_names: Iterable[str],
    rows_by_name: Dict[str, List[Dict[str, str]]],
    official_links: Dict[str, str],
    html_by_doc: Dict[str, str],
    entry_type: str,
) -> List[Dict[str, object]]:
    output: List[Dict[str, object]] = []
    for name in sorted(set(target_names)):
        rows = list(rows_by_name.get(name, []))
        if not rows and name in official_links:
            href = official_links[name]
            page_html = page_html_for_href(href, html_by_doc)
            section_html = section_for_anchor(page_html, href_to_anchor(href, name)) if page_html else ""
            sides = strip_span_side(section_html) or [""]
            rows = [
                {
                    "name": name,
                    "href": href,
                    "side": side,
                    "desc": "",
                }
                for side in dict.fromkeys(sides)
            ]
        for row in rows:
            href = row["href"]
            page_html = page_html_for_href(href, html_by_doc)
            section_html = section_for_anchor(page_html, href_to_anchor(href, name)) if page_html else ""
            sides = strip_span_side(section_html)
            side = row.get("side") or (sides[0] if sides else "")
            if entry_type == "event":
                class_path = "server.serverEvent" if side == "服务端" else "client.clientEvent"
            else:
                class_path = choose_method_path(section_html, side, row.get("href", ""))
            desc = parse_desc(section_html, row.get("desc", ""))
            entry = {
                "name": name,
                "path": class_path,
                "desc": desc,
                "doc_class_path": doc_class_path_from_href(href),
                "param": parse_params(section_html),
                "return": parse_return(section_html) if entry_type == "api" else {
                    "return_type": "",
                    "return_comment": "无",
                },
                "state": [{
                    "version": "3.8",
                    "operation": "同步",
                    "comment": "来自网易开发者官网 3.8 文档",
                }],
                "side": side,
            }
            output.append(entry)
    return output


def update_migration_aliases(interface_data: Dict[str, List[Dict[str, object]]]) -> None:
    by_name: Dict[str, Dict[str, object]] = {}
    for entries in interface_data.values():
        for entry in entries:
            by_name[str(entry.get("name"))] = entry
    for old_name, (new_name, note) in MIGRATION_ALIASES.items():
        existing = by_name.get(old_name)
        replacement = by_name.get(new_name)
        deprecated_desc = "3.8 已废弃：{} 旧名称仅保留用于搜索兼容，新开发请使用 {}。".format(note, new_name)
        if existing:
            existing["desc"] = deprecated_desc
            existing.setdefault("state", [])
            state = existing["state"]
            if isinstance(state, list) and not any(item.get("version") == "3.8" for item in state if isinstance(item, dict)):
                state.append({
                    "version": "3.8",
                    "operation": "废弃",
                    "comment": note,
                })
        elif replacement:
            alias_entry = dict(replacement)
            alias_entry["name"] = old_name
            alias_entry["desc"] = deprecated_desc
            alias_entry["state"] = [{
                "version": "3.8",
                "operation": "废弃",
                "comment": note,
            }]
            merge_entry(interface_data, alias_entry)


def sync(repo_root: Path, dry_run: bool = False, delay: float = 0.2) -> None:
    html_by_doc: Dict[str, str] = {}
    headers_by_doc: Dict[str, Dict[str, str]] = {}
    for doc_path in DOC_PATHS:
        url = official_url(doc_path)
        html, headers = fetch(url)
        html_by_doc[doc_path] = html
        headers_by_doc[doc_path] = headers
        markdown = html_to_markdown(extract_main_html(html))
        if not dry_run:
            write_doc(repo_root, doc_path, markdown, url, headers.get("Last-Modified", ""))
        print("synced doc: {} <- {}".format(doc_path, url))
        time.sleep(delay)

    changelog_html = html_by_doc[CHANGELOG_PATH]
    official_links = extract_official_links(changelog_html)
    api_names = {name for name, href in official_links.items() if "/接口/" in href}
    event_names = {name for name, href in official_links.items() if "/事件/" in href}
    api_names.update(ALWAYS_API_NAMES)
    event_names.update(ALWAYS_EVENT_NAMES)

    api_index_rows = parse_index_rows(html_by_doc["接口/Api索引表"])
    event_index_rows = parse_index_rows(html_by_doc["事件/事件索引表"])

    interface_path = repo_root / "docs" / "interface.json"
    events_path = repo_root / "docs" / "events.json"
    interface_data = load_json(interface_path)
    events_data = load_json(events_path)

    for entry in build_structured_entries(api_names, api_index_rows, official_links, html_by_doc, "api"):
        merge_entry(interface_data, entry)
    update_migration_aliases(interface_data)

    for entry in build_structured_entries(event_names, event_index_rows, official_links, html_by_doc, "event"):
        merge_entry(events_data, entry)

    if not dry_run:
        save_json(interface_path, interface_data)
        save_json(events_path, events_data)

    print("merged api entries: {}".format(len(api_names)))
    print("merged event entries: {}".format(len(event_names)))


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--delay", type=float, default=0.2)
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    try:
        sync(repo_root, dry_run=args.dry_run, delay=args.delay)
    except Exception as exc:
        print("official docs sync failed: {}".format(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
