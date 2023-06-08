## 1、列表的查询

- index：从左至右查询元素在列表中所处的位置，如果查询到该元素返回其第一次出现所在位置的正向下标，如果不存在则报错
- count：查询指定元素在列表中出现的次数
- in：查询指定元素是否在列表中
- not in：查询指定元素是否不在列表中

```python
# 索引查询
name_list = ['Bob', 'Jack', 'Rose']

# print(name_list[0])  # Bob
# print(name_list[1])  # Jack
# print(name_list[2])  # Rose
# print(name_list[-1])  # Rose
# print(name_list[-2])  # Jack
# print(name_list[-3])  # Bob

# 结论: 列表中的索引和字符串中完全一致,
# 正向索引从0开始,从左至右依次递增
# 负向索引,从-1开始,从右至左依次递减

# index  查询指定元素在列表中的索引,如果查询成功则返回该元素的正向索引,否则报错
# index  是从左至右查询,返回第一次出现的索引位置

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 5]
# 会返回从左至右第一次查询到的数据索引
print(num_list.index(5))  # 4
# ValueError: 9 is not in list
# 如果没有查询到数据则会报错
# print(num_list.index(9))


# rindex  在列表中没有这个方法
# AttributeError: 'list' object has no attribute 'rindex'
# print(num_list.rindex(5))

# find  在列表中没有这个方法
# AttributeError: 'list' object has no attribute 'find'
# print(num_list.find(5))

# count  计数, 查询指定元素在列表中出现的次数
print(num_list.count(5))  # 2

# in  判断数据元素是否在列表内  如果在  True  如果不在False
# TypeError: argument of type 'int' is not iterable
# print(num_list in 5)
# 注意使用in或者not in  数据元素在左边,  列表或者其他数据序列在右侧
print(5 in num_list)  # True
print(9 in num_list)  # False
# not in  判断数据元素是否不在列表内  如果不在  True  如果在False
print(5 not in num_list)  # False
print(9 not in num_list)  # True
```

## 2、列表的增加

- append： 在类表的末尾追加数据
- extend：将数据序列进行迭代依次提取出每一个元素添加到列表末尾
- insert：在指定位置追加数据元素

```python
# append 在列表末尾追加数据
num_list = [1, 2, 3, 4]
# 能够打印出1,2,3,4,5么?
# print(num_list.append(5)) # None
# 如果直接打印append方法的调用,将不会输出任何内容
# list类型在使用append 方法时不会产生新的列表,而是在原有列表上进行修改
num_list.append(5)
# append 追加的数据,默认追加到列表末尾,追加完成后在原有数据上修改
print(num_list)  # [1, 2, 3, 4, 5]

# # str
# str1 = 'abc'
# # str类型数据,调用replace方法时,不会修改原有数据,而是产生了一个新的字符串
# str2 = str1.replace('abc', 'cba')
# print(str1)
# print(str2)


# extend  追加数据序列
# 格式: 列表1.extend(数据序列)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# 追加数据序列后,调用extend的列表发生变化, 括号内的数据序列不变
# 其实底层逻辑就是讲括号内的数据序列迭代,依次放入调用该方法的列表中
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]
print(list2)  # [4, 5, 6]

# 追加字符串序列时,会将字母依次拆分并放入列表中
str1 = 'itcast'
list2.extend(str1)
print(list2)  # [4, 5, 6, 'i', 't', 'c', 'a', 's', 't']

# 如果括号内填写的数据,不是数据序列会怎样?
# TypeError: 'int' object is not iterable  括号内必须是可迭代对象
# list2.extend(4)
# 字符串累心哪怕只有一个值,或者只有一个空字符串,都是可迭代类型,同理可知,列表,元组等  哪怕只有以数据或者为空类型也是可迭代类型
list2.extend('3')
print(list2)

# insert 插入
num_list = [1, 2, 3, 4]
# 格式:列表.insert(要插入位置的索引, 要插入的对象)
# 在insert中第一个参数是要插入位置的索引,所以如果插入了数,则该被插入数据的索引变为第一参数所显示的索引
# 原来该位置的元素以及之后的元素下标+1(向后移动一位)
# 如果使用insert进行 插入,可能会造成索引混乱,原来引用的索引发生错误
# 在开发中除非明确所有的索引引用都修改完成,否则不要使用insert
# append 插入数据,要比insert插入数据更安全
num_list.insert(1, 5)
print(num_list)

# extend 和append 进行对比
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
# append将list2 当做一个元素追加到列表末尾
# list1.append(list2)  # [1, 2, 3, 4, [5, 6, 7, 8]]
# extend将list2 当做多个元素进行拆分后追加
list1.extend(list2)  # [1, 2, 3, 4, 5, 6, 7, 8]
print(list1)
```

