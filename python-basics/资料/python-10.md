## 1、在子类中调用父类方法

- super（）.方法名（）
- 类名.方法名（self）
- spuer（要从哪一个类的上一级类开始查找， self）.方法名（）

- 子类调用父类方法时，一般都是想对父类方法进行扩展

```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def driver(self):
        print('开车太好玩了 ,10迈,太快了')


class Father(Person):
    # 如果我们现在想在原有父类方法基础上扩展,例如我们现在需要重写一个init方法
    # 可以接收 name, age ,gender三个属性
    def __init__(self, name, age, gender):
        # 在父类方法中已经添加了name,和age我们可不可以直接使用呢???
        super().__init__(name, age)
        # 在父类方法的基础上我们在添加一个子类方法独有的功能
        self.gender = gender

    def driver(self):
        print('我要去天安门完,开挖掘机不让我进')

    def __str__(self):
        return f'我的姓名是{self.name},我的年龄是{self.age},我的性别是{self.gender}'

class Son(Father):
    def driver(self):
        # 调用Person中的dirver
        # TypeError: driver() missing 1 required positional argument: 'self'
        # Person.driver()
        Person.driver(self)
        # 从Father类的上一级类开始查找方法,并进行调用
        super(Father,self).driver()

        # 调用Father中的dirver
        super().driver()
        # 格式:super(从哪个类的上一级开始查找,self).方法名()
        # 如果类名是当前类,可以省略括号内的内容
        super(Son, self).driver()
        # 书写特有功能


# 所有的参数都传递到了Father类中,并且添加为当前对象的属性
print(Father('Jack', 28, '男'))
s1 =Son('xiaoming', 12, '男')
s1.driver()

# 子类中调用父类方法的三种方式:
# super().方法名()   # 只能调用当前类的上一级类中的方法或函数
# 类名.方法名(self)  # 所使用的类名,必须在当前类的继承关系中  这种方法可以调用不在类中的类方法，但是不能使用self作为对象出现
# super(要从哪一个类的上级类开始查询,self).方法名()  # 类名必须在继承关系内,如果类名是当前所在的类,则可以将括号内内容省略,就是第一中方式
```

## 2、多态

- 在继承链条中，子类重写父类方法，即多个子类和父类中都拥有同名方法，将其对象传入函数或方法内部，执行相同方法后，所展示的效果完全不同，这种现象叫做多态

```Python
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
```

## 3、类属性

- 类属性，就是所有的对象所共有的属性，在对其修改够，所有对象的类属性放生了改变
- 实例属性，每个对象所独有的，对象被创建后，添加修改实例属性，对其他对象不产生影响

```python
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
```

## 4、类方法

- 如果在方法内部不需要使用实例属性和实例方法，但是需要使用类属性或者类方法我们就定义类方法
- 定义方式：需要在方法上方写@classmethod
- 在类方法中会自动传入cls，这个参数代表的是当前类本身

```python
class Apple(object):
    num = 10
    def __init__(self):
        self.eat_num = 0

    def eat(self):
        # 每次吃苹果,当前的食用数量加1
        self.eat_num += 1
        # 每次吃苹果,让苹果总数 -1
        Apple.num -= 1
    # 当方法中不适用实例属性和实例方法,只会使用到类属性和类方法的时候我们就选择类方法
    # 因为类方法,不需要创建实例去进行调用,可以直接使用类名调用
    @classmethod
    def eat_apple_num(cls):
        # 在类方法中传入的cls即为当前类的类名
        print(f'一共被吃了{10-cls.num}个,还剩{cls.num}个')

# 类方法的调用
# 格式: 类名.类方法名
Apple.eat_apple_num()

# 创建对象
a1 = Apple()
a2 = Apple()
a3 = Apple()
a4 = Apple()
# 吃苹果
a1.eat()
a2.eat()
a3.eat()
a4.eat()
a4.eat()

# 调用类方法
Apple.eat_apple_num()

# 查看每人吃了几个苹果
print(a1.eat_num)
print(a2.eat_num)
print(a3.eat_num)
print(a4.eat_num)

# 类方法可以使用对象调用么?
# a1.eat_apple_num()  不推荐这样使用
```

## 5、静态方法

