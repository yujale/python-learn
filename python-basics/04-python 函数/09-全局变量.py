# 全局变量就是在函数体外部书写的一般要在文件内顶格书写,在函数体内部外部都可以调用的变量
a = 1
b = 2


def sum1():
    # 函数体内部可以使用
    print(a + b)


if __name__ == '__main__':
    sum1()
    # 函数体外部也可以使用
    print(a)
    print(b)

# for 循环中,  if 分支中创建的变量是全局变量还是局部变量呢? 全局变量
# for i in range(10):
#     pass
#
# print(i)
#
# if True:
#     c = 1
# print(c)
