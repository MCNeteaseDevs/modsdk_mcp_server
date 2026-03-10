"""
文档读取器模块
从 docs 目录读取 Markdown 文档并解析
支持模糊搜索、拼音搜索
"""

import os
import re
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
        self._index: Dict[str, List[str]] = {}  # 关键词索引
        
    def load_all_docs(self) -> None:
        """加载所有文档"""
        if not self.docs_path.exists():
            return
            
        for md_file in self.docs_path.rglob("*.md"):
            self._load_document(md_file)
        
        self._build_index()
    
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
    
    def _add_to_index(self, keyword: str, doc_path: str) -> None:
        """添加关键词到索引"""
        if keyword not in self._index:
            self._index[keyword] = []
        if doc_path not in self._index[keyword]:
            self._index[keyword].append(doc_path)
    
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
        
        # 相似度匹配
        similarity = self._similarity(query, target)
        if similarity >= threshold:
            return True, similarity
        
        # 编辑距离匹配（允许少量拼写错误）
        max_distance = max(1, len(query) // 3)  # 允许 1/3 的错误
        distance = self._edit_distance(query, target)
        if distance <= max_distance:
            # 转换为分数
            score = 1.0 - (distance / max(len(query), len(target)))
            return True, score
        
        return False, 0.0
    
    def _tokenize(self, text: str) -> List[str]:
        """
        分词：支持中文和英文
        """
        tokens = []
        
        # 提取英文单词和数字
        english_tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', text)
        tokens.extend(english_tokens)
        
        # 提取中文词（按字符，因为没有分词库）
        chinese_chars = re.findall(r'[\u4e00-\u9fff]+', text)
        for chars in chinese_chars:
            tokens.append(chars)
            # 也添加单个字
            if len(chars) > 1:
                tokens.extend(list(chars))
        
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
        模糊搜索文档
        
        支持：
        - 拼写容错（typo tolerance）
        - 部分匹配（partial matching）
        - 驼峰命名分词（camelCase tokenization）
        - 中文字符匹配
        
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
            
            # 2. 章节标题匹配
            for section in doc.sections:
                section_match, section_score = self._fuzzy_match(query_lower, section.title.lower(), threshold)
                if section_match:
                    doc_score += section_score * 5
                    matched_terms.append(f"章节: {section.title}")
            
            # 3. 索引关键词模糊匹配
            for keyword in self._index:
                if doc_path in self._index[keyword]:
                    for token in query_tokens:
                        kw_match, kw_score = self._fuzzy_match(token.lower(), keyword, threshold)
                        if kw_match:
                            doc_score += kw_score * 2
                            if keyword not in matched_terms:
                                matched_terms.append(f"关键词: {keyword}")
            
            # 4. 内容全文模糊匹配
            content_lower = doc.content.lower()
            for token in query_tokens:
                if token.lower() in content_lower:
                    doc_score += 1.5
                    # 计算出现次数加权
                    count = content_lower.count(token.lower())
                    doc_score += min(count * 0.1, 1.0)  # 最多额外加 1 分
            
            # 5. 驼峰命名特殊处理（如 GetEngineCompFactory）
            camel_matches = self._match_camel_case(query, doc.content)
            if camel_matches:
                doc_score += len(camel_matches) * 3
                matched_terms.extend([f"API: {m}" for m in camel_matches[:3]])
            
            if doc_score > 0:
                scores[doc_path] = doc_score
                match_details[doc_path] = matched_terms
        
        # 按分数排序
        sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit]
        
        results = []
        for doc_path, score in sorted_docs:
            doc = self._documents[doc_path]
            snippet = self._extract_fuzzy_snippet(doc.content, query_tokens)
            results.append({
                "filepath": doc.filepath,
                "title": doc.title,
                "score": round(score, 2),
                "snippet": snippet,
                "match_type": "fuzzy",
                "matched_terms": match_details.get(doc_path, [])[:5]  # 最多显示 5 个匹配项
            })
        
        return results
    
    def _match_camel_case(self, query: str, content: str) -> List[str]:
        """
        匹配驼峰命名的 API 名称
        例如：搜索 "comp factory" 可以匹配 "GetEngineCompFactory"
        """
        matches = []
        query_parts = query.lower().split()
        
        # 查找所有驼峰命名
        camel_pattern = r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b'
        camel_names = re.findall(camel_pattern, content)
        
        for name in set(camel_names):
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
                    # 模糊匹配
                    matched, _ = self._fuzzy_match(qp, pl, 0.7)
                    if matched:
                        match_count += 1
                        break
            
            if match_count >= len(query_parts) * 0.5:  # 至少匹配一半的查询词
                matches.append(name)
        
        return matches
    
    def _extract_fuzzy_snippet(self, content: str, tokens: List[str], context_length: int = 200) -> str:
        """提取模糊匹配的文本片段"""
        content_lower = content.lower()
        best_pos = -1
        best_score = 0
        
        # 找到匹配度最高的位置
        for i in range(0, len(content) - 50, 50):
            window = content_lower[i:i + 100]
            score = sum(1 for t in tokens if t.lower() in window)
            if score > best_score:
                best_score = score
                best_pos = i
        
        if best_pos >= 0:
            start = max(0, best_pos - 50)
            end = min(len(content), best_pos + context_length)
            snippet = content[start:end]
            
            # 清理片段
            snippet = re.sub(r'\s+', ' ', snippet).strip()
            
            if start > 0:
                snippet = "..." + snippet
            if end < len(content):
                snippet = snippet + "..."
            
            return snippet
        
        # 默认返回开头
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
