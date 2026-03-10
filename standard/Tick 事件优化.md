---
front: https://nie.res.netease.com/r/pic/20210728/5507b669-4c6f-4958-b5d0-b8556ab4cfb5.png
hard: 进阶
time: 20分钟
---

# Tick 事件优化指南

Tick 事件是网易版组件开发中最为核心的机制之一，绝大多数重要的游戏逻辑都需要在 Tick 事件中实现。

然而，由于事件系统的架构特性，多个逻辑模块集中在同一时间执行时，容易产生性能瓶颈。本文将分享几个经过实践验证的优化策略，帮助开发者提升游戏性能。

在后续示例中，我们将以 `ServerBlockEntityTickEvent` 事件为例进行说明。该事件会在方块实体配置并启用 tick 组件后，以每秒 20 次的频率执行。

## 一、设计原则

### 原则一：优先执行开销最小、访问频率最高的运算

由于 `ServerBlockEntityTickEvent` 事件会在所有启用了 tick 组件的方块实体上执行，通过在事件处理的最开始进行方块类型判断，可以有效避免不必要的性能开销：

```python
# -*- coding: utf-8 -*-

# ServerBlockEntityTickEvent 事件
def on_block_entity_tick(args):
    block_name = args["blockName"]        
    if block_name == "custom:some_tickable_block":
        # tick 逻辑
        pass
```

值得注意的是，网易版 API 中的 `serverApi.GetEngineCompFactory()` 等工厂方法在频繁调用时也会产生性能开销，在高频执行的 tick 事件中尤其需要注意这一点。

推荐的做法是将 tick 事件中常用的接口组件预先缓存为全局变量，避免重复创建：

```python
# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi

# 将部分组件缓存，以便后续高频访问使用
level_id = serverApi.GetLevelId()
factory = serverApi.GetEngineCompFactory()
block_info = factory.CreateBlockInfo(level_id)
be_comp = factory.CreateBlockEntityData(level_id)


# ServerBlockEntityTickEvent 事件
def on_block_entity_tick(args):
    block_name = args["blockName"]
    x = args["posX"]
    y = args["posY"]
    z = args["posZ"]
    dim_id = args["dimension"]

    if block_name == "custom:some_tickable_block":
        below_block = block_info.GetBlockNew((x, y - 1, z), dim_id)
        # 其他逻辑部分...
```

### 原则二：采用间隔执行机制，降低计算频率

并非所有游戏逻辑都需要在每个 tick 中执行。例如，在设计烤炉烤制食物的功能时，食物的烤制进度检查完全可以每隔 20 tick 或更长时间进行一次，而无需每 tick 都执行。

最简单的实现方式是引入全局计数变量，通过取余运算实现间隔执行：

```python
# -*- coding: utf-8 -*-

TICK_COUNT = 0


# OnScriptTickServer 事件
# 注意：OnScriptTickServer 每秒执行 30 次
# 而 ServerBlockEntityTickEvent 每秒执行 20 次
# 实际项目中需要考虑这一频率差异
def on_script_tick():
    # 每个 tick 计数变量递增
    global TICK_COUNT
    TICK_COUNT += 1


# ServerBlockEntityTickEvent 事件
def on_block_entity_tick(args):
    block_name = args["blockName"]

    if block_name == "custom:some_tickable_block" and TICK_COUNT % 20 == 0:
        # 每 20 tick 执行一次特定操作
        pass
```

## 二、Tick 计数的潜在问题与负载均衡策略

上述原则二中的 tick 计数方法虽然简单有效，但存在一个重要缺陷。

当玩家同时放置多个相同的可 tick 方块（如 20 个烤炉）时，由于它们共享同一个全局计数器 TICK_COUNT，所有方块的逻辑会在同一时刻集中触发，造成明显的间歇性卡顿现象。

解决这个问题的关键在于实现 tick 负载均衡，让每个方块的执行时机分散到不同的 tick 中。

### 加盐（Salt）机制

