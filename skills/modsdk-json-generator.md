# NetEase ModSDK JSON 生成器技能

## 概述

这是一个面向网易《我的世界》ModSDK 3.10 / BE 1.21.130 的 JSON 内容生成说明。开始前先调用 `get_development_guidance`，生成后以工具返回的校验报告为准。

## 核心能力

### 1. 物品 JSON 生成

#### 基础生成器
- `generate_item_json` - 生成通用物品 JSON

#### 高级一键生成器
| 工具名 | 功能 | 关键参数 |
|--------|------|----------|
| `generate_sword_json` | 剑类武器 | damage, durability |
| `generate_pickaxe_json` | 镐类工具 | mining_speed, durability |
| `generate_axe_json` | 斧类工具 | damage, mining_speed |
| `generate_shovel_json` | 锹类工具 | mining_speed |
| `generate_hoe_json` | 锄类工具 | durability |
| `generate_food_json` | 食物 | nutrition, saturation, effects |
| `generate_armor_json` | 盔甲 | slot, protection, durability |
| `generate_bow_json` | 弓类武器 | max_draw_duration |
| `generate_throwable_json` | 投掷物 | projectile_entity, launch_power |

### 2. 方块 JSON 生成
- `generate_block_json` - 生成自定义方块 JSON
- 支持 24 种方块组件（摩擦力、几何体、碰撞箱、事件触发等）

### 3. 实体 JSON 生成
- `generate_entity_json` - 生成自定义实体 JSON
- `runtime_identifier` 是否必需应按实体目标和当前官方详情核对，不能从旧示例推广为所有实体的硬规则
- 支持行为组件、寻路组件、战斗组件等

### 4. 清单、UI 与其他 JSON 生成
- `generate_manifest_json` - 双包最新标准 `manifest.json`（`format_version: 2`）
- `generate_ui_json` - 自定义 JSON UI、`ui/_ui_defs.json` 与 `ScreenNode` 客户端控制器
- `generate_recipe_json` - 配方（有序/无序/熔炉，位于 `netease_recipes/`）
- `generate_loot_table_json` - 战利品表
- `generate_spawn_rules_json` - 生成规则

## 内嵌知识库

### 组件查询工具
- `search_components` - 搜索组件（支持中英文）
- `get_component_details` - 获取组件详情
- `list_components` - 列出所有组件

### 最佳实践
- `get_best_practices` - 获取代码规范和最佳实践

### 事件系统
- `search_api` / `get_api_detail` - 查询并核对事件或 API

## 组件知识库

### 网易 1.10 支持的原版物品组件
```
minecraft:max_stack_size    最大堆叠数量（行为包）
minecraft:max_damage        最大耐久度（行为包，严禁与 stacked_by_data 共存）
minecraft:hand_equipped     手持武器渲染（行为包）
minecraft:stacked_by_data   按附加值分堆叠（行为包）
minecraft:foil              附魔光效（行为包）
minecraft:use_duration      最大使用时长（行为包，整数 tick）
minecraft:food              食物组件（行为包）
minecraft:seed              农作物种子（行为包）
minecraft:tags              原版物品标签（行为包）
minecraft:icon              物品贴图图标（资源包 netease_items_res）
minecraft:use_animation     使用动画（资源包 netease_items_res）
minecraft:hover_text_color  悬浮名称颜色（资源包 netease_items_res）
```

### 方块组件
```
minecraft:destructible_by_mining    可挖掘破坏（1.19.20+ 默认推荐）
minecraft:destructible_by_explosion 可爆炸破坏（1.19.20+ 默认推荐）
minecraft:light_emission            发光等级 0-15（1.19.20+ 默认推荐）
minecraft:light_dampening           遮光等级 0-15（1.19.20+ 默认推荐）
minecraft:friction                  摩擦力
minecraft:flammable                 可燃性
minecraft:geometry                  几何体
minecraft:material_instances        材质实例
minecraft:collision_box             碰撞箱
minecraft:selection_box             选择箱
minecraft:loot                      战利品表
```