## 3、列表中的删除

- del  先对列表中的元素进行查找（使用下标），找到后使用del删除

- pop：删除类表中指定下标位置的元素，如果不指定默认删除最后一个，并且返回被删除的值
- remove：删除指定值的下标，只删除丛左至右的第一次出现的该值元素
- clear：清空列表，和重新赋值为空有逻辑上的区别。

```python
# del  将数据引用切断
list1 = [1, 2, 3, 4]
# del list1
# NameError: name 'list1' is not defined
# del不仅可以删除元素,也可以删除任何变量,非常强大,但是有些不安全
# print(list1)
# 那del 怎样删除元素呢?  通过索引获取当前元素,并删除
del list1[2]
# IndexError: list assignment index out of range
# 使用下标查找数据时,下标索引不能不存在
# del list1[9]
print(list1)  # [1, 2, 4]

# 如果要是循环中能够删除么?
# 此处并没有删除,因为i是临时变量,我们使用del是在讲i和2的引用关系删除,但是list1 和 2 的引用关系没有删除
# for i in list1:
#     if i == 2:
#         del i
#
# print(list1)

# pop  删除指定索引的元素,并且返回该元素
list1 = [1, 2, 3, 4]
# 删除后可以返回被删除的对象
print(list1.pop(2))
# IndexError: pop index out of range
# 使用pop进行删除的元素下标一定要存在
# print(list1.pop(12))
# 删除后,指定索引位置的元素消失后边的元素统一向左移动一位
# pop也会造成索引变换
print(list1)
# 如果不给pop进行传值,默认删除最后一个元素
print(list1.pop())
# 查看删除后结果
print(list1)

# remove 删除指定的元素(从左至右第一次出现的元素)

list1 = [1, 2, 3, 3, 4, 2, 1]
# 删除列表中的2
# 将从左至右查询第一次遇到的2进行了删除,并不能删除类表中所有的的2
list1.remove(2)
print(list1)  # [1, 3, 3, 4, 2, 1]

# remove会返回被删除的内容? 不会
print(list1.remove(3))  # None
# remove删除的内容不存在会怎样?
# list1.remove(123)  # ValueError: list.remove(x): x not in list

# clear  清空列表
# 就是讲列表置为[],但是与list1 = [] 有本质区别
list1.clear()
print(list1)  # []
```

## 4、列表的修改

- 使用索引修改： 列表[索引] = 新值
  - 查询列表索引值必须在列表中存在
- reverse: 列表的反转
- sort：列表的排序，默认为升序
  - reverse：可以进行列表倒排，降序
  - key:添加函数，使排序规则更加复杂多变

```python
# 通过索引进行修改
list1 = [1, 2, 3, 4]
# 通过索引查找到指定位置的数据,并进行修改
list1[1] = 6
# IndexError: list assignment index out of range
# 获取的元素位置,必须是存在的
# list1[6] = 6
print(list1)

# 通过索引修改可以同时修改多个值么?  不能
# list1[(2,3)] = 6,7
# 可以使用对多变量赋值的形式修改多个值
list1[2], list1[3] = 6, 7
print(list1)

# reverse  列表的反转
list1 = [1, 2, 3, 4]
# 列表反转后,索引倒置,并且在原数据上修改,没有产生新的列表
print(list1.reverse())  # None
print(list1)  # [4, 3, 2, 1]

# sort  排序
list2 = [2, 6, 43, 2, 41, 421]
# sort是对原有的数据进行了排序,没有产生新的列表.同时,默认排序规则为升序
# print(list2.sort())  # None
# print(list2)  # [2, 2, 6, 41, 43, 421]
# 如果我想让列表降序排列怎么办?
# 方法一:可以先排序再反转
# list2.sort()
# list2.reverse()
# print(list2)  # [421, 43, 41, 6, 2, 2]
# 方法二: 可以直接使用倒叙排列
# list2.sort(reverse=True)  # [421, 43, 41, 6, 2, 2]
# print(list2)

# list2.sort(key=排序规则函数)可以帮助我们进行更加复杂的排序
# 根据每个元素 % 7 的余数大小进行排序
# 了解, 不要求掌握 后续会讲
list2.sort(key=lambda x: x % 7)
print(list2)
```

