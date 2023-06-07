if __name__ == "__main__":
    # 通过索引进行修改
    list1 = [1, 2, 3, 4]
    # 通过索引查找到指定位置的数据,并进行修改
    list1[1] = 6
    # IndexError: list assignment index out of range
    # 获取的元素位置,必须是存在的
    # list1[6] = 6
    print(list1)

    # 通过索引修改可以同时修改多个值么?  不能
    # list1[(2,3)] = 6,7
    # 可以使用对多变量赋值的形式修改多个值
    list1[2], list1[3] = 6, 7
    print(list1)

    # reverse  列表的反转
    list1 = [1, 2, 3, 4]
    # 列表反转后,索引倒置,并且在原数据上修改,没有产生新的列表
    print(list1.reverse())  # None
    print(list1)  # [4, 3, 2, 1]

    # sort  排序
    list2 = [2, 6, 43, 2, 41, 421]
    # sort是对原有的数据进行了排序,没有产生新的列表.同时,默认排序规则为升序
    # print(list2.sort())  # None
    # print(list2)  # [2, 2, 6, 41, 43, 421]
    # 如果我想让列表降序排列怎么办?
    # 方法一:可以先排序再反转
    # list2.sort()
    # list2.reverse()
    # print(list2)  # [421, 43, 41, 6, 2, 2]
    # 方法二: 可以直接使用倒叙排列
    # list2.sort(reverse=True)  # [421, 43, 41, 6, 2, 2]
    # print(list2)

    # list2.sort(key=排序规则函数)可以帮助我们进行更加复杂的排序
    # 根据每个元素 % 7 的余数大小进行排序
    # 了解, 不要求掌握 后续会讲
    list2.sort(key=lambda x: x % 7)
    print(list2)