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
except Exception as error:
    print('出现了未知异常', error, type(error))

# 为什么所有的Except我们都去进行指定错误名称是error????
# 因为在一个try..except中只能由一个分支捕获到error
# 在try...except内只有一个except中的命令会被执行,如果一个except捕获到异常,后续except都不会继续执行

# 练习:
# 所有的小朋友进行投票,支持去游泳(0)或者打乒乓球(1)
# 一共五个小朋友(五个实例,每个实例都有投票的权利)
# 每个小朋友只能投一票
# 唱票,  所有人投票完成,游泳xx票, 打乒乓球xx票

'''
分析:小朋友类(Child)
# 类属性: 游泳票数,  打乒乓球票数
# 实例方法: 投票
# 类方法: 唱票
'''


class Child(object):
    # 游泳的投票人都有谁
    swimming_socre = []
    # 乒乓球投票人都有谁
    ping_pang_score = []

    # 在初始化方法中添加学员姓名,查看是谁投了票
    def __init__(self, name):
        self.name = name

    # 投票方法(实例方法)
    def choose_sport(self, num):
        # 如果我们投票给游泳,就把对象存到游泳的列表中,反之存到乒乓球列表中
        if num == 0:
            Child.swimming_socre.append(self)
        elif num == 1:
            Child.ping_pang_score.append(self)
        else:
            print('输入错误')

    # 类方法 唱票
    @classmethod
    def show_score(cls):
        print(f'目前的票数游泳{cls.swimming_socre.__len__()}票, 乒乓球{cls.ping_pang_score.__len__()}票')


c1 = Child('小明')
c2 = Child('小红')
c3 = Child('小方')
c4 = Child('小绿')
c5 = Child('小胖')

c1.choose_sport(1)
c1.choose_sport(0)
c1.choose_sport(1)
c1.choose_sport(1)
c1.choose_sport(0)

Child.show_score()
print(Child.ping_pang_score)
print(Child.swimming_socre)