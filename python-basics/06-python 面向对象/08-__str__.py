# __str__()方法是在数据被转换为str类型时自动调用的方法

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # 在__str__方法中只能返回字符串类型数据,否则就会报错
        # TypeError: __str__ returned non-string (type int)
        # return 123
        # return None
        return f'我的名字是{self.name}, 我的年龄是{self.age}'


p1 = Person('Rose', 18)
# 如果我们打印p1会在控制台输出什么? # <__main__.Person object at 0x7fb70db848e0>
# 默认会输出对象类型,和内存地址
# print(p1)
# 我们如果让其在打印时输出我们想要输出的内容?  重写str方法

# 重写str方法后
# 结论:打印p1时,会自动调用__str__()方法
print(p1)

# 是因为print方法我们才将p1变为我们改写的str方法中的内容么?  不是
# 其实我们再执行print时,会做一次隐式的数据类型转换 也就是使用str(对象)

str1 = str(p1)
print(str1)

# 在什么场景下会自动调用__str__呢?
# 1.强制类型转换  str(对象)
# 2.隐式类型转换  %s 作为占位符,接收p1   print打印