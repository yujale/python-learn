# 继承:子类对象可以使用父类中的属性或方法的过程,叫做继承
# 格式: class 子类名(父类名):
# object是所有类的公共父类,基类,顶级类
# 如果使用经典类,或者新式类中括号内什么也不写,其实默认就继承了object
class Person(object):
    pass


class Man(Person):
    pass


class Boy(Man):
    pass