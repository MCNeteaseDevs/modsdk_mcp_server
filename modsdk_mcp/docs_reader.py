"""
文档读取器模块
从 docs 目录读取 Markdown 文档并解析
支持模糊搜索、结构化 API/事件索引
"""

import os
import re
import json
import math
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


# ============================================================================
# Minecraft ModSDK 领域双语术语词典（零依赖，用于查询扩展和索引语义对齐）
# 解决 vocabulary mismatch：用户中文搜索词 ≠ API英文名/描述措辞
# ============================================================================

# 英文驼峰词 → 中文关键词映射（索引端：将API英文名映射到中文搜索空间）
EN_TO_CN_MAP: Dict[str, List[str]] = {
    "add": ["加入", "添加"], "del": ["删除", "离开", "移除"],
    "remove": ["移除", "删除"], "join": ["加入", "登录"],
    "leave": ["离开", "退出"], "place": ["放置"],
    "destroy": ["破坏", "摧毁", "挖掘", "销毁"], "break": ["破坏", "打破"],
    "move": ["移动"], "interact": ["交互", "互动"],
    "use": ["使用"], "hit": ["命中", "碰撞", "击中"],
    "hurt": ["受伤", "伤害"], "die": ["死亡"],
    "spawn": ["生成", "刷出", "掉落"], "projectile": ["投射物", "抛射物", "弹射物"],
    "block": ["方块"], "player": ["玩家"],
    "entity": ["实体", "生物"], "item": ["物品"],
    "attack": ["攻击"], "damage": ["伤害"],
    "click": ["点击"], "touch": ["触摸", "触碰"],
    "key": ["按键"], "press": ["按下"],
    "drop": ["掉落", "丢弃"], "pick": ["拾取", "捡起"],
    "craft": ["合成", "制作"], "equip": ["装备"],
    "ride": ["骑乘"], "riding": ["骑乘"], "jump": ["跳跃"],
    "sneak": ["潜行"], "chat": ["聊天", "消息"],
    "command": ["命令", "指令"], "dimension": ["维度"],
    "teleport": ["传送"], "respawn": ["重生", "复活"],
    "inventory": ["背包", "物品栏", "库存"],
    "armor": ["盔甲", "护甲"], "weapon": ["武器"],
    "food": ["食物"], "potion": ["药水"],
    "effect": ["效果", "特效"], "particle": ["粒子"],
    "play": ["播放"], "create": ["创建", "生成"],
    "open": ["打开"], "close": ["关闭"],
    "tick": ["帧"], "timer": ["定时器"],
    "ui": ["界面"], "screen": ["屏幕"],
    "button": ["按钮"], "label": ["标签", "文本"],
    "image": ["图片"], "sprite": ["贴图"], "text": ["文本", "文字"],
    "model": ["模型"], "animation": ["动画"], "render": ["渲染"],
    "sound": ["声音", "音效"], "biome": ["群系"],
    "chunk": ["区块"], "world": ["世界"],
    "health": ["生命", "血量"], "hunger": ["饥饿"],
    "experience": ["经验"], "enchant": ["附魔"],
    "trade": ["交易"], "mob": ["生物", "怪物"],
    "name": ["名称", "名字"], "fire": ["火焰", "着火"],
    "explosion": ["爆炸"], "weather": ["天气"],
    "light": ["光照"], "redstone": ["红石"],
    "chest": ["箱子"], "furnace": ["熔炉"],
    "beacon": ["信标"], "try": ["尝试"],
    "stop": ["停止"], "cancel": ["取消"],
    "change": ["改变", "变化"], "update": ["更新"],
    # "set"/"get" 故意不映射：IDF极低(映射到数百API)，噪音远超收益
    "liquid": ["液体", "流体"], "fall": ["坠落", "掉落"],
    "swim": ["游泳"], "fly": ["飞行"],
    "pos": ["位置"], "position": ["位置", "坐标"],
    "attr": ["属性"], "attribute": ["属性"],
    "square": ["范围", "区域"], "area": ["范围", "区域"],
    "skin": ["皮肤"], "distance": ["距离"],
    "start": ["开始"], "register": ["注册"],
    "durability": ["耐久", "耐久度"], "carried": ["手持", "持有"],
    "loot": ["战利品", "掉落物"], "notify": ["通知"],
    "msg": ["消息"], "raining": ["下雨"], "thunder": ["打雷", "雷电"],
    "variant": ["变种"], "storage": ["存储"],
    # Round 5: 端到端测试发现的高频缺失映射
    "rot": ["朝向", "旋转", "方向"],  # GetRot ← "获取玩家朝向"
    "motion": ["速度", "运动"],  # GetMotion ← "获取实体速度"
    "inv": ["背包", "物品栏"],  # SetInvItemNum ← "移除背包物品"
    "kill": ["击杀", "杀死"],  # MobDieEvent/ActorKilledEvent ← "玩家击杀实体"
    "container": ["容器"],  # GetContainerItem ← "方块容器"
    "extra": ["额外", "自定义数据", "存储"],  # SetExtraData ← "存储玩家数据"
    "num": ["数量", "数目"],  # SetInvItemNum ← "设置数量"
    "sky": ["天空"],  # SetSkyColor — 区分"天空"vs"天气"
    "script": ["脚本"],  # OnScriptTickServer ← "脚本帧"
    "recipe": ["配方"],  # GetRecipeResult
    "loading": ["加载"],  # OnLocalPlayerStopLoading
    "level": ["等级"],  # AddLevelEvent ← "玩家等级变化"
    "exp": ["经验"],  # GetPlayerExp/AddExpEvent
    "perspect": ["视角"],  # GetPerspective — 避免被"天气"误匹配
    "dir": ["方向", "朝向"],  # GetDirFromRot
}

