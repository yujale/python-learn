# __init__():在对象创建完成后,初始化对象过程中自动调用的方法

# class Person(object):
#     def __init__(self):
#         print('我被调用了')


# init方法在什么时候被调用

# p1 = Person()  # 只需要实例化对象,不需要手动调用,init方法即可自动调用
# 在类的内部和外部都可以轻松调用init方法,但是不要调用
# p1.__init__()

# 既然init方法可以在对象被创建后自动调用,那我们讲添加实例属性的代码写入init方法中,是不是可以每个对象被创建后,都自动添加实例属性呢?

class Person(object):

    def __init__(self):
        # 由于init方法在对象被赋值之前就已经调用了,多以此时不能使用对象名.属性名进行属性添加,只能使用self
        self.name = 'xiaoming'
        self.age = 18


p1 = Person()
# 由于其自动调用init,所以对象被创建后,自动拥有name和age属性
print(p1.name)  # xiaoming
# 创建多个对象,每个对象都包含init中的属性名
p2 = Person()
print(p2.age)  # 18

# 结论: 在init方法中添加的属性,每一个由该类创建的对象,都包含,这种属性,我们称之为公有属性
# 在init之外添加的属性,只有被添加属性的对象本身才拥有,这种属性被称为独有属性