- 既不依赖于实例，也不依赖于类，这种方法我们就可以定义为静态方法

```python
class Person(object):
    # 在静态方法中,不会传入self, 也不会传入cls 所以在我们使用静态方法时,最好再静态方法中不要使用类或对象的属性或者方法
    # @classmethod  类方法修饰

    @staticmethod
    def func():
        print('我是一个静态方法')

# def func():
#     print('我是一个静态方法')
# 一般能够定义为函数的内容,都可以改写为静态方法,理论静态方法不依赖与类和对象,但是为了更好的封装,我们会将其写到类中
Person.func()


# 静态方法就是一个普通函数,放到类内部就是为了封装,方便我们去继承和导入模块
```

## 6、面向对象案例

```python
# 需求: 进行游戏
# 1/显示游戏信息
# 2/展示历史最高分
# 3/开始游戏

class Game(object):
    top_score = 100

    def __init__(self, name):
        self.name = name
    # 定义一个静态方法,与类和实例都没有关系
    @staticmethod
    def print_game_info():
        print('游戏信息展示')
    # 定义类方法,内部可以调用类属性和类方法,依赖于类
    @classmethod
    def show_top_score(cls):
        print(f'历史最高分数为{cls.top_score}')
    # 定义了一个实例方法,内部可以调用实例属性和实例方法,依赖于实例
    def start_game(self):
        print(f'{self.name}开始游戏')

Game.print_game_info()
Game.show_top_score()
# 实例方法必须使用实例进行调用
g1 = Game('xiaoming')
g1.start_game()
```

## 7、异常捕获

- 使用try和except可以捕获异常，也就是在出现异常后不会将代码终止运行，而是执行except中的代码处理异常

```python
# 异常捕获:通过代码将可能出现异常的文件放入try中,然后如果出现异常就执行except中的命令
'''
格式:
try:
    可能出现异常的代码
except:
    如果出现了异常,就执行其中的代码
'''

# 需求:读取文件,如果文件不存在,则以写入方式打开
# 如果我们try中的代码出现了异常,则执行except中的命令
# 如果我们try中的代码没有出现异常,则不会执行
try:
    file = open('test.py', 'r')
except:
    file = open('test.py', 'w')

# 在正常的Python开发中基本每个函数中都要出现一次异常捕获
# 代码健壮性:代码抵御异常的能力
```

## 8、捕获指定类型的异常

- 在except后边添加异常类型，就可以捕获指定类型的异常
- 如果我们想要捕获多种异常
  - 可以在except后边添加多个异常类型，中间用逗号隔开，但是需要用括号包裹，变成一个元组
  - 可以书写多个except
- 如果所有的异常类型都无法捕获到该异常， 或者我们需要捕获未知类型的异常，可以使用Exception

```python
# try:
#     # NameError: name 'a' is not defined
#     # 如果先出现NameError  我们的后边一句没有办法执行  ZeroDivisionError没有办法捕捉到
#     # print(a)
#     print(1/0)
# # 如果想要捕获指定异常,就在except 后边添加异常的类型
# except ZeroDivisionError: # 这种方式只能捕获指定异常
#     print('出现异常了!!!')

# 在出现异常后, NameError和 ZeroDivisionError  之类的Error就是异常类型
# ZeroDivisionError: division by zero
# print(1/0)
# NameError: name 'a' is not defined
# print(a)


# 能不能同时捕获多种异常呢?  可以
# 方法一:在except后边添加多个异常名称
# try:
#     # NameError: name 'a' is not defined
#     # 如果先出现NameError  我们的后边一句没有办法执行  ZeroDivisionError没有办法捕捉到
#     # print(a)
#     print(1 / 0)
# # 如果想要捕获指定异常,就在except 后边添加异常的类型
# except (ZeroDivisionError, NameError):  # 这种方式只能捕获指定异常
#     print('出现异常了!!!')

# 方法二: 在try后边书写多个except
# try:
#     # NameError: name 'a' is not defined
#     # 如果先出现NameError  我们的后边一句没有办法执行  ZeroDivisionError没有办法捕捉到
#     # 在出现异常之后,后续代码将不会继续执行
#     print(a)
#     print(1 / 0)
# # 如果想要捕获指定异常,就在except 后边添加异常的类型
# except ZeroDivisionError:
#     print('出现ZeroDivisionError异常了!!!')
# except  NameError:
#     print('出现NameError异常!!')

# 如果我们想要展示异常信息怎么办?
# 异常信息就是异常类型冒号之后的注释
# 可以通过获取异常对象,并对异常对象进行打印,得到异常信息
# try:
#     print(a)
#     print(1 / 0)
# # 如果想要捕获指定异常,就在except 后边添加异常的类型
# # 在异常类型之后添加上个as  变量名  这时候 变量就是异常对象,打印该对象就可以出现错误信息
# except ZeroDivisionError as error:
#     print(error)  # division by zero
# except  NameError as error:
#     print('出现NameError异常!!', error)

# 如果我们不知道异常类型是什么怎么办?

# 可以使用Exception进行捕获,Exception是所有异常类的父类,可以捕获所有异常类型

try:
    print('2' + 1)
    print(a)
    print(1 / 0)
except ZeroDivisionError as error:
    print(error)  # division by zero
except NameError as error:
    print('出现NameError异常!!', error)
except Exception:
    print('出现了未知异常')
```

