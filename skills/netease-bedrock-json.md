# 我的世界中国版 Bedrock JSON 数据驱动开发专家

## 技能描述

你是一位我的世界中国版 Bedrock JSON 数据驱动内容开发专家，精通：
- 自定义物品 (netease_items_beh / netease_items_res)
- 自定义方块 (netease_blocks)
- 自定义配方 (netease_recipes)
- 资源包配置 (item_texture.json / blocks.json / texts/)
- 行为包与资源包的 manifest.json

## 核心知识

### 1. NetEase 特有文件夹结构

NetEase 使用独有的文件夹命名（与国际版不同）：

```
behavior_pack_{ModName}_BP/
├── manifest.json
├── netease_items_beh/          # 物品行为定义（非国际版的 items/）
│   └── {namespace}_{item_id}.json
├── netease_blocks/             # 方块行为定义（非国际版的 blocks/）
│   └── {namespace}_{block_id}.json
├── netease_recipes/            # 配方定义
│   └── {recipe_id}.json
├── netease_effects/            # 自定义药水效果
├── netease_enchants/           # 自定义附魔
├── netease_features/           # 地物生成
├── netease_feature_rules/      # 地物规则
├── netease_tab/                # 创造模式标签页
├── netease_group/              # 物品组
├── loot_tables/                # 战利品表
└── entities/                   # 实体定义

resource_pack_{ModName}_RP/
├── manifest.json
├── netease_items_res/          # 物品资源定义
│   └── {namespace}_{item_id}.json
├── textures/
│   ├── items/                  # 物品贴图
│   │   └── {item_texture}.png
│   ├── blocks/                 # 方块贴图
│   │   └── {block_texture}.png
│   ├── item_texture.json       # 物品贴图映射
│   └── terrain_texture.json    # 方块贴图映射
├── models/
│   └── blocks/                 # 方块模型
├── texts/
│   └── zh_CN.lang              # 中文本地化
└── blocks.json                 # 方块渲染定义
```

---

## 物品定义规范

### 行为包物品 (netease_items_beh)

**文件路径**: `behavior_pack/netease_items_beh/{namespace}_{item_id}.json`

```json
{
    "format_version": "1.10",
    "minecraft:item": {
        "description": {
            "identifier": "{namespace}:{item_id}",
            "category": "items"
        },
        "components": {
            "minecraft:max_stack_size": 64,
            "minecraft:hand_equipped": false,
            "minecraft:foil": false
        }
    }
}
```

**description 字段**:

| 字段 | 类型 | 说明 |
|-----|------|-----|
| identifier | string | `namespace:item_id` 格式，**必须全小写+下划线** |
| category | string | 创造栏分类：`construction`/`equipment`/`items`/`nature`/`commands`/`none` |
| custom_item_type | string | 特殊物品类型：`weapon`/`armor`/`egg`/`ranged_weapon`/`bucket`/`projectile_item`/`shield` |

### 常用原版 Components

| Component | 示例 | 说明 |
|-----------|------|-----|
| `minecraft:max_stack_size` | `64` | 最大堆叠数，不超过64 |
| `minecraft:max_damage` | `1561` | 耐久度 [0, 32767] |
| `minecraft:hand_equipped` | `true` | 手持时竖直渲染（武器握法） |
| `minecraft:foil` | `true` | 附魔光效 |
| `minecraft:food` | `{"nutrition": 4, "saturation_modifier": "low"}` | 食物属性 |
| `minecraft:use_duration` | `32` | 使用时长（食物/蓄力） |
| `minecraft:seed` | `{"crop_result": "wheat", "plant_at": ["grass", "dirt"]}` | 种子属性 |
| `minecraft:stacked_by_data` | `true` | 不同aux值物品不可堆叠 |

### 网易独有 Components

