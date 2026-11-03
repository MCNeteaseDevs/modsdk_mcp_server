---
source_url: "https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/%E6%9E%9A%E4%B8%BE%E5%80%BC/PxEventMask.html"
last_modified: "Wed, 28 Oct 2026 10:10:37 GMT"
synced_from: "NetEase developer official website"
---

#  PxEventMask

class in mod.common.minecraftEnum

- 描述

碰撞事件枚举

```python
class PxEventMask(object):
    Null = 0x0          # 不需要碰撞事件。若不为Null，则Found或Lost必须有一个，Server或Client必须有一个
    Found = 0x1         # 需要接触开始事件
    Found_Detail = 0x2  # 接触开始事件需要附带碰撞点与法线信息。性能消耗较大。
    Lost = 0x4          # 需要接触结束事件
    Server = 0x8        # 需要服务器事件
    Client = 0x10       # 需要客户端事件

```
