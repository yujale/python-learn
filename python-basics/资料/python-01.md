## Python


## 1、Python概述

- 创始人：吉多·范罗苏姆  龟叔
- 为什么要学习Python：大势所趋，简单易学，使用范围广
- 我们本次学习使用Python3.x版本
- Python在大数据生态中应用非常广泛

## 2、Python解释器和pycharmIDE工具

- Python解释器是将Python代码解释为机器语言（二进制文件）的一种工具
- Python代码必须经过解释器解释，计算机才能够去执行命令
- 常见的解释器版本：
  - CPython： 官方版本，稳定，持续更新
  - Ipython：可交互，在CPython基础上进行了升级
  - pypy：使用Python编写的解释器
  - JPython：使用java编写的解释器，可以将Python便以为字节码文件，在java平台上运行
- pycharm IDE：
  - 语法高亮
  - 工程管理
  - 代码提示
  - 错误检查
  - 。。。。。。。
- pychram基本设置
  - 主题：file --- settings---在搜索栏搜索 theme ----修改主题
  - 字体：file --- settings -- 在搜索栏输入font  ---- 修改字体
  - 修改解释器：file --- project：项目名称--- Python interpreter --修改解释器
  - 工程管理：file -- open ---选择工程
    - this windows ： 在当前窗口打开
    - new windows：在新窗口打开
    - attach ：合并项目窗口
  - 关闭工程： file -- close project

## 3、Python中的注释

- 单行注释： # 注释的内容
  - 可以在语句末尾注释
  - 快捷键：ctrl+ /
- 多行注释：三对单引号，或者三对双引号
  - 可以在注释内部换行

```python
"""
我是文件开头的多行注释,颜色不一样,
但是功能没有区别
"""

# 注释:有提示作用,注释不参与代码执行,但是可以增加代码的可读性
# 语法规范:单行注释#号与注释内容之间存在一个空格, 如果在语句末尾注释,语句和#之间要有两个空格
# 单行注释
print('hello world')
# 我是一个优秀的单行注释
print('hello bigdata')
print('hello python')  # 打印Python,可以添加在语句的末尾
print('hello itcast')
# 单行注释快捷键:ctrl + /
# 如果想要快捷注释多行内容,选中多行信息,使用ctrl+ /进行对多行代码依次进行单行注释
# print('hello itcast')
# print('hello itcast')
# print('hello itcast')


# 多行注释
'''
我是一个多行注释
在多行注释内,可以随意换行
换行后可以正常书写
'''

"""
在Python中单双引号不敏感,但要成对出现
双引号也可以构建多行注释
"""

# ???多行注释可以用在语句末尾么?  不能
# print('hello python') """ abc """

# 在文件开始位置,多行注释和文件中间的多行注释颜色不一样,效果一样么? 一样
```

## 4、变量

- 变量特性：
  - 容器
  - 临时
  - 可变
- 变量定义的格式：
  - 变量名 = 值
- 标识符的命名规则：
  - 只能是数字字母下划线组成
  - 首字母不能是数字
  - 严格区分大小写
  - 不能是关键字
- 在Python中定义变量必须赋值，否则报错

```python
# 牛奶和可乐交换的案例
'''
交换方式:
获取一个空杯子
将牛奶倒入空杯子
将可乐倒入原牛奶现空杯子的杯子中.....
'''

'''
换一个方式进行描述:
# 开始
A杯子: 牛奶
B杯子: 可乐
C杯子: 空
# 过程
A >> C
B >> A
C >> B
# 结尾
A杯子: 可乐
B杯子: 牛奶
C杯子: 空
'''

a = '牛奶'
b = '可乐'
c = '空'
print(a, b)

c = a
a = b
b = c

print(a, b)

# 关键字: 系统定义的具有一定功能或者含义的字符组合.(关键字不要背诵,遇到了就记下来,如果记不下来,关键字有自己的高亮效果)
# 标识符: 程序员自己定义的具有一定功能或者含义的字符组合.

# 标识符的命名规则:
# 1/只能由数字,字母,下划线组成
# 2/首字母不能是数字
# 3/不能是关键字
# 4/严格区分大小写

# 什么地方使用了标识符:文件名,变量名, 函数名, 类型名  (只要是让程序员起名字,都是标识符)
# 文件名可以不遵循标识符的命名规则,但是在服务器中无法使用,不能当做模块进行导入,很多服务器工具或组件不支持非标识符文件.

'''
Python)abc  不能
_abc   可以
anc______  可以
123abc _____  不可以
and  不可以
ABC  可以
anc  可以
'''

# 在windows中文件名定义时,不严格区分大小写
# 程序员不可能定义变量出错

# aaa
# 在Python中创建变量必须赋值,否则将会报错
```

