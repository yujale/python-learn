if __name__ == "__main__":
    # 函数的说明文档,是对函数进行解释说明的
    # 函数的说明文档就是在函数体的第一行书写一个多行注释
    # def compute(num1, num2, symbol):
    #     """用于计算两个数的和差积商"""
    #     if symbol == '+':
    #         return num2 + num1
    #     elif symbol == '-':
    #         return num1 - num2
    #     elif symbol == '*':
    #         return num1 * num2
    #     elif symbol == '/':
    #         return num1 / num2
    #     else:
    #         print('输入错误')
    #
    # # 鼠标悬停到函数名位置,可以进行说明文档提示
    # compute(2, 3, '+')

    # 在函数体的第一行,输入三对双引号,在中间敲击回车,则自动提示要书写的内容,此处会让你注明参数及返回值含义
    def compute(num1, num2, symbol):
        """
        用于计算两个数的和差积商
        :param num1: 第一个参与计算的数字
        :param num2: 第二个参与计算的数字
        :param symbol: 计算的符号(+ - * /)
        :return: 两个数字运算的结果
        """
        if symbol == '+':
            return num2 + num1
        elif symbol == '-':
            return num1 - num2
        elif symbol == '*':
            return num1 * num2
        elif symbol == '/':
            return num1 / num2
        else:
            print('输入错误')


    # 鼠标悬停到函数名位置,可以进行说明文档提示
    compute(2, 3, '+')