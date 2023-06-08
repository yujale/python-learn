"""
格式:
try:
    可能会出现异常的代码
except:
    在出现异常后执行该命令处理异常
else:
    当没有出现异常时,执行该代码
"""

try:
    a = 1
    print(a)
except:
    print('出现异常了')
else:
    # try中的代码正常执行没有任何异常,则执行else里边的代码
    print('没有异常,虚惊一场')