#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全量同步官方 ModSDK 快照，并逐项比较两个官方版本。

版本和文档频道来自 standard/registry；MCP 运行时不会联网。
仅当所有索引、正文、来源和结构化条目均完整时，才事务性替换本地快照。
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple

BASE_URL = "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI"
SITE_URL = "https://mc.163.com"
PYTHON_WHITELIST_URL = (
    "https://mc.163.com/dev/mcmanual/mc-dev/mcguide/"
    "36-%E5%AE%A1%E6%A0%B8%E4%B8%8E%E4%B8%8B%E6%9E%B6/"
    "%E8%AF%BE%E7%A8%8B07-Python%E6%A8%A1%E5%9D%97%E7%99%BD%E5%90%8D%E5%8D%95.html"
)
PYTHON_WHITELIST_DOC_PATH = "审核与下架/Python模块白名单"
USER_AGENT = "Mozilla/5.0 (compatible; modsdk-mcp-doc-sync/3.0)"
API_INDEX_PATH = "接口/Api索引表"
EVENT_INDEX_PATH = "事件/事件索引表"
Fetcher = Callable[[str], Tuple[str, Mapping[str, str]]]


@dataclass
class SyncPlan:
    version: str
    files: Dict[Path, Optional[str]]
    discovered_doc_paths: List[str]
    api_entries: List[Dict[str, Any]]
    event_entries: List[Dict[str, Any]]
    comparison: Dict[str, Any]


@dataclass
class OfficialSnapshot:
    profile: Dict[str, Any]
    pages: Dict[str, Dict[str, Any]]
    api_entries: List[Dict[str, Any]]
    event_entries: List[Dict[str, Any]]
    tutorials: Dict[str, Dict[str, Any]]
    reference_aliases: List[Dict[str, str]] = field(default_factory=list)


class MarkdownConverter(HTMLParser):
    """足以转换官方参考页的轻量 HTML -> Markdown 转换器。"""

    def __init__(self, base_url: str = "") -> None:
        super().__init__(convert_charrefs=True)
        self.out: List[str] = []
        self.list_stack: List[str] = []
        self.in_pre = False
        self.in_code = False
        self.in_table = False
        self.in_cell = False
        self.current_row: List[str] = []
        self.current_cell: List[str] = []
        self.table_header_written = False
        self.skip_anchor_depth = 0
        self.base_url = base_url
        self.links: List[str] = []
        self.nested_cells = 0

    def handle_starttag(
        self,
        tag: str,
        attrs: Sequence[Tuple[str, Optional[str]]],
    ) -> None:
        attrs_map = dict(attrs)
        css_class = attrs_map.get("class", "") or ""
        if tag == "a" and "header-anchor" in css_class:
            self.skip_anchor_depth += 1
            return
        if self.skip_anchor_depth:
            return
        if self.in_cell:
            if tag in ("td", "th"):
                self.nested_cells += 1
            if tag in ("br", "p", "li", "tr", "td", "th"):
                self.current_cell.append(" ")
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
            language = "python" if "language-python" in css_class else ""
            self._blank()
            self.out.append("```{}\n".format(language))
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
            self.current_cell = []
        elif tag == "a":
            self.links.append(urllib.parse.urljoin(self.base_url, attrs_map.get("href", "") or ""))
            self.out.append("[")
        elif tag == "img":
            url = urllib.parse.urljoin(self.base_url, attrs_map.get("src", "") or "")
            self.out.append("![{}]({})".format(attrs_map.get("alt", "") or "图片", url))

    def handle_endtag(self, tag: str) -> None:
        if self.skip_anchor_depth:
            if tag == "a":
                self.skip_anchor_depth -= 1
            return
        if self.in_cell and tag not in ("td", "th"):
            if tag in ("p", "li", "tr"):
                self.current_cell.append(" ")
            return
        if self.in_cell and tag in ("td", "th") and self.nested_cells:
            self.nested_cells -= 1
            self.current_cell.append(" ")
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p", "li"):
            self._blank()
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
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
            self.current_row.append(normalize_text("".join(self.current_cell)))
            self.in_cell = False
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
        elif tag == "a" and self.links:
            self.out.append("]({})".format(self.links.pop()))

    def handle_data(self, data: str) -> None:
        if self.skip_anchor_depth:
            return
        if self.in_cell:
            self.current_cell.append(data)
        elif not self.in_pre and not data.strip():
            return
        else:
            self.out.append(data)

    def _blank(self) -> None:
        if not self.out:
            return
        text = "".join(self.out[-3:])
        if re.search(r"(?:^|\n)(?:- |1\. )$", text):
            return
        if text.endswith("\n\n"):
            return
        self.out.append("\n" if text.endswith("\n") else "\n\n")

    def markdown(self) -> str:
        text = "".join(self.out)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def normalize_text(value: str) -> str:
    value = unescape(re.sub(r"<[^>]+>", " ", value))
    value = value.replace("\xa0", " ")
    return re.sub(r"\s+", " ", value).strip()


def official_url(doc_path: str, base_url: str = BASE_URL) -> str:
    encoded = "/".join(urllib.parse.quote(part, safe="") for part in doc_path.split("/"))
    return "{}/{}.html".format(base_url.rstrip("/"), encoded)


def fetch(url: str) -> Tuple[str, Dict[str, str]]:
    encoded_url = urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%")
    request = urllib.request.Request(encoded_url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=45) as response:
        html = response.read().decode("utf-8")
        return html, {key: value for key, value in response.headers.items()}


def extract_main_html(html: str) -> str:
    marker = '<div class="theme-default-content content__default">'
    start = html.find(marker)
    if start == -1:
        raise ValueError("找不到官方文档正文容器")
    start += len(marker)
    candidates = [
        index
        for index in (
            html.find('<div class="page-info-hide"', start),
            html.find("<footer", start),
            html.find("</main>", start),
        )
        if index != -1
    ]
    end = min(candidates) if candidates else len(html)
    return html[start:end]


def html_to_markdown(main_html: str, source_url: str = "") -> str:
    parser = MarkdownConverter(source_url)
    parser.feed(main_html)
    parser.close()
    return parser.markdown()


def render_doc(markdown: str, url: str, last_modified: str) -> str:
    return (
        "---\n"
        'source_url: "{}"\n'
        'last_modified: "{}"\n'
        'synced_from: "NetEase developer official website"\n'
        "---\n\n"
        "{}"
    ).format(url, last_modified, markdown)


def extract_official_links(changelog_html: str) -> Dict[str, str]:
    main_html = extract_main_html(changelog_html)
    links: Dict[str, str] = {}
    pattern = re.compile(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.S | re.I)
    for href, label_html in pattern.findall(main_html):
        label = normalize_text(label_html)
        if label and re.search(r"/1-ModAPI(?:-beta)?/", href):
            links[label] = href
    return links


def href_to_doc_path(href: str) -> str:
    path = urllib.parse.urlparse(href).path
    match = re.search(r"/1-ModAPI(?:-beta)?/", path)
    if not match:
        raise ValueError("非 ModAPI 官方链接: {}".format(href))
    path = urllib.parse.unquote(path[match.end():])
    if path.endswith(".html"):
        path = path[:-5]
    parts = [part for part in path.replace("\\", "/").split("/") if part]
    if not parts or any(part in (".", "..") for part in parts):
        raise ValueError("非法官方文档路径: {}".format(href))
    return "/".join(parts)


