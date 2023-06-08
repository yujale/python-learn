## 直播注意事项

1. ### 作息时间

- 上午：9-12（讲课+练习）
- 下午：2-5（讲课+练习）
- 晚自习：6-8（晚自习：整理当天学习内容，写作业，答疑）

2. ### 提问要求

- 遇到问题先自己翻译一下问题。
- 答疑方式：
  - 把代码和报错提供给老师
  - 通过远程协作完成
  - 语音沟通（加企业微信）

3. ### 学习态度

- 同学之间互相监督
- 按组进行作业提交
  - 老师根据链接进行作业查询（完成率，抽查作业情况）
  - 每组组员将作业提交给组长：（将作业批改，并与组员沟通）
- 按组提交笔记
  - 如果时间充裕，自己整理当天笔记
  - 如果时间不充裕，使用老师整理的Xmind进行填充，扩展

4. ### 注意安全

- 班级内学员尽量在往返途中不要到处乱跑
- 在班级内全程做好防护



## 1、不定长参数

- 位置不定长参数（*args）：多余的位置参数，可以被args接收,并且打包为一个元组，保存在args当中。

```python
# 不定长参数主要就是在定义函数时,不确定参数的个数时即可进行不定长参数的书写

'''
位置不定长参数的定义格式:
def 参数名(*args):
    函数体
'''


# def func(*args):
#     print(*args)  # 相当于书写内容为  print(1,2,3)
#
#
# func(1, 2, 3)
# print(1, 2, 3)

# args变量到底内部是什么样子的?
# def func(*args):
#     return args

# 数据传入函数内部时,将传入的多个数据进行打包,转换为一个元组,被args接收.并且在函数体内部可以使用该元组参与运算
# print(func(1, 2, 3))  # (1, 2, 3)


# 案例:
# 输入不确定数量的多个值,判断其中的最大值

def max1(*args):
    max_num = args[0]  # 如果max_num = 0 这个时候我们所有值都没负的时候会判断出错
    for i in args:
        if i > max_num:
            max_num = i
    return max_num


print(max1(1, 4, 5, 3, 6, 12, 3))

# 如果输入的数值全部为负呢?
print(max1(-1, -2, -5))
```

- 关键字不定长参数（**kwargs）：将多余的关键字 参数，打包为一个字典，保存在kwargs当中

```python
# 关键字不定长参数,可以接收多个未定义参数的关键字赋值

'''
关键字不定长参数的格式:
def 函数名(**kwargs):
    函数体
'''


# TypeError: 'a' is an invalid keyword argument for print()
# def func(**kwargs):
#     print(**kwargs)  # 相当于给print输入了多个关键字参数  print(a=1, b=2, c=3)
#
#
# func(a=1, b=2, c=3)

# 使用**kwargs可以将关键字参数进行传递
# def func(**kwargs):
#     print(1, 2, **kwargs)  # 相当于print(1, 2, sep='&', end='a')
#
#
# func(sep='&', end='a')

# kwargs 内部到底是什么存储结构呢?
def func(**kwargs):
    # kwargs 在从传参之后,会将实参位置的所有未定义参数的关键字参数转换为字典的键值对,保存在kwargs当中
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}


func(a=1, b=2, c=3)


# 案例:
# 使用创建一个函数可以保存学员的全部信息,并将其储存到字典当中

def student_info(**kwargs):
    print(f'学员信息为:{kwargs}')


student_info(name='xiaoming', age=18, gender='男')
```



## 2、函数定义和调用时各类参数的排布顺序

- 形参： 位置参数》》位置不定长参数》》缺省参数》》关键字不定长参数
- 实参：顺序赋值》》关键字参数赋值
- 在开发中除非有特殊需求，一般参数种类不超过三种，参数个数不超过5个，如果种类或数量太多，会造成我们开发中沟通成本加大