## 5、列表遍历

- for遍历
- while遍历

```python
# while遍历列表
# len()函数可以查询列表的长度

list1 = [12, 123, 1, 1, 1234, 12, 34, 8]
# print(len(list1))
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

# for 遍历列表
# 推荐使用for循环遍历容器类型(数据序列)
for i in list1:
    print(i)
```

## 6、列表的嵌套

- 列表中嵌套其他的子列表，就是列表的嵌套
- 嵌套后的列表可以使用循环嵌套来进行遍历

```python
# 列表的嵌套: 在一个列表中包含其他的列表元素

name_list = [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]

# 需求:想要获取李四的值
# 获取李四所在的子列表的索引,并通过索引获取该子列表值
print(name_list[2])
# 再从子列表中通过李四所在的索引获取其值
print(name_list[2][1])

# 如果我们想要获取嵌套列表中的每一个值,我们需要怎么做?
# 如果进行一次循环,每次循环所得到的都一级列表中的元素,也就是每一个子列表
for i in name_list:
    print(i)

# 如果想要对嵌套后的列表进行输出,需要进行循环嵌套
for sub_list in name_list:
    for name in sub_list:
        print(name)

# 这样就可以进行所有名称的输出了

# 如果当前的列表内的数据不都是子列表,有其他数据类型的数据,则不能直接使用循环嵌套,需要先进行类型判断
```

## 7、元组的定义

- 单元素元组： 变量 = （数据，）
- 多元素元组：变量 =  （数据1， 数据2， 数据3....）

```python
# 元组:可以储存多个数据,但是元组内的数据不能被修改(元定义后只能被查询)
# 元组的定义:变量 = (数据1, 数据2, 数据3......)
tuple1 = (1, 2, 3, 4)
# 打印后可以展示元组中的全部信息
print(tuple1)  # (1, 2, 3, 4)
# 查询数据类型
print(type(tuple1))  # <class 'tuple'>

# 如果元组中只有一个元素怎么办? 在单一元素后添加逗号
tuple2 = (10)
print(type(tuple2))  # <class 'int'>

tuple3 = ('10')
print(type(tuple3))  # <class 'str'>

tuple4 = (10,)
print(type(tuple4))  # <class 'tuple'>

# 如果小括号包裹单一元素数据不添加逗号,则小括号的意义是提升算术运算符优先级

# 在定义元素或者传值时,元组的括号可以省略

tuple5 = 1, 2, 3, 4, 5
print(tuple5)  # (1, 2, 3, 4, 5)
print(type(tuple5))  # <class 'tuple'>

tuple6 = 5,
print(tuple6)  # (5,)
print(type(tuple6))

tuple7 = (1,2,3,)
print(tuple7)
```

## 8、元组的相关操作

- 元组中的数据不能增删改，所以只能查询
- 元组的查询方式
  - 索引查询：和列表的使用方式一致
  - index ：从左至右查询指定元素在元组中第一次出现的位置索引，如果存在则返回正向索引，如果不存在则报错
  - count：查询指定元素在元组中出现的次数
  - len：查询元组的长度：也就是查询元组中元素的个数

```python
# 元组的增删改:由于元组中的数据不可修改,所以元组中的数据不能进行增删改操作
tuple1 = (1, 2, 3, 4)
# 修改
print(tuple1[2])
# TypeError: 'tuple' object does not support item assignment
# 元组中的数据不能修改
# tuple1[2] = 6
# 删除
# TypeError: 'tuple' object doesn't support item deletion
# 元组中的数据不能删除
# del tuple1[2]

# 查询
# 通过索引进行查询
# 查询方法和列表一致
# 正向索引,从0开始,从左至右依次递增
# 负向索引,从-1开始,从右至左依次递减
tuple1 = (1, 2, 3, 4, 3)
# 需求:通过正向索引取出3
print(tuple1[2])
# 需求:通过负向索引取出3
print(tuple1[-2])

# index  查询指定元素在元组中所在的位置索引
# 需求:查询3所对应的索引值
# index是从左至右依次查询,返回第一个查到的数据的正向索引值
print(tuple1.index(3))  # 2
# 如果查询的内容不存在,则报错
# print(tuple1.index(8))  # ValueError: tuple.index(x): x not in tuple

# count 查询指定元素在元组中出现的次数
print(tuple1.count(3))  # 2
print(tuple1.count(1))  # 1

# len  查询元组的长度(对所有容器适用)  长度就是计算当前容器中有多少个元素
print(len(tuple1))  # 5
# 其实len()就是调用了括号内对象的__len__方法
print(tuple1.__len__())  # 5
```

