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