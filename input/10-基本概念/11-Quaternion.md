---
front:
hard: 入门
time: 分钟
---

# Quaternion

- 描述

  四元数用于表示旋转。

  它们结构紧凑，不受万向锁影响。

  它们基于复数，不容易理解。 您几乎不会有机会访问或修改单个四元数分量（x、y、z、w）

  您可以使用乘法对旋转进行旋转，或对向量进行旋转。

## 构造函数

### Quaternion(x, y, z, w)

- 描述

  用于构造一个旋转。

- 参数

  | 参数名 | 数据类型 | 说明                                  |
  | ------ | :------- | :------------------------------------ |
  | x      | float    | 四元数的x分量                         |
  | y      | float    | 四元数的y分量                         |
  | z      | float    | 四元数的z分量                         |
  | w      | float    | 四元数的 w 分量。请勿直接修改四元数。 |

- 返回值

  | 数据类型   | 说明                       |
  | :--------- | :------------------------- |
  | Quaternion | 返回Quaternion(x, y, z, w) |

- 示例

```python
from common.utils.mcmath import Quaternion
q = Quaternion(1, 2, 3, 4)
```



### Quaternion(vecTuple)

- 描述

  用于构造一个旋转。

- 参数

  | 参数名   | 数据类型                          | 说明               |
  | -------- | :-------------------------------- | :----------------- |
  | vecTuple | tuple(float, float, float, float) | 长度为4的tuple数组 |

- 返回值

  | 数据类型   | 说明                                                         |
  | :--------- | :----------------------------------------------------------- |
  | Quaternion | 返回Quaternion(vecTuple[0], vecTuple[1], vecTuple[2], vecTuple[3]) |

- 示例

```python
from common.utils.mcmath import Quaternion
a = (0, 0, 0, 1)
q = Quaternion(a)
```



## 静态方法

可以直接通过Quaternion.MethodName()调用的静态方法，无需创建实例。

### AngleAxis

- 描述

  创建一个围绕 `axis` 旋转 `angle` 度的旋转

- 参数

  | 参数名 | 数据类型 | 说明     |
  | ------ | :------- | :------- |
  | angle  | float    | 旋转角度 |
  | axis   | Vector3  | 旋转轴   |

- 返回值

  | 数据类型   | 说明                              |
  | :--------- | :-------------------------------- |
  | Quaternion | 围绕 `axis` 旋转 `angle` 度的旋转 |

- 示例

```python
from common.utils.mcmath import Quaternion
newQuaternion = Quaternion.AngleAxis(45, Vector3.Up()) # 创建一个围绕y轴旋转45°的旋转
```



### Euler

- 描述

  创建一个先围绕 Z 轴旋转 z 度、再围绕 X 轴旋转 x 度、最后围绕 Y 轴旋转 y 度的旋转（注意顺序）。注意：如果该欧拉旋转出现万向节锁，会导致四元数返回的EulerAngle异常

- 参数

  | 参数名 | 数据类型 | 说明              |
  | ------ | :------- | :---------------- |
  | x      | float    | 围绕x轴旋转的角度 |
  | y      | float    | 围绕y轴旋转的角度 |
  | z      | float    | 围绕z轴旋转的角度 |

- 返回值

  | 数据类型   | 说明                                                         |
  | :--------- | :----------------------------------------------------------- |
  | Quaternion | 先围绕 Z 轴旋转 z 度、再围绕 X 轴旋转 x 度、最后围绕 Y 轴旋转 y 度的旋转 |

- 示例

```python
from common.utils.mcmath import Quaternion
newQuaternion = Quaternion.Euler(30, 15, 45) # 创建一个先围绕z轴旋转45°、再围绕x轴旋转30°、最后围绕y轴旋转45°的旋转
```



### Dot

- 描述

  两个旋转的点积。

  点积是一个浮点值，它等于两个旋转对应分量之积求和。

- 参数

  | 参数名 | 数据类型   | 说明  |
  | ------ | :--------- | :---- |
  | a      | Quaternion | 旋转a |
  | b      | Quaternion | 旋转b |

- 返回值

  | 数据类型 | 说明           |
  | :------- | :------------- |
  | float    | 两个向量的点积 |

- 示例

```python
from common.utils.mcmath import Quaternion
a = Quaternion(1, 2, 3, 1)
b = Quaternion(0, 3, 1, 1)
c = Quaternion.Dot(a, b) # 1 * 0 + 2 * 3 + 3 * 1 + 1 * 1 = 10
```



### Cross

- 描述

  两个旋转格拉瑟曼积，Cross(a, b)表示旋转a后再旋转p的合成旋转。也可以直接通过a * b得到。

- 参数

  | 参数名 | 数据类型   | 说明  |
  | ------ | :--------- | :---- |
  | a      | Quaternion | 旋转a |
  | b      | Quaternion | 旋转b |

- 返回值

  | 数据类型   | 说明                 |
  | :--------- | :------------------- |
  | Quaternion | 两个向量的格拉斯曼积 |

- 示例

```python
from common.utils.mcmath import Quaternion
a = Quaternion(1, 2, 3, 1)
b = Quaternion(0, 3, 1, 1)
c = Quaternion.Cross(a, b)
```



