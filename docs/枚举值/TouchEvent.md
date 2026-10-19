---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI-beta/%E6%9E%9A%E4%B8%BE%E5%80%BC/TouchEvent.html"
last_modified: "Thu, 24 Sep 2026 12:01:38 GMT"
synced_from: "NetEase developer official website"
---

#  TouchEvent

class in mod.common.minecraftEnum

- 描述

触摸回调事件枚举值

```python
class TouchEvent:
	TouchUp = 0  		# 按钮抬起时触发回调
	TouchDown = 1  		# 按钮按下时触发回调
	TouchCancel = 3  	# 按钮按下后移出按钮范围抬起鼠标时触发回调
	TouchMove = 4  		# 按钮按下后移动鼠标触发回调
	TouchMoveIn = 5  	# 鼠标按下后移入按钮触发回调
	TouchMoveOut = 6  	# 鼠标按下后移出按钮触发回调
	TouchScreenExit = 7 # 按钮所在画布退出时若鼠标仍未抬起时触发

```
