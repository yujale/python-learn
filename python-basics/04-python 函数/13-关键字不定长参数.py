# 关键字不定长参数,可以接收多个未定义参数的关键字赋值

"""
关键字不定长参数的格式:
def 函数名(**kwargs):
    函数体
"""


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