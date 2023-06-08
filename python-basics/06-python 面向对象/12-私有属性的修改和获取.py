# 一般情况下,我们不会强行调用私有属性和方法
# 我们会设置 get方法和set方法进行调用和修改

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 如果一个数据只能存储数据,无法使用其中的数据,那这个数据存储方案将没有任何意义
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


p1 = Person('Rose', 18)
# 使用get方法,可以直接调用私有属性
print(p1.get_age())
# 在使用set方法时,可以对私有属性进行赋值
p1.set_age(45)
print(p1.get_age())


# 结论:使用get,set方法可以对私有属性进行赋值和获取,在类的外部也可以使用他

# 疑问: 为什么我们花了很大力气,将其进行私有化,然后又花了更大的力气把数据进行了提取和修改?????


class Person1(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 如果一个数据只能存储数据,无法使用其中的数据,那这个数据存储方案将没有任何意义
    def get_age(self):
        # 需求:获取年龄的时候,为了让别人觉得自己年轻,返回的年龄少 5岁,如果小于18岁,则说自己18岁
        age = self.__age - 5
        if age < 18:
            return 18
        else:
            return age

    def set_age(self, age):
        # 需求:保存的数据必须是大于0 小于100的,如果超如范围, 大于100 存入100,如果小于0 则存入0
        if age > 100:
            self.__age = 100
        elif age < 0:
            self.__age = 0
        else:
            self.__age = age


p1 = Person1('Rose', 35)
# 在使用get方法提取数据的时候,可以对提取规则进行指定
print(p1.get_age())
# 子使用set方法存入数据的时候,可以对规则进行指定
p1.set_age(115)
print(p1.get_age())

# 结论:某些数据,在存入或者提取的时候,需要按照指定的规则进行加工这时候使用get  set方法极为方便
# 例如: 提取手机号或身份证号进行脱敏  存入数据的逻辑存在偏差,比如存储性别,存入0,1 和男女 ,这个时候可以使用set方法进行规则调整,保证存入数据的一致性
