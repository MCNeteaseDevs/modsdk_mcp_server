---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI-beta/%E6%9E%9A%E4%B8%BE%E5%80%BC/RayFilterType.html"
last_modified: "Thu, 24 Sep 2026 12:01:38 GMT"
synced_from: "NetEase developer official website"
---

#  RayFilterType

class in mod.common.minecraftEnum

- 描述

射线检测类型

```python
class RayFilterType(object):
	OnlyEntities = 1 << 0 #仅检测实体
	OnlyBlocks = 1 << 1 #仅检测方块
	BothEntitiesAndBlock = OnlyEntities | OnlyBlocks #检测方块和实体

```
