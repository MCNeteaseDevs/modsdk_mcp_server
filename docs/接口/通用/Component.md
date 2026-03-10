---
sidebarDepth: 1
---
# Component

## CreateComponent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    给实体创建服务端组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.CreateComponent(entityId, "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，与GetComponent类似，如果已经创建会自动直接Get
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    给实体创建客户端组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，与GetComponent类似，如果已经创建会自动直接Get
```



## DestroyComponent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    删除实体的服务端组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
# entityId 根据游戏实际Id获取，这里'-12345678910'只是随便写的
comp = serverApi.DestroyComponent('-12345678910', "Minecraft", "item")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    删除实体的客户端组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    无

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.DestroyComponent(clientApi.GetLocalPlayerId(), "Minecraft", "item")
```



## GetComponent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    获取实体的服务端组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例或者None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetComponent(entityId, "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，如果没有创建过会返回None
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    获取实体的客户端组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例或者None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetComponent(clientApi.GetLocalPlayerId(), "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，如果没有创建过会返回None
```



## GetComponentCls

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    用于获取服务器component基类。实现新的component时，需要继承该接口返回的类

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | type(BaseComponent) | 组件基类 |

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerComponentCls = serverApi.GetComponentCls()
# Component要继承于基类才能生效
class ShootComponentServer(ServerComponentCls):
    def __init__(self, entityId):
        ServerComponentCls.__init__(self, entityId)
        # 这里设置了一个开关来开关更新射击
        self.mShoot = False
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    用于获取客户端component基类。实现新的component时，需要继承该接口返回的类

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | type(BaseComponent) | 组件基类 |

- 示例

```python
import mod.client.extraClientApi as clientApi
ClientComponentCls = clientApi.GetComponentCls()
# Component要继承于基类才能生效
class ShootComponentClient(ClientComponentCls):
    def __init__(self, entityId):
        ClientComponentCls.__init__(self, entityId)
        # 这里设置了一个开关来开关更新射击
        self.mShoot = False
```



## GetEngineCompFactory

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    获取引擎组件的工厂，通过工厂可以创建服务端的引擎组件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EngineCompFactoryServer | 服务端引擎组件工厂 |

- 示例

```python
import mod.server.extraServerApi as serverApi
compFactory = serverApi.GetEngineCompFactory()
gameComp = compFactory.CreateGame(serverApi.GetLevelId())
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    获取引擎组件的工厂，通过工厂可以创建客户端的引擎组件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EngineCompFactoryClient | 客户端引擎组件工厂 |

- 示例

```python
import mod.client.extraClientApi as clientApi
compFactory = clientApi.GetEngineCompFactory()
gameComp = compFactory.CreateGame(clientApi.GetLevelId())
```



## RegisterComponent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    用于将组件注册到引擎中

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | nameSpace | str | 命名空间，建议为mod名字 |
    | name | str | 组件名称 |
    | clsPath | str | 组件类路径，路径从脚本的第一层开始算起 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 注册成功与否 |

- 示例

```python
import mod.server.extraServerApi as serverApi
@Mod.InitServer()
def TutorialServerInit(self):
    # 注册一个自定义的服务端Component
    serverApi.RegisterComponent("TutorialMod", "ServerShoot", "tutorialScripts.modServer.serverComponent.shootComponentServer.ShootComponentServer")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    用于将组件注册到引擎中

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | nameSpace | str | 命名空间，建议为mod名字 |
    | name | str | 组件名称 |
    | clsPath | str | 组件类路径，路径从脚本的第一层开始算起 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 注册成功与否 |

- 示例

```python
import mod.client.extraClientApi as clientApi
@Mod.InitClient()
def TutorialClientInit(self):
    # 注册一个自定义的客户端Component
    clientApi.RegisterComponent("TutorialMod", "ClientShoot", "tutorialScripts.modClient.clientComponent.shootComponentClient.ShootComponentClient")
```



