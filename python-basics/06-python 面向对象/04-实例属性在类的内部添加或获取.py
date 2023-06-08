# 实例属性在类的内部添加或获取的格式
# self.属性名 = 值

class Person(object):
    def add_attr(self):
        self.name = 'xiaoming'
        self.age = 18
        self.gender = '女'


# 实例化对象
p1 = Person()
# 创建完成后,p1的实例属性添加了么?
# AttributeError: 'Person' object has no attribute 'name'\
# print(p1.name, p1.age, p1.gender)
# 为什么没有属性呢?  我们定义的添加实例属性的方法没有被调用
# 所以需要先调用添加实例属性的方法,才能使用实例属性
p1.add_attr()
print(p1.name, p1.age, p1.gender)  # xiaoming 18 女

p2 = Person()
# AttributeError: 'Person' object has no attribute 'name'
# 哪怕是在类的内部添加实例属性,两个对象之间没有任何关系,也就是执行方法在第一个对象中添加了实例属性,对第二个对象不产生影响,如果想要添加实例属性,需要再次调用方法
# print(p2.name)

# 在类的外部可以修改类内部添加的实例属性么?  可以
p1.name = 'Rose'
print(p1.name)  # Rose

# 同一个对象在类的内部和外部添加实例属性 本质上是一样的
# 在类的外部使用对象名,其实使用的是对象的引用地址,在其引用地址位置添加了对应的实例属性
# 在类的内部使用self,其实也代表该应用地址,也是在其应用地址位置添加了对饮的实例属性

# 为什么在类的内部要使用self 而不使用对象名?   简便,灵活.复用性高
# 1.我们每次使用的对象不一致,如果使用对象名,需要每次都传入不同的对象名,或者每个对象定义一个方法,这样不利于代码的复用.
# 2.在某些时刻,我们在没有将对象赋值给变量的时候,就需要添加其属性,这个时候,没有办法获取对象的名称.
