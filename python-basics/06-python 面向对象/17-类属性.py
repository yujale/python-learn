# 类属性 ,有些地方也叫类变量  就是在类中创建的属于所有对象的属性

class Chinese(object):
    # 类属性是所有对象所共有的
    color = 'yellow'

    def __init__(self, name):
        self.name = name


c1 = Chinese('xiaohong')
c2 = Chinese('xiaohuang')
c3 = Chinese('xiaolv')

# 上述三个对象拥有的实例属性是什么???  name
# 他们每个人的实例属性相同么???之间有联系么???  不相同,每个对象间的实例属性互不相关
# 但是三个对象的类属性是完全相同的
print(c1.color)
print(c2.color)
print(c3.color)
# 类属性的获取方式
# 格式1:对象名.类属性名  在实例属性中,不能有与类属性同名的属性,否则类属性不能通过这种方式提取
# 格式2:类名.类属性名  (推荐)

# 修改类属性
# 格式:类名.类属性名 = 值
Chinese.color = 'orange'
# 注意:修改类属性不能使用  对象名.属性名 = 值  这种方式会添加一个实例属性
print(c1.color)
print(c2.color)
print(c3.color)


# 类属性使用场景:
# 可以进行计数
# 可以控制或者包含多个对象
class Apple(object):
    apple_list = []

    def __init__(self):
        Apple.apple_list.append(self)

    count = 10

    def eat(self):
        Apple.count -= 1


a1 = Apple()
a2 = Apple()
a3 = Apple()
a4 = Apple()

a1.eat()
a2.eat()
a3.eat()
a4.eat()
print(Apple.count)
print(Apple.apple_list)