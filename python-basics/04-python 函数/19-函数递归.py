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
    return func(n - 1) + n


print(func(999))

# Python中默认的最大调用深度,是1000 也就是在Python中函数最多嵌套1000层
# 最大调用深度是为了保证系统性能的,否则无限递归下去,一会内存就满了
# 最大调用深度可以调整,可以调整到非常大的数字只要系统性能跟得上
# RecursionError: maximum recursion depth exceeded in comparison

# 注意事项:
# 在编程初期,尽量少使用递归,但是要理解递归的特性,别人写的递归函数也要能看懂