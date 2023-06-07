if __name__ == "__main__":
    # 嵌套:在if语句控制的代码块中存在其他的if语句

    # 需求: 如果有钱可以上车(money) 如果上车了又座位可以坐下(seat)

    money = 12
    seat = True

    if money >= 2:
        print('快上车,里边有大座')
        if seat == True:
            print('快坐下吧,别累着')
        else:
            print('我骗你的你能咋办')
    else:
        print('穷鬼,跟着车跑吧,不等你')

    # 判断时正数负数 还是正奇数正偶数,负奇数,负偶数
    # num = 12
    # if num < 0:
    #     print('负数')
    #     if num % 2 == 0:
    #         print('负偶数')
    #     else:
    #         print('负奇数')
    # else:
    #     print('正数')
    #     if num % 2 == 0:
    #         print('正偶数')
    #     else:
    #         print('正奇数')

    num = -13
    if num < 0:
        print('负', end='')
        if num % 2 == 0:
            print('偶数')
        else:
            print('奇数')
    else:
        print('正', end='')
        if num % 2 == 0:
            print('偶数')
        else:
            print('奇数')