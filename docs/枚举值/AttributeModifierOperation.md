---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI-beta/%E6%9E%9A%E4%B8%BE%E5%80%BC/AttributeModifierOperation.html"
last_modified: "Thu, 24 Sep 2026 12:01:38 GMT"
synced_from: "NetEase developer official website"
---

#  AttributeModifierOperation

class in mod.common.minecraftEnum

- 描述

属性修饰符操作类型枚举

```python
class AttributeModifierOperation(object):
	OperationAddition = 0		# 加法运算
	OperationMultiplyBase = 1	# 基础乘法运算
	OperationMultiplyTotal = 2	# 总值乘法运算
	OperationCap = 3			# 上限运算
	TotalOperations = 4			# 操作类型总数
	OperationInvalid = 5		# 无效操作类型

```