### Conjugate

- 描述

  返回该旋转的共轭旋转，其w分量不变，其他分量分别取反

- 参数

  | 参数名 | 数据类型   | 说明  |
  | ------ | :--------- | :---- |
  | q      | Quaternion | 旋转q |

- 返回值

  | 数据类型   | 说明         |
  | :--------- | :----------- |
  | Quaternion | 返回共轭旋转 |

- 示例

```python
from common.utils.mcmath import Quaternion
a = Quaternion(1, 2, 3, 1)
b = Quaternion.Conjugate(a) # (-1, -2, -3, 1)
```



### Inverse

- 描述

  返回该旋转的逆旋转，如果旋转q的模长为1，那么q*q<sup>-1</sup>将会得到零旋转(0, 0, 0, 1)

- 参数

  | 参数名 | 数据类型   | 说明  |
  | ------ | :--------- | :---- |
  | q      | Quaternion | 旋转q |

- 返回值

  | 数据类型   | 说明              |
  | :--------- | :---------------- |
  | Quaternion | 返回旋转q的逆旋转 |

- 示例

```python
from common.utils.mcmath import Quaternion
a = Quaternion(1, 2, 3, 1)
a.Normalize() # 将a标准化
b = Quaternion.Inverse(a) # b为a的逆旋转
print a * b # 打印结果约为 (0, 0, 0, 1)， 可能因为精度问题出现极小的非零数
```



## 成员方法

### Length

- 描述

  返回该向量的长度。

  向量长度为 `(x*x+y*y+z*z)` 的平方根。

  如果只需要比较一些向量的大小， 则可以使用LengthSquared()函数比较它们的平方数（计算平方数更快）。

- 返回值

  | 数据类型 | 说明             |
  | :------- | :--------------- |
  | float    | 该向量的长度 |

- 示例

```python
from common.utils.mcmath import Quaternion
q = Quaternion(3, 4, 0, 0)
print q.Length() # 打印 5
```



### LengthSquared

- 描述

  返回该向量的长度的平方。

- 返回值

  | 数据类型 | 说明                 |
  | :------- | :------------------- |
  | float    | 该向量的长度的平方 |

- 示例

```python
from common.utils.mcmath import Quaternion
q = Quaternion(3, 4, 0, 0)
print q.LengthSquared() # 打印 25
```



### ToTuple

- 描述

  返回该向量的tuple形式(x, y, z, w)，便于玩家转换后作为其他事件的参数进行传递。

- 返回值

  | 数据类型 | 说明                              |
  | :------- | :-------------------------------- |
  | tuple    | 返回该向量的tuple形式(x, y, z, w) |

- 示例

```python
from common.utils.mcmath import Quaternion
q = Quaternion(0, 0, 0, 1)
print q.ToTuple() # 打印 (0, 0, 0, 1)
```



### Normalized

- 描述

  返回该四元数，并且量值为 1。

  进行归一化时，四元数方向保持不变，但其量值为 1.0。

  请注意，当前四元数保持不变，返回一个新的归一化四元数。如果 要归一化原始四元数，请改用Normalize方法。

  如果四元数太小而无法归一化，则会返回(0, 0, 0, 1)，表示零旋转。

- 返回值

  | 数据类型   | 说明                   |
  | :--------- | :--------------------- |
  | Quaternion | 该向量标准化后的四元数 |

- 示例

```python
from common.utils.mcmath import Quaternion
q = Quaternion(3, 4, 0, 0)
print q.Normalized() # 打印结果(0.6, 0.8, 0, 0)
print q # 打印结果(3, 4, 0, 0)，q并没有发生变化
```



### Normalize

- 描述

  使该向量标准化，向量方向保持不变，但其长度变为 1.0。

  请注意，该函数无返回值，仅改变当前向量，如果要返回当前向量的标准化值且不改变该向量，请使用Normalized函数。

  如果向量太小而无法标准化，则设置为零向量。

- 示例

```python
from common.utils.mcmath import Quaternion
q = Quaternion(3, 4, 0, 0)
q.Normalize()
print q # 打印结果(0.6, 0.8, 0, 0)，q被标准化
```



### EulerAngles

- 描述

  返回围绕 z 轴旋转 euler.z 度、围绕 x 轴旋转 euler.x 度、围绕 y 轴旋转 euler.y 度（按此顺序）的旋转。可以从四元数中读取欧拉角。注意：如果该欧拉旋转出现万向节锁，会导致四元数返回的EulerAngle异常

- 示例

```python
from common.utils.mcmath import Quaternion
q = Quaternion.Euler(30, 15, 45) # 创建一个先围绕z轴旋转45°、再围绕x轴旋转30°、最后围绕y轴旋转45°的旋转
print q.EulerAngles() # 打印结果(30, 15, 45)
```



## 运算符

### operate *

- 描述

  旋转乘法，两个旋转相乘表示先旋转运算符左侧的旋转，再旋转运算符右侧的旋转。等价于Quaternion.Cross(a, b)。不满足乘法交换律，即`a*b != b*a`



### operate ==

- 描述

  判断两个旋转是否相等，只有当各分量均相等时返回True

