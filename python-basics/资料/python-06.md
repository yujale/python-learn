## 1、公共方法

- `+`
  - 加法运算适用于所有的基础数据类型（int  float  bool）
  - 加法运算所有两侧要是同种数据类型
  - 加法运算再容器类型中是拼接的意思，不是相加计算值

```python
# +法运算,都可以用于哪些数据类型之间
# int float  bool 肯定可以用于加法运算,不再赘述
print(1 + 12.3)  # 13.3

# str 可以相加么? 可以
str1 = 'hello'
str2 = ' python'
# 字符串相加,可以快速将字符串进行拼接
print(str1 + str2)
# 相加过后,str1 和str2 没有发生变化,可以推断+法运算产生了新的数据,源数据不变化
print(str1, str2, sep='\n')

# list 可以相加么? 可以
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# 列表相加可以将列表进行拼接,效果类似于extend
print(list1 + list2)  # [1, 2, 3, 4, 5, 6]
# list相加后,原数据不发生变化,将产生一个新的数据
print(list1)  # [1, 2, 3]
print(list2)  # [4, 5, 6]

# tuple 可以相加么?  可以
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)  # (1, 2, 3, 4, 5, 6)
# 由于元组内部元素不能修改,索引相加肯定没有对源数据产生影响,而是生成了新的数据

# set
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# # set之间不能进行加法运算
# print(set1 + set2)

# dict
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# dict 类型间不能进行加法运算
# dict1 = {'name': '小明'}
# dict2 = {'age':18}
# print(dict1 + dict2)

# 结论: 基础数据类型都可以进行加法运算,容器类型间只有列表,元组,字符串可以进行加法运算


# 不同容器类型间可以相加么?
list1 = [1,2,3]
tuple1 = (1,2,3)
set1 = {1,2,3}
dict1 = {'name': 'xiaoming'}

# TypeError: can only concatenate list (not "tuple") to list
# print(list1 + tuple1)
# TypeError: can only concatenate list (not "set") to list
# print(list1 + set1)
# TypeError: can only concatenate tuple (not "set") to tuple
print(tuple1 + set1)

# 结论,数据类型布偶无法进行加法运算(特指容器类型之间)
```

- `*`
  - 基础数据类型（int  float  bool）都可以进行乘法运算
  - 容器类型只能和int类型数据进行乘法运算
  - 容器类型进行乘法运算，就是将容器复制指定次数，并进行拼接

```python
# * 效果是设么?
# * 什么容器类型可以使用*

# 基础数据类型  int  float  bool都可以使用*法运算
print(12.1 * 2)

# 容器类型的乘法运算
# 格式: 容器类型 * int类型数据
# 乘法运算的 效果,就是讲容器类型复制指定次数,并拼接到一起

# list 可以使用*法运算么?  可以
list1 = [1, 2, 3]
# 将list1 复制3次并进行拼接
print(list1 * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# 使用list 类型乘以float类型可以实现么?
# TypeError: can't multiply sequence by non-int of type 'float'
# 乘法运算不能让容器与非int类型相乘
# print(list1 * 1.3)
# list 能乘以负数么?  可以相乘,但是结果为空列表
print(list1 * -3)  # []
# 可以与0 相乘,结果为空列表
print(list1 * 0)  # []

# tuple 可以使用*法运算么? 可以
tuple1 = (1, 2, 3, 4)
print(tuple1 * 2)  # (1, 2, 3, 4, 1, 2, 3, 4)
# tuple 只能与int类型相乘


# set可以使用 * 法运算么?  不可以
set1 = {1, 2, 3}
# TypeError: unsupported operand type(s) for *: 'set' and 'int'
# 集合类型数据不能做乘法运算
# print(set1 * 3)

# dict 能够使用 * 法运算么?  不可以
dict1 = {'name': 'jack'}
# TypeError: unsupported operand type(s) for *: 'dict' and 'int'
# 字典不能做乘法运算
# print(dict1 * 3)

# 乘号左右两侧的数据可以互换位置么?  可以
print(3 * list1)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

- `in`和`not in`
  - 判断元素是否在数据序列当中
  - 字符串，列表，元组，集合 ，字典都可以使用

```python
# in 判断元素是否存在于容器当中
list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
set1 = {1, 2, 3}

