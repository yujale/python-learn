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

# 注意给模块起别名,只在当前文件中生效