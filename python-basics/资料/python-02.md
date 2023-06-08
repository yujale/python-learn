## 1、转译字符

- \n:换行符
- \t：制表符
- %%：在字符串格式化拼接时输出%

```python
# \n  换行符
# 为什么两个print之间可以自动换行
# 在print定义时自动在结尾加上了'\n'所以每次打印结束后,会自动换行
print(123)
print('hello world \n')
print(456)
# 如果不想让其自动换行, 在字符串输入结束后,使用end = '结束符' 可以修改print打印结束后插入的字符
print(123, end='$$$')
print(456)

# \t 制表符
print('3  4\t5')
# %%  输出%
# 在不适用字符串格式化拼接时,可以进行%的单独输出
print('我的业绩增长了100%')

score = 100
# 在使用字符串格式化的时候,字符串中的%不能单独输出,必须配合占位符,或者使用%%进行输出
print('我的成绩增加了%d%%' % score)

# 转译字符:在字符串中,一般情况下n  或者 t这类字母没有特殊含义,如果想给他赋予特殊含义,则需要使用\进行转译
```

## 2、f-string

- f-string是Python3.6之后出现的格式化语法
- 格式：f'要输出的字符串{要拼接的变量}'
  - f可以是大写，也可以是小写，
  - 引号可以是单引号，也可以是双引号
  - 精度控制
    - {浮点型变量：.nf} 保留n位小数，四舍五入
    - {整型变量：0nd} 保留n位，不足位用0补齐，如果超出则原样显示
    - %可以单独输出

```python
# f-string是Python3.6以后推出的格式化方式
name = 'xiaoming'
age = 18
height = 1.85
weight = 69.5
score = 98
id = 12345678

# 格式化拼接上述变量
# 传统拼接方式
print('学员的姓名是%s, 学员的年龄是%d, 学员的身高是%f, 学员的体重是%f, 学员的分数是%d%%, 学员的学号是%d' % (name, age, height, weight, score, id))
# 使用f-string进行字符串拼接
# 格式:f'要输出的内容{变量}'
print(F'学员的姓名是{name}, 学员的年龄是{age}, 学员的身高是{height}, 学员的体重是{weight}, 学员的分数是{score}%%, 学员的学号是{id}')


# 修改格式:
print('学员的姓名是%s, 学员的年龄是%d, 学员的身高是%.2f, 学员的体重是%.3f, 学员的分数是%d%%, 学员的学号是%06d' % (name, age, height, weight, score, id))
# 如果需要调整精度
# {整数型变量:06d} 整型占六位,不足位用0补齐 d可以省略
# {浮点型变量:.2f} 浮点型保留两位小数, 四舍五入
# %可以单独输出
print(F'学员的姓名是{name}, 学员的年龄是{age}, 学员的身高是{height:.2f}, 学员的体重是{weight:.3f}, 学员的分数是{score}%, 学员的学号是{id:06d}')
print(F'学员的姓名是{name}, 学员的年龄是{age}, 学员的身高是{height:.2f}, 学员的体重是{weight:.3f}, 学员的分数是{score}%, 学员的学号是{id:06}')

# 练习:
# 输出自己的信息包括,姓名,年龄,身高(保留两位小数),学号(保留6位,不足位用0补齐),使用f-string进行拼接
```

## 3、数据类型转换

- 数据类型转换是为了不同类型数据之间可以进行拼接或运算
- 格式：数据类型（要转化类型的变量或值）
- int和float类型直接可以随意转换
  - float转换为int类型只保留整数部分
  - int转换为float类型在末尾添加。0

- 如果数值型转换为str类型，可以随意转换
- 如果str类型转换为数值型
  - float  必须保证str引号内部是浮点型数据或整型数据
  - int  必须保证str引号内部是整型数据