## 9、else 和 finally

- else： try中控制的代码没有出现异常，则执行该结构内的代码

```python
'''
格式:
try:
    可能会出现异常的代码
except:
    在出现异常后执行该命令处理异常
else:
    当没有出现异常时,执行该代码
'''

try:
    a = 1
    print(a)
except:
    print('出现异常了')
else:
    # try中的代码正常执行没有任何异常,则执行else里边的代码
    print('没有异常,虚惊一场')
```

- finally：无论出现什么情况都会执行finally里边的代码，哪怕程序崩溃

```python
'''
try:
    可能出现异常的代码
except:
    代码出现异常后执行该代码处理异常
else:
    如果try中的代码不出现异常,则执行其中的代码
finally:
    无论如何都会执行finally中的代码
'''

# 无论任何情况,finally中的代码都要被执行
try:
    a = 1
    print(a)
    print(1/0)
except NameError:
    print('出现异常了')
else:
    print('没有出现异常')
finally:
    print('出现不出现异常都要执行')
# 代码写到finally中,哪怕程序报错终止,代码依旧需要执行完成,但是写到try结构之外,程序报错终止将不会继续执行外部代码
print('try结构之外书写内容')
```

## 10、自定义异常抛出

- 自定义异常一定要继承自Exception
- 自定义异常可以使用raise抛出，可以进行捕获或者导致程序终止
- raise可以抛出系统异常，也可以抛出自定义异常

```python
# 自定义异常的逻辑
# 在自定义异常时,只要继承自Exception就可以当做异常抛出
# 继承后要重写 Exception方法,添加我们需要的内容

class PassWorldError(Exception):
    error_count = 0

    def __init__(self, str):
        super().__init__(str)
        # 在此处可以添加自定义操作
        PassWorldError.error_count += 1

# raise可以手动抛出异常,抛出异常后,可以直接终止程序,或者使用try except进行捕获
# raise可以抛出自定义异常,也可以抛出系统异常
try:
    password = input('请输入您的密码:')
    if len(password) < 6:
        raise PassWorldError('您的密码不足6位,请重新输入')
        # raise NameError('您的密码错误了')
except PassWorldError as error:
    print(error)

# raise PassWorldError('密码错误')
```

## 11、模块的导入

```python
import 模块名
调用: 模块名.功能名

from 模块名 import 功能名
调用: 功能名

from 模块名  import  *
import 模块名  as 别名
from 模块名 import 功能名 as 别名
```