| Component | 示例 | 说明 |
|-----------|------|-----|
| `netease:allow_offhand` | `{"value": true}` | 可放副手 |
| `netease:armor` | `{"defense": 10, "enchantment": 4, "armor_slot": 0}` | 盔甲属性（需 `custom_item_type: armor`） |
| `netease:weapon` | `{"type": "sword", "level": 3, "attack_damage": 7}` | 武器属性（需 `custom_item_type: weapon`） |
| `netease:egg` | `{"entity": "mymod:custom_mob"}` | 生物蛋（需 `custom_item_type: egg`） |
| `netease:cooldown` | `{"category": "item", "duration": 10}` | 冷却时间 |
| `netease:customtips` | `{"value": "§8右键可发射"}` | 描述信息 |
| `netease:fuel` | `{"duration": 3}` | 燃料（秒） |
| `netease:fire_resistant` | `{"value": true}` | 防火（类似下界合金） |
| `netease:compostable` | `48` | 堆肥成功概率（%） |
| `netease:projectile` | `"mymod:custom_arrow"` | 发射抛射物（需 `custom_item_type: projectile_item`） |
| `netease:initial_user_data` | `{"display": {"Name": "物品名"}}` | 初始NBT数据 |

### 资源包物品 (netease_items_res)

**文件路径**: `resource_pack/netease_items_res/{namespace}_{item_id}.json`

```json
{
    "format_version": "1.10",
    "minecraft:item": {
        "description": {
            "identifier": "{namespace}:{item_id}"
        },
        "components": {
            "minecraft:icon": "{texture_name}"
        }
    }
}
```

**资源包专用 Components**:

| Component | 示例 | 说明 |
|-----------|------|-----|
| `minecraft:icon` | `"my_item"` | 贴图名（对应 item_texture.json） |
| `minecraft:hover_text_color` | `"gold"` | 悬浮文本颜色 |
| `minecraft:use_animation` | `"eat"` / `"drink"` / `"bow"` | 使用动画 |
| `netease:frame_animation` | `{"frame_count": 3, "texture_name": "bow_pulling"}` | 蓄力帧动画 |
| `netease:render_offsets` | `{"controller_scale": 1.5}` | 手持渲染偏移 |

### item_texture.json

**文件路径**: `resource_pack/textures/item_texture.json`

```json
{
    "resource_pack_name": "mymod",
    "texture_name": "atlas.items",
    "texture_data": {
        "{texture_name}": {
            "textures": "textures/items/{texture_file}"
        }
    }
}
```

### 本地化 (zh_CN.lang)

**文件路径**: `resource_pack/texts/zh_CN.lang`

```
item.{namespace}:{item_id}.name=物品显示名称
```

---

## 方块定义规范

### 行为包方块 (netease_blocks)

**文件路径**: `behavior_pack/netease_blocks/{namespace}_{block_id}.json`

#### format_version 差异

| 版本 | 破坏时间写法 | 爆炸抗性写法 |
|-----|-------------|------------|
| 1.10.0 | `"minecraft:destroy_time": {"value": 4.0}` | `"minecraft:explosion_resistance": 20` |
| 1.16.0 | `"minecraft:destroy_time": 4.0` | `"minecraft:explosion_resistance": 20` |
| 1.19.20+ | `"minecraft:destructible_by_mining": {"seconds_to_destroy": 4.0}` | `"minecraft:destructible_by_explosion": {"explosion_resistance": 20}` |

#### 基础方块模板 (1.19.20+)

```json
{
    "format_version": "1.19.20",
    "minecraft:block": {
        "description": {
            "identifier": "{namespace}:{block_id}",
            "register_to_create_menu": true,
            "category": "Nature"
        },
        "components": {
            "minecraft:destructible_by_mining": {
                "seconds_to_destroy": 1.5
            },
            "minecraft:destructible_by_explosion": {
                "explosion_resistance": 10
            },
            "minecraft:light_emission": 0,
            "minecraft:light_dampening": 15,
            "minecraft:map_color": "#FFFFFF"
        }
    }
}
```

### 原版方块 Components

| Component | 示例 | 说明 |
|-----------|------|-----|
| `minecraft:destructible_by_mining` | `{"seconds_to_destroy": 1.5}` 或 `false` | 挖掘硬度 |
| `minecraft:destructible_by_explosion` | `{"explosion_resistance": 10}` 或 `false` | 爆炸抗性 |
| `minecraft:light_emission` | `15` | 发光等级 [0-15] |
| `minecraft:light_dampening` | `0` | 遮光等级 [0-15] |
| `minecraft:friction` | `0.6` | 摩擦力 (0.0-0.9) |
| `minecraft:map_color` | `"#FF5500"` | 地图颜色 |
| `minecraft:loot` | `"loot_tables/blocks/my_ore.json"` | 掉落物表 |
| `minecraft:geometry` | `{"identifier": "geometry.my_block"}` | 自定义模型 |
| `minecraft:material_instances` | 见下方 | 材质实例（配合geometry） |
| `minecraft:collision_box` | `{"origin": [-8, 0, -8], "size": [16, 16, 16]}` | 碰撞箱 |
| `minecraft:selection_box` | 同上 | 选择框 |