```Python
# 需求: 在超市中有两种水果,苹果和橘子
# 让售货员输入苹果的单价,苹果的重量,橘子的单价,橘子的重量,在控制台输出购买详情以及总价

# apple_price = input('请输入苹果的单价:')
# apple_weight = input('请输入苹果的重量:')
# orange_price = input('请输入橘子的单价:')
# orange_weight = input('请输入橘子的重量:')

# TypeError: can't multiply sequence by non-int of type 'str'
# 不同类型间的数据无法相乘
# 在此情况下,我们需要进行数据类型转换(input接收的数据默认为字符串类型),需要转化为float
# print(f'您购买了苹果{apple_weight}kg, 单价{apple_price}元, 橘子{orange_weight}kg, 单价{orange_price}元, 总共需要付款{apple_price * apple_weight + orange_price * orange_weight}')

# 如果需要将数据转换为float 就给其穿上float类型的衣服
# 格式: float(需要转换数据类型的变量或者值)
# apple_price = float(input('请输入苹果的单价:'))
# apple_weight = float(input('请输入苹果的重量:'))
# orange_price = float(input('请输入橘子的单价:'))
# orange_weight = float(input('请输入橘子的重量:'))
#
#
# print(f'您购买了苹果{apple_weight}kg, 单价{apple_price}元, 橘子{orange_weight}kg, 单价{orange_price}元, 总共需要付款{apple_price * apple_weight + orange_price * orange_weight}元')


int1 = 12
float1 = 14.9
str1 = '12'
str2 = '14.3'
str3 = 'python'

# 数据类型转换的细节
# int   float  str类型之间的转换
# int >> float
# int类型转换为float类型将会在整数末尾加.0
print(float(int1))
print(type(float(int1)))

# float >> int
# float转换为int类型,将会将小数部分去除,只保留整数部分
print(int(float1))

# int >> str
# int类型可以随意转换为str类型,但是输出结果不发生改变,转化为str类型后可以使用str类型的各种函数
print(str(int1))

# str >> int
# 字符串中是int类型数据,可以转换为int类型
print(int(str1))
# ValueError: invalid literal for int() with base 10: '14.3'
# 字符串中是float类型数据,不可以转换为int类型
# print(int(str2))
# ValueError: invalid literal for int() with base 10: 'python'
# 字符串中是字符型数据,不可以转换为int类型
# print(int(str3))

# float >> str
# float类型可以随意转换为str类型,但是输出结果不发生改变,转化为str类型后可以使用str类型的各种函数
print(str(float1))

# str >> float
# 字符串中是int类型数据,则可以转换为float类型数据,并且在末尾加.0
print(float(str1))
# 字符串中是float类型数据,可以转换为float类型数据
print(float(str2))
# ValueError: could not convert string to float: 'python'
# 字符串中是字符型数据则不能转换为float类型数据
print(float(str3))
```

## 4、算数运算符

- `+ - * / // % **`
- `//`取商
- `%`取余
- `**`幂次运算

```python
#  + - * / % // **

# 案例:求梯形的面积
# a = float(input('请输入梯形的上底长度:'))
# b = float(input('请输入梯形的下底长度:'))
# h = float(input('请输入梯形的高:'))
#
# print(f'梯形的面积为{(a + b) * h / 2}')

# 算数运算符优先级可以使用小括号控制,  先乘除后加减,同级运算从左至右依次运算

float1 = 10.2
int1 = 4
int2 = 11

# +
# 数值型数据(float, int, bool)之间可以进行算数运算
print(int1 + float1)
# 了解  bool 可以参与算数运算  True 代表1  false 代表0
# print(int1 + True)

# -
# 同加法运算一致

# *
print(int1 * int2)
print(int1 * float1)

# /
print(int1 / int2)
print(int1 / float1)

# //(整除)  两个数据相除 取商
# 11 / 4 商 2 余 3
print(int2 // int1)  # 2

# %(取模  取余) 两个数相除  取余
# 11 / 4 商 2 余 3
print(int2 % int1)  # 3

# ** (幂次运算)
# 幂次运算就是求变量的多少次方
# 扩展int1 开根号等于几  int1 ** 0.5
print(int1 ** 2)


# 在除法运算中,结果必定为浮点型
print(9 / 3)  # 3.0
# 浮点型参与运算后,结果一定是浮点型
# 商 3 余 2.2
print(11.2 // 3)  # 3.0
print(9.9 // 3.3)  # 3.0

# print(0.1 + 0.2)   # 0.30000000000000004
```