def href_to_anchor(href: str, name: str) -> str:
    fragment = urllib.parse.urlparse(href).fragment
    return urllib.parse.unquote(fragment) if fragment else name.lower()


def absolute_source_url(href: str) -> str:
    return urllib.parse.urljoin(SITE_URL, href)


def doc_class_path_from_href(href: str) -> List[str]:
    doc_path = href_to_doc_path(href)
    for prefix in ("接口/", "事件/"):
        if doc_path.startswith(prefix):
            return [doc_path[len(prefix):]]
    return [doc_path]


def parse_index_rows(index_html: str) -> Dict[str, List[Dict[str, str]]]:
    rows: Dict[str, List[Dict[str, str]]] = {}
    for row_html in re.findall(r"<tr\b[^>]*>(.*?)</tr>", extract_main_html(index_html), re.S | re.I):
        cells = re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", row_html, re.S | re.I)
        if len(cells) < 3:
            continue
        link_match = re.search(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', cells[0], re.S | re.I)
        if not link_match:
            continue
        name = normalize_text(link_match.group(2))
        if not re.match(r"^[A-Za-z_]\w*$", name):
            continue
        entry = {
            "name": name,
            "href": link_match.group(1),
            "side": normalize_text(cells[1]),
            "desc": normalize_text(cells[2]),
        }
        rows.setdefault(name, []).append(entry)
    return rows


def section_for_anchor(page_html: str, anchor: str) -> str:
    pattern = re.compile(r'<h2\b[^>]*\bid=["\']{}["\'][^>]*>'.format(re.escape(anchor)), re.I)
    match = pattern.search(page_html)
    if not match:
        return ""
    next_match = re.search(r"<h2\b", page_html[match.end():], re.I)
    end = match.end() + next_match.start() if next_match else len(page_html)
    return page_html[match.start():end]


def split_side_sections(section_html: str) -> Dict[str, str]:
    headings = list(re.finditer(r"<h3\b[^>]*>(.*?)</h3>", section_html, re.S | re.I))
    sections: Dict[str, str] = {}
    for index, heading in enumerate(headings):
        title = normalize_text(heading.group(1))
        side = ""
        if "服务端接口" in title:
            side = "服务端"
        elif "客户端接口" in title:
            side = "客户端"
        if not side:
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(section_html)
        sections[side] = section_html[heading.start():end]
    return sections


def strip_span_side(section_html: str) -> List[str]:
    return [
        normalize_text(side)
        for side in re.findall(r"<span\b[^>]*>\s*(服务端|客户端)\s*</span>", section_html, re.S)
    ]


class TableParser(HTMLParser):
    """保留最外层表格列；将单元格中的嵌套字典说明完整保留为文本。"""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.rows: List[List[str]] = []
        self.row: List[str] = []
        self.cell: Optional[List[str]] = None

    def handle_starttag(self, tag: str, attrs: Any) -> None:
        if tag == "table":
            self.depth += 1
        elif tag == "tr" and self.depth == 1:
            self.row = []
        elif tag in ("td", "th") and self.depth == 1:
            self.cell = []
        elif self.cell is not None and tag in ("td", "th", "tr", "br", "p", "li"):
            self.cell.append(" ")

    def handle_endtag(self, tag: str) -> None:
        if tag == "table":
            self.depth -= 1
        elif tag in ("td", "th") and self.depth == 1 and self.cell is not None:
            self.row.append(re.sub(r"\s+", " ", "".join(self.cell)).strip())
            self.cell = None
        elif tag == "tr" and self.depth == 1 and self.row:
            self.rows.append(self.row)
        elif self.cell is not None and tag in ("td", "th", "tr", "p", "li"):
            self.cell.append(" ")

    def handle_data(self, text: str) -> None:
        if self.cell is not None:
            self.cell.append(text)


def parse_table(table_html: str) -> List[List[str]]:
    parser = TableParser()
    parser.feed(table_html)
    parser.close()
    return parser.rows


def _table_after_label(section_html: str, label: str) -> str:
    match = re.search(
        r">\s*{}\s*</p>\s*(<table\b[^>]*>)".format(re.escape(label)),
        section_html,
        re.S | re.I,
    )
    if not match:
        return ""
    start = match.start(1)
    depth = 0
    for tag in re.finditer(r"</?table\b[^>]*>", section_html[start:], re.I):
        depth += -1 if tag.group(0).startswith("</") else 1
        if depth == 0:
            return section_html[start:start + tag.end()]
    raise ValueError("官方参数表或返回值表没有完整闭合: " + label)


def parse_params(section_html: str) -> List[Dict[str, str]]:
    table_html = _table_after_label(section_html, "参数")
    rows = parse_table(table_html) if table_html else []
    return [
        {
            "param_comment": row[2],
            "param_name": row[0],
            "param_type": row[1],
        }
        for row in rows[1:]
        if len(row) >= 3
    ]


def parse_return(section_html: str) -> Dict[str, str]:
    table_html = _table_after_label(section_html, "返回值")
    rows = parse_table(table_html) if table_html else []
    if len(rows) > 1 and len(rows[1]) >= 2:
        return {"return_type": rows[1][0], "return_comment": rows[1][1]}
    if re.search(r">\s*返回值\s*</p>\s*<p\b[^>]*>\s*无\s*</p>", section_html, re.S):
        return {"return_type": "", "return_comment": "无"}
    return {"return_type": "", "return_comment": ""}


def parse_desc(section_html: str, fallback: str) -> str:
    match = re.search(r">\s*描述\s*</p>\s*<p\b[^>]*>(.*?)</p>", section_html, re.S | re.I)
    return normalize_text(match.group(1)) if match else fallback


def parse_remarks(section_html: str) -> List[str]:
    marker = re.search(r">\s*备注\s*</p>", section_html, re.S | re.I)
    if not marker:
        return []
    tail = section_html[marker.end():]
    end_markers = [
        match.start()
        for match in (
            re.search(r"<li\b[^>]*>\s*<p\b[^>]*>\s*示例\s*</p>", tail, re.S | re.I),
            re.search(r"<h3\b", tail, re.I),
        )
        if match
    ]
    block = tail[:min(end_markers)] if end_markers else tail
    items = [normalize_text(item) for item in re.findall(r"<li\b[^>]*>(.*?)</li>", block, re.S | re.I)]
    items = [item for item in items if item]
    if not items:
        text = normalize_text(block)
        if text:
            items = [text]
    return list(dict.fromkeys(items))


def _code_text(code_html: str) -> str:
    text = unescape(re.sub(r"<[^>]+>", "", code_html))
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\xa0", " ")
    return "\n".join(line.rstrip() for line in text.strip().split("\n"))


def parse_examples(section_html: str) -> List[str]:
    examples = [
        _code_text(code_html)
        for code_html in re.findall(r"<pre\b[^>]*>\s*<code\b[^>]*>(.*?)</code>\s*</pre>", section_html, re.S | re.I)
    ]
    return [example for example in examples if example]


def choose_method_path(section_html: str, side: str, fallback: str) -> str:
    paths = re.findall(r"method\s+in\s+([A-Za-z0-9_.]+)", section_html)
    if not paths:
        return fallback
    selected = paths[0]
    if side == "服务端":
        for path in paths:
            if ".server." in path or path.endswith("Server"):
                selected = path
                break
    if side == "客户端":
        for path in paths:
            if ".client." in path or path.endswith("Client"):
                selected = path
                break
    # interface.json 的既有类路径从 server/client 起始，不包含 Python 包根 mod。
    return selected[4:] if selected.startswith("mod.") else selected


def _header_value(headers: Mapping[str, str], name: str) -> str:
    name_lower = name.lower()
    for key, value in headers.items():
        if str(key).lower() == name_lower:
            return str(value)
    return ""


def _page_html_for_href(href: str, html_by_doc: Mapping[str, str]) -> str:
    return html_by_doc.get(href_to_doc_path(href), "")


def build_structured_entries(
    target_names: Iterable[str],
    rows_by_name: Mapping[str, List[Dict[str, str]]],
    official_links: Mapping[str, str],
    html_by_doc: Mapping[str, str],
    headers_by_doc: Mapping[str, Mapping[str, str]],
    entry_type: str,
    version: str,
) -> List[Dict[str, object]]:
    output: List[Dict[str, object]] = []
    seen: Set[Tuple[str, str, str]] = set()
    for name in sorted(set(target_names)):
        rows = [dict(row) for row in rows_by_name.get(name, [])]
        if not rows and name in official_links:
            href = official_links[name]
            page_html = _page_html_for_href(href, html_by_doc)
            section_html = section_for_anchor(page_html, href_to_anchor(href, name))
            sides = list(split_side_sections(section_html).keys()) or strip_span_side(section_html) or [""]
            rows = [{"name": name, "href": href, "side": side, "desc": ""} for side in dict.fromkeys(sides)]

        for row in rows:
            href = row["href"]
            doc_path = href_to_doc_path(href)
            page_html = _page_html_for_href(href, html_by_doc)
            whole_section = section_for_anchor(page_html, href_to_anchor(href, name))
            if not whole_section:
                raise ValueError("索引引用的正文锚点不存在: {}".format(href))
            side_sections = split_side_sections(whole_section)
            side = row.get("side", "").replace("服务端 客户端", "服务端/客户端")
            if not side:
                sides = strip_span_side(whole_section)
                side = sides[0] if sides else ""
            section_html = side_sections.get(side, whole_section)
            identity = (name, side, href)
            if identity in seen:
                continue
            seen.add(identity)

            if entry_type == "event":
                class_path = {"服务端": "server.serverEvent", "客户端": "client.clientEvent", "Apollo": "apollo"}[side]
            else:
                class_path = choose_method_path(section_html, side, "doc:" + doc_path)

            output.append({
                "name": name,
                "path": class_path,
                "desc": parse_desc(section_html, row.get("desc", "")),
                "doc_class_path": doc_class_path_from_href(href),
                "param": parse_params(section_html),
                "return": parse_return(section_html),
                "state": [{
                    "comment": "来自网易开发者官网 {} 文档".format(version),
                    "operation": "同步",
                    "version": version,
                }],
                "side": side,
                "remarks": parse_remarks(section_html),
                "examples": parse_examples(section_html),
                "source_url": absolute_source_url(href),
                "sdk_version": version,
                "source_last_modified": _header_value(headers_by_doc.get(doc_path, {}), "Last-Modified"),
            })
    return output


def parse_python_whitelist_entries(html: str) -> List[Dict[str, str]]:
    """保留官方展示文本，同时生成用于精确匹配的规范化模块名。"""
    entries: List[Dict[str, str]] = []
    main_html = extract_main_html(html)
    for cell in re.findall(r"<td\b[^>]*>(.*?)</td>", main_html, re.S | re.I):
        raw_display = normalize_text(cell)
        # 官方表格中的 ast 带有“（3.3新增）”说明，说明文字不属于模块名。
        normalized = re.sub(r"[（(][^）)]*新增[^）)]*[）)]$", "", raw_display).strip()
        if normalized and re.match(r"^[A-Za-z_][A-Za-z0-9_.]*$", normalized):
            entries.append({
                "raw_display": raw_display,
                "normalized_name": normalized,
            })
    return entries


def parse_python_whitelist(html: str) -> List[str]:
    return [entry["normalized_name"] for entry in parse_python_whitelist_entries(html)]


def _http_date_to_iso(value: str) -> str:
    if not value:
        return "unknown"
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return value
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_python_whitelist_snapshot(
    html: str,
    headers: Mapping[str, str],
    entries: Sequence[Mapping[str, str]],
) -> Dict[str, object]:
    modules = [entry["normalized_name"] for entry in entries]
    module_text = "\n".join(modules) + "\n"
    annotations_removed = {
        entry["raw_display"]: entry["normalized_name"]
        for entry in entries
        if entry["raw_display"] != entry["normalized_name"]
    }
    cell_count = len(re.findall(r"<td\b[^>]*>.*?</td>", extract_main_html(html), re.S | re.I))
    retrieved_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "schema_version": "1.0",
        "source_id": "netease-python-module-whitelist",
        "source_url": PYTHON_WHITELIST_URL,
        "retrieved_at": retrieved_at,
        "last_modified": _http_date_to_iso(_header_value(headers, "Last-Modified")),
        "source_sha256": hashlib.sha256(html.encode("utf-8")).hexdigest(),
        "modules_sha256": hashlib.sha256(module_text.encode("utf-8")).hexdigest(),
        "module_count": len(modules),
        "normalization": {
            "discarded_cells": cell_count - len(entries),
            "annotations_removed": annotations_removed,
        },
        "entries": [dict(entry) for entry in entries],
        "modules": modules,
    }


