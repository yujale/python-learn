## 1、文件的基本操作

- 文件打开的格式：
  - file = open（文件路径，读写模式）
    - 文件路径：可以写相对路径，也可以写绝对路径
    - 读写模式：r（读取） w（写入） a（追加）
- 文件打开后，必须关闭，否则持续消耗服务器性能。

```python
# 文件读写,在使用的时候和我们正常使用文件一样
# 1.打开文件
# 2.操作文件
# 3.关闭文件

# 打开文件使用open函数即可
# 格式: open(file_name(文件路径), mode(读写模式)) 使用该函数会返回一个文件对象
# 文件路径:可以写相对路径, 也可以写绝对路径,路径需要以字符串形式传入
# 读写模式: r(只读)  w(写入)  a()追加
file = open('python.txt', 'r')
print(file) # <_io.TextIOWrapper name='python.txt' mode='r' encoding='UTF-8'>  在windows中默认读写格式是gbk
print(type(file))  # <class '_io.TextIOWrapper'>
# 将读取出来的内容进行打印
print(file.read())
# 关闭文件
file.close()

# 为什么要关闭文件?
# 在文件打开状态是会保持连接,这种状态下会持续消耗内存,不利于服务器性能优化(内存泄漏)

# 关闭文件后,文件对象有没有被释放?
# 没有释放
print(file)  # <_io.TextIOWrapper name='python.txt' mode='r' encoding='UTF-8'>
# 文件关闭后,相当于与文件的连接状态消失了,但是文件对象没有发生变化
# 在文件关闭后,file对象不能进行任何读写操作,因为已经无法连接文件
# ValueError: I/O operation on closed file.  无法操作一个已经关闭的文件
print(file.read())
```

## 2、文件的读取操作

- read：如果（）内填写数字，则读取指定字符的字符串，每次读取指定字符，在一个文件开启后，多次读取会持续向后读取字符，如果字符全部读取完成将会返回空字符串“”
  - 格式： 文件对象.read(单次最大读取字符数)
- 如果读取的文件不存在则直接报错

```python
# 文件在'r'模式下可以进行文件读取
# read 可以读取文件

# 打开文件
file = open('python.txt', 'r')
# 读取文件
# n:在read中传入数值,代表我们读取的最大字符数
# 如果开发中有一个文本文件,比如网络小说,4个G大小,一次性读取,用户依次读取这么大的文件,极度消耗性能,而且 等待时间过长
# 所以在开发中我们经常会给读取数据的值做一个限定,最大读取字符一般限定为(1024*1024)

# 那我们使用read只能依次读取3个字符,那省下的字符我们怎样读取呢?
# 文件每一次读取,都会持续向后读取,直到文件关闭或程序结束,所以可以使用循环进行读取
# 在所有的文件内容读取完成后,会持续返回空字符串("")
while True:
    content = file.read(3)
    if content == '':
        break
    print(content)

# 关闭文件
file.close()
```

- readline: 每次读取一行数据，以\n为分隔符，在一个文件开启后，多次执行读取操作会持续向后读取，如果字符全部被读取完成，则返回空字符串“”
  - 格式：文件对象.readline()

- readlines：一次性将文件全部读取，读取后，将文字以一行为一个元素保存到列表当中进行返回
  - 文件对象.readlines()

```python
# 除了read外还有一些读取方式
# 文件打开
file = open('python.txt', 'r')
# 文件操作
# readline  使用这种方式读取文件,每次读取一行以\n为分隔符,并且在文件打开状态下,会持续向下读取,直到所有文件被读取完成后,会读取空字符串""
# while True:
#     content = file.readline()
#     if content == '':
#         break
#     print(content,end='')

# readlines 读取所有的文件以\n为分隔符,将所有的行以字符串元素的方式保存到列表当中进行返回
# ['吴丝蜀桐张高秋\n', '空山凝云颓不流\n', '举头望明月\n', '低头思故乡\n']
content = file.readlines()

print(content)
# 文件关闭
file.close()
```

## 3、文件的写入操作

- 使用写入模式‘w’打开文件
  - 如果文件存在，则清空源数据
  - 如果文件不存在，则新建文件，不会报错
