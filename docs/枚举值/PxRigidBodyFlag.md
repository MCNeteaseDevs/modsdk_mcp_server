---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/%E6%9E%9A%E4%B8%BE%E5%80%BC/PxRigidBodyFlag.html"
last_modified: "Wed, 28 Oct 2026 10:10:37 GMT"
synced_from: "NetEase developer official website"
---

#  PxRigidBodyFlag

class in mod.common.minecraftEnum

- 描述

自定义刚体行为枚举

```python
class PxRigidBodyFlag(object):
    eKINEMATIC = (1 << 0)   # 设置刚体的运动学模式。运动学刚体不受力的影响，使用setKinematicTarget控制移动

```
