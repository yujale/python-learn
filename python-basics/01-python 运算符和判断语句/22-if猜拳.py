if __name__ == "__main__":
    # 需求:
    # 玩家键入拳型,电脑随机出拳
    # 比对玩家和电脑的拳型,如果玩家胜则输出玩家获胜,如果电脑获胜则输出电脑获胜,如果平局则输出平局

    # # 玩家键入拳型
    # player = int(input('请输入您要出的拳型:(0 石头 1 剪刀 2 布)'))
    # # 电脑随机出拳
    # computer = 2
    # # 比对拳型
    # # 玩家获胜情况: p: 0 c: 1  |  p: 1  c: 2  | p : 2  c : 0
    # if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    #     # 输出结果
    #     print('玩家获胜')
    # elif player == computer:
    #     # 输出结果
    #     print('平局')
    # else:
    #     # 输出结果
    #     print('电脑获胜')

    '''
    p  c  差值
    0  0  0    平局
    0  1  -1    p
    0  2  -2    c
    1  0  1     c
    1  1  0     平局
    1  2  -1    p
    2  0  2     p
    2  1  1     c
    2  2  0     平局

    找规律: 结果为0  平局
    结果为 -1 或 2 玩家获胜
    结果为 -2 或 1 电脑获胜
    '''
    # 玩家键入拳型
    player = int(input('请输入您要出的拳型:(0 石头 1 剪刀 2 布)'))
    # 电脑随机出拳
    # 在计算机中如果想要生成随机数据可以使用random模块进行生成
    import random  # 导入模块

    # 生成随机数  random.randint(m,n) 生成[m, n]区间内的任意一个整数
    computer = random.randint(0, 2)
    result = player - computer
    # 比对拳型
    # 玩家获胜情况: p: 0 c: 1  |  p: 1  c: 2  | p : 2  c : 0
    if result == -1 or result == 2:
        # 输出结果
        print('玩家获胜')
    elif result == 0:
        # 输出结果
        print('平局')
    else:
        # 输出结果
        print('电脑获胜')