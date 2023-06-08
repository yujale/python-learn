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

list1.sort(key=lambda x: list(x.values())[0])
# 格式: 列表.sort(key = lambda 每次传入的元素: 排序所依据的规则)
print(list1)