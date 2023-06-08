if __name__ == "__main__":
    # +法运算,都可以用于哪些数据类型之间
    # int float  bool 肯定可以用于加法运算,不再赘述
    print(1 + 12.3)  # 13.3

    # str 可以相加么? 可以
    str1 = 'hello'
    str2 = ' python'
    # 字符串相加,可以快速将字符串进行拼接
    print(str1 + str2)
    # 相加过后,str1 和str2 没有发生变化,可以推断+法运算产生了新的数据,源数据不变化
    print(str1, str2, sep='\n')

    # list 可以相加么? 可以
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    # 列表相加可以将列表进行拼接,效果类似于extend
    print(list1 + list2)  # [1, 2, 3, 4, 5, 6]
    # list相加后,原数据不发生变化,将产生一个新的数据
    print(list1)  # [1, 2, 3]
    print(list2)  # [4, 5, 6]

    # tuple 可以相加么?  可以
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    print(tuple1 + tuple2)  # (1, 2, 3, 4, 5, 6)
    # 由于元组内部元素不能修改,索引相加肯定没有对源数据产生影响,而是生成了新的数据

    # set
    # set1 = {1, 2, 3}
    # set2 = {4, 5, 6}
    # # TypeError: unsupported operand type(s) for +: 'set' and 'set'
    # # set之间不能进行加法运算
    # print(set1 + set2)

    # dict
    # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
    # dict 类型间不能进行加法运算
    # dict1 = {'name': '小明'}
    # dict2 = {'age':18}
    # print(dict1 + dict2)

    # 结论: 基础数据类型都可以进行加法运算,容器类型间只有列表,元组,字符串可以进行加法运算

    # 不同容器类型间可以相加么?
    list1 = [1, 2, 3]
    tuple1 = (1, 2, 3)
    set1 = {1, 2, 3}
    dict1 = {'name': 'xiaoming'}

    # TypeError: can only concatenate list (not "tuple") to list
    # print(list1 + tuple1)
    # TypeError: can only concatenate list (not "set") to list
    # print(list1 + set1)
    # TypeError: can only concatenate tuple (not "set") to tuple
    print(tuple1 + set1)

    # 结论,数据类型布偶无法进行加法运算(特指容器类型之间)