## 5、标识符的命名规范

- 见名知意
- 类名使用大驼峰命名法
  - ClassName
- 变量名，函数名，包名，模块名使用下划线命名法
  - class_name

```python
# 要见名知意
name = '小明'
age = 18

# abc = '小明'
# 见名知意不要写缩写,也不要写首字母,尤其是不要写拼音首字母,更不要写拼音全拼

# 命名法
# 大驼峰命名法:
# 首字母大写,如果由多个单词组成,所有单词的首字母大写
# 在Python中类名的书写使用大驼峰命名法
ClassName = 'Python+大数据54期'
# 小驼峰命名法:
# 首字母小写,如果由多个单词组成,第一个单词首字母小写,其余单词首字母大写
className = 'Python+大数据54期'
# 下划线命名法:
# 在Python中 变量,函数,文件名称(包和模块名称)使用下划线命名法
# 所有字母小写,多个单词中间用下划线连接
class_name = 'Python+大数据54期'

# 不满足命名规范一样不会报错,但是不利于协作开发
```

## 6、变量的使用

- 定义：变量名 = 值
- 调用：函数（变量名）   或者    使用变量名进行运算  变量名1 + 变量名2
- 变量必须先定义后调用

```Python
# 使用变量直接调用变量名即可,我们使用的是变量名,参与执行和运算的是变量中的数据(值)
name = 'xiaoming'  # 定义
print(name)  # 调用

a = 1  # 定义
b = 1  # 定义
print(a + b)  # 调用

# 所有的变量,要先定义后调用
# 程序运行起来后,从上到下依次执行代码,解释一行运行一行,在打印方法被执行时,还不知道price已经被定义,会报错
# print(price)
# price = 15
```

## 7、Python中的数据类型

- int  整型
- float 浮点型
- bool 布尔型
- str  字符型  字符串
- list  列表
- tuple 元组
- set  集合
- dict  字典
- 查看数据类型使用的函数是 type（）

```python
# 数据类型查看的函数 type(数据/变量名)
# 基础数据类型:int  float  bool
# 容器类型: str  list tuple  set dict

# 整型
int1 = 12
print(type(int1))  # <class 'int'>
# 浮点型
float1 = 12.1
print(type(float1))  # <class 'float'>
# 布尔型  (True/False)
bool1 = True
print(type(bool1))  # <class 'bool'>
# 字符串型
str1 = 'hello Python'
print(type(str1))  # <class 'str'>
# 元组
tuple1 = (1, 2, 3, 4)
print(type(tuple1))  # <class 'tuple'>
# 列表
list1 = [1, 2, 3, 4]
print(type(list1))  # <class 'list'>
# 集合
set1 = {1, 2, 3, 4}
print(type(set1))  # <class 'set'>
# 字典
dict1 = {'name': 'xiaoming', 'age': 18}
print(type(dict1))  # <class 'dict'>

# 代码格式化的快捷键:ctrl + alt + L

# 练习:

a = 12
# a是什么数据类型? int
a = 'str'
# a是什么数据类型? str
a = '12'
# a是什么数据类型? str
a = True
# a是什么数据类型? bool
a = 13.4
# a是什么数据类型? float


# 通过上述演示,我们发现在Python程序执行过程中,可以随意改变变量的数据类型
```

## 8、Python中的bug和调试

- 常见的bug类型：