def render_python_whitelist(modules: Sequence[str], last_modified: str) -> str:
    lines = [
        "# Python模块白名单",
        "",
        "本页由网易开发者官网白名单表格同步生成，共 {} 个唯一模块。".format(len(modules)),
        "",
        "| 序号 | 模块 |",
        "| --- | --- |",
    ]
    lines.extend("| {} | `{}` |".format(index, module) for index, module in enumerate(modules, 1))
    return render_doc("\n".join(lines) + "\n", PYTHON_WHITELIST_URL, last_modified)


def _json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_profile(repo_root: Path, version: str = "current") -> Dict[str, Any]:
    registry = repo_root / "standard" / "registry"
    manifest = json.loads((registry / "manifest.json").read_text(encoding="utf-8"))
    if version in ("current", "latest"):
        version = manifest["default_version"]
    if version not in manifest["version_files"]:
        raise ValueError("版本未注册: {}".format(version))
    return json.loads((registry / manifest["version_files"][version]).read_text(encoding="utf-8"))


class CachedFetcher:
    """显式缓存同一批调查的原始响应；不把 HTTP 200 的官网错误页当正文。"""

    def __init__(self, cache_dir: Optional[Path], delay: float = 0.15):
        self.cache_dir = cache_dir
        self.delay = delay
        if cache_dir:
            cache_dir.mkdir(parents=True, exist_ok=True)

    def __call__(self, url: str) -> Tuple[str, Mapping[str, str]]:
        cache_path = self.cache_dir / (_sha256(url) + ".json") if self.cache_dir else None
        if cache_path and cache_path.exists():
            cached = json.loads(cache_path.read_text(encoding="utf-8"))
            extract_main_html(cached["html"])
            return cached["html"], cached["headers"]
        for attempt in range(3):
            try:
                html, headers = fetch(url)
                extract_main_html(html)
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(attempt + 1)
        if cache_path:
            cache_path.write_text(_json_text({"url": url, "html": html, "headers": headers}), encoding="utf-8")
        if self.delay:
            time.sleep(self.delay)
        return html, headers


