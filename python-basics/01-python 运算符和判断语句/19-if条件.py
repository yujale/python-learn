if __name__ == "__main__":
    # 格式:
    '''
    if 条件:
        条件成立时执行的代码
    '''

    age = int(input('请输入你的年龄:'))

    # 上网
    if age >= 18:
        print('小帅哥快来玩啊')

    print('回家睡觉')
    # if ... else ...
    '''
    if 条件:
        条件成立时执行的代码
    else:
        条件不成立时执行的代码
    '''

    # 使用分支语句,只有一个分支内的代码会被执行
    age = int(input('请输入你的年龄:'))

    if age >= 18:
        print('小帅哥,快来玩啊')
    else:
        print('老板我就进去看别人玩')

    print('回家睡觉')