- 结论算数运算符优先级: + - < * / // % < **

- 如果忘记了也没关系使用()提高运算符优先级即可

```python
print(1 + 2 * 3)

# 先乘除 后加减

# //运算  优先级

print(2 + 11 // 3 ) # 优先级高于+ -
# // 与 * / 平级
print(2 * 11 // 3)
print(11 // 3 * 2)

# % 也和 * / 平级
print(2 + 11 % 3)  # 优先级高于+ -
print(2 * 11 % 3)
print(11 % 3 * 2)

# ** 优先级  高于  * /
print(2 * 3 ** 2)

# 结论算数运算符优先级: + - < * / // % < **
# 如果忘记了也没关系使用()提高运算符优先级即可
```

## 5、赋值符号

- = ：将等号右侧的值赋值给等号左侧的变量
- 可以给单个变量赋值： 变量= 值
- 可以给多个变量赋不同的值 ： 变量1， 变量2. 变量3 = 值1， 值2， 值3
- 可以给多个变量赋相同的值：变量1 = 变量2 = 变量3 = 值

```python
# = (在Python中等号不是判断相等的而是赋值使用)
# 赋值格式: 变量名 = 值

# 给单个变量赋值
a = 1

# 同时给多个变量赋值
# 等号左侧的变量数量一定要等于等号右侧的值的数量, 否则报错
name, age, gender = 'xiaoming', 18, '男'
# ValueError: not enough values to unpack (expected 3, got 2)
# name, age, gender = 'xiaoming', 18
print(name, age, gender)

# 同时给多个变量赋相同的值
# 此种情况前边可以有多个变量,但是最后只能有一个值,否则报错
a = b = c = 10
# a = b = c = 10 = 20
print(a, b, c)

# 等号左侧一定要是变量,右侧可以是值或者已经被定义的变量
int1 = 2
int2 = int1
print(int1, int2)
```

## 6、复合赋值运算符

- ```
  += -= *= /= //= %= **=
  ```

- 复合赋值运算符等号左侧一定是已经被定义的变量
- 复合赋值运算符右侧是已经被定义的变量或者值

```python
# += -= *= /= //= %= **=

a = 1
# a += 1  >>> a = a + 1  将a中的变量取出与1相加得到的数值赋值给a
a += 1
print(a)

# 符合赋值运算符等号左侧只能是已经定义的变量
# 符合赋值运算符等号右侧可以是已经定义的变量或者值

# NameError: name 'b' is not defined
# b必须已经被定义  b = b - 1  先计算b - 1  此时b必须存在
# b -= 1
# print(b)


# 复合赋值运算符不能连续使用
# a += 1 += 2


# 练习
a = 2

a *= 2
print(a)

b = 12
b //= 5
print(b)
```

## 7、比较运算

- `< > <= >= == !=`
- 比较运算就是比较数据值的大小
- 比较运算可以连续使用
- 比较运算中比较相等使用==  而 不能使用 = （赋值运算符）

```python
# < > <= >= !=  ==
# 比较运算符运算结果为bool值,如果成立,则返回True 如果不成立则返回False
print(1 < 2)  # True
print(5 > 6)  # False
print(1 >= 0)  # True
print(4 != 4)  # False

# 比较运算符可以连续使用(Python中的特性)
age = 13
print(12 < age < 30)  # True
# 不等号也可以连续使用
print(12 < age != 13)  # False

# <>  不可以使用
# print(1 <> 3)

# 判断是否相等使用==
print(age == 13)  # True
print(age == 11)  # False
# TypeError: 'age' is an invalid keyword argument for print()
# =是赋值运算不能判断是否相等
# print(age = 12)
```