def _discover_pages(html: str, base_url: str) -> Set[str]:
    prefix = urllib.parse.unquote(urllib.parse.urlsplit(base_url).path).rstrip("/") + "/"
    paths: Set[str] = set()
    for href in re.findall(r'href=["\']([^"\']+)["\']', html):
        parts = urllib.parse.urlsplit(urllib.parse.urljoin(base_url + "/", unescape(href)))
        path = urllib.parse.unquote(parts.path)
        if parts.hostname == "mc.163.com" and path.startswith(prefix) and path.endswith(".html"):
            relative = path[len(prefix):-5]
            if relative.startswith(("接口/", "事件/", "枚举值/")):
                paths.add(relative)
    return paths


def _canonical_entries(entries: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """同一个引擎方法重复出现在分类索引时合并出处；不同类的同名方法独立保留。"""
    unique: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for entry in entries:
        key = (entry["path"], entry["name"], entry["side"])
        if key in unique:
            previous = unique[key]
            for field in ("param", "return", "desc", "remarks", "examples"):
                if previous[field] != entry[field]:
                    raise ValueError("同一方法的官方正文互相冲突: {} / {}".format(previous["source_url"], entry["source_url"]))
            previous.setdefault("additional_source_urls", []).append(entry["source_url"])
            continue
        unique[key] = entry
    return [unique[key] for key in sorted(unique)]


def fetch_snapshot(
    profile: Dict[str, Any], fetcher: Fetcher, workers: int = 6,
) -> OfficialSnapshot:
    base_url = profile["docs_base_url"]
    version = profile["version"]
    pages: Dict[str, Dict[str, Any]] = {}
    reference_aliases: Dict[Tuple[str, str], Dict[str, str]] = {}

    def get_page(doc_path: str) -> Tuple[str, Dict[str, Any]]:
        url = official_url(doc_path, base_url)
        html, headers = fetcher(url)
        main = extract_main_html(html)
        return doc_path, {"url": url, "html": html, "headers": dict(headers), "markdown": html_to_markdown(main, url)}

    seeds = [API_INDEX_PATH, EVENT_INDEX_PATH, "更新信息/" + version]
    with ThreadPoolExecutor(max_workers=workers) as executor:
        pages.update(executor.map(get_page, seeds))
        # 同一个官网频道会随稳定版发布整体滚动，旧更新页仍在不代表接口仍属于旧版。
        channel_path = urllib.parse.urlsplit(base_url).path.rstrip("/") + "/更新信息/"
        published_versions = set()
        for href in re.findall(r'href=["\']([^"\']+)["\']', pages[API_INDEX_PATH]["html"]):
            path = urllib.parse.unquote(urllib.parse.urlsplit(urllib.parse.urljoin(base_url + "/", href)).path)
            if path.startswith(channel_path):
                match = re.fullmatch(r"(\d+\.\d+)\.html", path[len(channel_path):])
                if match:
                    published_versions.add(match.group(1))
        active_version = max(published_versions, key=lambda value: tuple(map(int, value.split(".")))) if published_versions else None
        if active_version != version:
            raise ValueError("官网频道当前版本为 {}，拒绝作为 {} 快照；历史比较必须使用冻结基线".format(active_version, version))
        paths: Set[str] = set(seeds)
        for page in pages.values():
            paths.update(_discover_pages(page["html"], base_url))
        for path, page in executor.map(get_page, sorted(paths - pages.keys())):
            pages[path] = page
        # 分类页之外还可引用专门的详情页，按正文引用补齐；导航里的页面不再是唯一发现来源。
        while True:
            discovered = set()
            for source_path, page in pages.items():
                for referenced_path in _discover_pages(extract_main_html(page["html"]), base_url):
                    # 官方部分物理参数链接误多写“接口/”；仅在正确枚举页已经实际抓取时归并。
                    canonical = referenced_path.removeprefix("接口/")
                    if referenced_path.startswith("接口/枚举值/") and canonical in pages:
                        reference_aliases[(source_path, referenced_path)] = {
                            "source_path": source_path, "original_url": official_url(referenced_path, base_url),
                            "resolved_url": pages[canonical]["url"],
                        }
                        referenced_path = canonical
                    discovered.add(referenced_path)
            missing = sorted(discovered - pages.keys())
            if not missing:
                break
            for path, page in executor.map(get_page, missing):
                pages[path] = page
    api_rows = parse_index_rows(pages[API_INDEX_PATH]["html"])
    event_rows = parse_index_rows(pages[EVENT_INDEX_PATH]["html"])
    if not api_rows or not event_rows:
        raise ValueError("官方索引为空，拒绝替换本地数据")
    html_by_doc = {path: page["html"] for path, page in pages.items()}
    headers_by_doc = {path: page["headers"] for path, page in pages.items()}
    entries = []
    for entry_type, rows in (("api", api_rows), ("event", event_rows)):
        parsed = build_structured_entries(rows, rows, {}, html_by_doc, headers_by_doc, entry_type, version)
        expected = {(r["name"], r["side"].replace("服务端 客户端", "服务端/客户端"),
                     href_to_doc_path(r["href"]), href_to_anchor(r["href"], r["name"]))
                    for group in rows.values() for r in group}
        actual = {(e["name"], e["side"], href_to_doc_path(e["source_url"]),
                   href_to_anchor(e["source_url"], e["name"])) for e in parsed}
        if expected != actual:
            raise ValueError("{} 索引与正文不完整: {}".format(entry_type, sorted(expected - actual)))
        entries.append(_canonical_entries(parsed))

    # 教程不按 ModSDK 版本分频道，只声明相对于仓库旧副本的变化。
    tutorials: Dict[str, Dict[str, Any]] = {}
    release = pages["更新信息/" + version]
    links = re.findall(r'href=["\']([^"\']+)["\']', extract_main_html(release["html"]))
    urls = {urllib.parse.urljoin(release["url"], href) for href in links if "/mcguide/" in href and "Demo" not in href}
    for url in sorted(urls):
        parts = urllib.parse.urlsplit(url)
        if parts.hostname != "mc.163.com":
            raise ValueError("教程链接不是网易官方来源: " + url)
        html, headers = fetcher(url)
        main = extract_main_html(html)
        relative = urllib.parse.unquote(parts.path.split("/mcguide/", 1)[1]).removesuffix(".html")
        tutorials["教程/" + relative] = {"url": url, "html": html, "headers": dict(headers), "markdown": html_to_markdown(main, url)}
    print("已抓取官方 {}: {} 文档，{} API，{} 事件，{} 关联教程".format(version, len(pages), len(entries[0]), len(entries[1]), len(tutorials)), flush=True)
    return OfficialSnapshot(profile, pages, entries[0], entries[1], tutorials, [reference_aliases[key] for key in sorted(reference_aliases)])


def _entry_key(entry: Mapping[str, Any]) -> Tuple[str, str, str]:
    return entry["path"], entry["name"], entry["side"]


def _entry_summary(entry: Mapping[str, Any]) -> Dict[str, Any]:
    return {field: entry[field] for field in ("name", "side", "path", "doc_class_path", "param", "return", "desc", "remarks", "examples", "source_url")}


def _release_changes(snapshot: OfficialSnapshot) -> List[Dict[str, Any]]:
    page = snapshot.pages["更新信息/" + snapshot.profile["version"]]
    text = re.sub(r"\[([^\]]+)\]\([^\n]*?\)", r"\1", page["markdown"])
    headings = list(re.finditer(r"(?m)^#\s+" + re.escape(snapshot.profile["version"]) + r"\s*$", text))
    if headings:
        text = text[headings[-1].end():]
    entries = []
    for operation, name, side, comment in re.findall(r"(?m)^(?:\d+\.\s*|-\s*)?(新增|调整|删除|废弃)([A-Za-z_]\w*)\((服务端|客户端)\)[，,]?\s*(.*)$", text):
        entries.append({"operation": operation, "name": name, "side": side, "comment": comment.strip(), "source_url": page["url"]})
    return entries


def _enum_values(page: Mapping[str, Any]) -> Dict[str, str]:
    values = {}
    for block in re.findall(r"```[^\n]*\n(.*?)```", page["markdown"], re.S):
        for name, value in re.findall(r"(?m)^\s*([A-Za-z_]\w*)\s*=\s*([^\n#]+)", block):
            values[name] = value.strip()
    return values


def compare_snapshots(before: OfficialSnapshot, after: OfficialSnapshot) -> Dict[str, Any]:
    """正文与索引双重比较；分类迁移不算删除，源地址和同步时间不算契约修改。"""
    report: Dict[str, Any] = {"schema_version": "1.0", "from_version": before.profile["version"], "to_version": after.profile["version"], "scope": "冻结的官方 {} 基线与当前官方 {} {} 文档的完整比较，非运行时行为证明".format(before.profile["version"], after.profile["version"], after.profile["status"])}
    for kind, old_entries, new_entries in (("api", before.api_entries, after.api_entries), ("event", before.event_entries, after.event_entries)):
        old = {_entry_key(entry): entry for entry in old_entries}
        new = {_entry_key(entry): entry for entry in new_entries}
        changes = []
        for key in sorted(old.keys() & new.keys()):
            fields = [f for f in ("param", "return", "desc", "remarks", "examples", "doc_class_path") if old[key][f] != new[key][f]]
            if fields:
                changes.append({"name": key[1], "side": key[2], "path": key[0], "changed_fields": fields, "source_url": new[key]["source_url"], "before": _entry_summary(old[key]), "after": _entry_summary(new[key])})
        report[kind] = {
            "before_count": len(old), "after_count": len(new),
            "added": [_entry_summary(new[k]) for k in sorted(new.keys() - old.keys())],
            "removed": [_entry_summary(old[k]) for k in sorted(old.keys() - new.keys())],
            "changed": changes,
        }
    report["documents"] = {"before_count": len(before.pages), "after_count": len(after.pages), "added": [], "removed": [], "changed": []}
    for path in sorted(before.pages.keys() | after.pages.keys()):
        a, b = before.pages.get(path), after.pages.get(path)
        if not a or not b:
            page = b or a
            report["documents"]["added" if b else "removed"].append({"path": path, "source_url": page["url"]})
        elif re.sub(r"/1-ModAPI(?:-beta)?/", "/1-ModAPI/", a["markdown"]) != re.sub(r"/1-ModAPI(?:-beta)?/", "/1-ModAPI/", b["markdown"]):
            report["documents"]["changed"].append({"path": path, "before_url": a["url"], "after_url": b["url"], "before_sha256": _sha256(a["markdown"]), "after_sha256": _sha256(b["markdown"])})
    enums: Dict[str, Any] = {"before_count": 0, "after_count": 0, "added": [], "removed": [], "changed": []}
    for path in sorted(before.pages.keys() | after.pages.keys()):
        if not path.startswith("枚举值/"):
            continue
        old = _enum_values(before.pages[path]) if path in before.pages else {}
        new = _enum_values(after.pages[path]) if path in after.pages else {}
        enums["before_count"] += len(old)
        enums["after_count"] += len(new)
        for name in sorted(old.keys() | new.keys()):
            if old.get(name) == new.get(name):
                continue
            op = "added" if name not in old else "removed" if name not in new else "changed"
            page = after.pages[path] if path in after.pages else before.pages[path]
            enums[op].append({"path": path, "name": name, "before_value": old.get(name), "after_value": new.get(name), "source_url": page["url"]})
    report["enum"] = enums
    release_entries = _release_changes(after)
    declared = {(e["name"], e["side"]): e["operation"] for e in release_entries}
    for kind in ("api", "event"):
        for entry in report[kind]["added"]:
            entry["declared_operation"] = declared.get((entry["name"], entry["side"]), "未列入该版本更新日志")
    api_keys = {(e["name"], e["side"]) for e in after.api_entries}
    event_keys = {(e["name"], e["side"]) for e in after.event_entries}
    report["release_notes"] = {"entries": release_entries, "summary": {
        "api_added": sum(e["operation"] == "新增" and (e["name"], e["side"]) in api_keys for e in release_entries),
        "event_added": sum(e["operation"] == "新增" and (e["name"], e["side"]) in event_keys for e in release_entries),
        "adjusted": sum(e["operation"] == "调整" for e in release_entries),
        "deleted_or_deprecated": sum(e["operation"] in {"删除", "废弃"} for e in release_entries),
    }}
    report["caveats"] = [
        "按端侧、类路径和名称计数，双端方法分别计数；官网重复分类引用已去重。",
        "索引新出现不等于 SDK 首次引入；更新日志分类、两版快照差异与旧仓库资料分别保留。",
        "当前文档版本 {}、状态 {}，以本次核验的官方频道为准；计划发布日期不能单独证明发布。".format(after.profile["version"], after.profile["status"]),
        "分类页迁移与历史更新页的频道差异不代表接口删除。",
        "官网稳定版频道会滚动更新；旧版签名以冻结基线正文为准，历史来源链接当前内容不能替代旧版证据。",
        "教程为非版本化官方页面，只能证明当前公开配置，不能直接归因于 3.9→3.10。",
        "文档、构建和文件核对不构成游戏功能验收。",
    ]
    return report


def _group_entries(entries: Sequence[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for entry in entries:
        grouped.setdefault(entry["path"], []).append(entry)
    return grouped


def render_comparison_report(repo_root: Path, before: OfficialSnapshot, after: OfficialSnapshot, comparison: Dict[str, Any]) -> str:
    """从差异快照生成可检索的调查报告，避免人工维护第二份变更清单。"""
    old_version, version = comparison["from_version"], comparison["to_version"]
    lines = ["# ModSDK {} → {} 调查与迁移说明".format(old_version, version), "",
             "调查时间：{}。".format(comparison["retrieved_at"]), "",
             "## 版本与证据范围", "",
             "| 版本 | BE | 当前官方状态 | 文档 |", "| --- | --- | --- | --- |"]
    for snapshot in (before, after):
        p = snapshot.profile
        lines.append("| {} | {} | {} | [官方更新信息]({}) |".format(p["version"], p["bedrock_version"], p["status"], snapshot.pages["更新信息/" + p["version"]]["url"]))
    p = after.profile
    if p["status"] == "stable":
        lines.extend(["", "已核验官方稳定版频道，更新信息列出的稳定版上线日期为 {}。".format(p["released_at"])])
    if p.get("scheduled_stable_at"):
        lines.extend(["", "官方计划稳定版：{}；计划全渠道更新：{}。这些日期不代表已经发布。".format(p["scheduled_stable_at"], p["scheduled_rollout_at"])])
    lines.extend(["", "逐页抓取 {} 份旧版参考文档、{} 份目标版参考文档及 {} 篇关联教程；另外重新抓取 Python 白名单。".format(len(before.pages), len(after.pages), len(after.tutorials)),
                  "原始 HTML 和转换正文的 SHA-256、来源 URL、更新时间见 [来源清单](../../standard/registry/snapshots/official-docs.json)。完整参数、返回、备注、示例和前后值见 [机器可读差异](../../standard/registry/snapshots/modsdk-{}-to-{}.json)。".format(old_version, version), ""])
    lines.extend("- " + item for item in comparison["caveats"])
    release = comparison["release_notes"]["summary"]
    lines.extend(["", "## 差异总量", "",
                  "官方发布日志明确新增 **{} 个接口条目、{} 个事件**，列出 {} 项调整，没有列出删除或废弃。".format(release["api_added"], release["event_added"], release["adjusted"]), "",
                  "| 比较对象 | {} | {} | 新出现 | 不再出现 | 有变化 |".format(old_version, version), "| --- | --- | --- | --- | --- | --- |"])
    for kind, label in (("api", "接口"), ("event", "事件"), ("enum", "枚举常量"), ("documents", "参考文档页")):
        d = comparison[kind]
        lines.append("| {} | {} | {} | {} | {} | {} |".format(label, d["before_count"], d["after_count"], len(d["added"]), len(d["removed"]), len(d["changed"])))
    api_changes = comparison["api"]["changed"]
    moves = sum(e["changed_fields"] == ["doc_class_path"] for e in api_changes)
    lines.extend(["", "接口变化中 {} 项只有分类迁移，{} 项包含参数、描述、备注或示例变化。参考文档页不再出现包含旧物理分类页迁移和版本更新页频道变化，不是接口删除。".format(moves, len(api_changes) - moves),
                  "计数保留客户端、服务端、双端与 Apollo 的官方条目；相同引擎方法的重复分类引用只计一次。", "",
                  "## 官方索引中新出现的全部接口", "",
                  "下表包含发布日志明确新增、发布日志列为调整、未列入日志三种情况；标注历史已收录的接口不能称为 SDK 首次新增。", "",
                  "| 接口与官方依据 | 端侧 | 分类 | 发布日志分类 | 旧仓库情况 |", "| --- | --- | --- | --- | --- |"])
    for e in comparison["api"]["added"]:
        lines.append("| [{}]({}) | {} | {} | {} | {} |".format(e["name"], e["source_url"], e["side"], "; ".join(e["doc_class_path"]), e["declared_operation"], "历史已收录" if e.get("historical_repository_entry") else "—"))
    lines.extend(["", "## 全部已有接口变化", "", "| 接口与官方依据 | 端侧 | 变化内容 |", "| --- | --- | --- |"])
    labels = {"param": "参数", "return": "返回值", "desc": "描述", "remarks": "备注", "examples": "示例", "doc_class_path": "分类"}
    for e in api_changes:
        notes = []
        for field in e["changed_fields"]:
            if field == "param":
                a = [p["param_name"] for p in e["before"][field]]
                b = [p["param_name"] for p in e["after"][field]]
                if a != b:
                    notes.append("参数列表：{} → {}".format(", ".join(a), ", ".join(b)))
                else:
                    notes.append("参数类型或说明调整")
            elif field == "doc_class_path":
                notes.append("分类：{} → {}".format("; ".join(e["before"][field]), "; ".join(e["after"][field])))
            else:
                notes.append(labels[field] + "调整")
        lines.append("| [{}]({}) | {} | {} |".format(e["name"], e["after"]["source_url"], e["side"], "；".join(notes)))
    lines.extend(["", "### 发布日志列出的全部调整", ""])
    for e in comparison["release_notes"]["entries"]:
        if e["operation"] == "调整":
            lines.append("- {}（{}）：{}".format(e["name"], e["side"], e["comment"]))
    lines.extend(["", "## 全部事件变化", "", "| 索引新出现事件与官方依据 | 端侧 | 参数 | 发布日志分类 |", "| --- | --- | --- | --- |"])
    for e in comparison["event"]["added"]:
        lines.append("| [{}]({}) | {} | {} | {} |".format(e["name"], e["source_url"], e["side"], ", ".join(p["param_name"] for p in e["param"]), e["declared_operation"]))
    for e in comparison["event"]["changed"]:
        lines.extend(["", "### {}（{}）".format(e["name"], e["side"])])
        for field in e["changed_fields"]:
            lines.append("- {}：{} → {}。".format(labels[field], json.dumps(e["before"][field], ensure_ascii=False), json.dumps(e["after"][field], ensure_ascii=False)))
        lines.append("- [官方正文]({})。说明文字移除本身不能证明游戏触发条件或设备支持被删除。".format(e["after"]["source_url"]))
    lines.extend(["", "## 枚举变化", "", "| 枚举与官方依据 | 原值 | 新值 |", "| --- | --- | --- |"])
    for op in ("added", "removed", "changed"):
        for e in comparison["enum"][op]:
            label = e["path"].split("/")[-1] + "." + e["name"]
            a = str(e["before_value"] if e["before_value"] is not None else "无").replace("|", "\\|")
            b = str(e["after_value"] if e["after_value"] is not None else "无").replace("|", "\\|")
            lines.append("| [{}]({}) | {} | {} |".format(label, e["source_url"], a, b))
    lines.extend(["", "## 迁移时需要处理的行为与其他内容", ""])
    rules_path = repo_root / "standard/registry/rules" / ("modsdk-{}.json".format(version))
    if rules_path.exists():
        for rule in json.loads(rules_path.read_text(encoding="utf-8"))["rules"]:
            lines.extend(["### " + rule["title"], ""])
            lines.extend("- " + item for item in rule["do"])
            lines.append("")
    lines.extend(["官方更新信息还说明：从 3.9 起包体合并，默认 OpenGL；3.10 文档要求在 MCS 创建世界时选择渲染引擎，局内切换仍需完善。", "",
                  "关联物理与标签教程为当前未分版本页面；本次同步其配置证据，不把其中所有内容宣称为 3.10 首次新增。"])
    for path, page in after.tutorials.items():
        lines.append("- [{}]({})。".format(path, page["url"]))
    reconciliation = comparison.get("repository_reconciliation")
    if reconciliation:
        lines.extend(["", "## 旧仓库资料清理与删除边界", "", reconciliation["interpretation"], "",
                      "升级前清单冻结于提交 `{}`，见 [原清单](../../standard/registry/snapshots/pre-{}-repository-inventory.json)。".format(reconciliation["git_commit"], version), "",
                      "| 类型 | 已不在当前官方公开索引的旧库条目 |", "| --- | --- |"])
        for kind, label in (("api", "接口"), ("event", "事件")):
            for e in reconciliation[kind]["absent_from_current_official"]:
                lines.append("| {} | {}（{}） |".format(label, e["name"], e["side"]))
    lines.extend(["", "## 全部参考文档页变化", "", "| 差异 | 页面与官方依据 |", "| --- | --- |"] )
    for operation, label in (("added", "新出现"), ("removed", "不再出现"), ("changed", "内容调整")):
        for item in comparison["documents"][operation]:
            lines.append("| {} | [{}]({}) |".format(label, item["path"], item.get("source_url") or item["after_url"]))
    lines.extend(["", "## 本工具升级方式", "",
                  "- 默认 ModSDK、BE 上限与发布状态统一读取版本注册表；历史版本保留规则入口，API 检索明确使用当前完整快照。",
                  "- 全量重建接口、事件和官方导航；按类路径、名称、端侧去重，保留不同类的同名方法。",
                  "- 已消失的旧官方分类正文从当前全文索引移除，旧条目清单单独保留，不混入当前 API。",
                  "- 官方事件生成器使用查证后的标准名称，保留 PhysX 大写 X，并明确排除普通双端生成器不支持的独立服务器事件。",
                  "- 新增 get_version_changes、modsdk-guidance://changes 和当前版本迁移规则；迁移报告由同一份差异自动生成。",
                  "- 同步前完成全部抓取和数据核对，再事务性创建、替换、移除文件；写入失败会回滚。运行时不联网。", "",
                  "## 制作检查与实机边界", "",
                  "不编写、恢复或运行离线单元测试。JSON、来源、条目、哈希、重复身份、编码和 Python 编译核对只属于制作检查，不构成游戏功能测试通过。",
                  "本次没有启动游戏，没有对 3.10 的接口行为作实机验收；官方文档同步不等同于运行时源码复核。",
                  "已运行的 MCP 进程需要重启连接，才能使用更新后的服务代码、描述、默认版本和新增工具。", ""])
    return "\n".join(lines)


def _reconcile_repository(repo_root: Path, snapshot: OfficialSnapshot, comparison: Dict[str, Any]) -> None:
    inventory_path = repo_root / "standard/registry/snapshots" / ("pre-{}-repository-inventory.json".format(snapshot.profile["version"]))
    if not inventory_path.exists():
        return
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    result: Dict[str, Any] = {"git_commit": inventory["git_commit"], "scope": inventory["provenance"], "interpretation": "旧仓库独有且在官方两版均未出现的条目从当前索引移除；这只证明旧资料不在当前官方公开目录，不能证明 3.10 运行时删除。"}
    for kind, current in (("api", snapshot.api_entries), ("event", snapshot.event_entries)):
        entries = inventory[kind]["entries"]
        old_keys = {(e["name"], e["side"]) for e in entries}
        current_keys = {(e["name"], e["side"]) for e in current}
        result[kind] = {"before_count": len(entries), "absent_from_current_official": [e for e in entries if (e["name"], e["side"]) not in current_keys]}
        historical = []
        for entry in comparison[kind]["added"]:
            if (entry["name"], entry["side"]) in old_keys:
                entry["historical_repository_entry"] = True
                historical.append({"name": entry["name"], "side": entry["side"], "source_url": entry["source_url"]})
        result[kind]["index_additions_already_in_repository"] = historical
    comparison["repository_reconciliation"] = result


def _snapshot_sources(snapshot: OfficialSnapshot) -> Dict[str, Any]:
    return {"version": snapshot.profile["version"], "status": snapshot.profile["status"], "docs_base_url": snapshot.profile["docs_base_url"], "api_count": len(snapshot.api_entries), "event_count": len(snapshot.event_entries), "reference_aliases": snapshot.reference_aliases, "documents": [
        {"path": path, "source_url": page["url"], "last_modified": _header_value(page["headers"], "Last-Modified"), "source_sha256": page.get("source_sha256") or _sha256(page["html"]), "markdown_sha256": _sha256(page["markdown"])}
        for path, page in sorted({**snapshot.pages, **snapshot.tutorials}.items())]}


def freeze_snapshot(snapshot: OfficialSnapshot) -> Dict[str, Any]:
    def pages(values: Mapping[str, Any]) -> Dict[str, Any]:
        return {path: {"url": page["url"], "headers": {key: value for key, value in page["headers"].items() if key.casefold() in {"last-modified", "etag"}}, "markdown": page["markdown"], "source_sha256": page.get("source_sha256") or _sha256(page["html"])} for path, page in sorted(values.items())}
    return {"schema_version": "1.0", "frozen_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"), "profile": snapshot.profile, "pages": pages(snapshot.pages), "tutorials": pages(snapshot.tutorials), "api_entries": snapshot.api_entries, "event_entries": snapshot.event_entries, "reference_aliases": snapshot.reference_aliases}


def load_frozen_snapshot(path: Path, version: str) -> OfficialSnapshot:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != "1.0" or payload["profile"]["version"] != version:
        raise ValueError("冻结基线版本不匹配: " + str(path))
    print("已载入冻结的官方 {} 基线（{}）".format(version, payload["frozen_at"]), flush=True)
    return OfficialSnapshot(payload["profile"], payload["pages"], payload["api_entries"], payload["event_entries"], payload["tutorials"], payload.get("reference_aliases", []))


def build_sync_plan(
    repo_root: Path, version: str = "current", compare_version: Optional[str] = None,
    include_python_whitelist: bool = True, workers: int = 6, fetcher: Fetcher = fetch,
    refresh_baseline: bool = False,
) -> SyncPlan:
    repo_root = repo_root.resolve()
    profile = load_profile(repo_root, version)
    version = profile["version"]
    if version != load_profile(repo_root)["version"]:
        raise ValueError("全量同步必须与注册表默认版本一致；历史版本由冻结基线保留")
    compare_version = compare_version or profile.get("previous_version")
    current = fetch_snapshot(profile, fetcher, workers)
    baseline_path = repo_root / "standard/registry/snapshots" / ("modsdk-{}-baseline.json".format(compare_version))
    if compare_version:
        previous = load_frozen_snapshot(baseline_path, compare_version) if baseline_path.exists() and not refresh_baseline else fetch_snapshot(load_profile(repo_root, compare_version), fetcher, workers)
    else:
        previous = None
    comparison = compare_snapshots(previous, current) if previous else {}
    if comparison:
        _reconcile_repository(repo_root, current, comparison)
    files: Dict[Path, Optional[str]] = {}
    if previous and (refresh_baseline or not baseline_path.exists()):
        files[baseline_path] = _json_text(freeze_snapshot(previous))
    elif previous:
        files[baseline_path] = baseline_path.read_text(encoding="utf-8")
    for path, page in {**current.pages, **current.tutorials}.items():
        files[repo_root / "docs" / (path + ".md")] = render_doc(page["markdown"], page["url"], _header_value(page["headers"], "Last-Modified"))
    files[repo_root / "docs/interface.json"] = _json_text(_group_entries(current.api_entries))
    files[repo_root / "docs/events.json"] = _json_text(_group_entries(current.event_entries))
    # 不留失效的分类页，否则全文搜索仍会把已经迁移的旧正文作为当前依据。
    for category in ("接口", "事件", "枚举值"):
        for path in (repo_root / "docs" / category).rglob("*.md"):
            if path not in files:
                files[path] = None
    # 导航直接从完整快照生成，不手工维护另一份版本列表。
    children = []
    for category in ("接口", "事件", "枚举值", "更新信息"):
        paths = sorted(path for path in current.pages if path.startswith(category + "/"))
        if category == "更新信息":
            paths = sorted(set(paths) | {"更新信息/" + p.stem for p in (repo_root / "docs/更新信息").glob("*.md") if re.fullmatch(r"\d+\.\d+", p.stem)})
        links = []
        for path in paths:
            channel = profile["docs_base_url"].rsplit("/", 1)[-1]
            if category == "更新信息" and path != "更新信息/" + version:
                channel = BASE_URL.rsplit("/", 1)[-1]
            links.append("/mcdocs/" + channel + "/" + path)
        children.append({"title": category, "children": links})
    files[repo_root / "docs/config.json"] = _json_text({"children": children})
    retrieved = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    source_manifest: Dict[str, Any] = {"schema_version": "1.0", "retrieved_at": retrieved, "current": _snapshot_sources(current)}
    if previous:
        source_manifest["baseline"] = _snapshot_sources(previous)
        source_manifest["baseline"]["frozen_snapshot_path"] = baseline_path.relative_to(repo_root).as_posix()
    if include_python_whitelist:
        html, headers = fetcher(PYTHON_WHITELIST_URL)
        entries = parse_python_whitelist_entries(html)
        modules = [entry["normalized_name"] for entry in entries]
        if not modules or len(set(modules)) != len(modules):
            raise ValueError("白名单为空或存在重复模块，拒绝覆盖")
        whitelist = build_python_whitelist_snapshot(html, headers, entries)
        files[repo_root / "standard/registry/snapshots/python-module-whitelist.json"] = _json_text(whitelist)
        files[repo_root / "docs" / (PYTHON_WHITELIST_DOC_PATH + ".md")] = render_python_whitelist(modules, _header_value(headers, "Last-Modified"))
        source_manifest["python_module_whitelist"] = {key: whitelist[key] for key in ("source_url", "source_sha256", "modules_sha256", "module_count", "last_modified")}
    if comparison:
        comparison["retrieved_at"] = retrieved
        files[repo_root / "standard/registry/snapshots" / ("modsdk-{}-to-{}.json".format(compare_version, version))] = _json_text(comparison)
        files[repo_root / "docs/更新信息" / (version + "-迁移说明.md")] = render_comparison_report(repo_root, previous, current, comparison)
    source_manifest["output_files"] = [{"path": path.relative_to(repo_root).as_posix(), "sha256": _sha256(content)} for path, content in sorted(files.items()) if content is not None]
    files[repo_root / "standard/registry/snapshots/official-docs.json"] = _json_text(source_manifest)
    # 只做落盘数据完整性检查，不运行产物功能或模拟游戏环境。
    for path, content in files.items():
        if content is not None and path.suffix == ".json":
            json.loads(content)
    return SyncPlan(version, files, sorted(current.pages), current.api_entries, current.event_entries, comparison)


def _read_text_preserving_newlines(path: Path) -> str:
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def _write_temp_file(target: Path, content: str) -> Path:
    descriptor, temp_name = tempfile.mkstemp(prefix=".modsdk-sync-", suffix=".tmp", dir=str(target.parent))
    temp_path = Path(temp_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    except Exception:
        if temp_path.exists():
            temp_path.unlink()
        raise
    return temp_path


def write_files_atomically(repo_root: Path, files: Mapping[Path, Optional[str]]) -> None:
    """以事务方式替换文本文件，任一替换失败时恢复此前目标。"""
    repo_root = Path(repo_root).resolve()
    targets = sorted((Path(path).resolve(), content) for path, content in files.items())
    for target, _ in targets:
        try:
            target.relative_to(repo_root)
        except ValueError as exc:
            raise ValueError("拒绝写入仓库外路径: {}".format(target)) from exc

    created_dirs: Set[Path] = set()
    originals: Dict[Path, Tuple[bool, str]] = {}
    temp_paths: Dict[Path, Path] = {}
    replaced: List[Path] = []
    try:
        for target, content in targets:
            missing: List[Path] = []
            current = target.parent
            while not current.exists() and current != repo_root.parent:
                missing.append(current)
                current = current.parent
            target.parent.mkdir(parents=True, exist_ok=True)
            created_dirs.update(missing)
            originals[target] = (target.exists(), _read_text_preserving_newlines(target) if target.exists() else "")
            if content is not None:
                temp_paths[target] = _write_temp_file(target, content)

        for target, content in targets:
            if content is None:
                if target.exists():
                    target.unlink()
            else:
                os.replace(str(temp_paths[target]), str(target))
                del temp_paths[target]
            replaced.append(target)
    except Exception as exc:
        rollback_errors: List[str] = []
        for target in reversed(replaced):
            existed, original = originals[target]
            try:
                if existed:
                    rollback_temp = _write_temp_file(target, original)
                    os.replace(str(rollback_temp), str(target))
                elif target.exists():
                    target.unlink()
            except Exception as rollback_exc:
                rollback_errors.append("{}: {}".format(target, rollback_exc))
        for temp_path in temp_paths.values():
            try:
                if temp_path.exists():
                    temp_path.unlink()
            except OSError:
                pass
        for directory in sorted(created_dirs, key=lambda path: len(path.parts), reverse=True):
            try:
                directory.rmdir()
            except OSError:
                pass
        if rollback_errors:
            raise RuntimeError("同步失败且回滚不完整: {}".format("; ".join(rollback_errors))) from exc
        raise




def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="全量同步网易官方文档并生成版本差异")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--version", default="current")
    parser.add_argument("--compare-version")
    parser.add_argument("--cache-dir", type=Path, help="本次调查的原始响应缓存，省略则每次重新抓取")
    parser.add_argument("--workers", type=int, choices=range(1, 9), default=6)
    parser.add_argument("--delay", type=float, default=0.15)
    parser.add_argument("--dry-run", action="store_true", help="完成抓取和数据核对但不替换知识库")
    parser.add_argument("--skip-python-whitelist", action="store_true")
    parser.add_argument("--refresh-baseline", action="store_true", help="仅在官网仍提供对应旧版频道时显式重新抓取比较基线")
    args = parser.parse_args(argv)
    try:
        plan = build_sync_plan(
            args.repo_root, args.version, args.compare_version,
            not args.skip_python_whitelist, args.workers,
            CachedFetcher(args.cache_dir, max(0, args.delay)),
            refresh_baseline=args.refresh_baseline,
        )
        if not args.dry_run:
            write_files_atomically(args.repo_root, plan.files)
        print("{} ModSDK {}: {} 文档，{} API，{} 事件，{} 个文件".format(
            "已核对" if args.dry_run else "已同步", plan.version,
            len(plan.discovered_doc_paths), len(plan.api_entries), len(plan.event_entries), len(plan.files),
        ))
    except Exception as exc:
        print("官方文档同步失败: {}".format(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
