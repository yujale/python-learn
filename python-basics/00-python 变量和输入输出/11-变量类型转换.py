if __name__ == "__main__":
    # 需求: 在超市中有两种水果,苹果和橘子
    # 让售货员输入苹果的单价,苹果的重量,橘子的单价,橘子的重量,在控制台输出购买详情以及总价

    # apple_price = input('请输入苹果的单价:')
    # apple_weight = input('请输入苹果的重量:')
    # orange_price = input('请输入橘子的单价:')
    # orange_weight = input('请输入橘子的重量:')

    # TypeError: can't multiply sequence by non-int of type 'str'
    # 不同类型间的数据无法相乘
    # 在此情况下,我们需要进行数据类型转换(input接收的数据默认为字符串类型),需要转化为float
    # print(f'您购买了苹果{apple_weight}kg, 单价{apple_price}元, 橘子{orange_weight}kg, 单价{orange_price}元, 总共需要付款{apple_price * apple_weight + orange_price * orange_weight}')

    # 如果需要将数据转换为float 就给其穿上float类型的衣服
    # 格式: float(需要转换数据类型的变量或者值)
    # apple_price = float(input('请输入苹果的单价:'))
    # apple_weight = float(input('请输入苹果的重量:'))
    # orange_price = float(input('请输入橘子的单价:'))
    # orange_weight = float(input('请输入橘子的重量:'))
    #
    #
    # print(f'您购买了苹果{apple_weight}kg, 单价{apple_price}元, 橘子{orange_weight}kg, 单价{orange_price}元, 总共需要付款{apple_price * apple_weight + orange_price * orange_weight}元')

    int1 = 12
    float1 = 14.9
    str1 = '12'
    str2 = '14.3'
    str3 = 'python'

    # 数据类型转换的细节
    # int   float  str类型之间的转换
    # int >> float
    # int类型转换为float类型将会在整数末尾加.0
    print(float(int1))
    print(type(float(int1)))

    # float >> int
    # float转换为int类型,将会将小数部分去除,只保留整数部分
    print(int(float1))

    # int >> str
    # int类型可以随意转换为str类型,但是输出结果不发生改变,转化为str类型后可以使用str类型的各种函数
    print(str(int1))

    # str >> int
    # 字符串中是int类型数据,可以转换为int类型
    print(int(str1))
    # ValueError: invalid literal for int() with base 10: '14.3'
    # 字符串中是float类型数据,不可以转换为int类型
    # print(int(str2))
    # ValueError: invalid literal for int() with base 10: 'python'
    # 字符串中是字符型数据,不可以转换为int类型
    # print(int(str3))

    # float >> str
    # float类型可以随意转换为str类型,但是输出结果不发生改变,转化为str类型后可以使用str类型的各种函数
    print(str(float1))

    # str >> float
    # 字符串中是int类型数据,则可以转换为float类型数据,并且在末尾加.0
    print(float(str1))
    # 字符串中是float类型数据,可以转换为float类型数据
    print(float(str2))
    # ValueError: could not convert string to float: 'python'
    # 字符串中是字符型数据则不能转换为float类型数据
    print(float(str3))
