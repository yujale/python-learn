if __name__ == "__main__":
    # and 同真即真
    print(True and False)  # False
    print(True and True)  # True
    print(False and True)  # False
    print(False and False)  # False

    # or 同假即假
    print(True or False)  # False
    print(True or True)  # True
    print(False or True)  # False
    print(False or False)  # False

    # not 真变假, 假变真
    print(not True)  # False
    print(not False)  # True

    # 结论:逻辑运算符的运算结果都是bool类型数据

    # 练习:
    print(not (1 > 2 and 4 < 5))