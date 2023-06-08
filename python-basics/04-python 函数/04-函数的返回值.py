if __name__ == "__main__":
    # 返回值:将函数体内部运行或计算得到的数据传递到函数体外部

    # def sum(a, b):
    #     print(a + b)
    #
    #
    # sum(1, 2)

    # 思考?如果我们想在函数体外部使用这个结果进行二次运算我应该怎么做?
    # NameError: name 'a' is not defined  a, b 是形参,只能在函数体内部使用
    # print(a + b)

    # 如果我们想将数据传递出来可以使用return
    def sum1(a, b):
        return a + b


    print(sum1(1, 3))  # 当函数执行完毕,函数调用位置就替换为函数的返回值
    # 返回的数据可以参与计算
    print(sum1(1, 3) + 12)
    # 注意:返回值内容不会自动打印到控制台,将数据返回后如果想要查看数据需要手动打印或者debug调试

    # 如果没有return 那么就没有返回值么?
    list1 = [1, 2]
    # 因为此处,append方法,没有返回值,默认返回None
    print(list1.append(3))  # None


    def eat():
        print('猫吃鱼,狗吃肉,奥特曼吃小怪兽')


    # 如果没有书写返回值,则返回值为None
    print(eat())  # None


    # 如果只写了return 没有写返回值内容会怎么样?  None

    def sum1(a, b):
        print(a + b)
        return


    print(sum1(1, 2))  # None


    # return 执行后会跳出函数,return之后的所有代码将不会继续执行
    # 在函数中可以有多个return 但是只能执行一个
    def function():
        print('hello python')
        return
        return
        # 同一分支中,在return之后的所有代码不会被执行
        print('hello bigdata')


    function()


    # 返回值只能是一个么?  可以返回多个返回值么?
    # 返回值只能是一个元素,如果要返回多个值只能通过容器类型进行打包
    def function1():
        return 1, 2, 3, 4


    print(function1())  # (1, 2, 3, 4)

    # 结论:
    '''
    1.返回值是将函数内计算或运行的结果返回到函数外部调用位置,参与计算或运行
    2.函数可以不写返回值或者只写一个return不写返回值内容,都会默认返回一个None
    3.return后将会立即跳出函数,如果在retrun后仍有代码,则不会被执行
    4.return只能返回一个元素,如果想返回多个元素需要使用容器类型
    '''


    # 需求:
    # 使用函数完成计算器
    # 可以进行加减乘除操作,   在函数内传入两个数字,并且传入符号,在判断符号后,return返回结果,在函数外部进行打印

    def compute(num1, num2, symbol):
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


    print(compute(2, 3, '+'))
    print(compute(2, 3, '*'))