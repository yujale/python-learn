if __name__ == "__main__":
    # continue: 跳出本次循环,继续执行下一次循环(不会影响循环的次数)

    # 需求: 吃苹果,一个五个.吃到第三个 有个虫子,扔掉第三个,继续吃第四个第五个
    # 注意,在循环结构中使用continue要在continue之前添加循环变量的自增,否则可能会造成无法跳出循环(死循环)
    i = 1
    while i <= 5:
        if i == 3:
            print('这个苹果有虫子,给女朋友吃吧')
            i += 1
            continue
        print(f'我吃了{i}个苹果')
        i += 1

    # 写法二
    # 可以先进行自增,再进行i的调用,此时,就不用担心continue的问题了
    i = 0
    while i < 5:
        i += 1
        if i == 3:
            print('这个苹果有虫子,给女朋友吃吧')
            continue
        print(f'我吃了{i}个苹果')

    # 输出1-10 的数字
    # 在循环体中,continue所在的分支中,continue之后不要书写任何代码,永远不可能被执行
    i = 1
    while i <= 10:
        print(i)
        continue
        i += 1

    # break 和continue只能用在循环体中
    # if True:
    #     print('123')
    #     break
    #     continue