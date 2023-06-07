if __name__ == "__main__":
    # 短路运算:
    a = 1
    b = 2
    # 当逻辑运算的第一个表达式已经可以决定整个逻辑运算的值的时候,后边的表达式将不会被运行
    print(a > b and a < b)

    # 在数值型数据中,非0即真
    # 在容器型数据中,非空即真
    # None 代表False
    print(False and 1)  # False
    print(0 and True)  # 0
    print(12 or False)  # 12
    print(None and True)  # None

    print(True and False)  # False
    print(True and 15)  # 15

    print(False or "")  # ""

    print(3 and 4 and 5)

    print(True and '123')

    print(5 and 6 or 7)

    # 世界杯小案例

    player1 = int(input('请输出自己球队的实力:'))
    player2 = int(input('请输出球队2的实力:'))
    player3 = int(input('请输出球队3的实力:'))
    player4 = int(input('请输出球队4的实力:'))

    score1 = (player1 > player2) * 3 + (player1 == player2)
    score2 = (player1 > player3) * 3 + (player1 == player3)
    score3 = (player1 > player4) * 3 + (player1 == player4)

    sum_score = score1 + score2 + score3
    print(sum_score)