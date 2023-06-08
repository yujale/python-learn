if __name__ == "__main__":
    # len  获取容器类型的元素个数,  或者说获取容器的长度
    str1 = '123'
    list1 = [1, 2, 3]
    tuple1 = (1, 2, 3)
    set1 = {1, 2, 3}
    dict1 = {'name': 123, 'age': 18}
    # 使用len可以获取list  str  tuple set中的元素个数
    print(len(str1))
    print(len(list1))
    print(len(tuple1))
    print(len(set1))
    # 使用len可以获取dict中的键值对的个数
    print(len(dict1))

    # len() 可以写成  容器.__len__()
    print(list1.__len__())

    # del
    # 删除容器内指定的元素
    # list
    # del list1[0]
    # print(list1)

    # tuple
    # del tuple1[0]
    # TypeError: 'tuple' object doesn't support item deletion
    # 元组内元素不能被删除
    # print(tuple1)

    # set
    # for i in set1:
    #     del i

    # dict
    # del dict1['name']
    # del 在dict中删除的是键值对
    print(dict1)

    # str
    # TypeError: 'str' object doesn't support item deletion
    # str 不能够使用del 删除内部元素
    # 注意 :str内部的元素也是不可修改的,类似于元组
    # del str1[0]
    # print(str1)

    # 结论:
    # 1.列表,字典可以使用del删除内部元素,但是,列表中是删除元素,字典中是删除键值对
    # 2.使用del 没法循环遍历删除set中的元素,因为引用机制问题
    # 3.str  tuple内部的元素都不可更改所以不能使用del删除元素

    # max  min
    # list tuple set str可以使用max  min获取容器内的最大最小值
    print(max(list1))
    print(max(tuple1))
    print(max(set1))
    print(max(str1))
    # dict是使用max和min获取键的最大最小值
    print(max(dict1))

    # enumerate  枚举函数:获取容器内数据时添加序号(默认序号从0开始可以作为索引使用)

    list2 = [1, 2, 3, 4, 5, 6, 7, 8]

    for i in list2:
        print(i)

    # 可不可以同时获取元素的值和元素的索引?  可以 使用enumerate

    # for i in enumerate(list2):
    #     # 直接打印,获取的是以(索引,值)组成的元组
    #     print(i)

    # list
    for index, value in enumerate(list2):
        print(index, value, sep=' : ')

    # tuple
    for index, value in enumerate(tuple1):
        print(index, value, sep=' : ')

    # set
    for index, value in enumerate(set1):
        print(index, value, sep=' : ')

    # str
    for index, value in enumerate(str1):
        print(index, value, sep=' : ')

    # dict
    for index, value in enumerate(dict1):
        print(index, value, sep=' : ')

    # 结论:所有的容器和课迭代类型都可以使用enumerate,并且产生序号,这个序号并不是索引值,而是在生成序号时默认从0开始,碰巧可以在list,str,tuple中当做索引使用
