## 1、实例属性的添加和获取

- 在类的外部添加和获取实例属性
  - 添加：对象名.属性名 = 值
  - 获取：对象名.属性名
  - 创建对象后，我们对其中一个对象添加实例属性，其他对象不发生变化

```python
# 在类的外部可以添加或获取实例属性
# 格式:
# 实例属性添加:对象.属性名 = 值
# 实例属性获取:对象.属性名

# 定义类
class Person(object):
    def eat(self):
        print('早饭吃了油条和包子,血糖110')


# 实例化属性
p1 = Person()
# 给p1添加实例属性
p1.name = 'xiaoming'
# 调用实例属性
print(p1.name)  # xiaoming

# 如果我们再创建一个对象,其实例属性name是否存在?  不存在
p2 = Person()
p2.age = 18
# AttributeError: 'Person' object has no attribute 'name'
# print(p2.name)
# print(p1.age)
# 结论:对象被创建后,添加实例属性,对其他的对象不产生影响

# 如果我们对同一个实例属性添加两次值会怎样?
p1.name = 'Rose'
print(p1.name)
# 对象名.属性名 = 值,  如果当前对象的该属性名存在,则重新赋值,如果不存在,则新建一个属性
# 类似于dict

# 扩展  __dict__
# 可以通过__dict__去查询对象的属性,该属性以字典形式保存
# 在计算机底层,对象的属性,保存在一个字典结构的空间内,多以多次赋值会覆盖原来的值,给新的属性赋值,会增加属性数量
print(p1.__dict__)

# 对象属性删除del(扩展)
del p1.name
# AttributeError: 'Person' object has no attribute 'name'
print(p1.name)
```

- 在类的内部添加和获取实例属性
  - 添加：self.属性名 = 值
  - 获取：self.属性名
  - 一般实例属性写在实例方法中，调用该方法才能获取实例属性，对象创建后，其中一个实例调用该方法，获取实例属性，其余对象不发生变化

```python
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
```

## 2、`__init__（）`方法

- `__init__()`方法在对象创建完成后，初始化对象时，自动调用
- 在init方法中添加的属性，由于每个对象都会执行该方法，所以都包含该属性，被称之为共有属性
- 在init方法之外添加的属性，由于不是每个对象都拥有，所以被称之为独有属性

```python
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
```

## 3、带参数的`__init__()`方法

- init方法在对象被创建时，可以将“类名（）”这里边括号添加的参数传递到init方法内部
- 在接收到参数时，可以动态给对象添加实例属性
- 如果init方法添加了参数，那么在创建对象时，必须给其赋值，否则报错

```python
# 每次我们创建对象时,如果使用init方法,是不是只能添加同一个值的属性呢?
# 如果我们能够将参数传递到init方法中,是不是就可以在创建对象时,动态添加属性值了呢?
# 我们怎样给init进行传参呢?
# 面临的问题: 1.我们不需要手动调用init  在哪里给他传参呢?  2.我们传参时到底传什么参数给init方法呢?

# 在实例化对象时,类名(参数1, 参数2....)这些参数会传递给init方法,进行使用

# class Person(object):
#     def __init__(self, name, age):
#         print(name, age)


# TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
# p1 = Person()
# 既然我们给init方法中添加了参数,就必须传值,否则就会报错
# 在Person的括号中传参,就可以传递到init方法中,传参的数量,就是init方法中除了self之外的位置参数的数量
# p1 = Person('Jack', 18)  # Jack 18
# 结论: 在Person类创建对象时,在()内添加参数,可以被init接收但是,传参数量和inti方法中的形参必须一致

# 怎样实现动态的实例属性添加呢?

class Person(object):
    def __init__(self, name, age):
        # self.属性名 = 参数  将函数外部传递进来的参数赋值给对象,创建实例属性
        self.name = name
        self.age = age


# 实例化对象时要正确传参
p1 = Person('Rose', 17)
print(p1.name, p1.age)
# 创建第二个对象,查看属性是否动态传递成功
p2 = Person('Jack', 18)
print(p2.name, p2.age)

# 通过这种方式,我们在创建对象时可以指定其不同对象属性的值不同,但是所有的对象包含的属性类别相同
# 这种形式下一定要给每一个对象单独赋值,或者给init方法中的属性一些默认值,否则会报错
```

## 4、`__str__()`方法

- 在类的内部实现`__str__()`方法，他会在我们讲对象转换为str类型时自动调用，返回其return内的数据
- str方法内只能返回str类型的数据
- str方法自动调用的场景
  - 强制类型转换： str（对象）
  - ==隐式==类型转换： %s作为占位符接收对象，或者 print打印等，都会自动调用

