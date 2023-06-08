a = 1


class Apple(object):
    num = 10

    def __init__(self):
        self.eat_num = 0

    def eat(self):
        # 每次吃苹果,当前的食用数量加1
        self.eat_num += 1
        # 每次吃苹果,让苹果总数 -1
        Apple.num -= 1

    # 当方法中不适用实例属性和实例方法,只会使用到类属性和类方法的时候我们就选择类方法
    # 因为类方法,不需要创建实例去进行调用,可以直接使用类名调用
    # 类方法 定义格式:在方法上方加一个 @classmethod
    @classmethod
    def eat_apple_num(cls):
        # 在类方法中传入的cls即为当前类的类名
        # 使用cls.类属性名   >>>>  Apple.类属性名
        print(f'一共被吃了{10 - cls.num}个,还剩{cls.num}个')


# 类方法的调用
# 格式: 类名.类方法名
Apple.eat_apple_num()

# 创建对象
a1 = Apple()
a2 = Apple()
a3 = Apple()
a4 = Apple()
# 吃苹果
a1.eat()
a2.eat()
a3.eat()
a4.eat()
a4.eat()

# 调用类方法
Apple.eat_apple_num()

# 查看每人吃了几个苹果
print(a1.eat_num)
print(a2.eat_num)
print(a3.eat_num)
print(a4.eat_num)

# 类方法可以使用对象调用么?
# a1.eat_apple_num()  不推荐这样使用