```python
# 在定义函数时:位置参数,缺省参数,位置不定长参数,关键字不定长参数  到底在定义时怎么排列呢?
# 调用函数时:顺序赋值, 关键字赋值  调用时的传参顺序是什么样的呢?


# 定义函数时:形参

# 位置参数和缺省参数的位置关系:
# def func1(a, b, c=10):
#     print(a)
#     print(b)
#     print(c)
# 缺省参数c 能否放到a,b之前或之间
# SyntaxError: non-default argument follows default argument
# 有默认值的参数只能放到没有默认值的参数之后,不能前置
# def func1(c=10,a, b ):
#     print(a)
#     print(b)
#     print(c)
#
# # 赋值时可以不给c传参因为其有默认值
# func1(1, 2)

# 结论: 在定义函数时,位置参数在缺省参数之前

# 位置参数,缺省参数,位置不定长参数之间的位置关系
# 顺序赋值多个参数,位置参数优先接收,然后缺省参数接收数据,多余的参数被args以元组形式打包接收
# 思考:为什么要设置缺省参数呢?  一般情况下,缺省参数是不进行赋值的,因为绝大多数情况下都会赋默认值,极少情况下会使用关键字参数赋值
# 如果放到*args之前,是不是每次给*args赋值,都要给缺省参数赋值,所以不是很方便
# 综上考虑,我们决定将缺省参数放到*args之后

# def func2(a, b, c=10, *args):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
# 传值逻辑如下:1.先给位置参数赋值 2.多余的未接收数据,被args打包为一个元组进行接收  3.缺省参数一般情况下不赋值,如果需要赋值,使用关键字参数赋值
# 在官方文档或者系统模块中,都是这种顺序书写的
# def func2(a, b, *args, c=10):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#
#
# func2(1, 2, 3, 4, 5)


# 结论:在定义函数时,先写位置参数,再写位置不定长参数,最后写缺省参数


# 位置参数,缺省参数,位置不定长参数,关键字不定长参数之间的位置关系

# def func2(a, b, *args, c=10, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
#
#
# func2(1, 23, 4, 5, 3, 2, c=1, name='xiaoming', age=18)

# 思考:**kwargs可不可以往前放
# **kwargs只能放到最后,否则会报错

# 结论:形参排布顺序为:位置参数>>位置不定长参数>>缺省参数>>关键字不定长参数


# 调用函数时:实参

def sum1(a, b):
    print(a + b)

# SyntaxError: positional argument follows keyword argument
# 顺序赋值,不能在关键字赋值之后
# sum1(a=1, 2)

# 结论,调用参数时,先使用顺序赋值,后使用关键字赋值
```

## 3、组包和拆包

- 组包：将多个数据，组合为一个容器类型，进行使用或变量保存
- 拆包：将一个容器类型，进行拆分，其中的每一个元组赋值给其他的变量

```python
# 组包:就是讲多个值进行组合,打包为一个容器类型的过程
# 拆包:就是讲一个容器类型,拆分成多个数据,分别赋值给多个变量的过程

# 组包
def func1():
    return 1, 2, 3, 4


# func1返回了多个数据,Python自动将其打包为一个元组,这个过程就是组包
print(func1())  # (1, 2, 3, 4)
# 将多个数据打包整合为一个容器,赋值给变量,这个就是组包过程
a = 1, 2, 3, 4
print(a)

# 拆包(解包)
# 将等号右侧的列表,拆分为四个数据元素,分别赋值给a,b,c,d这个过程就是拆包
a, b, c, d = [1, 2, 3, 4]
print(a, b, c, d)

# 之前我们在循环汇总用过拆包过程
list1 = [1, 2, 3, 4]
for index, value in enumerate(list1):
    print(index, value)

dict1 = {'name': 'xiaoming', 'age': 18}
for key, value in dict1.items():
    print(key, value)

# 同时应用组包和拆包的案例

a = 1
b = 2
# 需求:将a, b进行互换值
# 这个互换过程,是先讲a,b的值提取出来,组包为一个元组,然后进行拆包,将元组内的两个数据分别赋值给,a,b变量
a, b = b, a
print(a, b)

# 注意:字典可以拆包么?可以
dict1 = {'a': 1, 'b': 2, 'c': 3}
# 对字典进行拆包,得到的是字典的键
char1, char2, char3 = dict1
print(char1, char2, char3)

# 集合可以拆包么?  可以
# 对于集合进行拆包,没有任何问题,但是一般不会这样做,因为赋值顺序无法指定
set1 = {'Tom', 'Bob', 'Rose'}
a, b, c = set1
print(a, b, c)
```