## 8、逻辑运算

- and 同真即真
- or 同假即假
- not  真变假  假变真

```python
# and 同真即真
print(True and False)  # False
print(True and True)  # True
print(False and True)  # False
print(False and False)  # False

# or 同假即假
print(True or False)  # False
print(True or True)  # True
print(False or True)  # False
print(False or False)  # False

# not 真变假, 假变真
print(not True)  # False
print(not False)  # True

# 结论:逻辑运算符的运算结果都是bool类型数据

# 练习:
print(not(1 > 2 and 4 < 5))
```

## 9、短路运算

```python
# 短路运算:
a = 1
b = 2
# 当逻辑运算的第一个表达式已经可以决定整个逻辑运算的值的时候,后边的表达式将不会被运行
print(a > b and a < b)

# 在数值型数据中,非0即真
# 在容器型数据中,非空即真
# None 代表False
print(False and 1)  # False
print(0 and True)  # 0
print(12 or False)  # 12
print(None and True)  # None

print(True and False)  # False
print(True and 15)  # 15

print(False or "")  # ""
```

## 10、分支语句

- 单一条件判断

```python
if 条件：
		条件成立时执行的代码
# 格式:
'''
if 条件:
    条件成立时执行的代码
'''

age = int(input('请输入你的年龄:'))

# 上网
if age >= 18:
    print('小帅哥快来玩啊')

print('回家睡觉')
```

- 对立条件判断

```python
if 条件：
		条件成立时执行的代码
else：
		条件不成立时执行的代码
  
  
# if ... else ...
'''
if 条件:
    条件成立时执行的代码
else:
    条件不成立时执行的代码
'''

# 使用分支语句,只有一个分支内的代码会被执行
age = int(input('请输入你的年龄:'))

if age >= 18:
    print('小帅哥,快来玩啊')
else:
    print('老板我就进去看别人玩')

print('回家睡觉')
```

- 多条件判断

```Python
if 条件1：
		条件1成立时执行的代码
elif 条件2：
		条件2成立时执行的代码
elif 条件3：
		条件3成立时执行的代码
else：
		所有条件均不成立时执行的代码
  
  
# 格式;
'''
if 条件1:
    条件1成立时执行的代码
elif 条件2:
    条件2 成立时执行的代码
elif 条件3:
    条件3成立时执行的代码
else:
    所有条件均不成立时执行的代码
'''

# 需求:搭讪,主要是为了问路

age = int(input('请输入对方的年龄:'))

if age > 100 or age < 0:
    print('数据错误')
elif 0<= age <= 18:
    print('小妹妹你真可爱')
    print('叔叔 我们不约而同的认为我很可爱')
elif 18< age <= 30:
    print('美女,你真漂亮')
    print('流氓')
elif 30 < age <= 60:
    print('阿姨,我不想努力了')
    print('瞧你长那样')
else:
    print('老奶奶,您真慈祥')
    print('我北京三套房')

```

- 注意事项：
  - 分支语句中条件可以是bool值或者能够转换为bool值的数据或者表达式
  - 分支语句中只能执行其中一个分支的命令，如果一个条件符合则后续条件均不会进行判断

