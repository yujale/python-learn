if __name__ == "__main__":
    # remove
    set1 = {1, 2, 3, 4}
    # 使用remove可以删除指定值的元素
    # set1.remove(3)
    # print(set1)  # {1, 2, 4}

    # pop 随机删除一个元素,并且将删除的元素返回
    # print(set1.pop())
    # print(set1)

    # discard
    # 如果使用remove删除的元素不存在会怎样?  报错
    # set1.remove(13)  # KeyError: 13
    # 如果使用discard删除元素呢?  不会报错
    set1.discard(3)
    print(set1)  # {1, 2, 4}
    set1.discard(13)
    print(set1)