这是借鉴自密码学的概念。

通过在 tick 计数判断中加入特定的偏移值，使每个方块的执行时机产生差异：

```python
# -*- coding: utf-8 -*-

TICK_COUNT = 0


# OnScriptTickServer 事件
def on_script_tick():
    # 每 tick 时，此计数变量自增 1
    global TICK_COUNT
    TICK_COUNT += 1


# ServerBlockEntityTickEvent 事件
def on_block_entity_tick(args):
    block_name = args["blockName"]
    x = args["posX"]
    y = args["posY"]
    z = args["posZ"]
    dim_id = args["dimension"]

    if block_name == "custom:some_tickable_block":
        # 使用坐标和维度 ID 作为偏移量，确保不同位置的方块错开执行时机
        offset_tick_count = x + y + z + dim_id + TICK_COUNT
        # 每 20 tick 执行一次，但各方块的执行时机已经分散
        if offset_tick_count % 20 == 0:
            pass
```

通过这种方式，可以有效确保不同位置的方块避开在同一 tick 中执行操作。

### 逻辑模块化与分频执行

当可 tick 方块包含复杂的游戏逻辑，且这些逻辑可以划分为多个独立模块时，可以根据各模块的性能开销和实时性要求，采用不同的执行频率：

- 性能开销大、实时性要求低的模块：**低频执行**
- 性能开销小、实时性要求高的模块：**高频执行**

```python
# -*- coding: utf-8 -*-

TICK_COUNT = 0


# OnScriptTickServer 事件
def on_script_tick():
    # 每 tick 时，此计数变量自增 1
    global TICK_COUNT
    TICK_COUNT += 1


# ServerBlockEntityTickEvent 事件
def on_block_entity_tick(args):
    block_name = args["blockName"]
    x = args["posX"]
    y = args["posY"]
    z = args["posZ"]
    dim_id = args["dimension"]

    if block_name == "custom:some_tickable_block":
        # 使用坐标和维度 ID 作为偏移量，实现负载均衡
        offset_tick_count = x + y + z + dim_id + TICK_COUNT

        # 高频模块：每 5 tick 执行一次
        if offset_tick_count % 5 == 0:
            fast_logic(args)

        # 低频模块：每 100 tick 执行一次
        if offset_tick_count % 100 == 0:
            slow_logic(args)


def fast_logic(args):
    # 低开销、高频率执行的游戏逻辑
    pass


def slow_logic(args):
    # 高开销、低频率执行的游戏逻辑
    pass
```

### 使用质数间隔，避免执行时机冲突

当游戏逻辑足够复杂，需要拆分为多个不同执行频率的模块时

```python3
# 每 10 tick 执行一次特定操作
if offset_tick_count % 10 == 0:
    logic_a(args)

# 每 20 tick 执行一次特定操作
if offset_tick_count % 20 == 0:
    logic_b(args)
    
# 每 40 tick 执行一次特定操作
if offset_tick_count % 40 == 0:
    logic_c(args)

# 每 80 tick 执行一次特定操作
if offset_tick_count % 80 == 0:
    logic_d(args)
```

当游戏运行到 80 tick 的倍数时，会发现四个逻辑模块同时触发，导致性能峰值和卡顿现象。

使用质数作为执行间隔可以有效避免这一问题。将原有的间隔替换为质数 `11, 19, 41, 79`：

```python
# 每 11 tick 执行一次特定操作
if offset_tick_count % 11 == 0:
    logic_a(args)

# 每 19 tick 执行一次特定操作
if offset_tick_count % 19 == 0:
    logic_b(args)
    
# 每 41 tick 执行一次特定操作
if offset_tick_count % 41 == 0:
    logic_c(args)

# 每 79 tick 执行一次特定操作
if offset_tick_count % 79 == 0:
    logic_d(args)
```

利用质数的数学特性，这些逻辑模块在任何 tick 时刻都不会同时执行，从而实现了更均匀的性能负载分布。
