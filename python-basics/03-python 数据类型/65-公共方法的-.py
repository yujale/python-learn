if __name__ == "__main__":
    # * 效果是设么?
    # * 什么容器类型可以使用*

    # 基础数据类型  int  float  bool都可以使用*法运算
    print(12.1 * 2)

    # 容器类型的乘法运算
    # 格式: 容器类型 * int类型数据
    # 乘法运算的 效果,就是讲容器类型复制指定次数,并拼接到一起

    # list 可以使用*法运算么?  可以
    list1 = [1, 2, 3]
    # 将list1 复制3次并进行拼接
    print(list1 * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
    # 使用list 类型乘以float类型可以实现么?
    # TypeError: can't multiply sequence by non-int of type 'float'
    # 乘法运算不能让容器与非int类型相乘
    # print(list1 * 1.3)
    # list 能乘以负数么?  可以相乘,但是结果为空列表
    print(list1 * -3)  # []
    # 可以与0 相乘,结果为空列表
    print(list1 * 0)  # []

    # tuple 可以使用*法运算么? 可以
    tuple1 = (1, 2, 3, 4)
    print(tuple1 * 2)  # (1, 2, 3, 4, 1, 2, 3, 4)
    # tuple 只能与int类型相乘

    # set可以使用 * 法运算么?  不可以
    set1 = {1, 2, 3}
    # TypeError: unsupported operand type(s) for *: 'set' and 'int'
    # 集合类型数据不能做乘法运算
    # print(set1 * 3)

    # dict 能够使用 * 法运算么?  不可以
    dict1 = {'name': 'jack'}
    # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
    # 字典不能做乘法运算
    # print(dict1 * 3)

    # 乘号左右两侧的数据可以互换位置么?  可以
    print(3 * list1)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]