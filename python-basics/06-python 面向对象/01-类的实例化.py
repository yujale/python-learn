# 类的实例化又称为创建对象
# 定义一个类
class Student(object):
    # 定义方法.定义方式和函数定义类似
    def study(self):
        print('我在听直播课,贼有意思,就是学习非常不努力我也能听懂')

    def eat(self):
        print('我在吃脑白金,补补脑子继续学习')


# 类的实例化(创建对象)
# 格式: 类名()

s1 = Student()
# 我们可以直接打印对象,得到的是其所对应的类和所在的内存地址
print(s1)  # <__main__.Student object at 0x7f9be20848e0>
# 也可以打印对象的类型,其实就是我们创建对象所使用的类
print(type(s1))  # <class '__main__.Student'>

# 实例可以调用实例方法
s1.study()
s1.eat()

# 理论上类可以创建无数个实例对象
s2 = Student()
print(s2)

# 类名的定义要使用大驼峰命名法
# 类名严格区分大小写,类名遵循标识符的命名规则
# class ChineseStudent():
#     pass
#
# s3 = Student()
# s4 = student()
# s3.eat()
# s4.eat()