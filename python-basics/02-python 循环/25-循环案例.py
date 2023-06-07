
def example1():
    ## 求1-100的累加和
    # 初始状态
    i = 1
    sum1 = 0
    while i <= 100:
        # 求累加和
        # sum1 = sum1 + i
        sum1 += i
        # 为下一次循环做准备,自增
        i += 1

    print('1-100的累加和是%d\n' % sum1)

def example2():
    # 需求:输出10以内的所有奇数

    # 初始状态
    i = 1
    # 循环结束条件
    while i <= 10:
        # 要循环做什么
        if i % 2 != 0:
            print(i)
        # 为下一次循环做准备  自增
        i += 1

def example3():
    # 需求: 1-100的偶数累加和
    # 初始状态:
    i = 1
    sum1 = 0  # 累加器
    # 循环条件
    while i <= 100:
        # 要做什么?
        if i % 2 == 0:
            sum1 += i
        # 为下一次循环做准备  累加
        i += 1

    print(f'1-100的偶数累加和是{sum1}')


if __name__ == '__main__':
    example1()
    example2()
    example3()