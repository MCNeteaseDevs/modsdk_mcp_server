---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/%E6%9E%9A%E4%B8%BE%E5%80%BC/GameType.html"
last_modified: "Wed, 28 Oct 2026 10:10:37 GMT"
synced_from: "NetEase developer official website"
---

#  GameType

class in mod.common.minecraftEnum

- 描述

描述游戏类型的枚举值

```python
class GameType(object):
	Undefined = -1            # 未定义类型
	Survival = 0              # 生存模式
	Creative = 1              # 创造模式
	Adventure = 2             # 冒险模式
	Spectator = 6             # 旁观模式
	Default = Survival        # 默认类型，默认为生存模式

```