## 4、引用

- 数据的三个维度：值， 数据类型，唯一标识
  - 值： 数据计算时使用的值
  - 数据类型：数据的存储类型
  - 唯一标识：id ，也就是数据的内存地址的标识
- 如果我们想要判断id 或者说唯一标识是否相等，我们使用is进行判断

```python
# 在Python中所有的数据分为三个维度: 值(判断==), 数据类型(int...float...), 唯一标识(id)

# 值相等的数据,唯一标识和数据类型不一定相等
bool1 = False
int1 = 0
# 0 和False的值相等
print(bool1 == int1)  # True
# 数据类型不等
print(type(bool1) == type(int1))  # False
# 唯一标识不等
# id 判断数据是否是同一内存空间中的数据(同一内存空间中的数据必相等)
print(id(bool1) == id(int1))  # False

# 值和数据类型相等的,唯一标识不一定相等
list1 = [1, 2, 3]
list2 = [1, 2, 3]
# list1 和list2 值相等
print(list1 == list2)  # True
# list1和list2 数据类型相等
print(type(list1) == type(list2))  # True
# list1 和list2 的唯一标识不等,也就是说,其所在的内存空间不一致
print(id(list1) == id(list2))  # False

# 唯一标识相等的, 值和数据类型必然相等
# 在同一内存空间中只能储存同一个值
str1 = 'abc'
str2 = 'abc'
# str1 和str2 的唯一标识相等
print(id(str1) == id(str2))  # True
# 数据类型相等
print(type(str1) == type(str2))  # True
# 数据值相等
print(str1 == str2)  # True

# 怎样判断id  唯一标识是否相等呢?  is关键字
# 使用is可以判断是否为同一个内存空间中的数据
print(list1 is list2)  # False
print(str1 is str2)  # True
```

## 5、可变类型和不可变类型

- 可变类型：内存空间中的数据可以被修改的数据类型
  - list  set  dict
- 不可变数据类型：内存空间中的数据不可以被修改的数据类型
  - int  float  bool str  tuple

```python
# 传参或者变量的传递是进行了值的传递 还是进行了引用地址的传递呢?

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
#  id的值,我们称呼他为引用地址,list1 和list2 的引用地址不相同
print(id(list1))  # 140652966394496
print(id(list2))  # 140652968507776

# 如果我向list1 中添加以数字,次数list2 中的值为多少? [1,2,3,4]
list1.append(5)
print(list1)
print(list2)
# 在list1中添加了数据,那list1的引用地址会发生变化么? 不会变化
# list1,在使用append方法时,是将内存空间中的值进行了变化,没有修改内存地址,所以id值不变
print(id(list1))  # 140652966394496

# 如果我们使用list1 = list2,list1的引用地址发生变化了么?  变化
list1 = list2
# 在对list1赋值时,list2 将list1中的内存地址赋值给了list1,此时,list1和list2指向同一块内存空间
print(id(list1))  # 140652968507776

# 如果在list1中删除下标为1的元素,list2 会发生变化么? 会变化
# list1  和list2 指向同一块内存空间,所以内存空间中的数据发生了改变,list1 和list2 均发生了变化
list1.pop(1)
print(list1)  # [1, 3, 4]
print(list2)  # [1, 3, 4]

# list 内存空间中的数据可以发生改变,这种数据类型我们称之为可变数据类型

# 练习:
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list1 = [1, 2, 3, 4, 5]
list2 = list1
list1.pop(2)
list1 + list2
# list1 和list2  分别是多少
print(list1)
print(list2)

# 练习:
str1 = '12345'
str2 = '12345'
str1 = str2
str1 = '123'
str2 + str1
print(str1)
print(str2)

str1 = '123'
str2 = '123'
print(id(str1))  # 140509725727984
print(id(str2))  # 140509725727984

# 我么可以修改str内部的元素么?  不可以
# TypeError: 'str' object does not support item assignment
# str1[0] = '2'
# 既然内部元素不可修改,系统定义其值相同时,数据引用地址也相同

# 我么称这种内存空间中的数据无法被修改的值为不可变数据类型


# 结论:
# 可变数据类型:  列表,集合,字典
# 不可变数据类型: 字符串,元组,整型,浮点型,布尔型

# 结论:在数据的传递过程中,是引用传递,不是值的传递
```