print(3 in list1)  # True
print(3 in tuple1)  # True
print(3 in set1)  # True
# 如果要判断是否在set当中,要注意被判断的元素必须可以保存在set当中,如果是列表,字典,集合,则不能判断
# print([1, 2] in list1)  # False  可以判断,引为[1,2] 可以保存在list1当中
# print([1, 2] in set1)  # TypeError: unhashable type: 'list' 不能判断,因为[1,2]不能保存到set1当中


# str类型可以使用in么? 可以
str1 = '123'
# TypeError: 'in <string>' requires string as left operand, not int
# 字符串判断时,左侧的元素只能是字符串类型,否则报错
# print(1 in str1)
print('1' in str1)  # True

# dict 是否可以使用in???
dict1 = {'name': 123}
# dict使用in判断的是当前元素是否是dict中存在的键
print(123 in dict1)  # False
print('name' in dict1)  # True

# 如果使用此方法则不能判断字典  列表 集合
# TypeError: unhashable type: 'list'
# print([1,2] in dict1)

# not in  : 所有用法和in相同,只是取反而已

# 结论:
# 1.使用in 和not in  被判断的元素在关键字左侧, 数据序列在关键字右侧
# 2.如果想要判断该元素是否在容器内,该元素必须能保存到容器内,比如集合不能保存列表,字典,集合 所以就不能判断其类型的元素是否在集合内
# 3.字典判断的是元素是否在keys内,也就是是否是其中的键
```

- 切片
  - 通过切片按照规则获取数据序列中的一部分元素
  - tuple list str 可以使用切片
  - dict  set 不可以使用切片

```python
# 切片:通过切片方法可以按照一定规则截取容器的一部分数据

# str切片
str1 = 'abcde'
# 格式:[起始位置:终止位置:步长]
# 不会修改原有字符串,而是产生了一个新的字符串
print(str1[2:])  # cde

# list可以切片么?
list1 = [1, 2, 3, 4]
# list切片方式方法和str完全相同
# list切片后不会在原有数据上进行修改,而是产生了一个新的列表
print(list1[1:3:1])  # [2, 3]
print(list1)

# tuple 可以切片么?
tuple1 = (1, 2, 3, 4)
# tuple1切片方式方法和str完全相同
# 切片后不会在原有数据上进行修改,而是产生了一个新的列表
print(tuple1[1:3:1])  # (2, 3)
print(tuple1)

# dict可以切片么?  肯定不行,因为不能使用索引获取数据
# set 可以切片么?  肯定不行,因为不能使用索引获取数据

# 结论:
# 1.list str tuple 可以使用切片,格式是:[起始位置:终止位置:步长],三者使用方式完全一致
# 2.所有的切片都不会在原有的数据上进行修改,而是产生一个新的数据序列
# 3.集合和字典无法切片,因为不能使用索引获取数据元素
```

## 2、公共函数

- len ：获取容器内元素个数
- del：删除容器内元素
- max ：获取容器内数据的最大值
- min ： 获取容器内元素的最小值
- enumerate ： 获取容器内元素时可以携带序号
- range：根据一定规则获取整数序列

```python
# len  获取容器类型的元素个数,  或者说获取容器的长度
str1 = '123'
list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
set1 = {1, 2, 3}
dict1 = {'name': 123, 'age': 18}
# 使用len可以获取list  str  tuple set中的元素个数
print(len(str1))
print(len(list1))
print(len(tuple1))
print(len(set1))
# 使用len可以获取dict中的键值对的个数
print(len(dict1))

# len() 可以写成  容器.__len__()
print(list1.__len__())

# del
# 删除容器内指定的元素
# list
# del list1[0]
# print(list1)

