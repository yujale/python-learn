## 1、循环介绍

- 有条件的重复做相似的事情
- Python中循环分为while 和for

## 2、while循环的使用

- 格式： while 条件： 循环体
- while 循环的三个必要元素
  - while 关键字
  - 循环条件
  - 循环体
- 构造循环要想的四件事
  - 初始状态
  - 循环条件
  - 要重复做的事情
  - 循环控制

- 案例

```python
# 需求:求1-100的累加和

# 初始状态
i = 1
sum1 = 0
while i <= 100:
    # 求累加和
    # sum1 = sum1 + i
    sum1 += i
    # 为下一次循环做准备,自增
    i += 1

print('1-100的累加和是%d' % sum1)
```

```python
# 需求:输出10以内的所有奇数

# 初始状态
i = 1
# 循环结束条件
while i <= 10:
    # 要循环做什么
    if i % 2 != 0:
        print(i)
    # 为下一次循环做准备  自增
    i += 1
```

```python
# 需求: 1-100的偶数累加和
# 初始状态:
i = 1
sum1 = 0  # 累加器
# 循环条件
while i <= 100:
    # 要做什么?
    if i % 2 == 0:
        sum1 += i
    # 为下一次循环做准备  累加
    i += 1

print(f'1-100的偶数累加和是{sum1}')


# 练习 :计算 1-20 的奇数累乘积.
# 初始状态
i = 1
mult1 = 1
# 循环条件
while i <= 20:
    # 要做什么
    if i % 2 != 0:
        mult1 *= i
    # 自增
    i += 1
print(f'1-20的奇数累乘积是{mult1}')
```

## 3、continue和break

- continue ：跳出本次循环，进入下一次循环

```python
# continue: 跳出本次循环,继续执行下一次循环(不会影响循环的次数)

# 需求: 吃苹果,一个五个.吃到第三个 有个虫子,扔掉第三个,继续吃第四个第五个
# 注意,在循环结构中使用continue要在continue之前添加循环变量的自增,否则可能会造成无法跳出循环(死循环)
i = 1
while i <= 5:
    if i == 3:
        print('这个苹果有虫子,给女朋友吃吧')
        i += 1
        continue
    print(f'我吃了{i}个苹果')
    i += 1


# 写法二
# 可以先进行自增,再进行i的调用,此时,就不用担心continue的问题了
i = 0
while i < 5:
    i += 1
    if i == 3:
        print('这个苹果有虫子,给女朋友吃吧')
        continue
    print(f'我吃了{i}个苹果')


# 输出1-10 的数字
# 在循环体中,continue所在的分支中,continue之后不要书写任何代码,永远不可能被执行
i = 1
while i <= 10:
    print(i)
    continue
    i += 1


# break 和continue只能用在循环体中
# if True:
#     print('123')
#     break
#     continue
    
```

- break ： 结束当前循环，后续循环次数不再执行

```python
# break:跳出循环,终止此次循环之后的所有循环

# 吃苹果案例   吃到第三个 吃出半条虫子,后续无心再吃
i = 1
while i <= 5:
    print(f'我吃了{i}个苹果')
    if i == 3:
        print('吃不下了 虫子个太大吃撑了')
        # break之后的所有代码均不执行
        break
    i += 1

print('吃苹果完成')

# 输出1-10 十个数字
# 在循环体中,break所在的分支中,break之后不要写任何代码,不可能执行
# i = 1
# while i <= 10:
#     print(i)
#     break
#     i += 1
```

- break 和continue 只能在循环体中使用

## 4、死循环

- 死循环不是bug，是程序的一种特殊运行状态，程序员可以用死循环做很多事情
- 死循环就是循环条件永远满足的一种循环

```python
# 什么是死循环?  循环条件永远满足,可以持续循环的代码
# 死循环是bug么?  死循环不是bug可以利用死循环做很多事情
# 死循环可以退出么?  可以,死循环就是循环条件永远成立,但是在程序内部可以有很多方法跳出循环,  break

# 猜拳游戏  (死循环进阶版)
# 需求:在原来猜拳游戏的基础上,让电脑和玩家进行猜拳,一方达到3分则退出游戏,宣布获胜方,否则游戏持续进行
# 普通循环
# player_score = 0
# computer_score = 0
# while player_score < 3 and computer_score < 3:
#     # 获取玩家拳型
#     player1 = int(input('请输入您要出的拳型:(0 石头  1 剪刀  2 布)'))
#     # 获取电脑随机拳型
#     import random
#     computer = random.randint(0, 2)
#     result = player1 - computer
#     # 拳型比对     # 输出结果
#     if result == -1 or result == 2:
#         player_score += 1
#         print('玩家获胜')
#     elif result == 0:
#         print('平局')
#     else:
#         computer_score += 1
#         print('电脑获胜')
#     print(f'当前比分为{player_score}:{computer_score}')

# 死循环
player_score = 0
computer_score = 0
while True:
    # 获取玩家拳型
    player1 = int(input('请输入您要出的拳型:(0 石头  1 剪刀  2 布)'))
    # 获取电脑随机拳型
    import random
    computer = random.randint(0, 2)
    result = player1 - computer
    # 拳型比对     # 输出结果
    if result == -1 or result == 2:
        player_score += 1
        print('玩家获胜')
    elif result == 0:
        print('平局')
    else:
        computer_score += 1
        print('电脑获胜')
    print(f'当前比分为{player_score}:{computer_score}')
    if player_score >= 3:
        print('玩家取得最终胜利')
        break
    if computer_score >= 3:
        print('电脑取得最终胜利')
        break
```

## 5、循环嵌套

- 循环体中包含其他循环结构的状态叫做循环嵌套
- 外层循环执行一次，内层循环将全部执行完成

