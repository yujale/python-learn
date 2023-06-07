if __name__ == "__main__":
    # 数据是否在集合中
    set1 = {1, 2, 3, 4}
    # in 判断元素是否在集合中出现
    print(4 in set1)  # True
    print(5 in set1)  # Fasle

    # not in 判断元素是否不在集合中
    print(4 not in set1)  # False
    print(5 not in set1)  # True

    # 注意:格式  元素 in  集合

    # 判断的数据必须要在集合中能够被储存
    # TypeError: unhashable type: 'list'
    # print([1, 2] in set1)