if __name__ == "__main__":
    # 格式: '字符串,占位符' % 变量
    # 在上述格式中,格式化完成后,会将占位符位置填充上对应的变量
    # 不同数据类型的变量,要使用不同的占位符进行占位

    # 字符串数据使用 %s
    # 浮点型数据使用 %f
    # 整型数据使用   %d

    name = 'xiaoming'
    age = 18
    height = 1.85
    weight = 69.5
    marriage = False

    # 一个占位符的格式化输出
    print('学员的姓名是 %s' % name)
    print('学员的年龄是 %d' % age)
    print('学员的身高是 %f' % height)
    print('学员的体重是 %f' % weight)
    print('学生的婚姻状况是 %s' % marriage)

    # 有多个动态变量的时候,我们就需要使用多个占位符进行占位
    # TypeError: not enough arguments for format string
    # 如果前边有多个占位符,那后边的多个变量要使用括号进行包裹
    print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%f米, 学员的体重是%fkg, 学员的婚姻状况是%s' % (
    name, age, height, weight, marriage))
    # 括号内的变量数量不能少于占位符数量
    print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%f米, 学员的体重是%fkg, 学员的婚姻状况是%s' % (name, age, height, weight))
    # not all arguments converted during string formatting
    # 括号内的变量数量不能多于占位符的数量
    # print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%f米, 学员的体重是%fkg, 学员的婚姻状况是%s' % (name, age, height, weight,marriage,name))

    # 结论:占位符的数量,与%后的变量数量必须保持一致,如果是一个占位符,则可以使用一个变量,如果是多个占位符,那么多个变量必须使用括号包裹起来

    # 能否控制变量输出的结果的样式:可以
    name = 'xiaoming'
    age = 18
    height = 1.85
    weight = 69.5
    id = 12

    # 需求:1.身高保留两位小数,体重保留三位小数
    # 需求:2.学员的id共占用6位,不足位用0填充
    # 使用ctrl + d 可以整行复制
    print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%f米, 学员的体重是%fkg, 学员的编号是%d' % (
    name, age, height, weight, id))
    # 浮点型保留n位小数: %.nf
    # 整型占用n位数据,不足位用0补齐  %0nd
    print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%.2f米, 学员的体重是%.3fkg, 学员的编号是%06d' % (
    name, age, height, weight, id))