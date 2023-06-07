if __name__ == "__main__":
    # 索引查询
    name_list = ['Bob', 'Jack', 'Rose']

    # print(name_list[0])  # Bob
    # print(name_list[1])  # Jack
    # print(name_list[2])  # Rose
    # print(name_list[-1])  # Rose
    # print(name_list[-2])  # Jack
    # print(name_list[-3])  # Bob

    # 结论: 列表中的索引和字符串中完全一致,
    # 正向索引从0开始,从左至右依次递增
    # 负向索引,从-1开始,从右至左依次递减

    # index  查询指定元素在列表中的索引,如果查询成功则返回该元素的正向索引,否则报错
    # index  是从左至右查询,返回第一次出现的索引位置

    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 5]
    # 会返回从左至右第一次查询到的数据索引
    print(num_list.index(5))  # 4
    # ValueError: 9 is not in list
    # 如果没有查询到数据则会报错
    # print(num_list.index(9))

    # rindex  在列表中没有这个方法
    # AttributeError: 'list' object has no attribute 'rindex'
    # print(num_list.rindex(5))

    # find  在列表中没有这个方法
    # AttributeError: 'list' object has no attribute 'find'
    # print(num_list.find(5))

    # count  计数, 查询指定元素在列表中出现的次数
    print(num_list.count(5))  # 2

    # in  判断数据元素是否在列表内  如果在  True  如果不在False
    # TypeError: argument of type 'int' is not iterable
    # print(num_list in 5)
    # 注意使用in或者not in  数据元素在左边,  列表或者其他数据序列在右侧
    print(5 in num_list)  # True
    print(9 in num_list)  # False
    # not in  判断数据元素是否不在列表内  如果不在  True  如果在False
    print(5 not in num_list)  # False
    print(9 not in num_list)  # True