## 6、引用当做参数传递

- 在函数传参过程中，变量会以引用的形式进行传参，也就是说我们的变量或参数传递是引用传递，不是值传递
  - 如果参数是可变数据类型，那么在函数内修改其引用地址指向空间内的数据，外部数据同时发生变化
  - 如果参数是不可变数据类型，其实也是引用传递，只不过引用地址指向的数据空间中的数据无法被修改

```python
# 将数字1所在空间的引用地址赋值给了a
# a = 1
# 将a所保存的引用你地址给了b
# b = a


def func(num_list):
    print(id(num_list))  # 140490414045760
    num_list.append(2)
    return num_list


# 在进行参数传递时,是进行了地址传递,将list1 的引用地址传递给了num_list,num_list 修改内存空间中的数据时,list1,也会发生变化
list1 = [1, 2, 3, 4]


# print(id(list1))  # 140490414045760
# print(func(list1))
# print(list1)

def func2(num_list):
    print(id(num_list))  # 140326362233472
    # 无论什么情况下,使用=赋值运算,就是讲等号右侧数据的引用地址,赋值给等号左侧的变量
    num_list = [1, 2, 3, 4, 5]
    print(id(num_list))  # 140466340833664
    return num_list


print(id(list1))  # 140326362233472
print(func2(list1))  # [1, 2, 3, 4, 5]
print(list1)  # [1, 2, 3, 4]


# 不可变数据类型
def func1(char1):
    print(id(char1))  # 140228523715632
    # 不可变数据类型,在进行参数传递时,也是引用传递,但是他无法修改原有数据空间内的数据,如果想要修改只能改变引用地址,重新赋值(只有=才有改变引用的功能)
    char1.replace('a', 'b')
    return char1


str1 = 'abc'
print(id(str1))  # 140228523715632
print(func1(str1))  # abc
print(str1)  # abc
```

## 7、学生管理系统

