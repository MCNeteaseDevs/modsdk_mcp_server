---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/%E6%9E%9A%E4%B8%BE%E5%80%BC/PermissionChangeCause.html"
last_modified: "Wed, 28 Oct 2026 10:10:37 GMT"
synced_from: "NetEase developer official website"
---

#  PermissionChangeCause

class in mod.common.minecraftEnum

- 描述

玩家权限变更原因枚举

```python
class PermissionChangeCause(object):
	ProgrammingInterfaceCaused = 1 	#  API变更
	CommandCaused = 2 				#  指令变更（包含玩家输入/命令方块）
	UserInterfaceCaused = 3			#  房主变更（也即房主在设置给他人变更）
	CocosInterfaceCaused = 4		#  cocos发起变更

```