### 网易特有组件
```
netease:weapon              自定义武器与工具（type: sword/pickaxe/hatchet/shovel/hoe）
netease:armor               自定义盔甲（armor_slot: 0~3，需配套 attachables）
netease:projectile          右键投掷抛射物（配合 projectile_item）
netease:cooldown            物品冷却
netease:fuel                熔炉燃料
netease:customtips          自定义提示
netease:frame_animation     蓄力序列帧动画（资源包）
netease:show_in_hand        手持显示
netease:liquid_clipped      流体点击检测
netease:aabb                方块碰撞箱
netease:tier                挖掘等级
netease:block_entity        方块实体
netease:random_tick         随机刻
netease:redstone            红石信号
```

## 格式版本规范

| 内容类型 | format_version | 说明 |
|----------|----------------|------|
| 包清单 `manifest.json` | `2`（整数） | 最新标准，避免 3.8+ 生物蛋贴图异常 |
| 物品 | `"1.10"` | 网易官方物品格式（严禁混用 1.16.100+ 国际版组件） |
| 方块 | `"1.19.20"`（默认）/ `"1.16.0"` / `"1.10.0"` | 默认推荐 `modern_1_19_20`；旧档 `block_light_emission` 仅限 `[0.0, 1.0]` |
| 实体 | `"1.10.0"`（模型 `"1.12.0"`） | 配套生成 `models/entity/*.geo.json` |
| 盔甲穿戴 | `"1.8.0"` | `resource_pack/attachables/*.json` |
| 配方 | `"1.12"` | 必须放在 `behavior_pack/netease_recipes/` |
| 生成规则 | `"1.8.0"` | `behavior_pack/spawn_rules/` |

## 标准双包项目结构

```
behavior_pack/
├── manifest.json             # format_version: 2（绑定 resource_pack 依赖）
├── entities/                 # 实体定义（中国版必选目录）
├── {mod_id}_Script/          # Python 脚本根目录（直接位于 behavior_pack 下）
│   ├── __init__.py
│   ├── modConfig.py
│   ├── modMain.py
│   ├── serverSystem.py
│   └── clientSystem.py
├── netease_items_beh/        # 物品行为定义
├── netease_blocks/           # 方块行为定义
├── netease_recipes/          # 合成与烧炼配方
├── loot_tables/              # 战利品表
└── spawn_rules/              # 生成规则

resource_pack/
├── manifest.json             # format_version: 2
├── blocks.json               # 方块渲染与音效注册
├── netease_items_res/        # 物品资源定义
├── attachables/              # 盔甲穿戴渲染定义
├── entity/                   # 实体客户端表现定义
├── models/entity/            # 实体与盔甲几何体 (*.geo.json)
├── ui/                       # JSON UI 与 _ui_defs.json
├── textures/                 # 中国版必选目录
│   ├── item_texture.json     # 物品贴图映射表
│   ├── terrain_texture.json  # 方块贴图映射表
│   ├── items/                # 物品纹理 PNG
│   ├── blocks/               # 方块纹理 PNG
│   └── entity/               # 实体纹理 PNG
└── texts/
    ├── languages.json        # ["zh_CN"]
    └── zh_CN.lang            # 中文本地化词条
```

## 使用示例

### 创建自定义剑

```
调用: generate_sword_json
参数:
  namespace: "mymod"
  item_id: "flame_sword"
  damage: 10
  durability: 500
  enchantability: 22
  repair_material: "minecraft:blaze_rod"
```

### 创建自定义食物

```
调用: generate_food_json
参数:
  namespace: "mymod"
  item_id: "golden_apple_plus"
  nutrition: 8
  saturation: "max"
  can_always_eat: true
  effects: [
    {"name": "regeneration", "duration": 10, "amplifier": 2, "chance": 1.0}
  ]
```

## 注意事项

1. **Python 2.7 兼容性**：ModSDK 使用 Python 2.7，代码不能使用 f-string、type hints 等
2. **runtime_identifier**：只在相应实体格式和目标要求时设置，并通过文档查证
3. **版本—结构一致**：不要把现代组件写入旧版方块格式，也不要把旧对象形状写入标量档
4. **命名空间**：3.9 起自定义维度的 `biome_type` 必须使用完整 `namespace:id`
5. **证据边界**：3.10 已同步官方稳定版文档，尚无可读的 Python 运行时源码复核，也没有本次游戏实机验收

## 版本信息

- MCP Server 版本: 1.1.0
- 当前 ModSDK 版本: 3.10（稳定版）
- 对应基岩版版本: 1.21.130
- MCP 工具总数: 41 个
