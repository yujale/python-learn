if __name__ == "__main__":
    # = (在Python中等号不是判断相等的而是赋值使用)
    # 赋值格式: 变量名 = 值

    # 给单个变量赋值
    a = 1

    # 同时给多个变量赋值
    # 等号左侧的变量数量一定要等于等号右侧的值的数量, 否则报错
    name, age, gender = 'xiaoming', 18, '男'
    # ValueError: not enough values to unpack (expected 3, got 2)
    # name, age, gender = 'xiaoming', 18
    print(name, age, gender)

    # 同时给多个变量赋相同的值
    # 此种情况前边可以有多个变量,但是最后只能有一个值,否则报错
    a = b = c = 10
    # a = b = c = 10 = 20
    print(a, b, c)

    # 等号左侧一定要是变量,右侧可以是值或者已经被定义的变量
    int1 = 2
    int2 = int1
    print(int1, int2)