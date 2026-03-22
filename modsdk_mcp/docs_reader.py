"""
文档读取器模块
从 docs 目录读取 Markdown 文档并解析
支持模糊搜索、结构化 API/事件索引
"""

import re
import json
import bisect
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass
from difflib import SequenceMatcher


@dataclass
class DocSection:
    """文档章节"""
    title: str
    level: int
    content: str
    subsections: List["DocSection"]


@dataclass
class Document:
    """文档对象"""
    filename: str
    filepath: str
    title: str
    content: str
    sections: List[DocSection]
    metadata: Dict[str, Any]


@dataclass
class ApiEntry:
    """结构化 API 条目（来自 interface.json / events.json）"""
    name: str
    desc: str
    side: str  # 客户端 / 服务端
    category: str  # doc_class_path 分类
    params: List[Dict[str, str]]
    return_info: Dict[str, str]
    entry_type: str  # "api" 或 "event"
    class_path: str  # 完整类路径


class DocsReader:
    """文档读取器"""
    
    def __init__(self, docs_path: str = "docs"):
        """
        初始化文档读取器
        
        Args:
            docs_path: docs 目录路径，相对于项目根目录或绝对路径
        """
        self.docs_path = Path(docs_path)
        if not self.docs_path.is_absolute():
            # 如果是相对路径，基于当前文件位置计算
            self.docs_path = Path(__file__).parent.parent / docs_path
        
        self._documents: Dict[str, Document] = {}
        self._index: Dict[str, List[str]] = {}  # 关键词 -> 文档路径列表
        self._sorted_keywords: List[str] = []  # 排序后的关键词列表，用于前缀二分查找
        
        # 结构化 API/事件索引
        self._api_entries: Dict[str, ApiEntry] = {}  # unique_key -> ApiEntry
        self._api_name_lower_map: Dict[str, List[str]] = {}  # name.lower() -> [unique_keys]
        self._api_keywords: Dict[str, List[str]] = {}  # keyword.lower() -> [unique_keys]
        self._sorted_api_keywords: List[str] = []  # 排序后的 API 关键词列表
        
    def load_all_docs(self) -> None:
        """加载所有文档"""
        if not self.docs_path.exists():
            return
            
        for md_file in self.docs_path.rglob("*.md"):
            self._load_document(md_file)
        
        self._build_index()
        self._load_structured_data()
    
    def _load_document(self, filepath: Path) -> Optional[Document]:
        """加载单个文档"""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 解析元数据（YAML front matter）
            metadata = {}
            if content.startswith("---"):
                end_idx = content.find("---", 3)
                if end_idx != -1:
                    yaml_content = content[3:end_idx].strip()
                    for line in yaml_content.split("\n"):
                        if ":" in line:
                            key, value = line.split(":", 1)
                            metadata[key.strip()] = value.strip()
                    content = content[end_idx + 3:].strip()
            
            # 解析标题
            title = self._extract_title(content) or filepath.stem
            
            # 解析章节
            sections = self._parse_sections(content)
            
            # 计算相对路径
            rel_path = str(filepath.relative_to(self.docs_path))
            
            doc = Document(
                filename=filepath.name,
                filepath=rel_path,
                title=title,
                content=content,
                sections=sections,
                metadata=metadata
            )
            
            self._documents[rel_path] = doc
            return doc
            
        except Exception as e:
            print(f"加载文档失败 {filepath}: {e}")
            return None
    
    def _extract_title(self, content: str) -> Optional[str]:
        """从内容中提取标题"""
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return None
    
    def _parse_sections(self, content: str) -> List[DocSection]:
        """解析文档章节"""
        sections = []
        lines = content.split("\n")
        
        current_section = None
        current_content = []
        
        for line in lines:
            header_match = re.match(r"^(#{1,6})\s+(.+)$", line)
            if header_match:
                # 保存之前的章节
                if current_section:
                    current_section.content = "\n".join(current_content).strip()
                    sections.append(current_section)
                
                level = len(header_match.group(1))
                title = header_match.group(2).strip()
                current_section = DocSection(
                    title=title,
                    level=level,
                    content="",
                    subsections=[]
                )
                current_content = []
            else:
                current_content.append(line)
        
        # 保存最后一个章节
        if current_section:
            current_section.content = "\n".join(current_content).strip()
            sections.append(current_section)
        
        return sections
    
    def _build_index(self) -> None:
        """构建关键词索引"""
        self._index.clear()
        
        for doc_path, doc in self._documents.items():
            # 索引标题
            self._add_to_index(doc.title.lower(), doc_path)
            
            # 索引章节标题
            for section in doc.sections:
                self._add_to_index(section.title.lower(), doc_path)
            
            # 索引内容关键词
            words = re.findall(r"\b\w+\b", doc.content.lower())
            for word in set(words):
                if len(word) > 2:  # 忽略太短的词
                    self._add_to_index(word, doc_path)
        
        # 构建排序后的关键词列表，用于前缀二分查找
        self._sorted_keywords = sorted(self._index.keys())
    
    def _add_to_index(self, keyword: str, doc_path: str) -> None:
        """添加关键词到索引"""
        if keyword not in self._index:
            self._index[keyword] = []
        if doc_path not in self._index[keyword]:
            self._index[keyword].append(doc_path)
    
    def _load_structured_data(self) -> None:
        """加载 JSON 结构化数据（events.json, interface.json）构建精确索引"""
        self._api_entries.clear()
        self._api_name_lower_map.clear()
        self._api_keywords.clear()
        self._sorted_api_keywords.clear()
        
        # 加载 interface.json
        interface_path = self.docs_path / "interface.json"
        if interface_path.exists():
            try:
                with open(interface_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for class_path, methods in data.items():
                    for method in methods:
                        entry = ApiEntry(
                            name=method["name"],
                            desc=method.get("desc", ""),
                            side=method.get("side", ""),
                            category="/".join(method.get("doc_class_path", [])),
                            params=method.get("param", []),
                            return_info=method.get("return", {}),
                            entry_type="api",
                            class_path=class_path,
                        )
                        # 用 class_path::name 作为唯一 key，避免同名覆盖
                        unique_key = f"{class_path}::{entry.name}"
                        self._api_entries[unique_key] = entry
                        self._api_name_lower_map.setdefault(entry.name.lower(), []).append(unique_key)
                        # 建立关键词索引：API名拆词、中文描述
                        self._index_api_entry(entry, unique_key)
            except Exception as e:
                print(f"加载 interface.json 失败: {e}")
        
        # 加载 events.json
        events_path = self.docs_path / "events.json"
        if events_path.exists():
            try:
                with open(events_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for event_path, events in data.items():
                    for event in events:
                        entry = ApiEntry(
                            name=event["name"],
                            desc=event.get("desc", ""),
                            side=event.get("side", ""),
                            category="/".join(event.get("doc_class_path", [])),
                            params=event.get("param", []),
                            return_info=event.get("return", {}),
                            entry_type="event",
                            class_path=event_path,
                        )
                        unique_key = f"{event_path}::{entry.name}"
                        self._api_entries[unique_key] = entry
                        self._api_name_lower_map.setdefault(entry.name.lower(), []).append(unique_key)
                        self._index_api_entry(entry, unique_key)
            except Exception as e:
                print(f"加载 events.json 失败: {e}")
        
        # 构建排序后的 API 关键词列表，用于前缀二分查找
        self._sorted_api_keywords = sorted(self._api_keywords.keys())
    
    def _index_api_entry(self, entry: ApiEntry, unique_key: str) -> None:
        """为 API/事件条目建立关键词索引"""
        # 1. 完整名称
        self._add_api_keyword(entry.name.lower(), unique_key)
        
        # 2. 驼峰拆词: GetPlayerPos -> get, player, pos
        camel_parts = re.findall(r'[A-Z][a-z]+|[a-z]+|[A-Z]+(?![a-z])', entry.name)
        for part in camel_parts:
            self._add_api_keyword(part.lower(), unique_key)
        
        # 3. 中文描述关键词
        chinese_phrases = re.findall(r'[\u4e00-\u9fff]+', entry.desc)
        for phrase in chinese_phrases:
            self._add_api_keyword(phrase, unique_key)
        
        # 4. 分类关键词
        if entry.category:
            for cat in entry.category.split("/"):
                if cat:
                    self._add_api_keyword(cat.lower(), unique_key)
        
        # 5. 端侧关键词
        if entry.side:
            self._add_api_keyword(entry.side, unique_key)
    
    def _add_api_keyword(self, keyword: str, unique_key: str) -> None:
        """添加 API 关键词映射"""
        if keyword not in self._api_keywords:
            self._api_keywords[keyword] = []
        if unique_key not in self._api_keywords[keyword]:
            self._api_keywords[keyword].append(unique_key)
    
    # ========================================================================
    # 结构化 API/事件搜索
    # ========================================================================
    
    def search_api(self, query: str, limit: int = 10, entry_type: str = "all") -> List[Dict[str, Any]]:
        """
        精确搜索 API/事件（利用结构化 JSON 数据）
        
        Args:
            query: 搜索关键词（API名、中文描述等）
            limit: 返回结果数量限制
            entry_type: "api" / "event" / "all"
            
        Returns:
            匹配的 API/事件列表，按相关度排序
        """
        query_lower = query.lower()
        scores: Dict[str, float] = {}  # unique_key -> score
        
        # 1. 精确名称匹配（最高优先级）
        if query_lower in self._api_name_lower_map:
            for uk in self._api_name_lower_map[query_lower]:
                scores[uk] = 100.0
        
        # 2. 名称前缀/子串匹配
        for name_lower, unique_keys in self._api_name_lower_map.items():
            if query_lower in name_lower:
                for uk in unique_keys:
                    scores.setdefault(uk, 0)
                    scores[uk] = max(scores[uk], 20.0)
            elif name_lower in query_lower:
                for uk in unique_keys:
                    scores.setdefault(uk, 0)
                    scores[uk] = max(scores[uk], 15.0)
        
        # 3. 关键词索引匹配（使用二分查找优化前缀匹配）
        query_tokens = self._tokenize(query)
        for token in query_tokens:
            token_lower = token.lower()
            # 精确关键词匹配
            if token_lower in self._api_keywords:
                for uk in self._api_keywords[token_lower]:
                    scores.setdefault(uk, 0)
                    scores[uk] += 5.0
            # 前缀匹配（仅对长度>=3的token，使用二分查找）
            if len(token_lower) >= 3:
                candidates = self._find_api_prefix_candidates(token_lower)
                for kw in candidates:
                    if kw == token_lower:
                        continue  # 已在精确匹配中处理
                    for uk in self._api_keywords.get(kw, []):
                        scores.setdefault(uk, 0)
                        scores[uk] += 2.0
        
        # 4. 描述子串匹配
        for unique_key, entry in self._api_entries.items():
            if query_lower in entry.desc.lower():
                scores.setdefault(unique_key, 0)
                scores[unique_key] += 8.0
        
        # 过滤类型
        if entry_type != "all":
            scores = {
                uk: score for uk, score in scores.items()
                if self._api_entries[uk].entry_type == entry_type
            }
        
        # 排序并返回
        sorted_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit]
        
        results = []
        for unique_key, score in sorted_results:
            entry = self._api_entries[unique_key]
            results.append({
                "name": entry.name,
                "type": entry.entry_type,
                "side": entry.side,
                "category": entry.category,
                "desc": entry.desc,
                "params": entry.params,
                "return": entry.return_info,
                "class_path": entry.class_path,
                "score": round(score, 2),
            })
        
        return results
    
    def _find_api_prefix_candidates(self, token: str, max_candidates: int = 50) -> List[str]:
        """
        从排序后的 API 关键词列表中，用前缀二分查找快速筛选候选。
        """
        token_lower = token.lower()
        if len(token_lower) < 2:
            return []
        
        prefix = token_lower[:2]
        prefix_end = prefix[:-1] + chr(ord(prefix[-1]) + 1)
        
        start = bisect.bisect_left(self._sorted_api_keywords, prefix)
        end = bisect.bisect_left(self._sorted_api_keywords, prefix_end)
        
        candidates = self._sorted_api_keywords[start:end]
        
        if len(candidates) > max_candidates and len(token_lower) >= 3:
            prefix3 = token_lower[:3]
            prefix3_end = prefix3[:-1] + chr(ord(prefix3[-1]) + 1)
            start = bisect.bisect_left(self._sorted_api_keywords, prefix3)
            end = bisect.bisect_left(self._sorted_api_keywords, prefix3_end)
            candidates = self._sorted_api_keywords[start:end]
        
        return candidates[:max_candidates]
    
    # ========================================================================
    # 模糊搜索辅助方法
    # ========================================================================
    
    def _similarity(self, s1: str, s2: str) -> float:
        """计算两个字符串的相似度（0-1）"""
        return SequenceMatcher(None, s1.lower(), s2.lower()).ratio()
    
    def _edit_distance(self, s1: str, s2: str) -> int:
        """计算编辑距离（Levenshtein Distance）"""
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    def _fuzzy_match(self, query: str, target: str, threshold: float = 0.6) -> Tuple[bool, float]:
        """
        模糊匹配
        
        Returns:
            (是否匹配, 匹配分数)
        """
        query = query.lower()
        target = target.lower()
        
        # 精确包含
        if query in target:
            return True, 1.0
        
        # 目标包含在查询中
        if target in query:
            return True, 0.9
        
        # 长度差异过大时跳过（早退出优化）
        len_ratio = min(len(query), len(target)) / max(len(query), len(target), 1)
        if len_ratio < 0.3:
            return False, 0.0
        
        # 相似度匹配
        similarity = self._similarity(query, target)
        if similarity >= threshold:
            return True, similarity
        
        # 编辑距离匹配（仅对英文、长度>=3 的 token 使用）
        if len(query) >= 3 and query.isascii():
            max_distance = max(1, len(query) // 3)  # 允许 1/3 的错误
            distance = self._edit_distance(query, target)
            if distance <= max_distance:
                score = 1.0 - (distance / max(len(query), len(target)))
                return True, score
        
        return False, 0.0
    
    def _find_prefix_candidates(self, token: str, max_candidates: int = 50) -> List[str]:
        """
        从排序后的关键词列表中，用前缀匹配快速筛选候选关键词。
        利用二分查找 O(log N) 定位前缀起始位置。
        """
        token_lower = token.lower()
        if len(token_lower) < 2:
            return []
        
        # 取前2个字符作为前缀进行范围搜索
        prefix = token_lower[:2]
        # 计算前缀的上界
        prefix_end = prefix[:-1] + chr(ord(prefix[-1]) + 1)
        
        start = bisect.bisect_left(self._sorted_keywords, prefix)
        end = bisect.bisect_left(self._sorted_keywords, prefix_end)
        
        candidates = self._sorted_keywords[start:end]
        
        # 如果候选太多，进一步用更长前缀过滤
        if len(candidates) > max_candidates and len(token_lower) >= 3:
            prefix3 = token_lower[:3]
            prefix3_end = prefix3[:-1] + chr(ord(prefix3[-1]) + 1)
            start = bisect.bisect_left(self._sorted_keywords, prefix3)
            end = bisect.bisect_left(self._sorted_keywords, prefix3_end)
            candidates = self._sorted_keywords[start:end]
        
        return candidates[:max_candidates]
    
    def _tokenize(self, text: str) -> List[str]:
        """
        分词：支持中文和英文。
        
        优化：不再将中文词拆成单字，避免 "玩家事件" -> ["玩","家","事","件"] 产生大量噪音匹配。
        保留完整中文词组，仅对长度>=4 的中文词额外做 2-gram 拆分。
        """
        tokens = []
        
        # 提取英文单词和数字
        english_tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', text)
        tokens.extend(english_tokens)
        
        # 提取中文词组（保持完整，不拆单字）
        chinese_phrases = re.findall(r'[\u4e00-\u9fff]+', text)
        for phrase in chinese_phrases:
            tokens.append(phrase)
            # 对长度>=4 的中文词做 2-gram 拆分，提供适度的子串匹配能力
            if len(phrase) >= 4:
                for i in range(len(phrase) - 1):
                    tokens.append(phrase[i:i+2])
        
        # 提取驼峰命名的子词
        for token in english_tokens:
            # GetEngineCompFactory -> Get, Engine, Comp, Factory
            camel_parts = re.findall(r'[A-Z][a-z]+|[a-z]+|[A-Z]+(?![a-z])', token)
            if len(camel_parts) > 1:
                tokens.extend([p.lower() for p in camel_parts])
        
        return list(set(tokens))
    
    def get_document(self, filepath: str) -> Optional[Document]:
        """获取指定文档"""
        return self._documents.get(filepath)
    
    def get_all_documents(self) -> List[Document]:
        """获取所有文档"""
        return list(self._documents.values())
    
    def list_documents(self) -> List[Dict[str, str]]:
        """列出所有文档的基本信息"""
        return [
            {
                "filepath": doc.filepath,
                "filename": doc.filename,
                "title": doc.title
            }
            for doc in self._documents.values()
        ]
    
    def search(self, query: str, limit: int = 10, fuzzy: bool = True) -> List[Dict[str, Any]]:
        """
        搜索文档（支持模糊搜索）
        
        Args:
            query: 搜索关键词
            limit: 返回结果数量限制
            fuzzy: 是否启用模糊搜索（默认启用）
            
        Returns:
            匹配的文档列表
        """
        if fuzzy:
            return self.fuzzy_search(query, limit)
        else:
            return self._exact_search(query, limit)
    
    def _exact_search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """精确搜索（原始搜索逻辑）"""
        query = query.lower()
        query_words = query.split()
        
        scores: Dict[str, float] = {}
        
        for word in query_words:
            if word in self._index:
                for doc_path in self._index[word]:
                    scores[doc_path] = scores.get(doc_path, 0) + 2
            
            for keyword in self._index:
                if keyword.startswith(word) or word in keyword:
                    for doc_path in self._index[keyword]:
                        scores[doc_path] = scores.get(doc_path, 0) + 1
        
        sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit]
        
        results = []
        for doc_path, score in sorted_docs:
            doc = self._documents[doc_path]
            snippet = self._extract_snippet(doc.content, query_words)
            results.append({
                "filepath": doc.filepath,
                "title": doc.title,
                "score": score,
                "snippet": snippet,
                "match_type": "exact"
            })
        
        return results
    
    def fuzzy_search(self, query: str, limit: int = 10, threshold: float = 0.5) -> List[Dict[str, Any]]:
        """
        模糊搜索文档（优化版）
        
        优化策略：
        1. 先通过标题精确/前缀匹配产生候选集，避免全量遍历
        2. 索引关键词匹配改为：精确查找 + 前缀二分查找候选 + 少量模糊匹配
        3. 中文 token 不拆单字，减少噪音
        4. 增加长度比例早退出，跳过不可能匹配的对
        
        Args:
            query: 搜索关键词
            limit: 返回结果数量限制
            threshold: 模糊匹配阈值（0-1，越高越严格）
            
        Returns:
            匹配的文档列表，按相关度排序
        """
        query_lower = query.lower()
        query_tokens = self._tokenize(query)
        
        # 文档得分
        scores: Dict[str, float] = {}
        match_details: Dict[str, List[str]] = {}  # 记录匹配详情
        
        for doc_path, doc in self._documents.items():
            doc_score = 0.0
            matched_terms = []
            
            # 1. 标题匹配（权重最高）
            title_match, title_score = self._fuzzy_match(query_lower, doc.title.lower(), threshold)
            if title_match:
                doc_score += title_score * 10
                matched_terms.append(f"标题: {doc.title}")
            
            # 2. 章节标题匹配（限制最多记录 3 个匹配章节）
            section_matches = 0
            for section in doc.sections:
                if section_matches >= 3:
                    break
                section_match, section_score = self._fuzzy_match(query_lower, section.title.lower(), threshold)
                if section_match:
                    doc_score += section_score * 5
                    matched_terms.append(f"章节: {section.title}")
                    section_matches += 1
            
            # 3. 索引关键词匹配（优化：避免暴力遍历全部关键词）
            matched_keywords: Set[str] = set()
            for token in query_tokens:
                token_lower = token.lower()
                
                if token_lower.isascii():
                    # 3a. 英文 token：精确匹配索引
                    if token_lower in self._index:
                        if doc_path in self._index[token_lower]:
                            doc_score += 2.0
                            matched_keywords.add(token_lower)
                    
                    # 3b. 英文 token：前缀候选匹配（用二分查找代替全量遍历）
                    if len(token_lower) >= 3:
                        candidates = self._find_prefix_candidates(token_lower)
                        for keyword in candidates:
                            if keyword == token_lower:
                                continue  # 已在 3a 处理
                            if doc_path in self._index.get(keyword, []):
                                kw_match, kw_score = self._fuzzy_match(token_lower, keyword, threshold)
                                if kw_match:
                                    doc_score += kw_score * 1.5
                                    matched_keywords.add(keyword)
                else:
                    # 3c. 中文 token：精确索引匹配 + 子串匹配（不做模糊匹配）
                    if len(token_lower) >= 2:
                        if token_lower in self._index and doc_path in self._index[token_lower]:
                            doc_score += 2.0
                            matched_keywords.add(token_lower)
                        # 检查 token 作为子串出现在哪些关键词中（限制搜索范围）
                        for keyword in self._index:
                            if not keyword.isascii() and token_lower in keyword and keyword != token_lower:
                                if doc_path in self._index[keyword]:
                                    doc_score += 1.0
                                    matched_keywords.add(keyword)
                                    break  # 每个 token 最多额外匹配 1 个
            
            if matched_keywords:
                matched_terms.extend([f"关键词: {kw}" for kw in list(matched_keywords)[:2]])
            
            # 4. 内容全文精确子串匹配（去掉模糊，只做精确子串）
            content_lower = doc.content.lower()
            for token in query_tokens:
                tl = token.lower()
                if len(tl) >= 2 and tl in content_lower:
                    doc_score += 1.5
                    count = content_lower.count(tl)
                    doc_score += min(count * 0.1, 1.0)
            
            # 5. 驼峰命名特殊处理
            camel_matches = self._match_camel_case(query, doc.content)
            if camel_matches:
                doc_score += len(camel_matches) * 3
                matched_terms.extend([f"API: {m}" for m in camel_matches[:2]])
            
            if doc_score > 0:
                scores[doc_path] = doc_score
                match_details[doc_path] = matched_terms
        
        # 按分数排序
        sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit]
        
        results = []
        for doc_path, score in sorted_docs:
            doc = self._documents[doc_path]
            snippet = self._extract_fuzzy_snippet(doc.content, query_tokens, context_length=120)
            results.append({
                "filepath": doc.filepath,
                "title": doc.title,
                "score": round(score, 2),
                "snippet": snippet,
                "match_type": "fuzzy",
                "matched_terms": match_details.get(doc_path, [])[:3]  # 最多显示 3 个匹配项
            })
        
        return results
    
    def _match_camel_case(self, query: str, content: str) -> List[str]:
        """
        匹配驼峰命名的 API 名称（优化版）
        限制最多返回 3 个匹配，避免大文档中产生过多结果
        """
        matches = []
        query_parts = query.lower().split()
        
        # 查找所有驼峰命名（去重后限制数量）
        camel_pattern = r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b'
        camel_names = set(re.findall(camel_pattern, content))
        
        for name in camel_names:
            if len(matches) >= 3:
                break
            
            # 拆分驼峰命名
            parts = re.findall(r'[A-Z][a-z]+', name)
            parts_lower = [p.lower() for p in parts]
            
            # 检查查询词是否匹配任何部分
            match_count = 0
            for qp in query_parts:
                for pl in parts_lower:
                    if qp in pl or pl in qp:
                        match_count += 1
                        break
                    # 仅对长度>=3 的英文词做模糊匹配
                    if len(qp) >= 3 and qp.isascii():
                        matched, _ = self._fuzzy_match(qp, pl, 0.7)
                        if matched:
                            match_count += 1
                            break
            
            if match_count >= len(query_parts) * 0.5:  # 至少匹配一半的查询词
                matches.append(name)
        
        return matches
    
    def _extract_fuzzy_snippet(self, content: str, tokens: List[str], context_length: int = 120) -> str:
        """提取模糊匹配的文本片段（精简版，默认 120 字符）"""
        content_lower = content.lower()
        best_pos = -1
        best_score = 0
        
        # 用更大步长扫描，减少计算量
        step = 80
        window = 120
        for i in range(0, max(1, len(content) - step), step):
            w = content_lower[i:i + window]
            score = sum(1 for t in tokens if len(t) >= 2 and t.lower() in w)
            if score > best_score:
                best_score = score
                best_pos = i
        
        if best_pos >= 0:
            start = max(0, best_pos - 30)
            end = min(len(content), best_pos + context_length)
            snippet = content[start:end]
            snippet = re.sub(r'\s+', ' ', snippet).strip()
            if start > 0:
                snippet = "..." + snippet
            if end < len(content):
                snippet = snippet + "..."
            return snippet
        
        return content[:context_length].strip() + "..." if len(content) > context_length else content
    
    def _extract_snippet(self, content: str, keywords: List[str], context_length: int = 150) -> str:
        """提取包含关键词的文本片段"""
        content_lower = content.lower()
        
        for keyword in keywords:
            idx = content_lower.find(keyword)
            if idx != -1:
                start = max(0, idx - context_length // 2)
                end = min(len(content), idx + len(keyword) + context_length // 2)
                snippet = content[start:end]
                if start > 0:
                    snippet = "..." + snippet
                if end < len(content):
                    snippet = snippet + "..."
                return snippet
        
        # 如果没找到关键词，返回开头部分
        return content[:context_length] + "..." if len(content) > context_length else content
    
    def search_in_section(self, query: str, section_title: str) -> List[Dict[str, Any]]:
        """在指定章节标题中搜索"""
        results = []
        query_lower = query.lower()
        section_lower = section_title.lower()
        
        for doc in self._documents.values():
            for section in doc.sections:
                if section_lower in section.title.lower():
                    if query_lower in section.content.lower():
                        results.append({
                            "filepath": doc.filepath,
                            "title": doc.title,
                            "section": section.title,
                            "content": section.content
                        })
        
        return results
    
    def get_section_content(self, filepath: str, section_title: str) -> Optional[str]:
        """获取指定文档的指定章节内容"""
        doc = self._documents.get(filepath)
        if not doc:
            return None
        
        section_lower = section_title.lower()
        for section in doc.sections:
            if section_lower in section.title.lower():
                return section.content
        
        return None
    
    def get_document_structure(self, filepath: str) -> Optional[List[Dict[str, Any]]]:
        """获取文档结构（章节目录）"""
        doc = self._documents.get(filepath)
        if not doc:
            return None
        
        return [
            {
                "title": section.title,
                "level": section.level
            }
            for section in doc.sections
        ]
    
    def reload(self) -> None:
        """重新加载所有文档"""
        self._documents.clear()
        self._index.clear()
        self._sorted_keywords.clear()
        self._api_entries.clear()
        self._api_name_lower_map.clear()
        self._api_keywords.clear()
        self._sorted_api_keywords.clear()
        self.load_all_docs()


# 全局文档读取器实例
_docs_reader: Optional[DocsReader] = None


def get_docs_reader(docs_path: str = "docs") -> DocsReader:
    """获取文档读取器实例（单例模式）"""
    global _docs_reader
    if _docs_reader is None:
        _docs_reader = DocsReader(docs_path)
        _docs_reader.load_all_docs()
    return _docs_reader


def reload_docs() -> None:
    """重新加载文档"""
    global _docs_reader
    if _docs_reader:
        _docs_reader.reload()