- 使用write可以写入字符
- 在windows电脑中书写文件读写时，需要使用encoding进行编码格式指定
  - 格式：open（文件路径， 读写模式， encoding = 编码格式）

```python
# write 写入
# 当文件读写模式时 'w',可以使用文件的写入操作
# 当文件执行写入模式打开时,如果被打开的文件不存在,则重新创建一个新的文件,不会报错
# file = open('test.txt', 'w')
# 当文件执行写入模式打开时,如果被打开的文件存在,则会将源文件内的字符清空
# 如果使用windows电脑进行开发,在写入文件时,需要制定编码格式为'utf-8'
# 如果使用linux 或者mac 默认是utf-8编码 不需要转码
file = open('python.txt', 'w', encoding='utf-8')
# 当完成文件的读写操作时,我们写入文件  和读取文件所使用的编码格式必须一致
# UnicodeDecodeError: 'gbk' codec can't decode byte 0x89 in position 14: illegal multibyte sequence
print(file)  # <_io.TextIOWrapper name='python.txt' mode='w' encoding='UTF-8'>
# 写入操作
# file.write('我爱北京天安门,天安门上太阳升')
# 如果写入的字符串时三对引号包过内部的换行符会不会写入呢?  会写入格式
file.write("""
我爱北京天安门,
天安门上太阳升
""")

# writelines 是配合readlines进行使用的,可以将一个由字符串元素组成的列表一次性写入文件
# file.writelines('我爱北京天安门')
lines = ['吴丝蜀桐张高秋\n', '空山凝云颓不流\n', '举头望明月\n', '低头思故乡\n']
file.writelines(lines)

file.close()
```

## 4、文件的追加操作

- ‘a’：模式下进行文件打开
  - 如果文件不存在，则创建新文件
  - 如果文件存在，则在原有文件内进行字符串追加，不会清空源文件
- 在追加模式下，也是使用write进行文件写入，没有单独的追加方法，写入方式和‘w’模式一致

```python
# 'a'模式写入:追加模式
# 在追加模式下可以进行文件字符的追加,在原有数据的末尾添加 新的字符
# 在追加模式下打开文件,如果文件存在,则不会讲源文件清空
# file = open('python.txt', 'a', encoding='utf-8')
# 在追加模式下打开文件,如果文件不存在,则新建一个文件
# 打开文件
file = open('bigdata.txt', 'a', encoding='utf-8')
# 进行追加操作(注意:没有append方法,追加操作也是使用write进行写入,只不过不会清空源文件)
file.write('乱我心者今日之日多烦忧')
# 关闭文件
file.close()
```

## 5、文件读写模式拓展（了解，看到能明白意思即可）

- a： a  a + ab ab+
  - a：字符追加模式
  - a+ ：字符追加模式下可以进行字符读取
  - ab：字节追加
  - ab+：字节追加模式下，可以进行字节读取

- w： w  w + wb wb+
  - w：字符写入模式
  - w+：字符写入模式下可以进行字符读取
  - wb：字节写入模式
  - wb+：字节写入模式下，可以进行字节读取

- r： r  r + rb rb+
  - r：字符读取模式
  - r+：字符读取模式下可以进行字符写入
  - rb：字节读取模式
  - rb+：字节读取模式下，可以进行字节写入

## 6、文件备份案例

```python
# 需求:用户输入一个文件名,通过文件读写操作进行文件备份,并且将备份文件名称更改为:源文件名[备份].后缀

# 1.获取用户键入的文件名
# 2.要通过文件读写操作进行备份
#   2.1.拼接备份后的文件的文件名
#   2.2.读取源文件
#   2.3.写入新文件

# 1.获取用户键入的文件名
file_name = input('请输入您要备份的文件名称:')
file = open(file_name, 'r', encoding='utf-8')
# 2.要通过文件读写操作进行备份
# 2.1.拼接备份后的文件的文件名
copy_file_name = file_name.replace('.', '[备份].')
# 打开新文件
copy_file = open(copy_file_name, 'a')
# # 读取旧文件数据
# content = file.read()
# # 写入新文件
# copy_file.write(content)
# 一般情况下,文件都是指定单次读取的最大字符的
# 循环进行读取并写入,直到所有字符读取完成
while True:
    content = file.read(3)
    if content == '':
        break
    copy_file.write(content)

# 关闭文件
file.close()
copy_file.close()
```

