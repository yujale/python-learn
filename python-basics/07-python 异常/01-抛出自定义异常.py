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