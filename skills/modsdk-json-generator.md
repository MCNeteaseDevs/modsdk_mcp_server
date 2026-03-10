# NetEase ModSDK JSON 生成器技能

## 概述

这是一个专门用于网易我的世界 ModSDK 3.7 基岩版 JSON 内容生成的 MCP 技能。它提供了完整的数据驱动内容生成能力，支持物品、方块、实体、配方、战利品表等 JSON 文件的生成。

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
- **重要**：网易 ModSDK 3.7 必须设置 `runtime_identifier`
- 支持行为组件、寻路组件、战斗组件等

### 4. 其他 JSON 生成
- `generate_recipe_json` - 配方（有序/无序/熔炼/酿造）
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
- `list_modsdk_events` - 列出 ModSDK 常用事件

## 组件知识库

### 物品组件（22个）
```
minecraft:max_stack_size    最大堆叠大小
minecraft:hand_equipped     手持装备
minecraft:damage            伤害
minecraft:durability        耐久
minecraft:armor             盔甲
minecraft:food              食物
minecraft:weapon            武器
minecraft:digger            挖掘器
minecraft:wearable          可穿戴
minecraft:throwable         可投掷
minecraft:projectile        弹射物
minecraft:shooter           发射器
minecraft:cooldown          冷却
minecraft:repairable        可修复
minecraft:enchantable       可附魔
minecraft:fuel              燃料
minecraft:block_placer      方块放置器
minecraft:entity_placer     实体放置器
...
```

### 方块组件（22个）
```
minecraft:destructible_by_mining    可挖掘破坏
minecraft:destructible_by_explosion 可爆炸破坏
minecraft:friction                  摩擦力
minecraft:flammable                 可燃性
minecraft:geometry                  几何体
minecraft:material_instances        材质实例
minecraft:collision_box             碰撞箱
minecraft:on_interact               交互事件
minecraft:on_step_on                踩踏事件
minecraft:random_ticking            随机刻
minecraft:queued_ticking            计划刻
...
```

### 网易特有组件
```
netease:customtips          自定义提示
netease:frame_animation     帧动画
netease:show_in_hand        手持显示
netease:aabb                方块碰撞箱
netease:tier                挖掘等级
netease:block_entity        方块实体
netease:random_tick         随机刻
netease:redstone            红石信号
...
```

## 格式版本规范

| 内容类型 | format_version | 说明 |
|----------|----------------|------|
| 物品 | 1.16.100 | 标准基岩版 |
| 方块 | 1.16.100 | 标准基岩版 |
| 实体 | 1.10.0 | 网易 ModSDK 兼容 |
| 配方 | 1.12.0 | 标准基岩版 |
| 战利品表 | 1.12.0 | 标准基岩版 |
| 生成规则 | 1.8.0 | 标准基岩版 |

## 项目结构

```
{mod_id}_Script/
├── __init__.py
├── modMain.py
└── scripts/
    └── {mod_id}/
        ├── server.py
        └── client.py

behavior_pack/
├── netease_items_beh/        # 物品行为定义
├── netease_blocks/           # 方块定义
├── entities/                 # 实体定义
├── recipes/                  # 配方
├── loot_tables/              # 战利品表
└── spawn_rules/              # 生成规则

resource_pack/
├── netease_items_res/        # 物品资源定义
├── textures/
│   ├── items/                # 物品纹理
│   └── blocks/               # 方块纹理
└── texts/
    └── zh_CN.lang            # 本地化
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
2. **runtime_identifier**：网易 ModSDK 3.7 实体必须设置此属性
3. **组件工厂缓存**：`GetEngineCompFactory()` 必须在文件顶部缓存
4. **Tick 降帧**：所有 Tick 逻辑必须使用质数间隔降帧

## 版本信息

- MCP Server 版本: 1.0.0
- 支持的 ModSDK 版本: 3.7
- 支持的基岩版格式版本: 1.8.0 - 1.16.100
- 工具总数: 34 个