# 中文同义词映射（查询端：扩展中文查询到同义中文词）
CN_SYNONYM_MAP: Dict[str, List[str]] = {
    "投射物": ["抛射物", "弹射物"], "抛射物": ["投射物", "弹射物"],
    "弹射物": ["投射物", "抛射物"],
    "交互": ["互动"], "互动": ["交互"],
    "登录": ["加入", "进入"], "加入": ["登录"],
    "离开": ["退出"], "退出": ["离开"],
    "移动": ["位移"], "碰撞": ["命中", "击中"],
    "命中": ["碰撞", "击中"], "破坏": ["摧毁", "损坏"],
    "使用": ["用"], "创建": ["生成"], "生成": ["创建"],
    "受伤": ["伤害"], "伤害": ["受伤", "损伤"],
    "拾取": ["捡起"], "掉落": ["丢弃"],
    "装备": ["穿戴"], "背包": ["物品栏"], "物品栏": ["背包"],
    "界面": ["面板"], "面板": ["界面"],
    "粒子": ["特效"], "特效": ["粒子", "效果"],
    "名字": ["名称"], "名称": ["名字"],
    "怪物": ["生物"], "速度": ["移速"],
    "血量": ["生命值", "生命"], "生命值": ["血量"],
    "放置": ["摆放"], "播放": ["播"],
    "存档": ["保存", "存储"], "存储": ["存档", "保存"],
    "耐久": ["耐久度"], "耐久度": ["耐久"],
    "手持": ["持有"], "持有": ["手持"],
    "设置": ["修改"], "修改": ["设置", "改变"],
    # Round 5: 端到端测试发现的同义词缺失
    "朝向": ["方向", "旋转"], "方向": ["朝向"],
    "旋转": ["朝向", "方向"],
    "击杀": ["杀死", "死亡"], "杀死": ["击杀"],
    "容器": ["箱子"], "箱子": ["容器"],
    "定时器": ["计时器", "帧"], "计时器": ["定时器"],
    "坐标": ["位置"], "位置": ["坐标"],
    "天气": ["下雨", "打雷"], "下雨": ["天气"], "打雷": ["天气", "雷电"],
    "速度": ["运动", "移速"], "运动": ["速度"],
    "经验": ["等级"], "等级": ["经验"],
    "属性": ["属性值"], "属性值": ["属性"],
    "数据": ["存储", "信息"],
}


