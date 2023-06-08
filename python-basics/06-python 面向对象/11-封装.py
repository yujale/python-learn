# 封装:将属性和方法,写到类的内部,使实例获得较为全面的功能,并且可以将属性和方法设置私有权限,保证暴露接口的安全性

# 封装的优点:
# 1.可以找到一个对象能够完成所有的功能或者业务,迭代和维护较为方便
# 2.可以设置私有属性或方法,提高代码安全性,只暴露我们想要暴露的接口
# 3.可以降低模块或者类的使用难度,暴露少量接口即可完成全部功能

# 私有属性,私有方法
# 当前属性或方法只能在类的内部进行调用,在类的外部无法使用,则称该属性,或者方法为私有属性,或者私有方法
# 格式:在属性或方法前加上两个下划线  __属性名  或者 __方法名

class Person(object):
    def __drive(self):
        print('我开着小汽车,嘟嘟嘟')

    def go_shopping(self):
        self.__drive()
        print('我去购物了')


p1 = Person()
p1.go_shopping()


# 如果 我只想使用购物方法, 开车只不过是一个中间方法,不会单独使用
# 那么我们暴露多个方法,反而让用户不知道该调用什么方法,所以我们讲无用的方法进行私有化,降低类或者模块的使用难度
# AttributeError: 'Person' object has no attribute '__drive'
# 在类的外部无法调用drive方法,所以私有化成功
# p1.__drive()
# 私有属性或私有方法,也是告诫其他人不要轻易调用

# 私有属性

class Women(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        # 私有属性和私有方法在类的内部是随意调用的
        return f'我的名字是{self.name}, 我的年龄是{self.__age}'


w1 = Women('Rose', 45)
print(w1.name)
# AttributeError: 'Women' object has no attribute '__age'
# 在属性名前加上__可以进行私有化
# print(w1.__age)
# 在类的外部添加的属性,不是私有属性,可以在类的外部进行调用
w1.__gender = '女'
print(w1.__gender)

# 拓展  使用__dict__查询私有属性
print(w1.__dict__)
# 在类的外部怎么调用私有属性???? _类名__私有属性名
# 在类的外部可以通过该方法获取私有属性并且修改,但是不要使用,因为如果别人定义了私有属性,大概率是不想让你修改,如果霸王硬修改,会让其他同时侮辱你的职业
print(w1._Women__age)
print(w1)