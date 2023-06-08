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