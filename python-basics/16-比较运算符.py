if __name__ == "__main__":
    # < > <= >= !=  ==
    # 比较运算符运算结果为bool值,如果成立,则返回True 如果不成立则返回False
    print(1 < 2)  # True
    print(5 > 6)  # False
    print(1 >= 0)  # True
    print(4 != 4)  # False

    # 比较运算符可以连续使用(Python中的特性)
    age = 13
    print(12 < age < 30)  # True
    # 不等号也可以连续使用
    print(12 < age != 13)  # False

    # <>  不可以使用
    # print(1 <> 3)

    # 判断是否相等使用==
    print(age == 13)  # True
    print(age == 11)  # False
    # TypeError: 'age' is an invalid keyword argument for print()
    # =是赋值运算不能判断是否相等
    # print(age = 12)