class DocsReader:
    """文档读取器"""

    # 网易官方教程文档的高优先级子目录（相对于 netease-modsdk-wiki/docs/）
    # 这些目录包含 JSON UI、自定义维度/方块/实体、粒子特效等关键教程
    # 开闭原则：新增子目录即可扩展，不改核心逻辑
    GUIDE_SUBDIRS = [
        "mcguide/18-界面与交互",                     # JSON UI 完整说明（2741行）
        "mcguide/20-玩法开发/15-自定义游戏内容",       # 维度/群系/方块/实体/物品教程
        "mcguide/20-玩法开发/10-基本概念",            # 基础概念
        "mcguide/16-美术/9-特效",                    # 粒子/序列帧特效 JSON 配置
        "mcguide/16-美术/6-模型和动作",               # 模型动画教程
        "mconline/10-addon教程",                     # addon 开发课程（17章）
    ]

    def __init__(self, docs_path: str = "docs", guide_root: str = ""):
        """
        初始化文档读取器

        Args:
            docs_path: docs 目录路径，相对于项目根目录或绝对路径
            guide_root: 网易官方教程文档根目录（netease-modsdk-wiki/docs/），为空则不加载教程
        """
        self.docs_path = Path(docs_path)
        if not self.docs_path.is_absolute():
            # 如果是相对路径，基于当前文件位置计算
            self.docs_path = Path(__file__).parent.parent / docs_path

        self.guide_root = Path(guide_root) if guide_root else None
        
        self._documents: Dict[str, Document] = {}
        self._index: Dict[str, List[str]] = {}  # 关键词 -> 文档路径列表
        self._sorted_keywords: List[str] = []  # 排序后的关键词列表，用于前缀二分查找
        
        # 结构化 API/事件索引
        self._api_entries: Dict[str, ApiEntry] = {}  # unique_key -> ApiEntry
        self._api_name_lower_map: Dict[str, List[str]] = {}  # name.lower() -> [unique_keys]
        self._api_keywords: Dict[str, List[str]] = {}  # keyword.lower() -> [unique_keys]
        self._sorted_api_keywords: List[str] = []  # 排序后的 API 关键词列表

        # IDF 权重数据
        self._api_keyword_doc_freq: Dict[str, int] = {}  # keyword -> 关联 API 数量
        self._total_api_entries: int = 0

        # 分类关键词集合（用于评分降权）
        self._category_keywords: Set[str] = set()

        # 枚举值数据（从 docs/枚举值/*.md 自动解析）
        self._enum_data: Dict[str, List[tuple]] = {}  # enum_name -> [(NAME, VALUE, COMMENT), ...]

    def load_all_docs(self) -> None:
        """加载所有文档（API参考 + 官方教程）"""
        if not self.docs_path.exists():
            return

        # 1. 加载 API 参考文档（接口/事件/枚举值）
        for md_file in self.docs_path.rglob("*.md"):
            self._load_document(md_file)

        # 2. 加载网易官方教程文档（mcguide/mconline 的高优先级子目录）
        if self.guide_root and self.guide_root.exists():
            guide_count = 0
            for subdir in self.GUIDE_SUBDIRS:
                guide_dir = self.guide_root / subdir
                if guide_dir.exists():
                    for md_file in guide_dir.rglob("*.md"):
                        self._load_document(md_file, source_tag="guide")
                        guide_count += 1
            if guide_count > 0:
                print("[DocsReader] 已加载 {} 篇官方教程文档".format(guide_count))

        self._build_index()
        self._load_structured_data()
        self._load_enum_data()
    
    def _load_document(self, filepath: Path, source_tag: str = "") -> Optional[Document]:
        """加载单个文档

        Args:
            filepath: 文档文件路径
            source_tag: 来源标签，如 "guide" 表示教程文档
        """
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

            if source_tag:
                metadata["source"] = source_tag

            # 解析标题
            title = self._extract_title(content) or filepath.stem

            # 解析章节
            sections = self._parse_sections(content)

            # 计算相对路径（教程文档用 guide_root，API文档用 docs_path）
            try:
                rel_path = str(filepath.relative_to(self.docs_path))
            except ValueError:
                # 教程文档不在 docs_path 下，用 guide_root 计算
                if self.guide_root:
                    try:
                        rel_path = "guide/" + str(filepath.relative_to(self.guide_root))
                    except ValueError:
                        rel_path = filepath.name
                else:
                    rel_path = filepath.name
            
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
        
        # 构建 IDF 权重数据
        self._total_api_entries = len(self._api_entries)
        self._api_keyword_doc_freq = {kw: len(uks) for kw, uks in self._api_keywords.items()}

        # 构建排序后的 API 关键词列表，用于前缀二分查找
        self._sorted_api_keywords = sorted(self._api_keywords.keys())
    
    def _index_api_entry(self, entry: ApiEntry, unique_key: str) -> None:
        """为 API/事件条目建立关键词索引"""
        # 1. 完整名称
        self._add_api_keyword(entry.name.lower(), unique_key)
        
        # 2. 驼峰拆词: GetPlayerPos -> get, player, pos
        camel_parts = re.findall(r'[A-Z][a-z]+|[a-z]+|[A-Z]+(?![a-z])', entry.name)
        for part in camel_parts:
            part_lower = part.lower()
            self._add_api_keyword(part_lower, unique_key)
            # 2b. 英文驼峰词 → 中文语义索引（跨语言检索核心）
            for cn_kw in EN_TO_CN_MAP.get(part_lower, []):
                self._add_api_keyword(cn_kw, unique_key)
                # 3+字中文关键词做2-gram分解，与查询端_tokenize对齐
                # 例：投射物→投射+射物，确保搜"投射物碰撞"能匹配
                if len(cn_kw) >= 3:
                    for i in range(len(cn_kw) - 1):
                        self._add_api_keyword(cn_kw[i:i+2], unique_key)

        # 3. 中文描述关键词（预处理：去噪 + 截断前80字避免长描述霸榜）
        desc_for_index = entry.desc
        desc_for_index = re.sub(r'^触发时机[：:]\s*', '', desc_for_index)
        desc_for_index = desc_for_index[:80]
        chinese_phrases = re.findall(r'[\u4e00-\u9fff]+', desc_for_index)
        for phrase in chinese_phrases:
            self._add_api_keyword(phrase, unique_key)
            # 2-gram 拆分：索引端与查询端对齐，确保搜 "位置" 可匹配 "获取实体位置"
            if len(phrase) >= 2:
                for i in range(len(phrase) - 1):
                    self._add_api_keyword(phrase[i:i+2], unique_key)

        # 4. 分类关键词（标记用于评分降权）
        if entry.category:
            for cat in entry.category.split("/"):
                if cat:
                    cat_lower = cat.lower()
                    self._add_api_keyword(cat_lower, unique_key)
                    self._category_keywords.add(cat_lower)

        # 5. 端侧关键词
        if entry.side:
            self._add_api_keyword(entry.side, unique_key)

        # 6. 类名关键词（补充无 doc_class_path 的 UI 控件等 190 个 API 盲区）
        if entry.class_path:
            class_name = entry.class_path.rsplit(".", 1)[-1]
            class_parts = re.findall(r'[A-Z][a-z]+|[a-z]+|[A-Z]+(?![a-z])', class_name)
            for part in class_parts:
                self._add_api_keyword(part.lower(), unique_key)
    
    def _add_api_keyword(self, keyword: str, unique_key: str) -> None:
        """添加 API 关键词映射"""
        if keyword not in self._api_keywords:
            self._api_keywords[keyword] = []
        if unique_key not in self._api_keywords[keyword]:
            self._api_keywords[keyword].append(unique_key)
    
    def _idf_weight(self, keyword: str) -> float:
        """IDF 权重：稀有词权重高，高频词权重低"""
        doc_freq = self._api_keyword_doc_freq.get(keyword, 0)
        if doc_freq == 0:
            return 1.0
        total = max(self._total_api_entries, 1)
        raw_idf = math.log(float(total) / doc_freq)
        return max(0.2, min(3.0, raw_idf))

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
        
        # 3. 关键词索引匹配（IDF 加权 + 同义词扩展 + 覆盖率追踪）
        query_tokens = self._tokenize(query)
        token_hits: Dict[str, set] = {}  # unique_key -> 匹配到的 token 集合

        # 3a. 同义词查询扩展
        expanded_tokens: List[str] = []
        original_set = set(t.lower() for t in query_tokens)
        for token in query_tokens:
            tl = token.lower()
            if not tl.isascii():
                # 中文同义词
                for syn in CN_SYNONYM_MAP.get(tl, []):
                    if syn.lower() not in original_set:
                        expanded_tokens.append(syn)
            else:
                # 英文→中文映射
                for cn in EN_TO_CN_MAP.get(tl, []):
                    if cn not in original_set:
                        expanded_tokens.append(cn)

        # 原始token正常权重，扩展token 0.6× 权重
        all_tokens = [(t, 1.0) for t in query_tokens] + [(t, 0.6) for t in expanded_tokens]

        for token, weight_factor in all_tokens:
            token_lower = token.lower()
            idf = self._idf_weight(token_lower)
            is_category = token_lower in self._category_keywords
            # 分类词激进降权（1.0 vs 5.0），且不计入覆盖率
            base_weight = 1.0 if is_category else 5.0
            # 精确关键词匹配
            if token_lower in self._api_keywords:
                for uk in self._api_keywords[token_lower]:
                    scores.setdefault(uk, 0)
                    scores[uk] += base_weight * idf * weight_factor
                    # 分类词不计入覆盖率，避免"实体"/"方块"膨胀覆盖率
                    if not is_category:
                        token_hits.setdefault(uk, set()).add(token_lower)
            # 前缀匹配：英文>=3字符，中文仅>=4字符（2-gram本身已是最小匹配单元）
            is_chinese = any('\u4e00' <= c <= '\u9fff' for c in token_lower)
            min_prefix_len = 4 if is_chinese else 3
            if len(token_lower) >= min_prefix_len:
                candidates = self._find_api_prefix_candidates(token_lower)
                for kw in candidates:
                    if kw == token_lower:
                        continue
                    for uk in self._api_keywords.get(kw, []):
                        scores.setdefault(uk, 0)
                        scores[uk] += 2.0 * self._idf_weight(kw) * weight_factor
                        if not is_category:
                            token_hits.setdefault(uk, set()).add(token_lower)

        # 3b. 覆盖率奖励：匹配越多 query token 的 API 额外加分
        if len(query_tokens) >= 2:
            for uk, matched in token_hits.items():
                coverage = len(matched) / float(len(query_tokens))
                if coverage >= 0.5:
                    scores[uk] += coverage * 10.0

        # 4. 描述子串匹配（逐 token，解决 "玩家位置" 不是 "获取实体位置" 子串的问题）
        for unique_key, entry in self._api_entries.items():
            desc_lower = entry.desc.lower()
            if query_lower in desc_lower:
                scores.setdefault(unique_key, 0)
                scores[unique_key] += 8.0
            else:
                desc_hits = sum(1 for t in query_tokens if len(t) >= 2 and t.lower() in desc_lower)
                if desc_hits > 0:
                    scores.setdefault(unique_key, 0)
                    scores[unique_key] += min(desc_hits * 3.0, 8.0)
        
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
    
    def get_api_categories(self) -> Dict[str, Dict[str, int]]:
        """获取API/事件的分类树：{一级分类: {二级分类: 条目数}}"""
        tree: Dict[str, Dict[str, int]] = {}
        for entry in self._api_entries.values():
            if not entry.category:
                continue
            parts = entry.category.split("/")
            top = parts[0]
            sub = parts[1] if len(parts) > 1 else ""
            if top not in tree:
                tree[top] = {}
            tree[top][sub] = tree[top].get(sub, 0) + 1
        return tree

    def browse_api_category(self, category: str, entry_type: str = "all") -> List[Dict[str, str]]:
        """按分类浏览API/事件，返回该分类下所有条目的简要信息"""
        results = []
        cat_lower = category.lower()
        for entry in self._api_entries.values():
            if not entry.category:
                continue
            if entry_type != "all" and entry.entry_type != entry_type:
                continue
            if cat_lower in entry.category.lower():
                results.append({
                    "name": entry.name,
                    "type": entry.entry_type,
                    "side": entry.side,
                    "category": entry.category,
                    "desc": entry.desc[:60],
                })
        results.sort(key=lambda x: x["name"])
        return results

    def generate_compact_index(self, include_params: bool = False) -> str:
        """
        生成紧凑的 API/事件索引，按分类组织。
        设计目标：让 LLM 直接看到所有 API 名称+简述，用自身语义能力匹配，
        而不是依赖关键词搜索引擎的 EN_TO_CN_MAP 做中英翻译。

        Args:
            include_params: 是否包含参数签名（True 时 tokens 更多但信息更完整）

        Returns:
            按分类组织的紧凑索引字符串
        """
        # 按分类组织 entries
        categorized: Dict[str, List[ApiEntry]] = {}
        uncategorized: List[ApiEntry] = []

        for entry in self._api_entries.values():
            if entry.category:
                cat = entry.category
                if cat not in categorized:
                    categorized[cat] = []
                categorized[cat].append(entry)
            else:
                uncategorized.append(entry)

        lines = []
        lines.append("# ModSDK API/事件紧凑索引")
        lines.append("")

        # 常见操作速查表（意图→API 直接映射）
        lines.append("## 常见操作速查")
        lines.append("给玩家物品 → SpawnItemToPlayerInv | 移除背包物品 → SetInvItemNum(slot,0)")
        lines.append("获取实体位置 → GetPos/GetFootPos | 设置实体位置 → SetPos")
        lines.append("获取实体朝向 → GetRot | 方向向量 → GetDirFromRot")
        lines.append("获取实体速度 → GetMotion | 设置速度 → SetMotion")
        lines.append("实体造成伤害 → Hurt | 添加状态效果 → AddEffectToEntity")
        lines.append("获取属性值 → GetAttrValue | 设置属性值 → SetAttrValue")
        lines.append("创建实体 → CreateEngineEntityByTypeStr | 销毁实体 → DestroyEntity")
        lines.append("创建投射物 → CreateProjectileEntity | 创建掉落物 → CreateEngineItemEntity")
        lines.append("获取方块 → GetBlockNew | 设置方块 → SetBlockNew")
        lines.append("播放音效 → PlayCustomMusic | 创建粒子 → CreateEngineParticle")
        lines.append("创建UI → CreateUI/RegisterUI | 发消息 → NotifyOneMessage")
        lines.append("添加定时器 → AddTimer/AddRepeatedTimer | 取消 → CancelTimer")
        lines.append("存储数据 → SetExtraData | 读取数据 → GetExtraData")
        lines.append("玩家经验 → GetPlayerExp/AddPlayerExperience")
        lines.append("设置实体跟随 → behavior.follow_owner(JSON行为组件)")
        lines.append("不可被攻击 → DamageEvent cancel 或 damage_sensor(JSON组件)")
        lines.append("")

        # 按分类输出
        # 先按顶级分类排序，再按二级分类排序
        sorted_cats = sorted(categorized.keys())

        current_top = ""
        for cat in sorted_cats:
            entries = categorized[cat]
            top = cat.split("/")[0]

            if top != current_top:
                current_top = top
                # 统计该顶级分类的总数
                top_total = sum(len(v) for k, v in categorized.items() if k.split("/")[0] == top)
                lines.append(f"## {top} ({top_total})")

            # 二级分类标题
            if "/" in cat:
                sub = cat.split("/", 1)[1]
                lines.append(f"### {sub} ({len(entries)})")

            # 按 entry_type 分组：先事件后API
            events = [e for e in entries if e.entry_type == "event"]
            apis = [e for e in entries if e.entry_type == "api"]

            for group_label, group in [("事件", events), ("接口", apis)]:
                if not group:
                    continue
                for e in sorted(group, key=lambda x: x.name):
                    desc_short = e.desc[:35].replace("\n", " ")
                    # 去掉"触发时机："前缀
                    desc_short = re.sub(r'^触发时机[：:]\s*', '', desc_short)
                    side_tag = "S" if e.side == "服务端" else "C"

                    if include_params and e.params:
                        param_str = ",".join(p.get("param_name", "") for p in e.params[:4])
                        if len(e.params) > 4:
                            param_str += ",..."
                        ret = e.return_info.get("return_type", "") if e.return_info else ""
                        if ret:
                            lines.append(f"- [{side_tag}][{e.entry_type[0]}] {e.name}({param_str})->{ret} {desc_short}")
                        else:
                            lines.append(f"- [{side_tag}][{e.entry_type[0]}] {e.name}({param_str}) {desc_short}")
                    else:
                        lines.append(f"- [{side_tag}][{e.entry_type[0]}] {e.name} {desc_short}")

            lines.append("")

        # 未分类条目
        if uncategorized:
            lines.append(f"## 未分类 ({len(uncategorized)})")
            for e in sorted(uncategorized, key=lambda x: x.name):
                desc_short = e.desc[:35].replace("\n", " ")
                desc_short = re.sub(r'^触发时机[：:]\s*', '', desc_short)
                side_tag = "S" if e.side == "服务端" else "C"
                lines.append(f"- [{side_tag}][{e.entry_type[0]}] {e.name} {desc_short}")

        return "\n".join(lines)

    def get_api_detail(self, name: str) -> Optional[Dict[str, Any]]:
        """
        按精确名称获取 API/事件的完整详情。
        用于 LLM 通过紧凑索引找到 API 名后获取完整签名。

        Args:
            name: API/事件的精确名称

        Returns:
            完整的 API 详情字典，或 None
        """
        # 先精确匹配
        name_lower = name.lower()
        matches = []
        for uk, entry in self._api_entries.items():
            if entry.name.lower() == name_lower:
                matches.append(entry)

        if not matches:
            return None

        results = []
        for entry in matches:
            result = {
                "name": entry.name,
                "type": entry.entry_type,
                "side": entry.side,
                "category": entry.category,
                "desc": entry.desc,
                "params": entry.params,
                "return": entry.return_info,
                "class_path": entry.class_path,
            }
            results.append(result)

        return results if len(results) > 1 else results[0]

    def _load_enum_data(self) -> None:
        """从 docs/枚举值/*.md 自动解析枚举值定义。
        DRY: 不硬编码枚举值，从已有的 73 个 MD 文件自动提取。
        """
        enum_dir = self.docs_path / "枚举值"
        if not enum_dir.exists():
            return

        for md_file in enum_dir.glob("*.md"):
            if md_file.name == "索引.md":
                continue

            enum_name = md_file.stem  # 文件名即枚举名，如 "AttrType"
            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception:
                continue

            # 提取 python 代码块中的枚举值定义
            entries = []
            in_code_block = False
            for line in content.splitlines():
                stripped = line.strip()
                if stripped.startswith("```python"):
                    in_code_block = True
                    continue
                if stripped.startswith("```") and in_code_block:
                    break
                if not in_code_block:
                    continue
                if stripped.startswith("class ") or not stripped:
                    continue

                # 解析 NAME = VALUE  # comment 格式
                match = re.match(
                    r'([A-Za-z_]\w*)\s*=\s*([^#\n]+?)(?:\s*#\s*(.*))?$',
                    stripped
                )
                if match:
                    name = match.group(1).strip()
                    value = match.group(2).strip().strip('"\'')
                    comment = (match.group(3) or "").strip()
                    entries.append((name, value, comment))

            if entries:
                self._enum_data[enum_name] = entries

    def get_enum_inline(self, enum_name: str) -> Optional[str]:
        """获取枚举值的紧凑内联字符串。
        ≤20 个值: 返回 "NAME=VALUE, NAME2=VALUE2, ..."
        >20 个值: 返回摘要 + 提示查文档
        """
        entries = self._enum_data.get(enum_name)
        if not entries:
            return None

        if len(entries) <= 20:
            return ", ".join(f"{name}={value}" for name, value, _ in entries)
        else:
            preview = ", ".join(f"{name}={value}" for name, value, _ in entries[:10])
            return f"{preview}, ... (共{len(entries)}个，用 search_docs '{enum_name}' 查看完整列表)"

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
        self._api_keyword_doc_freq.clear()
        self._total_api_entries = 0
        self._category_keywords.clear()
        self.load_all_docs()


