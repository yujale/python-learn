# 在类的内部定义方法的时候,自动传入一个self
# 在调用实例方法时,不需要对self 进行传值

# self到底是什么?有什么用?
class Student(object):
    def study(self):
        # 由于s1和self指向同一块内存空间,所以其必为同一个对象
        # 也就是说在对象调用方法时会将对象本身传入方法内部进行使用
        print(self)  # <__main__.Student object at 0x7fa2654848e0>
        print('我要学习了,谁也不要打扰我,我知道你们为了超过我不择手段,但是没有用')

    def eat(self):
        # self 有什么作用呢?
        # 可以在方法内部调用实例所拥有的属性或者方法
        print('我要吃饭了吃完就学习')
        self.study()


# 实例化对象
s1 = Student()
print(s1)  # <__main__.Student object at 0x7fa2654848e0>
s1.study()
s1.eat()

# 我们为什么要讲对象传入进去呢?
# 方法时定义在类的内部的,所有的对象共有一个类,所以我们再调用方法的时候,需要传入我们调用方法所使用的类

# s2 调用study方法时所指向的空间和s1无关所以两个对象指向不同的内存空间,修改一个,另一个不发生变化
s2 = Student()
s2.study()