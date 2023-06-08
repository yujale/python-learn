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
print(__name__)  # __main__


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