```python
# 需求:锻炼身体:跑步四圈,做深蹲10分钟,此为一组训练,要做三组
# 在循环嵌套中,外层循环执行一次,内层循环全部执行完成
# 做三组训练的初始状态
i = 1
# 做三组训练后退出循环
while i <= 3:
    print(f'第{i}组训练开始')
    # 跑圈初始状态
    j = 1
    # 跑四圈后退出循环
    while j <= 4:
        print(f'我跑了{j}圈')
        # 内层循环自增变量
        j += 1
    print('我做了10分钟深蹲')
    # 外层循环自增变量
    i += 1
```

- 注意：break 和continue 控制的是当前所在的循环结构

```Python
# 需求:锻炼身体:跑步四圈,做深蹲10分钟,此为一组训练,要做三组
# break 和continue 只能控制本身所在的循环结构
# 在循环嵌套中,外层循环的break和cotinue可能会影响内层循环, 但是内层循环中的break和continue不会影响外层循环

# 做三组训练的初始状态
i = 1
# 做三组训练后退出循环
while i <= 3:
    print(f'第{i}组训练开始')
    # 跑圈初始状态
    j = 1
    # 跑四圈后退出循环
    if  i== 2:
        print('我女朋友来找我了 先休息一下')
        i += 1
        continue
    while j <= 4:
        print(f'我跑了{j}圈')
        # 内层循环自增变量
        if j ==3 and i == 2:
            print('太累了 休息下')
            break
        j += 1
    print('我做了10分钟深蹲')
    # 外层循环自增变量
    i += 1
```

## 6、循环嵌套案例：

```python
# 需求:打印五行五列的一个*组成的矩形
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# 打印一行*号,使用while循环实现?
# i = 1
# while i <= 5:
#     print('*', end=' ')
#     i += 1

# 使用while循环将刚才打印的* 输出5次,每次分别占用一行
# i 控制外层循环的次数
i = 1
while i <= 5:
    # j 控制内层循环的次数
    j = 1
    while j <= 5:
        # 打印* 后更换结束符, 防止打印后自动换行
        print('*', end=' ')
        j += 1
    # 一行结束后,强制换行
    print()
    i += 1

# 结论:外层循环控制的是行数, 内层循环控制的是列数 ,外层循环的i变量就是打印时的行号,内层循环的j变量就是打印列时的列号

# 如果现在要打印6行8列的矩阵  i = 6  j = 8

```

```python
# 使用while语句打印三角形,第一行一个* 第二行两个* .....
"""
*
* *
* * *
* * * *
* * * * *
"""

# 外层循环的数量:5 该图形有5行,所以i <= 5
# 内层循环的数量:根据行号进行设定,  第一行 j <= 1  第二行 j <= 2.......

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1
```

```python
# 使用while循环的嵌套打印九九乘法表
"""
1 * 1 = 1
1 * 2 = 2  2 * 2 = 4
.......
"""

# 打印一个九行九列的直角三角形
# 外层循环控制行
i = 1
while i <= 9:
    # 内层循环控制列
    j = 1
    while j <= i:
        # 九九乘法表中,公式规则就是  列 * 行 = 值
        print(f'{j} * {i} = {i * j}', end='\t')
        j += 1
    print()
    i += 1
```

## 7、for循环

- for循环时遍历数据序列，每次获取一个元素，直到元素全部被获取，结束循环。

```python
# for循环的语法结构
"""
for 临时变量 in 数据序列(容器):
    要重复执行的代码
"""
# 循环逻辑:for循环会依次提取数据序列中的元素,每次提取一个,放入临时变量中储存,在循环体中可以使用临时变量,数据序列中有多少个元素,for循环的循环体将会被执行多少次

str1 = 'helloPython'
# 循环遍历str1  遍历:依次提取每一个元素
for i in str1:
    print(i)

# for循环和while循环的区别:
# 1/for循环数据序列,元素提取完成自动停止,不需要使用循环变量
# 2/for循环不需要循环条件,所以也不会有循环条件成立喝不成立的说法
# 3/在开发中我们使用for循环的比例居多,while循环主要是构造死循环结构
# 4/for循环需要配合容器类型(数据序列)进行使用
```

## 8、for循环中的break 和continue

- 和while循环中使用方法一致
  - break：打破循环，后续循环不再执行
  - continue： 结束本次循环，进入下一次循环，不会影响循环次数

```python
# break 打破循环,后续循环不会执行
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e了,结束循环')
        break
    print(i)

# continue 跳出本次循环,进入下一次循环,不会影响循环次数
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e了,进入下一次循环')
        continue
    print(i)

'''
案例：用for循环实现用户登录
① 输入用户名和密码
② 判断用户名和密码是否正确（username='admin'，password='admin888'） 
③ 登录仅有三次机会，超过3次会报错 
'''
# 循环三次
for i in range(3):
    # 获取用户名和密码
    username = input('请输入您的用户名:')
    password = input('请输入您的密码:')
    # 比对用户名和密码
    if username == 'admin' and password == 'admin888':
        print('登录成功')
        break
    else:
        print('用户名或密码错误')
    if i == 2:
        print('三次机会已经用完,账号被冻结')
```

## 9、for循环嵌套

```python
# 打印一个直角三角形

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j} * {i} = {i * j}', end='\t')
    print()

# 在for循环之外还可以调用i 或者j 么? 能

# 在Python中for循环中创建的临时变量可以被外界调用,但是不要用
# print(i)
# print(j)
# 使用for循环临时变量可能会出现报错
# for i in range(1,1):
#     print(123)

# 当for循环执行后,没有一次进入循环体内,也就是遍历的序列是一个空序列,那么临时变量将不会被定义,所以不要使用
# NameError: name 'i' is not defined
# print(i)
```