```python
# Python中的模块就是可以将别人写好的,或者自己以前写好的功能直接导入新的文件或工程内,导入后可以直接调用  例如 : random  time os

# 我们没有实现模块中的功能,但是我们讲模块导入后就可以使用该功能,类似于继承

# 导入模块的方式
'''
import 模块名
调用: 模块名.功能名

from 模块名 import 功能名
调用: 功能名

from 模块名  import  *
import 模块名  as 别名
from 模块名 import 功能名 as 别名
'''
# # 导入os模块
# import os
#
# # 使用os模块
# print(os.listdir())

# # 导入os模块中部分功能
# from os import listdir, mkdir
# # 使用os模块中的功能
# print(listdir())

# # 导入os模块中的所有功能
# from os import *
# # *就是通配符,表示导入os模块中所有允许导入的模块
#
# # 使用os模块
# print(listdir())

# # 导入os模块,将模块改名为xitong
# import os as xitong
# # 使用os模块
# # NameError: name 'os' is not defined
# # print(os.listdir())
# # 如果给模块起了别名.则原名称不可使用
# print(xitong.listdir())

# from os import listdir as ls
# print(ls())
# NameError: name 'listdir' is not defined
# 给功能名称起别名后,无法使用原名称只能使用新的功能名称
# print(listdir())
```

## 12、自定义模块

- 模块名一定要遵循标识符的命名规则才能被导入

- 模块中书写的全局变量，函数，类可以盗取其他文件

- 导入模块时，会将模块中的所有文件执行一遍

- 为了保证测试代码在导入模块时不被执行，我们的测试代码需要写入

  `if __name__ == '__main__:'`

```python
# 标识符的命名规则
# 1/以字母数字下划线组成
# 2/不能以数字开头
# 3/不能是关键字
# 4/严格区分大小写

age = 18


def func():
    print('我是module中的函数')


class Person(object):
    def eat(self):
        print('西瓜真好吃呀')




# 在书写模块或者工具类的时候,经常需要调试,每次调试完成后还要将代码删除,否则导包结束后测试代码都会被执行一遍

# 所以我们需要想一个办法,将我们写的测试代码在当前模块中执行时,调用,在导入模块时不调用
# __name__就是说明当前文件执行的模块名是什么?
# print(__name__)   # __main__如果在当前文件中执行,模块名就是main
# 如果导入其他模块,则__name__的值就是文件名称module_01
# 所以我们根据__name__的值的判断,就可以断定他是咋当前文件执行,还是导入模块

# 使用该判断,让我们的测试代码只有在当前文件中执行的时候才会被调用
if __name__ == '__main__':
    if age > 10:
        print('今晚不能尿床了')
```

## 13、模块查询顺序

- sys.path可以查询模块调用路径列表，越靠前的路径越优先查询

```python
# 可以使用sys.path查看模块的定位顺序,如果模块名相同,优先从最新的序列查找

import sys
print(sys.path)
# sys.path的返回值是一个路径列表,排名越靠前的路径,在调用模块时优先查找,如果这个路径下没有对应模块才去下一个路径中查找.

# 在开发中可以在列表中你添加路径(了解)
```

- 开发中可以添加调用路径  sys.path.append(路径)

## 14、`__all__`的使用方式

```python
# __all__可以控制模块使用功能from 模块名 import *所导入的功能列表

from module_02 import *

# NameError: name 'age' is not defined
# 如果__all__控制的类表中没有改功能则不能在文件中使用
# print(age)
# 如果写到__all__中则可以使用
func()


import module_02
# __all__不能控制import的导入效果
print(module_02.age)

from module_02 import age
# 如果针对性导入某个功能,不受__all__影响
print(age)
```

## 15、包的的导入

- 导入包
  - import 包名.模块名
  - from 包名 import 模块名
  - 如果想要使用功能from 包名 import *
    - 要在`__init__.py`文件中书写`__all__`添加指定模块名才能导入

```python
# 包:多个有关联的模块在一起,保存在同一个文件夹内,并且文件内有一个__init__.py为文件,这种文件夹就叫做包
# 创建包的方式: mew >>> package   这中创建方式会自动添加一个__init__.py文件

# # 导入包 : import 报名.模块名
# import my_package.module_02
# # 调用 : 包名.模块名.功能名称
# my_package.module_02.func()

# 导入包: from 包名 import 模块名
# from my_package import module_01
# # 调用: 模块名.功能名称
# print(module_01.age)

# 导入包: from 包名 import *
from my_package import *
# 必须在__init__.py文件中的__all__里添加模块列表,才能使用import* 进行导入

print(module_01.age)
module_02.func()
```

## 16、学生管理系统面向对象版

- main.py