# tuple
# del tuple1[0]
# TypeError: 'tuple' object doesn't support item deletion
# 元组内元素不能被删除
# print(tuple1)

# set
# for i in set1:
#     del i

# dict
# del dict1['name']
# del 在dict中删除的是键值对
print(dict1)

# str
# TypeError: 'str' object doesn't support item deletion
# str 不能够使用del 删除内部元素
# 注意 :str内部的元素也是不可修改的,类似于元组
# del str1[0]
# print(str1)

# 结论:
# 1.列表,字典可以使用del删除内部元素,但是,列表中是删除元素,字典中是删除键值对
# 2.使用del 没法循环遍历删除set中的元素,因为引用机制问题
# 3.str  tuple内部的元素都不可更改所以不能使用del删除元素


# max  min
# list tuple set str可以使用max  min获取容器内的最大最小值
print(max(list1))
print(max(tuple1))
print(max(set1))
print(max(str1))
# dict是使用max和min获取键的最大最小值
print(max(dict1))

# enumerate  枚举函数:获取容器内数据时添加序号(默认序号从0开始可以作为索引使用)

list2 = [1, 2, 3, 4, 5, 6, 7, 8]

for i in list2:
    print(i)

# 可不可以同时获取元素的值和元素的索引?  可以 使用enumerate

# for i in enumerate(list2):
#     # 直接打印,获取的是以(索引,值)组成的元组
#     print(i)

# list
for index, value in enumerate(list2):
    print(index, value, sep=' : ')

# tuple
for index, value in enumerate(tuple1):
    print(index, value, sep=' : ')

# set
for index, value in enumerate(set1):
    print(index, value, sep=' : ')

# str
for index, value in enumerate(str1):
    print(index, value, sep=' : ')

# dict  
for index, value in enumerate(dict1):
    print(index, value, sep=' : ')
    
# 结论:所有的容器和课迭代类型都可以使用enumerate,并且产生序号,这个序号并不是索引值,而是在生成序号时默认从0开始,碰巧可以在list,str,tuple中当做索引使用
```

## 3、推导式

- 列表推导式
  - 格式：[要插入的值  for 临时变量 in 数据序列   if  条件]
- 集合推导式
  - 格式：{要插入的值 for 临时变量 in 数据序列 if 条件}
- 字典推导式
  - 格式：{要插入的键：要插入的值 for 临时变量 in 数据序列 if 条件 }
- 没有元组推导式和字符串推导式，因为其内部元素无法被修改

```python
# 推导式:通过一定的规则快速构建数据序列
# 列表推导式
# 获取从0 到9的数据序列
# while
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# for
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 推导式
# 格式: [要插入列表的表达式 for 临时变量 in 数据序列]
list3 = [i for i in range(10)]
print(list3)

# 使用推导式,创建一个从1-100的偶数的数据序列

# for
list4 = []
for i in range(1, 101):
    if i % 2 == 0:
        list4.append(i)

print(list4)

# 推导式
# 格式: [要插入列表的表达式 for 临时变量 in 数据序列 if  条件]
list5 = [i for i in range(1, 101) if i % 2 == 0]
print(list5)

# 练习:
# 用推导式进行九九乘法表的生成,将所有的算式放入列表中
list6 = []
for i in range(1, 10):
    for j in range(1, i + 1):
        list6.append(f'{j} * {i} = {j * i}')

print(list6)

# 改写为推导式:
list7 = [f'{j} * {i} = {j * i}' for i in range(1, 10) for j in range(1, i + 1)]
print(list7)

# 集合推导式
# 集合推导式和列表推导式完全一致,只不过使用推导式时,外层用{}包裹,并且在序列中会去重
set1 = {i for i in range(10)}
print(set1)

# 获取从1-10 的偶数集合
set2 = {i for i in range(1, 11) if i % 2 == 0}
print(set2)

# 字典推导式
keys = ['name', 'age', 'gender', 'id']
values = ['xiaoming', 18, '女', '001']

