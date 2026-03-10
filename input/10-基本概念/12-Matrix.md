---
front:
hard: 入门
time: 分钟
---

# Matrix

- 描述

  矩阵（Matrix）是一个按照长方阵列排列的复数或实数集合，在计算机图形学中，常用作物体位置、运动等数学描述

## 构造函数

### Matrix(rowNum, colNum)

- 描述

  用于构造一个rowNum行,colNum列的零矩阵。

- 参数

  | 参数名 | 数据类型 | 说明                                  |
  | ------ | :------- | :------------------------------------ |
  | rowNum      | int    | 矩阵行数                         |
  | colNum      | int    |  矩阵列数 |

- 返回值

  | 数据类型   | 说明                       |
  | :--------- | :------------------------- |
  | Matrix | 返回Matrix(rowNum, colNum)的零矩阵 |

- 示例

```python
from common.utils.mcmath import Matrix
q = Matrix(3, 4)
```

## 静态方法

可以直接通过Matrix.MethodName()调用的静态方法，无需创建实例。

### CreateEye

- 描述

  创建一个单位矩阵

- 参数

  | 参数名 | 数据类型 | 说明     |
  | ------ | :------- | :------- |
  | rowNum/colNum      | int    | 矩阵行/列数                         |


- 返回值

  | 数据类型   | 说明                              |
  | :--------- | :-------------------------------- |
  | Matrix | 返回Matrix(num, num) 的单位矩阵|

- 示例

```python
from common.utils.mcmath import Matrix
newMatrix = Matrix.CreateEye(3)
```

### Create

- 描述

  通过数字列表创建一个矩阵

- 参数

  | 参数名 | 数据类型 | 说明     |
  | ------ | :------- | :------- |
  | data      | list(list(int/float))    | 矩阵数据源                        |


- 返回值

  | 数据类型   | 说明                              |
  | :--------- | :-------------------------------- |
  | Matrix | 返回Matrix(len(data), len(data[0])) ,数据为data的矩阵|

- 示例

```python
from common.utils.mcmath import Matrix
data = [[1,2,3], [4,5,6], [7,8,9]]
newMatrix = Matrix.Create(data)
```

### FromEulerXYZ

- 描述

  创建欧拉角对应的旋转矩阵，以xyz的旋转顺序应用

- 参数

  | 参数名 | 数据类型 | 说明     |
  | ------ | :------- | :------- |
  | Euler      | tuple(xAngle, yAngle, zAngle)    | 欧拉角                        |


- 返回值

  | 数据类型   | 说明                              |
  | :--------- | :-------------------------------- |
  | Matrix | 返回欧拉角对应的Matrix|

- 示例

```python
from common.utils.mcmath import Matrix
data = (30, 65, 20)
newMatrix = Matrix.FromEulerXYZ(data)
```

### ToEulerXYZ

- 描述

  返回矩阵对应的欧拉角

- 参数

  | 参数名 | 数据类型 | 说明     |
  | ------ | :------- | :------- |
  | mat      | Matrix   | 旋转矩阵                        |


- 返回值

  | 数据类型   | 说明                              |
  | :--------- | :-------------------------------- |
  | Euler | tuple(xAngle, yAngle, zAngle)|

- 示例

```python
from common.utils.mcmath import Matrix
data = [30, 65, 20]
newMatrix = Matrix.FromEulerXYZ(data)
newEular = Matrix.ToEulerXYZ(newMatrix)
```

### matrix4_multiply

- 描述

  返回两个4*4矩阵相乘后结果

- 参数

  | 参数名 | 数据类型 | 说明     |
  | ------ | :------- | :------- |
  | mat1      | Matrix   | 左边矩阵,大小为4*4                       |
  | mat2     | Matrix   | 右边矩阵,大小为4*4                       |


- 返回值

  | 数据类型   | 说明                              |
  | :--------- | :-------------------------------- |
  | Matrix      | 结果,大小为4*4                    |

- 示例

```python
from common.utils.mcmath import Matrix
q = Matrix.Create([[1,2,3,4], [3,4,5,6], [5,6,7,8], [7,8,9,10]])
p = Matrix.Create([[5,6,7,8], [7,8,9,10], [9,10,11,12], [11,12,13,14]])
newMatrix = Matrix.matrix4_multiply(q, p) # 与q*p效果相同，但是只能用于4*4矩阵，并且实现更底层，因此运算速度更快
```

