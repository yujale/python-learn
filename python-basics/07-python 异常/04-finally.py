"""
try:
    可能出现异常的代码
except:
    代码出现异常后执行该代码处理异常
else:
    如果try中的代码不出现异常,则执行其中的代码
finally:
    无论如何都会执行finally中的代码
"""

# 无论任何情况,finally中的代码都要被执行
try:
    a = 1
    print(a)
    print(1 / 0)
except NameError:
    print('出现异常了')
else:
    print('没有出现异常')
finally:
    print('出现不出现异常都要执行')
# 代码写到finally中,哪怕程序报错终止,代码依旧需要执行完成,但是写到try结构之外,程序报错终止将不会继续执行外部代码
print('try结构之外书写内容')