# 自定义模块可以书写什么?
# 什么都可以写但是导入时会将模块中的代码全部执行一遍
# 自定义模块可以导入其他文件中什么?
# 可以导入其他文件中,全局变量  函数  类
# 自定义模块的注意事项 : 自定义模块的文件名必须符合标识符的命名规则,并且不要和系统模块重名
# 自定义模块名要见名知意,不要随意乱起

import module_01

# 不满足标识符命名规则的文件不能当做模块使用
# import 09-else

# 全局变量可以被导入
print(module_01.age)  # 18

# 函数也可以被导入
module_01.func()  # 我是module中的函数

# 类可以被导入
p1 = module_01.Person()
p1.eat()

# 分支语句循环语句,函数调用等等是不能导入的

# 在导入某个文件时,我们会先将该文件进行执行,将所有的类和函数保存在内存当中,同时模块中的代码也会执行一遍