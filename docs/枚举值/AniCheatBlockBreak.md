---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/%E6%9E%9A%E4%B8%BE%E5%80%BC/AniCheatBlockBreak.html"
last_modified: "Wed, 28 Oct 2026 10:10:37 GMT"
synced_from: "NetEase developer official website"
---

#  AniCheatBlockBreak

class in mod.common.minecraftEnum

- 描述

反作弊配置枚举值，破坏方块相关

```python
class AniCheatBlockBreak(object):
	OpenSwitch = "server-authoritative-block-breaking"		# 是否开启破坏方块反作弊检查
	PickRangeScalar = "server-authoritative-block-breaking-pick-range-scalar"	# 破坏方块距离检查参数，最小值为1.0，设置小于1.0无效

```
