if __name__ == "__main__":
    # 使用变量直接调用变量名即可,我们使用的是变量名,参与执行和运算的是变量中的数据(值)
    name = 'xiaoming'  # 定义
    print(name)  # 调用

    a = 1  # 定义
    b = 1  # 定义
    print(a + b)  # 调用

    # 所有的变量,要先定义后调用
    # 程序运行起来后,从上到下依次执行代码,解释一行运行一行,在打印方法被执行时,还不知道price已经被定义,会报错
    # print(price)
    # price = 15