## 9、字典的定义

- 格式：变量 = {key1 : value1, key2: value2......}
- 空字典定义：
  - {}
  - dict（）
- 字典中键不能重复，是唯一的，但是值可以重复
- 字典中的键要见名知意，体现字典可以见名知意的特性

```python
# 字典:储存多个数据,以键值对形式存储,方便快速存取
# 字典的键要见名知意

# 字典定义格式: 变量 = {键1:值1, 键2:值2.....}
dict1 = {'name': 'xiaoming', 'age': 18, 'gender': '女'}
# 使用print打印可以显示字典中的所有数据
print(dict1)
# 查看字典类型
print(type(dict1))  # <class 'dict'>

# 空字典定义方法
dict2 = {}
# 或者
dict3 = dict()
print(dict2, dict3)
print(type(dict2), type(dict3))

# 见名知意的重要性
# 需求: 使用字典保存一个人的信息  xiaoming  18   男  001
# 保存方式一:
# dict4 = {'name': 'xiaoming', 'age': 18, 'gender': '男', '学号': '001'}
# print(dict4)
# 保存方式二:
# 字典的优势是快速存取,注意命名键的时候要见名知意,并且易于记忆
# 字典占用空间远大于列表,使用字典存储数据本来就是牺牲空间确保时间,所以要尽量利用字典快速存取的特性,而不要想空间的节省
# dict5 = {'xiaoming':18, '男':'001'}  # 不建议这样写

# 定义字典时 ,不能有重复的键,否则后定义的键值对会覆盖先定义的

dict6 = {'name': 'xiaoming', 'age': 18, 'name': 'rose'}
# 字典中的键是惟一的,后定义的内容值会覆盖先定义的
print(dict6)

# 字典中键是唯一的但是值可以随意重复
dict7 = {'name': '小明', 'age': 18, 'id': 18}
print(dict7)
```

## 10、字典的增加

- 字典[新的key] = 值
- 如果key在原字典中已经存在则为修改原key对应的值

```python
# 增  使用新的键 = 值的形式增加键值对
dict1 = {'name':'xiaoming', 'age': 18}
# 使用新的键= 值
# 格式:字典变量[key] = 值  如果为新增,则key在原字典中不存在
dict1['gender'] = '男'
print(dict1)  # {'name': 'xiaoming', 'age': 18, 'gender': '男'}

# 如果原字典中存在该key 则为修改原key所对应的值
dict1['name'] = 'xiaowang'
print(dict1)  # {'name': 'xiaowang', 'age': 18, 'gender': '男'}

# update
# 一般用于两个字典间的拼接
# 如果update中添加的键已经存在则修改原有的值
dict1.update({'id': '001', 'color': 'yellow', 'name': 'rose'})
print(dict1)
```

## 11、字典的删除

- del  查找到字典的键所对应的值进行删除
- clear（）清空字典所在数据空间中的多有键值对
- pop：删除指定键所对应的键值对，会将删除的键值对所对应的值进行返回
- popitem： 删除随机一个键值对，尝试后发现总是删除最后一个，会将删除的键值对以元组的形式进行返回

```python
# del
# 使用del删除键值对,先要找到dict所对应的键,进行删除
# 注意,在字典中键值对是成对出现的,删除键值也就消失了,不能出现单独的键或者单独的值
dict1 = {'name': 'xiaoming', 'age': 18}
del dict1['age']
print(dict1)  # {'name': 'xiaoming'}

# clear() 清空字典
# 使用clear将字典所对应的内存空间中的数据进行了清空
dict1.clear()
print(dict1)  # {}

# 通过之前的学习经验我们猜测 pop是删除简直对用的
dict2 = {'name': 'xiaoming', 'age': 18, 'gender': '男'}
# 使用pop可以根据指定的key删除键值对
# 使用pop删除键值对后会将其键对应的值进行返回
# print(dict2.pop('name'))  # xiaoming
# print(dict2)  # {'age': 18, 'gender': '男'}

# 猜测:popitem也是删除键值对使用的
# 随机删除一个键值对,一般都是删除最后一个
# 删除后会将我们所删除的键值对以元组的形式进行返回
print(dict2.popitem())  # ('gender', '男')
print(dict2.popitem())  # ('age', 18)
print(dict2)  # {'name': 'xiaoming'}

# dict  无序的  因为其不能通过索引进行键值对的获取(了解)
# Python3.5以后,字典中键值对的顺序和我们插入键值对的顺序保持一致,但是该顺序没法被利用(了解)
```

