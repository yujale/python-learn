# 单继承:一个子类,只继承一个父类,并且可以多级继承

# 定义一个Person类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age


# 定义一个Father类,继承Person
class Father(Person):
    def __sing(self):
        print('我会唱学猫叫,跟我一起来')

    def dance(self):
        print('我会跳四小天鹅,就是天鹅还缺仨')


# 定义一个Son类,继承Father
class Son(Father):
    def play(self):
        # AttributeError: 'Son' object has no attribute '_Son__sing'
        # 继承父类时,只能继承父类中的非私有属性和方法
        self.__sing()
        self.dance()


# 实例化一个Son对象
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
# 应为son继承了father father继承了person, 在person中书写了init方法的参数,所以此处必须传参
# s1 = Son()
s1 = Son('xiaoming', 12)
# s1 继承了父类的属性和方法,在Son类中我们没有书写任何内容,但是可以调用父类及其父类的父类中的方法
# s1.sing()
# 调用方法时如果父类中书写了 我们就可以调用到,但是父类中的私有属性或者方法,我们无法调用
# AttributeError: 'Son' object has no attribute '__age'
# print(s1.__age)
# AttributeError: 'Son' object has no attribute '__sing'
# s1.__sing()
# s1.play()

# 结论:
# 1.在继承中可以多级继承,子类中可以使用父类及父类的父类中非私有的属性和方法
# 2.如果在父类或者更高级的父类中实现了init方法,并且书写了参数,则实例化对象时,必须传值

# 扩展:
# 怎样查询类的继承链条
# (<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Person'>, <class 'object'>)
# 使用类名.__mro__可以输出类的继承链条,同时这个顺序也是方法或属性查找的顺序
print(Son.__mro__)