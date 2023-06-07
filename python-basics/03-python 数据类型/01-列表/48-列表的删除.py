if __name__ == "__main__":
    # del  将数据引用切断
    list1 = [1, 2, 3, 4]
    # del list1
    # NameError: name 'list1' is not defined
    # del不仅可以删除元素,也可以删除任何变量,非常强大,但是有些不安全
    # print(list1)
    # 那del 怎样删除元素呢?  通过索引获取当前元素,并删除
    del list1[2]
    # IndexError: list assignment index out of range
    # 使用下标查找数据时,下标索引不能不存在
    # del list1[9]
    print(list1)  # [1, 2, 4]

    # 如果要是循环中能够删除么?
    # 此处并没有删除,因为i是临时变量,我们使用del是在讲i和2的引用关系删除,但是list1 和 2 的引用关系没有删除
    # for i in list1:
    #     if i == 2:
    #         del i
    #
    # print(list1)

    # pop  删除指定索引的元素,并且返回该元素
    list1 = [1, 2, 3, 4]
    # 删除后可以返回被删除的对象
    print(list1.pop(2))
    # IndexError: pop index out of range
    # 使用pop进行删除的元素下标一定要存在
    # print(list1.pop(12))
    # 删除后,指定索引位置的元素消失后边的元素统一向左移动一位
    # pop也会造成索引变换
    print(list1)
    # 如果不给pop进行传值,默认删除最后一个元素
    print(list1.pop())
    # 查看删除后结果
    print(list1)

    # remove 删除指定的元素(从左至右第一次出现的元素)

    list1 = [1, 2, 3, 3, 4, 2, 1]
    # 删除列表中的2
    # 将从左至右查询第一次遇到的2进行了删除,并不能删除类表中所有的的2
    list1.remove(2)
    print(list1)  # [1, 3, 3, 4, 2, 1]

    # remove会返回被删除的内容? 不会
    print(list1.remove(3))  # None
    # remove删除的内容不存在会怎样?
    # list1.remove(123)  # ValueError: list.remove(x): x not in list

    # clear  清空列表
    # 就是讲列表置为[],但是与list1 = [] 有本质区别
    list1.clear()
    print(list1)  # []