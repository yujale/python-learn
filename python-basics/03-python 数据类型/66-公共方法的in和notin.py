if __name__ == "__main__":
    # in 判断元素是否存在于容器当中
    list1 = [1, 2, 3]
    tuple1 = (1, 2, 3)
    set1 = {1, 2, 3}

    print(3 in list1)  # True
    print(3 in tuple1)  # True
    print(3 in set1)  # True
    # 如果要判断是否在set当中,要注意被判断的元素必须可以保存在set当中,如果是列表,字典,集合,则不能判断
    # print([1, 2] in list1)  # False  可以判断,引为[1,2] 可以保存在list1当中
    # print([1, 2] in set1)  # TypeError: unhashable type: 'list' 不能判断,因为[1,2]不能保存到set1当中

    # str类型可以使用in么? 可以
    str1 = '123'
    # TypeError: 'in <string>' requires string as left operand, not int
    # 字符串判断时,左侧的元素只能是字符串类型,否则报错
    # print(1 in str1)
    print('1' in str1)  # True

    # dict 是否可以使用in???
    dict1 = {'name': 123}
    # dict使用in判断的是当前元素是否是dict中存在的键
    print(123 in dict1)  # False
    print('name' in dict1)  # True

    # 如果使用此方法则不能判断字典  列表 集合
    # TypeError: unhashable type: 'list'
    # print([1,2] in dict1)

    # not in  : 所有用法和in相同,只是取反而已

    # 结论:
    # 1.使用in 和not in  被判断的元素在关键字左侧, 数据序列在关键字右侧
    # 2.如果想要判断该元素是否在容器内,该元素必须能保存到容器内,比如集合不能保存列表,字典,集合 所以就不能判断其类型的元素是否在集合内
    # 3.字典判断的是元素是否在keys内,也就是是否是其中的键