### 网易独有方块 Components

| Component | 示例 | 说明 |
|-----------|------|-----|
| `netease:tier` | `{"digger": "pickaxe", "level": 2, "destroy_special": true}` | 挖掘工具需求 |
| `netease:aabb` | `{"collision": {...}, "clip": {...}}` | 碰撞盒 |
| `netease:face_directional` | `{"type": "direction"}` | 多面向（4面/6面） |
| `netease:render_layer` | `{"value": "alpha"}` | 渲染层：`opaque`/`alpha`/`blend`/`optionalAlpha` |
| `netease:solid` | `{"value": false}` | 是否实心（窒息伤害） |
| `netease:pathable` | `{"value": true}` | AI寻路是否当作空气 |
| `netease:block_entity` | `{"tick": true, "movable": false}` | 方块实体 |
| `netease:random_tick` | `{"enable": true, "tick_to_script": true}` | 随机刻 |
| `netease:redstone` | `{"type": "producer", "strength": 15}` | 红石属性 |
| `netease:connection` | `{"blocks": ["minecraft:fence", "mymod:my_fence"]}` | 连接方块（栅栏类） |
| `netease:may_place_on` | `{"block": ["grass", "dirt"]}` | 可放置于 |
| `netease:fire_resistant` | `{"value": true}` | 掉落物防火 |
| `netease:fuel` | `{"duration": 15}` | 燃料属性 |
| `netease:block_chest` | `{"chest_capacity": 4, "can_pair": true}` | 箱子功能 |
| `netease:custom_tips` | `{"value": "提示文字"}` | 物品描述 |
| `netease:no_crop_face_block` | `{}` | 相邻面不裁剪（叶子效果） |

### blocks.json (资源包)

**文件路径**: `resource_pack/blocks.json`

```json
{
    "format_version": [1, 1, 0],
    "{namespace}:{block_id}": {
        "textures": "{texture_name}",
        "sound": "stone"
    }
}
```

对于六面不同贴图：

```json
{
    "{namespace}:{block_id}": {
        "textures": {
            "up": "top_texture",
            "down": "bottom_texture",
            "side": "side_texture"
        }
    }
}
```

### terrain_texture.json

**文件路径**: `resource_pack/textures/terrain_texture.json`

```json
{
    "resource_pack_name": "mymod",
    "texture_name": "atlas.terrain",
    "padding": 8,
    "num_mip_levels": 4,
    "texture_data": {
        "{texture_name}": {
            "textures": "textures/blocks/{texture_file}"
        }
    }
}
```

---

## 配方定义规范

### 有序合成 (Shaped)

**文件路径**: `behavior_pack/netease_recipes/{recipe_id}.json`

```json
{
    "format_version": "1.20.10",
    "minecraft:recipe_shaped": {
        "description": {
            "identifier": "{namespace}:{recipe_id}"
        },
        "tags": ["crafting_table"],
        "pattern": [
            "AAA",
            "ABA",
            "AAA"
        ],
        "key": {
            "A": {"item": "minecraft:iron_ingot"},
            "B": {"item": "minecraft:diamond"}
        },
        "unlock": {"context": "AlwaysUnlocked"},
        "result": {
            "item": "{namespace}:{item_id}",
            "count": 1
        }
    }
}
```

### 无序合成 (Shapeless)

```json
{
    "format_version": "1.12",
    "minecraft:recipe_shapeless": {
        "description": {
            "identifier": "{namespace}:{recipe_id}"
        },
        "tags": ["crafting_table"],
        "ingredients": [
            {"item": "minecraft:coal"},
            {"item": "minecraft:stick"}
        ],
        "result": {
            "item": "{namespace}:{item_id}",
            "count": 4
        }
    }
}
```

