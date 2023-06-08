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