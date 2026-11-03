---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/%E6%9E%9A%E4%B8%BE%E5%80%BC/PlayerExhauseRatioType.html"
last_modified: "Wed, 28 Oct 2026 10:10:37 GMT"
synced_from: "NetEase developer official website"
---

#  PlayerExhauseRatioType

class in mod.common.minecraftEnum

- 描述

饥饿度消耗倍率类型

```python
class PlayerExhauseRatioType(object):
	HEAL = 0         #通过饥饿值恢复生命
	JUMP = 1         #跳跃
	SPRINT_JUMP = 2  #疾跑跳跃
	MINE = 3         #破坏方块
	ATTACK = 4       #攻击
	GLOBAL = 9       #全局

```