### 熔炉配方

```json
{
    "format_version": "1.12",
    "minecraft:recipe_furnace": {
        "description": {
            "identifier": "{namespace}:{recipe_id}"
        },
        "tags": ["furnace"],
        "input": "minecraft:iron_ore",
        "output": "{namespace}:{item_id}"
    }
}
```

### 配方 tags 选项

| Tag | 说明 |
|-----|-----|
| `crafting_table` | 工作台 |
| `stonecutter` | 切石机 |
| `cartography_table` | 制图台 |
| `furnace` | 熔炉 |
| `blast_furnace` | 高炉 |
| `smoker` | 烟熏炉 |
| `campfire` | 营火 |
| `brewing_stand` | 酿造台 |
| `smithing_table` | 锻造台 |

### 配方解锁

```json
"unlock": {"context": "AlwaysUnlocked"}
// 或
"unlock": {"context": "PlayerInWater"}
// 或
"unlock": {"context": "PlayerHasManyItems"}
// 或基于物品：
"unlock": [{"item": "minecraft:iron_ingot"}]
```

---

## manifest.json 规范

### 行为包 manifest

```json
{
    "format_version": 2,
    "header": {
        "name": "{ModName} Behavior Pack",
        "description": "模组描述",
        "uuid": "{生成的UUID}",
        "version": [1, 0, 0],
        "min_engine_version": [1, 19, 0]
    },
    "modules": [
        {
            "type": "data",
            "uuid": "{另一个UUID}",
            "version": [1, 0, 0]
        }
    ],
    "dependencies": [
        {
            "uuid": "{资源包的header.uuid}",
            "version": [1, 0, 0]
        }
    ]
}
```

### 资源包 manifest

```json
{
    "format_version": 2,
    "header": {
        "name": "{ModName} Resource Pack",
        "description": "模组描述",
        "uuid": "{生成的UUID}",
        "version": [1, 0, 0],
        "min_engine_version": [1, 19, 0]
    },
    "modules": [
        {
            "type": "resources",
            "uuid": "{另一个UUID}",
            "version": [1, 0, 0]
        }
    ]
}
```

---

## 完整物品创建示例

### 需求：创建一个名为 "magic_wand" 的魔法棒

**1. 行为包物品定义**
`behavior_pack/netease_items_beh/mymod_magic_wand.json`

```json
{
    "format_version": "1.10",
    "minecraft:item": {
        "description": {
            "identifier": "mymod:magic_wand",
            "category": "equipment"
        },
        "components": {
            "minecraft:max_stack_size": 1,
            "minecraft:max_damage": 100,
            "minecraft:hand_equipped": true,
            "minecraft:foil": true,
            "netease:cooldown": {
                "category": "wand",
                "duration": 3
            },
            "netease:customtips": {
                "value": "§b右键施放魔法"
            }
        }
    }
}
```

**2. 资源包物品定义**
`resource_pack/netease_items_res/mymod_magic_wand.json`

```json
{
    "format_version": "1.10",
    "minecraft:item": {
        "description": {
            "identifier": "mymod:magic_wand"
        },
        "components": {
            "minecraft:icon": "magic_wand",
            "minecraft:hover_text_color": "light_purple"
        }
    }
}
```

**3. 贴图映射**
`resource_pack/textures/item_texture.json`

```json
{
    "resource_pack_name": "mymod",
    "texture_name": "atlas.items",
    "texture_data": {
        "magic_wand": {
            "textures": "textures/items/magic_wand"
        }
    }
}
```

**4. 本地化**
`resource_pack/texts/zh_CN.lang`

```
item.mymod:magic_wand.name=§d魔法棒
```

**5. 合成配方**
`behavior_pack/netease_recipes/magic_wand_recipe.json`

```json
{
    "format_version": "1.20.10",
    "minecraft:recipe_shaped": {
        "description": {
            "identifier": "mymod:magic_wand_recipe"
        },
        "tags": ["crafting_table"],
        "pattern": [
            "  D",
            " B ",
            "S  "
        ],
        "key": {
            "D": {"item": "minecraft:diamond"},
            "B": {"item": "minecraft:blaze_rod"},
            "S": {"item": "minecraft:stick"}
        },
        "unlock": {"context": "AlwaysUnlocked"},
        "result": {
            "item": "mymod:magic_wand"
        }
    }
}
```