```python
# 什么样的内容可以作为条件出现?
# bool值或者可以转换为布尔值的数据或表达式
# 表达式:经过运算或者执行后,可以得到一个值的代码块或语句都是表达式
# 分支结构,循环结构,赋值,函数定义 不能作为条件出现
# if  a = 1:
#     print('qqwe')
# a = 1
# if if a==1:
#     print()

# 分支语句中只有一个分支的命令会被执行
# 如果运行过程中其中一个条件成立,则后续所有条件不会进行判断
age = int(input('请输入对方的年龄:'))

if age > 100 or age < 0:
    print('数据错误')
elif age <= 18:
    print('小妹妹你真可爱')
    print('叔叔 我们不约而同的认为我很可爱')
elif age <= 30:
    print('美女,你真漂亮')
    print('流氓')
elif age <= 60:
    print('阿姨,我不想努力了')
    print('瞧你长那样')
else:
    print('老奶奶,您真慈祥')
    print('我北京三套房')
```

## 11、分支语句嵌套

- 在分支语句中包含其他分支语句

```python
# 嵌套:在if语句控制的代码块中存在其他的if语句

# 需求: 如果有钱可以上车(money) 如果上车了又座位可以坐下(seat)

money = 12
seat = True

if money >= 2:
    print('快上车,里边有大座')
    if seat == True:
        print('快坐下吧,别累着')
    else:
        print('我骗你的你能咋办')
else:
    print('穷鬼,跟着车跑吧,不等你')

# 判断时正数负数 还是正奇数正偶数,负奇数,负偶数
# num = 12
# if num < 0:
#     print('负数')
#     if num % 2 == 0:
#         print('负偶数')
#     else:
#         print('负奇数')
# else:
#     print('正数')
#     if num % 2 == 0:
#         print('正偶数')
#     else:
#         print('正奇数')

num = -13
if num < 0:
    print('负', end='')
    if num % 2 == 0:
        print('偶数')
    else:
        print('奇数')
else:
    print('正', end='')
    if num % 2 == 0:
        print('偶数')
    else:
        print('奇数')
```

## 12、猜拳游戏

```python
# 需求:
# 玩家键入拳型,电脑随机出拳
# 比对玩家和电脑的拳型,如果玩家胜则输出玩家获胜,如果电脑获胜则输出电脑获胜,如果平局则输出平局

# # 玩家键入拳型
# player = int(input('请输入您要出的拳型:(0 石头 1 剪刀 2 布)'))
# # 电脑随机出拳
# computer = 2
# # 比对拳型
# # 玩家获胜情况: p: 0 c: 1  |  p: 1  c: 2  | p : 2  c : 0
# if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
#     # 输出结果
#     print('玩家获胜')
# elif player == computer:
#     # 输出结果
#     print('平局')
# else:
#     # 输出结果
#     print('电脑获胜')


'''
p  c  差值
0  0  0    平局
0  1  -1    p
0  2  -2    c
1  0  1     c
1  1  0     平局
1  2  -1    p
2  0  2     p
2  1  1     c
2  2  0     平局

找规律: 结果为0  平局
结果为 -1 或 2 玩家获胜
结果为 -2 或 1 电脑获胜
'''
# 玩家键入拳型
player = int(input('请输入您要出的拳型:(0 石头 1 剪刀 2 布)'))
# 电脑随机出拳
# 在计算机中如果想要生成随机数据可以使用random模块进行生成
import random # 导入模块
# 生成随机数  random.randint(m,n) 生成[m, n]区间内的任意一个整数
computer = random.randint(0,2)
result = player - computer
# 比对拳型
# 玩家获胜情况: p: 0 c: 1  |  p: 1  c: 2  | p : 2  c : 0
if result == -1 or result == 2:
    # 输出结果
    print('玩家获胜')
elif result == 0:
    # 输出结果
    print('平局')
else:
    # 输出结果
    print('电脑获胜')
```

## 13、三目运算

- 格式：条件成立时返回的数据 if  条件 else 条件不成立时返回的数据

```python
# 三元运算符又叫三目运算
# 格式: 条件成立时返回的数据  if 条件 else 条件不成立时返回的数据

# 需求输出a和b中的最大值

a = 4
b = 5
max1 = a if a > b else b
print(max1)
```

