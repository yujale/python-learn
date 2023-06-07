if __name__ == "__main__":
    # 什么是死循环?  循环条件永远满足,可以持续循环的代码
    # 死循环是bug么?  死循环不是bug可以利用死循环做很多事情
    # 死循环可以退出么?  可以,死循环就是循环条件永远成立,但是在程序内部可以有很多方法跳出循环,  break

    # 猜拳游戏  (死循环进阶版)
    # 需求:在原来猜拳游戏的基础上,让电脑和玩家进行猜拳,一方达到3分则退出游戏,宣布获胜方,否则游戏持续进行
    # 普通循环
    # player_score = 0
    # computer_score = 0
    # while player_score < 3 and computer_score < 3:
    #     # 获取玩家拳型
    #     player1 = int(input('请输入您要出的拳型:(0 石头  1 剪刀  2 布)'))
    #     # 获取电脑随机拳型
    #     import random
    #     computer = random.randint(0, 2)
    #     result = player1 - computer
    #     # 拳型比对     # 输出结果
    #     if result == -1 or result == 2:
    #         player_score += 1
    #         print('玩家获胜')
    #     elif result == 0:
    #         print('平局')
    #     else:
    #         computer_score += 1
    #         print('电脑获胜')
    #     print(f'当前比分为{player_score}:{computer_score}')

    # 死循环
    player_score = 0
    computer_score = 0
    while True:
        # 获取玩家拳型
        player1 = int(input('请输入您要出的拳型:(0 石头  1 剪刀  2 布)'))
        # 获取电脑随机拳型
        import random

        computer = random.randint(0, 2)
        result = player1 - computer
        # 拳型比对     # 输出结果
        if result == -1 or result == 2:
            player_score += 1
            print('玩家获胜')
        elif result == 0:
            print('平局')
        else:
            computer_score += 1
            print('电脑获胜')
        print(f'当前比分为{player_score}:{computer_score}')
        if player_score >= 3:
            print('玩家取得最终胜利')
            break
        if computer_score >= 3:
            print('电脑取得最终胜利')
            break