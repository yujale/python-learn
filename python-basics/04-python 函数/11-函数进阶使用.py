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