```python
# __str__()方法是在数据被转换为str类型时自动调用的方法

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        # 在__str__方法中只能返回字符串类型数据,否则就会报错
        # TypeError: __str__ returned non-string (type int)
        # return 123
        # return None
        return f'我的名字是{self.name}, 我的年龄是{self.age}'


p1 = Person('Rose', 18)
# 如果我们打印p1会在控制台输出什么? # <__main__.Person object at 0x7fb70db848e0>
# 默认会输出对象类型,和内存地址
# print(p1)
# 我们如果让其在打印时输出我们想要输出的内容?  重写str方法

# 重写str方法后
# 结论:打印p1时,会自动调用__str__()方法
print(p1)

# 是因为print方法我们才将p1变为我们改写的str方法中的内容么?  不是
# 其实我们再执行print时,会做一次隐式的数据类型转换 也就是使用str(对象)

str1 = str(p1)
print(str1)

# 在什么场景下会自动调用__str__呢?
# 1.强制类型转换  str(对象)
# 2.隐式类型转换  %s 作为占位符,接收p1   print打印
```

## 5、`__del__()`方法

- 对象被释放前，自动执行`__del__()`方法
- 释放对象的几个场景
  - 出了函数作用域后，局部变量被释放
  - 程序执行完成后，所有变量被释放
  - 执行del操作后，可以提前释放变量

```python
# 之前我们学过del操作
# del 变量名  或者  del (变量名)

# del操作  可以切断数据和引用位置的联系
# 切断引用后,a 没有引用任何数据,1也没有任何变量引用,所以双双被释放掉
# a = 1
# del a
# print(a)

# __del__()方法,在c语言中成为析构函数
# 在对象被释放前自动执行该方法,执行后,对象立即被释放

# 定义类
# class Person(object):
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age


# p1 = Person('Rose', 18)

# del p1
# NameError: name 'p1' is not defined
# 在这种情况下,我们能否知道p1已经被释放了?  没有提示
# 如果已经被释放了还继续使用,是不是会报错? 会报错
# 我么你怎样去进行提示?  使用__del__()
# print(p1)


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('我被释放了,真爽',self.name)


p1 = Person('Rose', 18)

# del p1 # 使用del造成p1被提前释放,在程序结束前将对象释放了
# p1被释放后,我们就接收到了提示,证明p1不存在了,之后就不要使用了
# print(p1)
# 如果没有del操作,则在程序结束后,会将所有的变量进行统一释放
# print('程序结束')

# 结论:在对象被释放时,会自动调用__del__方法,并且,使用del操作可以提前释放对象,否则在程序结束后,也会将变量统一释放

# 如果一个对象,或者说同一块内存空间,被多个变量引用,使用del可以释放么?
# p2 = p1  # p1和p2指向同一内存空间,或者说两个变量引用同一个数据
# del p1
# # 如果只删除p1的引用,对象还被p2引用着,该对象不会被释放,必须切断所有引用,才能正常 释放
# del p2
# # 如果将p2的引用也切断了,则对象正常释放
# print('程序结束')


# 结论:对象被引用时无法释放,除非程序终止,如果一个对象被多个变量引用,必须将所有引用切断才能正常释放,否则无法释放对象
# 举例:多个主人牵一条狗,如果有一个主人没有撒手,狗也跑不了
p4 = None
def func():
    p3 = Person('xiaoming', 15)
    global p4
    p4 = p3
    print(p3)

func()
# 上述代码可以推断,在函数执行完成后,出了作用域,会将函数内所有的临时变量释放掉,除非其被外部变量引用

print('程序结束')

# 切断引用或释放对象的几个场景
# 1.出了函数作用域会自动释放函数内的局部变量
# 2.程序结束会自动释放所有的变量
# 3.使用del操作可以提前释放变量
```

## 6、面向对象案例

