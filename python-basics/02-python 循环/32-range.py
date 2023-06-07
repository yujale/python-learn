if __name__ == "__main__":
    # range一般配合for循环使用 range是一个整数序列,是一个可迭代类型,可以使用for进行遍历,但是没办法直接print输出内部的所有元素

    # range(起始值,结束值,步长)  其整数序列范围,包含起始位置,不包含结束位置
    for i in range(1, 10):
        print(i)

    # 怎样打印range中的所有元素呢?  list(range类型)
    # range 构造的是一个整数序列,包含多个整数,区间范围为[起始,结束) 同时根据步长进行筛选数据
    print(list(range(0, 5, 1)))  # [0, 1, 2, 3, 4]
    # 步长可以省略,省略后,步长默认为1
    print(list(range(0, 5)))  # [0, 1, 2, 3, 4]
    # 步长就是序列内前后两个数据的差值
    print(list(range(1, 10, 3)))  # [1, 4, 7]

    # 如果起始位置是0则起始位置可以省略,但是起始值省略时,步长也必须省略
    print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(list(range(10,3)))

    # 如果步长是正数,起始值要小于终止值,否则会没有数据
    print(list(range(10, 3)))
    # 如果步长是负数,起始值要大于终止值,否则会没有数据
    print(list(range(10, 3, -1)))
    print(list(range(3, 10, -1)))

    for i in range(10):
        print(i)
