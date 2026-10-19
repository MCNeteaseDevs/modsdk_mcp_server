---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI-beta/%E6%9E%9A%E4%B8%BE%E5%80%BC/PxForceMode.html"
last_modified: "Thu, 24 Sep 2026 12:01:38 GMT"
synced_from: "NetEase developer official website"
---

#  PxForceMode

class in mod.common.minecraftEnum

- 描述

添加力的模式

```python
class PxForceMode(object):
    eFORCE = 0              # 力，单位为质量 × 距离 / 时间²
    eIMPULSE = 1            # 冲量，单位为质量 × 距离 / 时间
    eVELOCITY_CHANGE = 2    # 速度变化，单位为距离 / 时间，直接改变速度，与质量无关
    eACCELERATION = 3       # 加速度，单位为距离 / 时间²，直接施加加速度，与质量无关

```