# 需求想将key 和value以一对应,形成一个字典
dict1 = {}
for i in range(len(keys)):
    dict1[keys[i]] = values[i]

print(dict1)

# 改写推导式
# 格式:{要插入的键:要插入的值  for 临时变量 in 数据序列  if 条件}
dict2 = {keys[i]: values[i] for i in range(len(keys))}
print(dict2)

# 所有的推导式都可以使用for循环改写,所以我们进行推导式的时候先不要急于求成,多改写几次就不用再改写了直接可以写出推导式
```

## 4、函数介绍

- 函数的定义：

  - def 函数名（参数）：

    ​		函数体

    ​		return 返回值

- 函数的调用：函数名（参数）

```python
# 函数: 将特定的功能所对应的代码片段进行打包,封存在一个函数内,如果我们想要重复使用该功能,就直接调用函数即可
# 函数的作用: 提高代码复用率,提高开发效率,易于维护

'''
函数定义的格式:
def 函数名(参数1, 参数2,参数3....):
    函数体
    return 返回值

函数调用的格式:
函数名(参数1,参数2,参数3.....)

# 函数名:绝大多数函数都有函数名,没有函数名的函数不能被复用
# 参数:为了让函数灵活性更高,更容易被复用,会动态对函数进行传值,传递的值可以在函数体内部进行使用
# 函数体: 特定功能的代码,写在函数内部,调用函数时可全部执行
# 返回值: 写在return之后,将函数内部计算或运行得到的数据传递到函数体外部
'''

# 定义的时候可以不传参,如果不传调用的时候也不用传参
def run():
    print('我跑的老快了,没人追的上我,钱包在我手里')
    print('我跑的老快了,没人追的上我,手机在我手里')
    print('我跑的老快了,没人追的上我,女朋友在我手里')

# 调用时可以将函数内的代码全部执行一遍
run()
run()
```

- 函数的调用顺序：从上到下依次执行，先键函数名保存到函数列表中，调用的时候去类表中查询，如果存在则调用其中的代码，如果不存在则报错

```python
# NameError: name 'sing' is not defined
# 函数需要先定义后调用否则会报错
# sing()
# 定义一个唱歌方法
def sing():
    print('我再唱青藏高原')
# 定义一个跳舞方法
def dance():
    print('我再跳广场舞')

sing()
dance()

# 执行顺序: 先讲所有函数的函数名执行一遍将其储存到缓存中的方法列表中,后续调用函数时去方法列表中查询,如果函数名存在,则调用函数内部的代码,如果函数名不存在将报错
```

## 5、函数参数

- 函数的参数可以增加代码的灵活性
  - 在定义时传入的参数是形参，只能在函数体内部使用
  - 在调用的时候传入的参数是实参，可以传入到函数体内部被形参接收

```Python
# 定义一个eat方法,通过传入不同的参数,可以输出不同的生物吃不同的食物


def eat_cat():
    print('猫吃鱼')

def eat_dog():
    print('狗吃肉')

def eat_person():
    print('人吃藕')

# 上述函数定义方法不太方便,因为如果有更多的生物去吃不同的东西,就要重复书写函数不利于函数的复用

# 改进 >> 传参
# 通过传入参数,可以控制函数体内部的执行结果发生变化,让函数更加灵活
def eat(who, food):  # 在定义时传入的参数叫做形参,只能在函数体内部使用
    print(f'{who}吃{food}')

# 在调用的时候传入的参数叫做实参,会传入到函数内部被形参接收
eat('猫', '🐟')
eat('狗', '肉')
eat('人', '藕')

# TypeError: eat() missing 1 required positional argument: 'food'
# 进行传值时需要保证传参数量满足要求,否则会报错
# eat('人')
```

## 6、函数返回值

- 1.返回值是将函数内计算或运行的结果返回到函数外部调用位置,参与计算或运行
- 2.函数可以不写返回值或者只写一个return不写返回值内容,都会默认返回一个None
- 3.return后将会立即跳出函数,如果在retrun后仍有代码,则不会被执行
- 4.return只能返回一个元素,如果想返回多个元素需要使用容器类型

```python
# 返回值:将函数体内部运行或计算得到的数据传递到函数体外部