```python
# 需求拆分:
'''
1.展示学生管理系统的功能有哪些,引导用户键入序号选择功能
2.获取用户键入的功能
3.分析具体要执行哪一项功能
4.执行功能
'''


def print_all_option():
    """用户功能界面展示"""
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员信息')
    print('2: 删除学员信息')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 遍历输出所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


def choose_option(num):
    """分析要执行哪一项功能"""
    if num == '1':
        # 添加学员函数
        add_student_info()
    elif num == '2':
        # 删除学员函数
        delete_student_info()
    elif num == '3':
        # 修改学员函数
        modify_student_info()
    elif num == '4':
        # 查询学员函数
        search_student_info()
    elif num == '5':
        # 展示所有学员函数
        show_students_info()
    elif num == '6':
        # 退出程序函数
        exit_program()
    else:
        print('无此选项,请重新输入')


def add_student_info():
    """添加学员信息"""
    # 1.用户输入学员信息
    # 1.1当用户输入的id值已经存在时,则不让其继续输入,警告,该id已经存在
    stu_id = input('请输入要添加学员的id:')
    # 获取students_list中所有学员的id值(推导式)
    students_id = [i['id'] for i in students_list]
    # 1.2 比对id是否存在,存在则不允许运行
    if stu_id in students_id:
        print('该id值已经存在,无法添加学员')
    else:
        name = input('请输入要添加学员的姓名:')
        age = input('请输入要添加学员的年龄:')
        mobile = input('请输入要添加学员的手机号:')
        # 2.将学员信息添加到students_list当中
        students_list.append({'id': stu_id, 'name': name, 'age': int(age), 'mobile': mobile})
        print('学员添加完成')


def delete_student_info():
    """删除学员信息"""
    # 1.获取要删除学员的id值
    stu_id = input('请输入要删除学员的id:')
    # 2.判断该学员是否存在,如果存在则删除该学员,如果不存在,则提示该学员不存在
    for stu_info in students_list:
        # 判断是否是要删除的学员
        if stu_info['id'] == stu_id:
            # 删除学员并跳出函数
            students_list.remove(stu_info)
            print('该学员已删除')
            return
    else:
        # 执行该命令警告用户没有该学员
        print('该学员不存在,无法删除')


def modify_student_info():
    """修改学员信息"""
    # 1.输入要修改的学员的id值
    stu_id = input('请输入您要修改学员的id:')
    # 2.如果学员存在就修改学员信息,如果不存在则进行提示,学员不存在
    for stu_info in students_list:
        if stu_info['id'] == stu_id:
            # 学员信息修改
            name = input('请输入您要修改为的名字:')
            age = input('请输入您要修改为的年龄')
            mobile = input('请输入您要修改为的手机号:')
            stu_info['name'] = name
            stu_info['age'] = age
            stu_info['mobile'] = mobile
            print('学员信息修改完成')
            return
    else:
        print('该学员不存在,修改失败')


def search_student_info():
    """查询学员信息"""
    # 1.输入要查询学员的id值
    stu_id = input('请输入要查询学员的id:')
    # 2.判断id值是否存在,如果存在则展示,如果不存在,则警告学员不存在
    for stu_info in students_list:
        if stu_info['id'] == stu_id:
            print(
                f'学员的学号是:{stu_info["id"]}, 学员的姓名是:{stu_info["name"]}, 学员的年龄是:{stu_info["age"]}, 学员的手机号是:{stu_info["mobile"]}')
            return
    else:
        print('该学员不存在,查询失败')


def show_students_info():
    """展示所有学员信息"""
    for stu_info in students_list:
        print(
            f'学员的学号是:{stu_info["id"]}, 学员的姓名是:{stu_info["name"]}, 学员的年龄是:{stu_info["age"]}, 学员的手机号是:{stu_info["mobile"]}'
        )


# def exit_program():
#     # import sys
#     # # 退出当前程序,结束进程
#     # sys.exit()
#     exit()

def exit_program():
    """结束程序"""
    # 通过控制变量结束死循环
    global is_stop
    # 在修改之前需要进行声明 ,修改的变量为全局变量
    is_stop = True


# # 展示功能界面
# print_all_option()
#
# # 引导用户输入功能序号,并获取序号
# option = input('请输入您要执行功能的序号:')
#
# # 根据获取的序号分析要执行哪些功能
# chose_option(option)


# 思考:学生管理系统,是不是需要输入6  才能退出 不然就一直询问您要输入的选项
# 这中情况下建议使用 while True 构造死循环

students_list = [
    {'id': '001', 'name': 'xiaoming', 'age': 18, 'mobile': '13833838338'},
    {'id': '002', 'name': 'xiaohong', 'age': 18, 'mobile': '13900000000'}
]
is_stop = False

while not is_stop:
    # 展示功能界面
    print_all_option()

    # 引导用户输入功能序号,并获取序号
    option = input('请输入您要执行功能的序号:')

    # 根据获取的序号分析要执行哪些功能
    choose_option(option)
    # 方便展示,显示所有学员信息,开发完成后删除
    # print(students_list)
    input()

# 死循环的退出方式有哪些?
# break
# return
# exit()
# 控制变量
...
```

