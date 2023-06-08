# 定义一个Person类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 定义一个Father类,继承Person
class Father(Person):
    def sing(self):
        print('我会唱学猫叫,跟我一起来')

    def dance(self):
        print('我会跳四小天鹅,就是天鹅还缺仨')


# 定义一个Son类,继承Father
class Son(Father):
    # 需求:在Son执行sing方法时,我么你让他唱一分钱
    def sing(self):
        print('我喜欢唱一分钱, 你自己学猫叫吧')

    # 我们进行方法 重写的时候,不需要关注参数,只需方法名相同即可
    def __init__(self):
        pass


# s1 = Son('xiaoming', 12)
# s1.sing()

# 为什么子类中重写了父类方法就不能进行调用了?
# 之前我么讲了__mro__  打印继承顺序,同时其也是方法或属性的调用顺序,例如想使用Son对象调用sing方法,但是不知道sing在哪个类中
# 所以,系统先去当前Son类中查找,查看是否存在sing方法
# 如果存在,则调用,如果不存在,则去父类中 Father中查找,如果Father类中存在sing则调用,如果不存在,则去更高级父类(person)中查找
# 直到查询到object类中,如果依然不存在,则报错

# 所以如果子类中书写了对应的方法,则父类中的同名方法无法被调用

# 可不可以让Son类不需要使用name和age就可以创建对象呢?  在Son中重写init方法
s1 = Son()
s1.sing()
