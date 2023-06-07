if __name__ == "__main__":
    #  + - * / % // **

    # 案例:求梯形的面积
    # a = float(input('请输入梯形的上底长度:'))
    # b = float(input('请输入梯形的下底长度:'))
    # h = float(input('请输入梯形的高:'))
    #
    # print(f'梯形的面积为{(a + b) * h / 2}')

    # 算数运算符优先级可以使用小括号控制,  先乘除后加减,同级运算从左至右依次运算

    float1 = 10.2
    int1 = 4
    int2 = 11

    # +
    # 数值型数据(float, int, bool)之间可以进行算数运算
    print(int1 + float1)
    # 了解  bool 可以参与算数运算  True 代表1  false 代表0
    # print(int1 + True)

    # -
    # 同加法运算一致

    # *
    print(int1 * int2)
    print(int1 * float1)

    # /
    print(int1 / int2)
    print(int1 / float1)

    # //(整除)  两个数据相除 取商
    # 11 / 4 商 2 余 3
    print(int2 // int1)  # 2

    # %(取模  取余) 两个数相除  取余
    # 11 / 4 商 2 余 3
    print(int2 % int1)  # 3

    # ** (幂次运算)
    # 幂次运算就是求变量的多少次方
    # 扩展int1 开根号等于几  int1 ** 0.5
    print(int1 ** 2)

    # 在除法运算中,结果必定为浮点型
    print(9 / 3)  # 3.0
    # 浮点型参与运算后,结果一定是浮点型
    # 商 3 余 2.2
    print(11.2 // 3)  # 3.0
    print(9.9 // 3.3)  # 3.0

    # print(0.1 + 0.2)   # 0.30000000000000004