## 8、函数递归

- 函数内部调用函数本身
- 函数有明确的递归跳出条件
- 不超出最大调用深度

```python
# 函数递归的三个必备条件
'''
1/函数体内部,调用函数本身
2/递归够明确的跳出条件
3/不能超出最大调用深度
'''

# 需求:
'''
func(1) = 1
func(2) = 1 + 2 = func(1) + 2
func(3) = 1 + 2 + 3 = func(2) + 3
func(4) = 1 + 2 + 3 + 4 = func(3) + 4
.....
func(n) = 1 + 2 + 3 .... + n = func(n-1) + n
'''

# RecursionError: maximum recursion depth exceeded
# 这种方式无法跳出递归,所以在使用的时候就会无限递归下去
# def func(n):
#     return func(n-1) + n

'''
func(1) = 1
func(2) = func(1) + 2
func(3) = func(2) + 3
func(4) = func(3) + 4
.....
func(n) = func(n-1) + n
'''

def func(n):
    if n == 1:
        return 1
    return func(n-1) + n


print(func(999))


# Python中默认的最大调用深度,是1000 也就是在Python中函数最多嵌套1000层
# 最大调用深度是为了保证系统性能的,否则无限递归下去,一会内存就满了
# 最大调用深度可以调整,可以调整到非常大的数字只要系统性能跟得上
# RecursionError: maximum recursion depth exceeded in comparison

# 注意事项:
# 在编程初期,尽量少使用递归,但是要理解递归的特性,别人写的递归函数也要能看懂
```

## 9、lambda函数

- 匿名函数，在函数定义时没有函数名
- 可以用变量保存，在变量之后添加括号即可调用

```Python
# lambda表达式,也叫匿名函数
# 格式: lambda 参数: 返回值

# 需求: 根据传入的参数返回最大值  使用lambda函数书写
# 三目运算  :  条件成立时返回的代码 if 条件 else 条件不成立时返回的代码
max_num = lambda a, b: a if a > b else b
# 使用变量可以储存lambda函数
print(max_num(1, 2))
print(max_num(9, 2))

print(type(max_num))  # <class 'function'>


def func():
    print('abc')


print(type(func))  # <class 'function'>
# 通过对数据类型的查看,我们发现lambda和普通函数本质上是一样的,只不过在使用时构造更为简单

# 在使用lambda函数时可以不用变量接收
print((lambda a, b: a if a > b else b)(3, 4))  # 4
# 但是不适用变量接收,lambda函数只能使用一次,使用后集被释放,无法再次使用


# lambda缺点: 没有办法书写负责的函数,因为其没有函数体,只有返回值,所以返回值后边只能书写一个表达式,lambda可读性极差


# 使用lambda完成递归(了解,一般不建议写复杂的代码)
func1 = lambda n: func1(n - 1) + n if n != 1 else 1
# RecursionError: maximum recursion depth exceeded
# 超出最大调用深度,没有明确的递归跳出条件
print(func1(100))

# lambda应用场景
# 可以用于一次性函数使用
# 可以作为函数的参数进行传递

# list  sort(key= )
# lsit sort排序方法中的key所需要的参数就是一个函数,我们可以传入lambda表示

list1 = [{'a': 1}, {'b': 12}, {'c': 10}]
# 排序规则:根据字典的第一个键所对应的值进行排序

list1.sort(key=lambda x:list(x.values())[0])
# 格式: 列表.sort(key = lambda 每次传入的元素: 排序所依据的规则)
print(list1)
```