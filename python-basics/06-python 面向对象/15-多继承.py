# 多继承:一个类定义时,继承了多个父类,同时可以使用多个父类中的方法或者属性
# 格式: class 子类名(父类名1, 父类名2):

class Father(object):
    def dance(self):
        print('我现在要跳一个舞,赶紧出去')

    def sing(self):
        print('我要唱一个学猫叫,一起来')


class Mother(object):
    def dance(self):
        print('我现在要跳一个广场舞,离我远点,不然摔倒了赖你')

    def sing(self):
        print('我要唱一个大河向东流,赶紧跑')


# 同时继承两个父类,则在使用子类对象时可以调用两个父类中的所有非私有属性和方法
# class Son(Father, Mother):
#     pass
#
#
# s1 = Son()
#
# s1.dance()
# s1.sing()

# 疑问: 如果两个父类中有重名方法该怎么办?
# 在下述情况下,只会调用Father类中的sing和dance方法
# class Son(Father, Mother):
#     pass
#
#
# s1 = Son()
#
# s1.dance()
# s1.sing()

# 如果我将两个父类的顺序进行调换
# 此时,只会调用Mother类中的sing 和dance方法
class Son(Mother, Father):
    pass


s1 = Son()

s1.dance()
s1.sing()

# 结论:如果存在同名方法,在继承时,谁的继承位置更靠前就调用谁内部的代码