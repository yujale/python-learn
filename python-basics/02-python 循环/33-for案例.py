def example1():
    # 求 1-100的累加和
    sum1 = 0
    for i in range(1, 101):
        sum1 += i
    print(f'1-100的累加和为{sum1}')

    # 求1-100的偶数累加和
    sum1 = 0
    for i in range(1, 101):
        if i % 2 == 0:
            sum1 += i

    print(f'1-100的偶数累加和为{sum1}')

    # 求1-100的偶数累加和
    # 在开发中尽量不要这样写 相当于人脑计算了规律,让代码按照人脑捕获的规律执行
    # sum1 = 0
    # for i in range(0, 101, 2):
    #     sum1 += i
    #
    # print(f'1-100的偶数累加和为{sum1}')


def example2():
    # break 打破循环,后续循环不会执行
    # continue 跳出本次循环,进入下一次循环,不会影响循环次数
    """
    案例：用for循环实现用户登录
    ① 输入用户名和密码
    ② 判断用户名和密码是否正确（username='admin'，password='admin888'）
    ③ 登录仅有三次机会，超过3次会报错
    """
    # 循环三次
    for i in range(3):
        # 获取用户名和密码
        username = input('请输入您的用户名:')
        password = input('请输入您的密码:')
        # 比对用户名和密码
        if username == 'admin' and password == 'admin888':
            print('登录成功')
            break
        else:
            print('用户名或密码错误')
        if i == 2:
            print('三次机会已经用完,账号被冻结')


def example3():
    # 打印一个直角三角形

    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{j} * {i} = {i * j}', end='\t')
        print()

    # 在for循环之外还可以调用i 或者j 么? 能

    # 在Python中for循环中创建的临时变量可以被外界调用,但是不要用
    # print(i)
    # print(j)
    # 使用for循环临时变量可能会出现报错
    # for i in range(1,1):
    #     print(123)

    # 当for循环执行后,没有一次进入循环体内,也就是遍历的序列是一个空序列,那么临时变量将不会被定义,所以不要使用
    # NameError: name 'i' is not defined
    # print(i)
