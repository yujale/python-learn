class Person(object):

    def driver(self):
        print('开车太好玩了 ,10迈,太快了')


class Father(Person):

    def driver(self):
        print('我要去天安门完,开挖掘机不让我进')


class Mother(Person):
    def driver(self):
        print('我会开小汽车,嘟嘟嘟')


class Son(Father):
    def driver(self):
        print('我会骑自行车,真好玩')


def go_shopping(Driver):
    Driver.driver()
    print('很快就到超市了,真好呀')


class Monkey(object):
    def driver(self):
        print('我在骑自行车')


# 在我调用go_shopping时,可以将什么对象传进来???

p1 = Person()
f1 = Father()
s1 = Son()
m1 = Mother()

# 多态: 在继承链条中,无论是多级继承还是多继承,不同的类同种方法会进行重写,重写后在函数或者方法中传入不同的子类创建的对象,调用相同方法所展示的效果完全不同
go_shopping(p1)
go_shopping(f1)
go_shopping(s1)
go_shopping(m1)

# 如果创建一个Monkey对象,能否传入go_shopping并正确执行???
# 如果一个没有继承关系的类,也存在指定方法,也可以进行对象的传递,并在方法或函数内部使用,但是逻辑会有偏差,这种语法没有问题,但是逻辑上有严重偏差的方式叫做"鸭子类型"(扩展,不要求掌握)
# monkey1 = Monkey()
# go_shopping(monkey1)