# def sum(a, b):
#     print(a + b)
#
#
# sum(1, 2)


# 思考?如果我们想在函数体外部使用这个结果进行二次运算我应该怎么做?
# NameError: name 'a' is not defined  a, b 是形参,只能在函数体内部使用
# print(a + b)

# 如果我们想将数据传递出来可以使用return
def sum1(a, b):
    return a + b


print(sum1(1, 3))  # 当函数执行完毕,函数调用位置就替换为函数的返回值
# 返回的数据可以参与计算
print(sum1(1, 3) + 12)
# 注意:返回值内容不会自动打印到控制台,将数据返回后如果想要查看数据需要手动打印或者debug调试


# 如果没有return 那么就没有返回值么?
list1 = [1, 2]
# 因为此处,append方法,没有返回值,默认返回None
print(list1.append(3))  # None


def eat():
    print('猫吃鱼,狗吃肉,奥特曼吃小怪兽')


# 如果没有书写返回值,则返回值为None
print(eat())  # None


# 如果只写了return 没有写返回值内容会怎么样?  None

def sum1(a, b):
    print(a + b)
    return


print(sum1(1, 2))  # None


# return 执行后会跳出函数,return之后的所有代码将不会继续执行
# 在函数中可以有多个return 但是只能执行一个
def function():
    print('hello python')
    return
    return
    # 同一分支中,在return之后的所有代码不会被执行
    print('hello bigdata')


function()


# 返回值只能是一个么?  可以返回多个返回值么?
# 返回值只能是一个元素,如果要返回多个值只能通过容器类型进行打包
def function1():
    return 1, 2, 3, 4
print(function1())  # (1, 2, 3, 4)

# 结论:
'''
1.返回值是将函数内计算或运行的结果返回到函数外部调用位置,参与计算或运行
2.函数可以不写返回值或者只写一个return不写返回值内容,都会默认返回一个None
3.return后将会立即跳出函数,如果在retrun后仍有代码,则不会被执行
4.return只能返回一个元素,如果想返回多个元素需要使用容器类型
'''
```

## 7、函数的嵌套

- 在一个函数体内部嵌套了另一个函数的调用

```python
# 函数的嵌套,就是在一个函数的内部嵌套了另一个函数的调用

def function2():
    print('我是func2-----')
    function1()
    print('我是func2-----')

def function1():
    print('func1执行开始')
    print('func1执行结束')


# def function2():
#     print('我是func2-----')
#     function1()
#     print('我是func2-----')

function2()

# 执行顺序,只要函数在调用之前被定义即可,定义函数的顺序不做规定
```

## 8、局部变量和全局变量

- 局部变量就是在函数体内部进行定义函数体外部无法调用的变量
- 全局变量就是在函数体外部，一般在文件顶格处书写，函数体内外都可以使用的变量
- if 和for结构中的控制语句中定义的变量都是全局变量

```python
# 全局变量就是在函数体外部书写的一般要在文件内顶格书写,在函数体内部外部都可以调用的变量
a = 1
b = 2


def sum1():
    # 函数体内部可以使用
    print(a + b)


sum1()
# 函数体外部也可以使用
print(a)
print(b)

# for 循环中,  if 分支中创建的变量是全局变量还是局部变量呢? 全局变量
# for i in range(10):
#     pass
#
# print(i)
#
# if True:
#     c = 1
# print(c)
```

## 9、gloal

- global能声明我们当前使用的变量是全局变量
- LEGB原则
  - L：在函数体内部查找
  - E：在外层函数中查找
  - G：在全局变量中查找
  - B：在内置变量中查找

```python
# global  全局  :作用就是声明我要使用的这个变量是全局变量

# 如果要在函数体内修改全局变量,就要使用global
a = 100

