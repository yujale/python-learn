if __name__ == "__main__":
    # while遍历列表
    # len()函数可以查询列表的长度

    list1 = [12, 123, 1, 1, 1234, 12, 34, 8]
    # print(len(list1))
    i = 0
    while i < len(list1):
        print(list1[i])
        i += 1

    # for 遍历列表
    # 推荐使用for循环遍历容器类型(数据序列)
    for i in list1:
        print(i)

    # 练习: list1 = [1,2,3,4,5,5,4,3,2,1,1,2,3,4,5]
    # 需求:使用remove 删除所有的5
    # 需求:使用pop 删除所有的5
    # 需求:使用del 删除所有的5

    # for 循环的本质是什么?  依次提取数据序列中的元素
    # 按照什么依次提取呢?  索引
    # 规律:第一次循环提取下标为0的元素,  第二次循环,提取下标为1的元素,第三次循环提取下标为2的元素.......

    list1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
    # 使用remove删除
    # ValueError: list.remove(x): x not in list
    # 下述方法,循环了len(list1) 次== 15次  一共只有3个5  所以删除到第四次,就没有5了 所以报错
    # for i in list1:
    #     list1.remove(5)

    # 缺点:只有三个5  执行循环15次 性能浪费
    # for i in list1:
    #     if list1.count(5):
    #         list1.remove(5)

    # 这种方法有多少个5就循环多少次
    # for i in range(list1.count(5)):
    #     list1.remove(5)

    # 使用pop删除
    # for i in range(list1.count(5)):
    #     index_1 = list1.index(5)
    #     list1.pop(index_1)

    # 这种方式无法删除所有的5,因为在删除后索引发生了变换,for循环时会跳过某些数据
    '''
    list1 = [1, 2, 3, 4]
    index    0  1  2  3
    for循环遍历 0--列表中没有多余的元素
    第一次循环取下标为0的元素 1, 
    第二次循环取下标为1的元素 2 并且将2 删除
    [1, 3, 4]
     0  1  2
    第三次循环取下标为2的元素 4
    '''
    # for i in list1:
    #     if i == 5:
    #         list1.pop(i)
    # print(list1)

    # i = 0
    # while i < len(list1):
    #     if list1[i] == 5:
    #         list1.pop(i)
    #         continue
    #     i += 1
    # print(list1)

    # 使用del删除
    # for i in range(list1.count(5)):
    #     index_1 = list1.index(5)
    #     del list1[index_1]
    #
    # print(list1)

    # i = 0
    # while i < len(list1):
    #     if list1[i] == 5:
    #         del list1[i]
    #         continue
    #     i += 1
    # print(list1)