## 12、字典的修改

- 字典[key] = 值
  - 字典中key必须存在
- update：
  - update（键 = 值）
  - update（{键：值}）
  - 对应的键一定存在

```python
# 通过索引修改字典中的键值对
dict1 = {'name':'小明', 'age':18}
dict1['name'] = '小红'
print(dict1)

# update
# 可以进行制定字段值的修改
# dict1.update(name='小绿')
dict1.update({'name': '小绿'})
print(dict1)
```

## 13、字典的查询

- 使用键查询值：字典[key]
  - 查询的键不存在时则报错
- get：字典.get(key)
  - 查询的键不存在时，不报错，可以默认返回None，或者手动设置返回内容
- keys：获取所有的键
- values：获取所有的值
- items：获取所有的键值对组成的元组

```python
# 直接使用key进行查询
dict1 = {'name': '小明', 'age': 18, 'gender': '男', 'id': '001'}
# 查询学员的名称?
print(dict1['name'])

# get查询
# 如果我们查询的键不存在会真么样??? 报错
# KeyError: 'apple'  会出现keyerror  表示查询的键不存在  报错
# print(dict1['apple'])
# 使用get进行查询,只需要在get中传入对应的键即可
# 如果使用get查询的键不存在,则不会报错,会默认返回一个None
print(dict1.get('name'))  # 小明
print(dict1.get('apple'))  # None
# 如果查询的键不存在,get可以自定义默认返回值
# 格式 字典.get(要查询的键, 查询的键不存在时返回的数据)
print(dict1.get('apple', '小刚'))
print(dict1.get('apple', 9))

# keys 获取当前字典中所有的键
print(dict1.keys())  # dict_keys(['name', 'age', 'gender', 'id'])
# keys返回的内容不是列表,而是dict_keys,该数据类型不能直接使用索引查询数据,但是可以进行for遍历
print(type(dict1.keys()))  # <class 'dict_keys'>
keys_1 = dict1.keys()
#  不能使用索引查询
# TypeError: 'dict_keys' object is not subscriptable
# print(keys_1[1])
# 可以被迭代
for i in keys_1:
    print(i)

# values 获取当前字典中所有的值
print(dict1.values())  # dict_values(['小明', 18, '男', '001'])
# dict_values不能使用索引查询,但是可以迭代
print(type(dict1.values()))  # <class 'dict_values'>

# items 获取当前字典中所有的键值对,键值对以元组形式展示
print(dict1.items())  # dict_items([('name', '小明'), ('age', 18), ('gender', '男'), ('id', '001')])
# dict_items不能使用索引查询,但是可以迭代
print(type(dict1.items()))  # <class 'dict_items'>
```

## 14、字典的遍历

```python
# 字典的遍历
dict1 = {'name': '小明', 'age': 18, 'gender': '男', 'id': '001'}

# 使用for循环对字典进行遍历,默认获取的是字典的每一个键
for i in dict1:
    print(i)
'''
name
age
gender
id
'''
# 获取的是字典的每一个键
for i in dict1.keys():
    print(i)
'''
name
age
gender
id
'''

# 获取的是字典的每一个值
for i in dict1.values():
    print(i)
'''
小明
18
男
001
'''

# 获取的是字典中每一个键值对组成的元组
for i in dict1.items():
    print(i)
'''
('name', '小明')
('age', 18)
('gender', '男')
('id', '001')
'''
# 有没有办法可以分别拿到字典的键和值呢?

for i in dict1:
    print(i, dict1[i])

for key, value in dict1.items():
    print(key, value )
```

## 15、集合的定义

- 变量 = {数据1， 数据2， 数据3.。。。}
- 空集合：set（）
- 集合是一个无序的 不重复的数据序列