```python
# 主程序入口
# 一般开发中 文件夹会使用大驼峰命名法, 包和模块都是下划线分割法
from StudentManagerSystem.student_manager import StudentManager

def main():
    # 需求:循环输入,直到用户选择7 则退出
    s1 = StudentManager()
    s1.load_student_info()
    while True:
        # 提示用户输入信息 调用静态方法
        StudentManager.show_info()
        # 接收用户输入的信息
        num = int(input('请输入您要执行的功能:'))
        # 判断要执行的功能并且执行
        s1.choose_option(num)
        input()


main()
```

- Student.py

```python
# 定义学员类,并且在创建学员对象的时候添加学员信息

class Student(object):
    def __init__(self, student_id, name, age):
        """在创建学员对象时,传入学员信息"""
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        """在打印学员对象时,展示学员信息"""
        return f'学员的名字是{self.name}, 今年{self.age}岁, 学号是{self.student_id}'
```

- Student_manager.py

```python
# 方法:
# 1.判断用户键入的数字,执行不同的命令
# 2.添加学员
# 3.删除学员
# 4.修改学员
# 5.查询学员
# 6.展示所有学员
# 7.退出程序
# 8.展示信息
from StudentManagerSystem.student import Student


class StudentManager(object):

    def __init__(self):
        self.students_list = []

    @staticmethod
    def show_info():
        print('请选择如下功能-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    def choose_option(self, num):
        if num == 1:
            self.add_student_info()
        elif num == 2:
            self.delete_student_info()
        elif num == 3:
            self.modify_student_info()
        elif num == 4:
            self.search_student_info()
        elif num == 5:
            self.show_all_student_info()
        elif num == 6:
            self.save_student_info()
        elif num == 7:
            self.exit_program()
        else:
            print('数据有误')

    def add_student_info(self):
        """添加学员信息"""
        # 获取要添加的学员id
        student_id = input('请输入您要添加的学员id:')
        # 判断学员id是否存在
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                print('该id已经存在,无法添加')
                return
        else:
            name = input('请输入您要添加的学员姓名:')
            age = input('请输入您要添加的学员年龄:')
            s1 = Student(student_id, name, age)
            self.students_list.append(s1)
            print('学员添加成功')

    def delete_student_info(self):
        """删除学员信息"""
        # 获取要删除的学员id
        student_id = input('请输入您要删除的学员id:')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                self.students_list.remove(student_info)
                print('学员删除成功')
                return
        else:
            print('此学员不存在')

    def modify_student_info(self):
        """修改学员信息"""
        # 获取要修改的学员的id
        student_id = input('请输入您要修改的学员id')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                name = input('请输入您要修改为的姓名')
                age = input('请输入您要修改为的年龄')
                student_info.name = name
                student_info.age = age
                print('学员信息修改完成')
                return
        else:
            print('查无此学员')

    def search_student_info(self):
        """查询学员信息"""
        # 获取要查询学员的id
        student_id = input('请输入要查询学员的id')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                # 由于已经重写对了__str__方法,所以打印对象就可以输出信息
                print(student_info)
                return
        else:
            print('要查询的学员不存在')

    def show_all_student_info(self):
        for student_info in self.students_list:
            print(student_info)

    def save_student_info(self):
        """保存学员信息"""
        # 打开文件  如果要依次写入,我们使用a模式
        file = open('student_info.txt', 'a')
        # 遍历学员列表依次将学员信息写入, 学员对象.__dict__
        for student_info in self.students_list:
            file.write(str(student_info.__dict__) + '\n')
        # 关闭文件
        file.close()

    def load_student_info(self):
        """加载学员信息"""
        # 打开文件
        file = open('student_info.txt', 'r')
        # 将学员信息读取出来
        while True:
            content = file.readline()
            # 将字典类型的字符串转换为字典
            if content == '':
                break
            dict1 = eval(content)
            # 创建一个student对象
            # 字典前面+ ** 可以转换为  key = 值的 这种关键字参数赋值形式
            # 将学员信息赋值给对象
            s1 = Student(**dict1)
            self.students_list.append(s1)

        # 关闭文件
        file.close()

    def exit_program(self):
        """退出程序"""
        self.save_student_info()
        exit()
```

