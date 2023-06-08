def example01():
    """
    规则如下：
    可以不间断的进行猜数字游戏环节，找到猜对了，结束程序，猜不对，可以不断的进行游戏，并且需要提示用户猜大了还是猜小了。

    拓展功能实现：

    1.最后需要统计出，用户猜了多少次才猜对。

    2.每一个用户的初始分数为100，每猜错一次扣5分，最后程序结束，统计用户的得分。
    :return:
    """
    import random
    # 100 分
    score = 100
    count = 0
    num = int(random.random() * 100)
    print(num)
    while True:
        count += 1
        guess = input("请输入猜测的数字：")
        if type(guess) != 'int':
            print('请输入数字')
            break
        if guess < num:
            print("猜小了")
            score -= 5
        elif guess > num:
            print("猜大了")
            score -= 5
        else:
            print("猜对了")
            break
        if score < 0:
            break
    if score < 0:
        print("当前得分为0，请重新开始")
    else:
        print("一共猜了 %d 次，总的分为: %d" % (count, score))


if __name__ == "__main__":
    example01()