## 成员方法

### Copy

- 描述

  返回矩阵的拷贝

- 返回值

  | 数据类型   | 说明                              |
  | :--------- | :-------------------------------- |
  | Matrix      | 结果                    |

- 示例

```python
from common.utils.mcmath import Matrix
q = Matrix.Create([[1,2], [3,4]])
print q.Copy()
```

### Eye

- 描述

  把矩阵设置成单位矩阵，要求该矩阵行列数相同，否则报错

- 示例

```python
from common.utils.mcmath import Matrix
q = Matrix.Create([[1,2], [3,4]])
q.Eye()
print q
```

### SetData

- 描述

  根据数据源设置矩阵数据，要求数据源行列大于等于矩阵，否则报错

- 参数

  | 参数名 | 数据类型 | 说明     |
  | ------ | :------- | :------- |
  | data    | list(list(int/float))   | 数据源                        |

- 示例

```python
from common.utils.mcmath import Matrix
q = Matrix.Create([[1,2], [3,4]])
q.SetData([[4,5], [6,7]])
print q
```

### Transpose

- 描述

  返回转置矩阵

- 返回值

  | 数据类型 | 说明                              |
  | :------- | :-------------------------------- |
  | Matrix    | 返回对应的转置矩阵 |

- 示例

```python
from common.utils.mcmath import Matrix
q = Matrix.Create([[1,2], [3,4]])
print q.Transpose()
```

### Inverse

- 描述

  返回逆矩阵，矩阵必须是个方阵，否则函数报错

- 返回值

  | 数据类型   | 说明                   |
  | :--------- | :--------------------- |
  | Matrix | 返回对应的逆矩阵 |

- 示例

```python
from common.utils.mcmath import Matrix
q = Matrix.Create([[1,2], [3,4]])
print q.Inverse()
```


### Decompose

- 描述

  对矩阵进行位姿分解，分解成位移向量 * 旋转四元数 * 缩放向量。请注意，并非所有矩阵都可以位姿分解，若矩阵存在非线性变换，强行进行位姿分解会导致信息丢失

- 返回值

  | 数据类型   | 说明                   |
  | :--------- | :--------------------- |
  | tuple(float, float, float), tuple(float, float, float, float),tuple(float, float, float) | 返回矩阵对应的位移向量 * 旋转四元数 * 缩放向量 |

- 示例

```python
from common.utils.mcmath import Matrix
q = Matrix.Create([[2,0,0,1], [0,3,0,1], [1,1,1,1], [1,1,1,1]])
print q.Decompose()
```

### ToQuaternion

- 描述

  返回矩阵的旋转四元数

- 返回值

  | 数据类型   | 说明                   |
  | :--------- | :--------------------- |
  | tuple(float, float, float, float)| 返回矩阵对应的旋转四元数 |

- 示例

```python
from common.utils.mcmath import Matrix
q = Matrix.Create([[2,0,0,1], [0,3,0,1], [1,1,1,1], [1,1,1,1]])
print q.ToQuaternion()
```


## 运算符

### operate +

- 描述

  矩阵加法，两个矩阵相加表示向量的平移、多项式运算等，满足交换律、结合律，且要求两个矩阵行列数量相同

### operate *

- 描述

  矩阵乘法，两个矩阵相乘表示线性映射、变换、多项式运算等，不满足交换律，但是满足结合律，且要求两个矩阵行列数量对应

### operate -

- 描述

  矩阵减法，两个矩阵相加表示向量的平移、多项式运算等，满足交换律、结合律，且要求两个矩阵行列数量相同


### operate `__str__`

- 描述

  用于输出矩阵的字符串形式，即`print(matrix)`

### operate row

- 描述

  返回矩阵的行数

### operate col

- 描述

  返回矩阵的列数

### operate [int, int]

- 描述

  返回矩阵的x行，y列的值,即`print mat[x,y]`

### operate [int, int]=

- 描述

  设置矩阵x行y列的值，即`mat[x,y] = 1`