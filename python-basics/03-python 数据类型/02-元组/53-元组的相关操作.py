if __name__ == "__main__":
    # 元组的增删改:由于元组中的数据不可修改,所以元组中的数据不能进行增删改操作
    tuple1 = (1, 2, 3, 4)
    # 修改
    print(tuple1[2])
    # TypeError: 'tuple' object does not support item assignment
    # 元组中的数据不能修改
    # tuple1[2] = 6
    # 删除
    # TypeError: 'tuple' object doesn't support item deletion
    # 元组中的数据不能删除
    # del tuple1[2]

    # 查询
    # 通过索引进行查询
    # 查询方法和列表一致
    # 正向索引,从0开始,从左至右依次递增
    # 负向索引,从-1开始,从右至左依次递减
    tuple1 = (1, 2, 3, 4, 3)
    # 需求:通过正向索引取出3
    print(tuple1[2])
    # 需求:通过负向索引取出3
    print(tuple1[-2])

    # index  查询指定元素在元组中所在的位置索引
    # 需求:查询3所对应的索引值
    # index是从左至右依次查询,返回第一个查到的数据的正向索引值
    print(tuple1.index(3))  # 2
    # 如果查询的内容不存在,则报错
    # print(tuple1.index(8))  # ValueError: tuple.index(x): x not in tuple

    # count 查询指定元素在元组中出现的次数
    print(tuple1.count(3))  # 2
    print(tuple1.count(1))  # 1

    # len  查询元组的长度(对所有容器适用)  长度就是计算当前容器中有多少个元素
    print(len(tuple1))  # 5
    # 其实len()就是调用了括号内对象的__len__方法
    print(tuple1.__len__())  # 5