## 7、rename和remove

- rename可以进行文件的重命名或文件移动
- remove 可以进行文件删除

```python
# 如果想要使用这两个方法,就要去进行模块导入
import os

# rename  重命名  >>>类似于linux命令中的mv
# 格式:os.rename(旧文件路径,新文件路径)
# 需求:将Python.txt重命名为 abc.txt
# rename可以对文件进行重命名
# rename中源文件路径必须存在
# os.rename('bigdata.txt', 'abcd.txt')
# 文件可以通过rename进行移动,移动的位置根据新文件路径决定,移动后同样可以修改名称
# os.rename('abcd.txt', '文件/abcd.txt')
# 文件移动时必须有文件名称,否则无法移动,移动后可以改名
# os.rename('abc.txt', '文件/a.txt')


# remove  删除文件  >>> 类似于linux里的rm
# 可以删除文件,但是不会有任何提示,但是也不会出现在回收站中,误删后无法回复,删除需谨慎
# os.remove('bigdata[备份].txt')
# 可以删除指定路径下的文件
# 如果被删除的路径不存在,则报错  (路径可以使用绝对路径,和相对路径)
# os.remove('文件/a.txt')
# os.remove('python[备份].txt')
# PermissionError: [Errno 1] Operation not permitted: '文件'
# 使用remove不能删除文件夹
os.remove('文件')
```

## 8、文件夹的操作

- mkdir：创建一个空文件夹，不能创建多级文件夹
- rmdir：删除空文件夹，不能删除有文件的文件夹
- getcwd：获取当前使用的工作目录的路径
- chdir：切换当前的工作目录
- listdir：查询指定目录的目录结构，将该目录下所有文件名以字符串形式保存在列表中进行返回
  - 括号内不填写任何内容则为查询工作目录的目录结构
  - 如果填写路径，则是对指定目录的查询

```python
# 在使用下方函数或方法时,需要先导入os模块方可使用
import os
# mkdir 创建文件夹
# FileExistsError: [Errno 17] File exists: 'student'
# 如果创建的文件夹已经存在则报错
# os.mkdir('student')
# 可以在已经存在的文件夹下创建文件夹
# os.mkdir('文件/students')
# FileNotFoundError: [Errno 2] No such file or directory: 'aaa/bbb'
# os.mkdir('aaa/bbb')  # 如果上级目录不存在则无法创建文件夹

# rmdir 删除文件夹
# FileNotFoundError: [Errno 2] No such file or directory: 'aaa/bbb'
# 如果删除的文件已经不存在,则会报错
# os.rmdir('student')
# os.rmdir('文件/students')
# 如果文件夹非空使用rmdir能否删除
# OSError: [Errno 66] Directory not empty: '文件'
# 如果文件非空则不能使用rmdir删除,需要进行递归删除
# os.rmdir('文件')


# getcwd  可以获取当前活动的工作目录 >> 类似于linux中的pwd
# /Users/day08/02-代码
# 默认工作目录就是我们工程所在的根目录
print(os.getcwd())


# chdir  切换工作目录  >> 类似于linux中的cd
# os.chdir('文件')
# /Users/day08/02-代码/文件
# print(os.getcwd())

# listdir  指定目录下的目录结构  >>> 类似于linux命令中的ls
# ['04-文件写入.py', '文件', '.DS_Store', '08-文件夹的操作.py', 'python[备份].txt', '01-文件读写操作体验.py', '00-作业讲解.py', '02-文件的读取.py', 'test.txt', '07-rename和remove.py', '06-文件备份案例.py', '03-其他读取方式.py', '05-文件追加.py', '.idea']
# print(os.listdir())
# os.chdir('文件')
# 如果listdir括号内没有书写对应的路径,则我们使用的路径就是工作目录,如果工作目录进行了切换则查找目录结构的位置也发生了变化
# ['abcd.txt']
# print(os.listdir())

# 查询指定位置的目录结构,可以在listdir括号内填写指定的目录,我们就会查询该目录的结构
# ['abcd.txt']
print(os.listdir('文件'))
```

