class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def driver(self):
        print('开车太好玩了 ,10迈,太快了')


class Father(Person):
    # 如果我们现在想在原有父类方法基础上扩展,例如我们现在需要重写一个init方法
    # 可以接收 name, age ,gender三个属性
    def __init__(self, name, age, gender):
        # 在父类方法中已经添加了name,和age我们可不可以直接使用呢???
        super().__init__(name, age)
        # 在父类方法的基础上我们在添加一个子类方法独有的功能
        self.gender = gender

    def driver(self):
        print('我要去天安门完,开挖掘机不让我进')

    def __str__(self):
        return f'我的姓名是{self.name},我的年龄是{self.age},我的性别是{self.gender}'


class Son(Father):
    def driver(self):
        # 调用Person中的dirver
        # TypeError: driver() missing 1 required positional argument: 'self'
        # Person.driver()
        Person.driver(self)
        # Monkey.driver(Monkey())
        # 从Father类的上一级类开始查找方法,并进行调用
        super(Father, self).driver()

        # 调用Father中的dirver
        super().driver()
        # 格式:super(从哪个类的上一级开始查找,self).方法名()
        # 如果类名是当前类,可以省略括号内的内容
        super(Son, self).driver()
        # 书写特有功能


# 所有的参数都传递到了Father类中,并且添加为当前对象的属性
print(Father('Jack', 28, '男'))
s1 = Son('xiaoming', 12, '男')
s1.driver()

# 子类中调用父类方法的三种方式:
# super().方法名()   # 只能调用当前类的上一级类中的方法或函数
# 类名.方法名(self)  # 所使用的类名,必须在当前类的继承关系中
# super(要从哪一个类的上级类开始查询,self).方法名()  # 类名必须在继承关系内,如果类名是当前所在的类,则可以将括号内内容省略,就是第一中方式

# class Monkey(object):
#     def driver(self):
#         print('我在骑自行车')
#
# m1 = Monkey()
# # 如果使用实例调用实例方法,可以自动将对象传入方法
# m1.driver()
# # 如果使用类调用实例方法,需要手动传递实例到方法内
# Monkey.driver(m1)