```python
'''
需求:
1.创建phone类  Phone
2.在类中添加方法,  充电   听歌  打电话  玩游戏
3.每个手机都有初始的电量,并且在创建对象时可以手动输入电量
4.充电可以输入充电时长, 充电1小时获得20个单位的电量
5.听歌(15)  打电话(10)  玩游戏(30)都会消耗电量
6.电量最高100  最低 0  充电到100 就就会结束,  使用手机,如果电量不足以支撑完成操作则警告,并自动关机
'''

# 分析:
'''
1.在上述需求中有哪些类?  一个 Phone
2.在上述类中有哪些属性?  一个 电量
3.在上述类中有哪些方法?  四个  充电  听歌 打电话 玩游戏
4.有哪些数值判断:在使用手机  和充电过程中,让电量范围保持在0-100之间
'''


# 定义类
class Phone(object):

    def __init__(self, power):
        """初始化对象的方法,在定义对象时,需要输入电量"""
        if power >= 100:
            self.power = 100
        elif power <= 0:
            self.power = 0
        else:
            self.power = power

    def add_power(self, time):
        """充电方法"""
        print(f'充电开始,共充电{time}小时')
        # 对于对象中的电量进行增加
        self.power += 20 * time
        if self.power > 100:
            self.power = 100
            print('充满电了,赶紧收起来吧不然充坏了')
        else:
            # 输出电量
            print(f'充电结束,当前电量为{self.power}')

    def music(self):
        """听音乐"""
        print('音乐真好听呀,再来一首大河向东流')
        self.power -= 15
        if self.power > 0:
            print(f'听歌结束,剩余电量为{self.power}')
        else:
            # 在手机没电时需要将电量赋值为0,防止出现负数电量
            self.power = 0
            print(f'手机没电了赶紧充电吧,别听歌了')

    def call(self):
        """打电话"""
        print('给女朋友打个电话,希望还没睡觉')
        self.power -= 10
        if self.power > 0:
            print(f'电话打完了,成功分手,剩余电量为{self.power}')
        else:
            # 在手机没电时需要将电量赋值为0,防止出现负数电量
            self.power = 0
            print(f'手机没电了赶紧充电吧,别打电话了')

    def play_game(self):
        """玩游戏"""
        print('我最爱玩游戏了,每次都赢没办法,就是这么厉害')
        self.power -= 30
        if self.power > 0:
            print(f'游戏打完了,打游戏太爽了,我打游戏,舍友打我,剩余电量{self.power}')
        else:
            # 在手机没电时需要将电量赋值为0,防止出现负数电量
            self.power = 0
            print('手机没电了,赶紧充电吧,别玩游戏了')


p1 = Phone(20)
p1.music()
p1.call()
p1.play_game()
p1.add_power(4)
p1.add_power(4)
print(p1.power)
```

## 7、单继承

- 单继承就是某个类只继承自一个父类，同时，继承关系中可以有多级继承
  - 继承过程中，子类可以使用父类的所有非私有属性或方法
  - 如果父类或更高级的父类，实现了init方法，并且进行了参数设定，实例化子类对象时必须传值

```python
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
```



## 8、多继承

- 一个子类，继承多个父类的过程就是多继承
- 在多继承中，子类可以调用多个父类中的非私有方法或者属性

- 多继承中，如果出现同名属性或方法，优先调用继承位置靠前的父类中的方法或属性

```python
# 多继承:一个类定义时,继承了多个父类,同时可以使用多个父类中的方法或者属性
# 格式: class 子类名(父类名1, 父类名2):

class Father(object):
    def dance(self):
        print('我现在要跳一个舞,赶紧出去')

    def sing(self):
        print('我要唱一个学猫叫,一起来')


class Mother(object):
    def dance(self):
        print('我现在要跳一个广场舞,离我远点,不然摔倒了赖你')

    def sing(self):
        print('我要唱一个大河向东流,赶紧跑')


# 同时继承两个父类,则在使用子类对象时可以调用两个父类中的所有非私有属性和方法
# class Son(Father, Mother):
#     pass
#
#
# s1 = Son()
#
# s1.dance()
# s1.sing()

# 疑问: 如果两个父类中有重名方法该怎么办?
# 在下述情况下,只会调用Father类中的sing和dance方法
# class Son(Father, Mother):
#     pass
#
#
# s1 = Son()
#
# s1.dance()
# s1.sing()

# 如果我将两个父类的顺序进行调换
# 此时,只会调用Mother类中的sing 和dance方法
class Son(Mother, Father):
    pass


s1 = Son()

s1.dance()
s1.sing()

# 结论:如果存在同名方法,在继承时,谁的继承位置更靠前就调用谁内部的代码
```

## 9、子类中重写父类方法

- 子类中重写父类方法，则调用方法时，直接调用子类中的方法，不会调用父类的
- 重写时只要方法名称相等即可，不需要进行参数的校对
- 为什么可以重写父类方法，因为在调用方法或者属性时，会按照继承层级依次查找

```python
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
```