## 9、批量修改文件名案例

```python
# 需求:批量修改指定目录下所有文件的文件名
'''
1.修改时可以通过参数控制是增加,还是删除字符
2.传入指定字符用于增加或者删除
3.使用rename进行重命名
'''

# 导入os模块
import os

# 定义一个控制增加还是删除的变量,True是增加 False 是删除
flag = False
# 指定字符的定义
str1 = '[黑马出品]'


# 构造多个文件:要在文件目录下构造 test1-test10 十个文件
# for i in range(1, 11):
#     open('文件/test' + str(i), 'w')

# 定义函数
def modify_files_name(flag, str1, path):
    # 切换工作目录为指定的目录path
    os.chdir(path)
    # 遍历指定路径下的所有文件名称
    for file_name in os.listdir():
        # 判断时增加字符还是删除字符
        if flag:
            # 重命名添加文件前缀
            os.rename(file_name, str1 + file_name)
        else:
            # 重命名删除文件名中指定的字符
            os.rename(file_name, file_name.replace(str1, ''))


# 将文件目录下所有的文件添加[黑马出品]的前缀
# modify_files_name(flag, str1, '文件')
modify_files_name(flag, str1, '文件')
```

## 10、面向对象的思维方式

- 面向对象，是一个编程思想，并不是一项技术，重在理解
- 面向过程：一步一步的完成功能：自上而下，逐步细化
- 面向对象：找到或者构造一个可以完成功能的主体：找到实体，功能完备

## 11、类和对象

- 类就是一系列拥有相同或相似功能的对象的集合，或者说类就是一系列事物的统称
- 对象就是类的具体的表现形式

```Python
1、手机是对象还是类？
2、苹果手机，是对象还是类？
3、iPhonex 手机是对象还是类？
4、我手里的苹果手机，是对象还是类？
```

## 12、类的定义

- 经典类
  - class 类名：
- 新式类
  - class 类名（父类名）：

```Python
# 定义一个类:
'''
格式:
# 经典类
class 类名:
# 新式类
class 类名(父类名):
'''

# 经典类
# 不由任何类派生,或者说不继承任何类
class student:
    pass  # 为了保证代码结构完整,在类下边必须书写表达式,如果没有使用pass占位

# 新式类
# 括号内就是我们的父类,也就是存在一定的继承关系
# 有些地方称其为object的派生类
class teacher(object):
    # pass
    ...  # 为了保障代码结构完整,也可以使用...来进行占位
```

## 13.类的实例化

- 类的实例化又叫做创建对象
- 类中实例化后的对象可以调用类中的方法
- 一个类理论上可以实例化无数个对象
- 格式： 类名（）

```python
# 类的实例化又称为创建对象
# 定义一个类
class Student(object):
    # 定义方法.定义方式和函数定义类似
    def study(self):
        print('我在听直播课,贼有意思,就是学习非常不努力我也能听懂')

    def eat(self):
        print('我在吃脑白金,补补脑子继续学习')


# 类的实例化(创建对象)
# 格式: 类名()

s1 = Student()
# 我们可以直接打印对象,得到的是其所对应的类和所在的内存地址
print(s1)  # <__main__.Student object at 0x7f9be20848e0>
# 也可以打印对象的类型,其实就是我们创建对象所使用的类
print(type(s1))  # <class '__main__.Student'>

# 实例可以调用实例方法
s1.study()
s1.eat()

# 理论上类可以创建无数个实例对象
s2 = Student()
print(s2)

# 类名的定义要使用大驼峰命名法
# 类名严格区分大小写,类名遵循标识符的命名规则
# class ChineseStudent():
#     pass
#
# s3 = Student()
# s4 = student()
# s3.eat()
# s4.eat()
```

## 14、self

- self就是讲调用方法的实例传入方法内部，在方法内部可以调用实例的属性和方法

```python
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
```