# 此处,使用a=1相当于再函数体内定义了一个局部变量,并没有修改全局变量的值
# def func1():
#     a = 1
# 如果想要在函数体内修改全局变量就要使用global
# def func1():
#     global a
#     a = 1
#
# func1()
# print(a)

# 扩展:  在Python中所有的变量查询遵循legb原则
# 调用变量时的查询顺序
'''
L:local :首先在函数体内部查询
E:edge :在外部函数中查询
g:global:在全局变量中查询
b:built-in:在系统内置变量中查询
'''
def func1():
    # L:我们再调用变量时,先在函数体内部查找
    a = 1
    print(a)
func1()

def out_func():
    # E: 如果当前函数中没有此变量,我们将在外部函数中查找
    a = 2
    def in_func():
        print(a)
    in_func()

out_func()

def func2():
    # 如果函数体内部和外部函数中都没有该变量,则去全局变量中查找
    print(a)

func2()

# 当这个函数在函数体内部,外部函数中,全局变量中都不存在时, 则去内置变量中查找
print(__name__) # __main__


def func3():
    # a = a + 10
    # 首先用a + 10 进行计算,根据legb原则先从函数体内部查找,查找后发现a 在函数体内部定义,但是在调用时未定义则报错
    # a += 10
    # print(a)
    a = 1

def func4():
    # SyntaxError: name 'a' is assigned to before global declaration
    # 如果要对全局变量进行修改,则先对变量进行global修饰,在修改,否则报错
    a = 15
    # global a
func4()
print(a)

# 能否在函数体内部创建全局变量  可以 只要用global修饰即可
def func5():
    global num1
    num1 = 105

func5()
print(num1)
```

## 10、函数参数进阶

- 位置参数：直接书写参数名，在传值时顺序传值，调用时既不能多传参，也不能少传参（形参）
- 关键字参数：使用”参数名 = 值“的形式进行传参（实参）
  - 可以不按顺序赋值
  - 必须在顺序赋值之后完成赋值
- 缺省参数：在定义函数时，给参数一个默认值，如果调用时，不给其传参，则使用默认值，如果传参，则使用传入的值

```python
# 位置参数:按照位置顺序进行赋值的参数(形参)

def func(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# TypeError: func() missing 1 required positional argument: 'd'
# 如果有位置参数没有被赋值,则报错
# func(1, 2, 3)

# TypeError: func() takes 4 positional arguments but 5 were given
# 如果位置参数传参过多也会报错
# func(1, 2, 3, 4, 5)
# 结论:位置参数在使用时需要保证每个参数都被赋值,且不要重复赋值或赋多个值
# 在为位置参数顺序赋值时,所有的参数按序赋值给每个位置参数
func(1, 2, 3, 4)


# 关键字参数 : 关键字参数就是通过"参数名 = 值"的形式进行赋值的参数(实参)

def func(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

# 使用关键字参数,不需要按照顺序赋值,只要参数名称正确即可
func(d=4, a=1, c=3, b=2)


# 使用参数=值的形式赋值,就是关键字参数
# func(a=1, b=2, c=3, d=4)
# TypeError: func() got an unexpected keyword argument 'f'
# 使用关键字参数赋值时,要注意所使用的参数是否存在,最好是提示出来在用
# func(f=1, b=2, c=3, d=4)
# 注意:使用关键字参数要防止重复赋值
# TypeError: func() got multiple values for argument 'a'
# func(1,2,3,a=5)
# 一般情况下,关键字参数都是给默认参数(缺省参数)赋值的

# 缺省参数:就是在定义时给参数一个默认值,如果参数没有赋值,则使用默认值
def func(a, b, c, d=10):
    print(a)
    print(b)
    print(c)
    print(d)


# 不给缺省参数传值则使用默认值
# func(1, 2, 3)
# 给缺省参数传值则使用传入的值
# func(1, 2, 3, 4)

# 一般使用关键字参数给缺省参数赋值
# func(1, 2, 3, d=12)
# 关键字参数赋值,不能在顺序赋值之前
# func(d=12,1, 2, 3)
```