# 全局文档读取器实例
_docs_reader: Optional[DocsReader] = None


def get_docs_reader(docs_path: str = "docs") -> DocsReader:
    """获取文档读取器实例（单例模式）"""
    global _docs_reader
    if _docs_reader is None:
        # 自动检测网易官方教程文档路径
        guide_root = _find_guide_root()
        _docs_reader = DocsReader(docs_path, guide_root=guide_root)
        _docs_reader.load_all_docs()
    return _docs_reader


def _find_guide_root() -> str:
    """自动检测网易官方教程文档根目录（netease-modsdk-wiki/docs/）"""
    project_root = Path(__file__).parent.parent

    # 候选路径列表（按优先级）
    candidates = [
        # 环境变量指定
        os.environ.get("MODSDK_WIKI_PATH", ""),
        # MCP Server 项目内
        str(project_root / "external" / "netease-modsdk-wiki" / "docs"),
        # 常见的兄弟目录布局
        str(project_root.parent / "netease-modsdk-wiki" / "docs"),
        # new-mg 项目中的路径
        str(project_root.parent / "new-mg" / "external" / "netease-modsdk-wiki" / "docs"),
    ]

    for path in candidates:
        if path and Path(path).exists() and (Path(path) / "mcguide").exists():
            print("[DocsReader] 找到官方教程文档: {}".format(path))
            return path

    print("[DocsReader] 未找到官方教程文档，跳过教程加载")
    return ""


def reload_docs() -> None:
    """重新加载文档"""
    global _docs_reader
    if _docs_reader:
        _docs_reader.reload()
