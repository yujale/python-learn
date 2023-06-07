if __name__ == "__main__":
    # 输入使用的是input函数
    # 格式: input(提示字符)         (阻塞函数)
    # 使用input函数会造成程序阻塞,等待程序员输入信息,输入完成后,按enter键结束键入,程序继续执行
    # print('hello python')
    # input()
    # print('hello bigdata')

    # 提示字符
    # 输入:我们键入给计算机的字符
    # 输出:计算机给我们展示的字符,提示字符属于输出
    # input('请输入一个字母:')

    # 如果我们想要使用input函数接收到的键入信息,需要使用变量进行接收
    # 我们使用input接收到的是我们键入的信息
    # 我们键入的信息都会转化为字符串类型保存在input中,可以使用变量接收
    num = input('请输入一个数字:')
    print(num)

    # 练习:
    # 按要求输入账号和密码,并且将账号密码进行打印
    account = input('请输入您的账号:')
    password = input('请输入您的密码')
    print(f'您的账号是{account}, 您的密码是{password}')