```Python
# 常见的bug
# NameError: name 'a' is not defined (一般只变量名错误)
# 如果遇到此类错误,查看变量名是否被定义或者变量名是否书写错误
# print(a)

# ZeroDivisionError: division by zero (零不能做分母)
# a = 10
# print(a / 0)

# IndentationError: unexpected indent  (缩进错误)
# 修改缩进,或者去调整函数关系
# a = 5
#     b = 10

# SyntaxError: unexpected EOF while parsing (语法错误)
# 找到报错位置,查看语法是否存在问题,最好的办法就是将其进行格式化
# print(123

# TypeError: can only concatenate str (not "int") to str (数据类型错误)
# a = '123'
# print(a + 12)

# Process finished with exit code 0 程序结束后 正常退出 code 为 0
# print('hello world')

# Process finished with exit code 1  程序异常结束 code 为 1
# print(a)
```

- bug调试工具的使用
  - 打断点：在行号后边点击出现小红点
  - 右键debug进入调试模式，代码执行暂停到断点位置代码执行之前
    - debugger ：查看参数及变量在执行过程中的变化情况
    - console：查看控制台输出内容
    - step over：单步执行代码
    - resume ：执行到下一次断点位置或者程序结束
    - stop：让程序终止

## 9、字符串的格式化及输出

- 格式化是字符串所具有的功能，与print无关，哪怕不进行输出，也可以进行字符串的格式化

```python
# 字符串格式化 :格式化是字符串所具有的功能
# print 输出: print函数只能将传入的内容显示到控制台中,与格式化没有任何关系

# 需求:想让小明的年龄,跟着age变量的变化,不断发生变化,那么我们应该怎么做?
age = 16
print('小明14岁')

# 字符串的格式化
# 格式化输出,到底是print 的功能还是字符串的功能呢?
print('小明 %d 岁' % age)

# 探索
str1 = '小明 %d 岁' % age
print(str1)
```

- 格式：
  - 单占位符：'要书写的内容，占位符' % 变量名
  - 多占位符: '要书写的内容，占位符1， 占位符2， 。。。。' % （变量1， 变量2，。。。。）
    - %之前的占位符数量要和%之后的变量数量相匹配，一一对应否则会报错

```python
# 格式: '字符串,占位符' % 变量
# 在上述格式中,格式化完成后,会将占位符位置填充上对应的变量
# 不同数据类型的变量,要使用不同的占位符进行占位

# 字符串数据使用 %s
# 浮点型数据使用 %f
# 整型数据使用   %d

name = 'xiaoming'
age = 18
height = 1.85
weight = 69.5
marriage = False

# 一个占位符的格式化输出
print('学员的姓名是 %s' % name)
print('学员的年龄是 %d' % age)
print('学员的身高是 %f' % height)
print('学员的体重是 %f' % weight)
print('学生的婚姻状况是 %s' % marriage)

# 有多个动态变量的时候,我们就需要使用多个占位符进行占位
# TypeError: not enough arguments for format string
# 如果前边有多个占位符,那后边的多个变量要使用括号进行包裹
print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%f米, 学员的体重是%fkg, 学员的婚姻状况是%s' % (name, age, height, weight, marriage))
# 括号内的变量数量不能少于占位符数量
# print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%f米, 学员的体重是%fkg, 学员的婚姻状况是%s' % (name, age, height, weight))
# not all arguments converted during string formatting
# 括号内的变量数量不能多于占位符的数量
# print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%f米, 学员的体重是%fkg, 学员的婚姻状况是%s' % (name, age, height, weight,marriage,name))

# 结论:占位符的数量,与%后的变量数量必须保持一致,如果是一个占位符,则可以使用一个变量,如果是多个占位符,那么多个变量必须使用括号包裹起来

# 能否控制变量输出的结果的样式:可以
name = 'xiaoming'
age = 18
height = 1.85
weight = 69.5
id = 12

# 需求:1.身高保留两位小数,体重保留三位小数
# 需求:2.学员的id共占用6位,不足位用0填充
# 使用ctrl + d 可以整行复制
print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%f米, 学员的体重是%fkg, 学员的编号是%d' % (name, age, height, weight, id))
# 浮点型保留n位小数: %.nf
# 整型占用n位数据,不足位用0补齐  %0nd
print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%.2f米, 学员的体重是%.3fkg, 学员的编号是%06d' % (name, age, height, weight, id))
```

