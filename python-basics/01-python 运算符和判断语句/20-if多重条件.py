if __name__ == "__main__":
    # 格式;
    '''
    if 条件1:
        条件1成立时执行的代码
    elif 条件2:
        条件2 成立时执行的代码
    elif 条件3:
        条件3成立时执行的代码
    else:
        所有条件均不成立时执行的代码
    '''

    # 需求:搭讪,主要是为了问路

    age = int(input('请输入对方的年龄:'))

    if age > 100 or age < 0:
        print('数据错误')
    elif 0 <= age <= 18:
        print('小妹妹你真可爱')
        print('叔叔 我们不约而同的认为我很可爱')
    elif 18 < age <= 30:
        print('美女,你真漂亮')
        print('流氓')
    elif 30 < age <= 60:
        print('阿姨,我不想努力了')
        print('瞧你长那样')
    else:
        print('老奶奶,您真慈祥')
        print('我北京三套房')