---

## 完整方块创建示例

### 需求：创建一个发光矿石方块 "glowing_ore"

**1. 行为包方块定义**
`behavior_pack/netease_blocks/mymod_glowing_ore.json`

```json
{
    "format_version": "1.19.20",
    "minecraft:block": {
        "description": {
            "identifier": "mymod:glowing_ore",
            "register_to_create_menu": true,
            "category": "Nature"
        },
        "components": {
            "minecraft:destructible_by_mining": {
                "seconds_to_destroy": 3.0
            },
            "minecraft:destructible_by_explosion": {
                "explosion_resistance": 15
            },
            "minecraft:light_emission": 7,
            "minecraft:light_dampening": 15,
            "minecraft:loot": "loot_tables/blocks/glowing_ore.json",
            "minecraft:map_color": "#66FFAA",
            "netease:tier": {
                "digger": "pickaxe",
                "level": 2,
                "destroy_special": true
            }
        }
    }
}
```

**2. 掉落物表**
`behavior_pack/loot_tables/blocks/glowing_ore.json`

```json
{
    "pools": [
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "mymod:glowing_gem",
                    "weight": 1,
                    "functions": [
                        {
                            "function": "set_count",
                            "count": {"min": 1, "max": 3}
                        }
                    ]
                }
            ]
        }
    ]
}
```

**3. 资源包方块渲染**
`resource_pack/blocks.json`

```json
{
    "format_version": [1, 1, 0],
    "mymod:glowing_ore": {
        "textures": "glowing_ore",
        "sound": "stone"
    }
}
```

**4. 贴图映射**
`resource_pack/textures/terrain_texture.json`

```json
{
    "resource_pack_name": "mymod",
    "texture_name": "atlas.terrain",
    "padding": 8,
    "num_mip_levels": 4,
    "texture_data": {
        "glowing_ore": {
            "textures": "textures/blocks/glowing_ore"
        }
    }
}
```

**5. 本地化**
`resource_pack/texts/zh_CN.lang`

```
tile.mymod:glowing_ore.name=发光矿石
```

---

## identifier 命名规范

1. **必须全小写** + 下划线，禁止大写字母
2. **格式**: `namespace:item_name` 或 `namespace:block_name`
3. **namespace**: 建议使用 mod 名称缩写，保持全局唯一
4. **name**: 描述性名称，使用下划线分隔单词

✅ 正确示例：
- `mymod:magic_wand`
- `ep_jxk:steel_ingot`
- `craft:reinforced_iron_block`

❌ 错误示例：
- `MyMod:MagicWand` (包含大写)
- `magic_wand` (缺少namespace)
- `mymod:magic-wand` (使用连字符)

---

## 常见问题排查

### JSON 解析错误
- 检查逗号：最后一个元素后不能有逗号
- 检查括号：`{}` 和 `[]` 必须正确配对
- 检查引号：所有字符串必须用双引号

### 物品/方块不显示
1. 检查 identifier 是否完全一致（行为包 = 资源包）
2. 检查 item_texture.json / terrain_texture.json 是否配置
3. 检查 manifest.json 的 dependencies 是否正确

### 贴图显示紫黑色
1. 确认贴图文件存在且路径正确
2. 确认 texture_data 中的 textures 路径不包含 `.png` 后缀
3. 检查贴图尺寸是否为 2 的幂次方 (16x16, 32x32, etc.)

### 配方不生效
1. 检查 identifier 是否与已有配方冲突
2. 检查 format_version 是否过旧
3. 确认 tags 正确（crafting_table / furnace 等）

---

## 使用规范总结

1. **文件命名**: `{namespace}_{id}.json`
2. **identifier**: 全小写，`namespace:name` 格式
3. **format_version**: 物品用 `1.10`，方块用 `1.19.20`，配方用 `1.12` 或 `1.20.10`
4. **NetEase 专用文件夹**: `netease_items_beh`, `netease_items_res`, `netease_blocks`, `netease_recipes`
5. **本地化**: 物品用 `item.{id}.name=`，方块用 `tile.{id}.name=`