```python
# 集合: 集合是一个无序,不重复的数据序列
# 无序: 程序员无法控制其排不顺序,  程序员无法使用索引查找或修改数据
# 不重复:没有办法在字典中放入相同的值,会自动去重,类似于字典的键

# 无序:
set1 = {1, 2, 5, 6, 3, 4}
# 程序员无法利用其顺序,有顺序也无用
# 了解:在集合中会使用数据的值计算哈希值,根据哈希值顺序进行排序
print(set1)  # {1, 2, 3, 4, 5, 6}

# 不重复
set2 = {1, 2, 3, 4, 5, 6, 7, 2, 3}
# set会自动去重
print(set2)  # {1, 2, 3, 4, 5, 6, 7}

# 定义空集合
set3 = set()
# {} 是定义空字典的
print(set3)

# 集合中能够储存什么数据?
# 布尔值在进行计算时  True == 1 Fasle == 0
# 基础数据类型 int  float  bool  字符串 都可以用集合储存
set4 = {1, 12.3, True, 0, False, ''}
print(set4)

# TypeError: unhashable type: 'list'
# 列表数据无法用集合储存
# set5 = {1, 12.3, True, 0, False, '', [1, 2]}
# print(set5)

# 元组类型可以放入集合内储存
set6 = {1, 12.3, True, 0, False, '', (1, 2)}
print(set6)

# TypeError: unhashable type: 'dict'
# 字典类型无法用集合储存
# set6 = {1, 12.3, True, 0, False, '', {1:2}}

# TypeError: unhashable type: 'set'
# 集合类型同样不能使用集合嵌套
# set6 = {1, 12.3, True, 0, False, '', {1,2}}

# 结论:列表  字典  集合,不能放入集合中,作为元素出现

# 拓展:不能作为集合元素的数据类型,同样不能作为字典的键出现
dict1 = {(1, 2): 3}
print(dict1)
# TypeError: unhashable type: 'list'
# 列表 字典 集合不能作为字典的键出现
dict2 = {[1, 2]: 3}
print(dict2)
```

## 16、集合的相关操作

- 集合的增加
  - add：添加一个元素，如果值已存在，则去重
  - update： 更新元素（在括号中添加可迭代类型），如果值已存在则去重

```python
# add 增加
set1 = {1, 2, 3, 4}
# set 在使用add命令后,不会产生新的数据,而是原集合中进行修改
set1.add(5)
print(set1)  # {1, 2, 3, 4, 5}

# update 更新
# TypeError: 'int' object is not iterable
# update内部只能填写容器类型(数据序列)
# set1.update(6)
set1.update([6, 7])
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
# 如果更新的数据已经存在,则去重
set1.update([1,2])
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
```

- 集合的删除
  - remove：根据元素值进行删除，如果元素不存在则报错
  - discard：根据元素值进行删除，如果元素值不存在则不报错
  - pop：删除任意元素，并返回被删除的值

```python
# remove
set1 = {1, 2, 3, 4}
# 使用remove可以删除指定值的元素
# set1.remove(3)
# print(set1)  # {1, 2, 4}

# pop 随机删除一个元素,并且将删除的元素返回
# print(set1.pop())
# print(set1)

# discard
# 如果使用remove删除的元素不存在会怎样?  报错
# set1.remove(13)  # KeyError: 13
# 如果使用discard删除元素呢?  不会报错
set1.discard(3)
print(set1)  # {1, 2, 4}
set1.discard(13)
print(set1)
```

- 集合判断：
  - in
  - not in

```python
# 数据是否在集合中
set1 = {1, 2, 3, 4}
# in 判断元素是否在集合中出现
print(4 in set1)  # True
print(5 in set1)  # Fasle

# not in 判断元素是否不在集合中
print(4 not in set1)  # False
print(5 not in set1)  # True

# 注意:格式  元素 in  集合

# 判断的数据必须要在集合中能够被储存
# TypeError: unhashable type: 'list'
# print([1, 2] in set1)
```

- 集合可以使用for循环遍历，但是遍历顺序随机

```python
# for 遍历
set1 = {1, 2, 3, 4}
for i in set1:
    print(i)

# 注意遍历集合,顺序不定
name_set = {'Tom', 'Bob', 'Rose'}
for i in name_set:
    print(i)
'''
Rose
Tom
Bob
'''
```

