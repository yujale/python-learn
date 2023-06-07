if __name__ == "__main__":
    # append 在列表末尾追加数据
    num_list = [1, 2, 3, 4]
    # 能够打印出1,2,3,4,5么?
    # print(num_list.append(5)) # None
    # 如果直接打印append方法的调用,将不会输出任何内容
    # list类型在使用append 方法时不会产生新的列表,而是在原有列表上进行修改
    num_list.append(5)
    # append 追加的数据,默认追加到列表末尾,追加完成后在原有数据上修改
    print(num_list)  # [1, 2, 3, 4, 5]

    # # str
    # str1 = 'abc'
    # # str类型数据,调用replace方法时,不会修改原有数据,而是产生了一个新的字符串
    # str2 = str1.replace('abc', 'cba')
    # print(str1)
    # print(str2)

    # extend  追加数据序列
    # 格式: 列表1.extend(数据序列)
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    # 追加数据序列后,调用extend的列表发生变化, 括号内的数据序列不变
    # 其实底层逻辑就是讲括号内的数据序列迭代,依次放入调用该方法的列表中
    list1.extend(list2)
    print(list1)  # [1, 2, 3, 4, 5, 6]
    print(list2)  # [4, 5, 6]

    # 追加字符串序列时,会将字母依次拆分并放入列表中
    str1 = 'itcast'
    list2.extend(str1)
    print(list2)  # [4, 5, 6, 'i', 't', 'c', 'a', 's', 't']

    # 如果括号内填写的数据,不是数据序列会怎样?
    # TypeError: 'int' object is not iterable  括号内必须是可迭代对象
    # list2.extend(4)
    # 字符串累心哪怕只有一个值,或者只有一个空字符串,都是可迭代类型,同理可知,列表,元组等  哪怕只有以数据或者为空类型也是可迭代类型
    list2.extend('3')
    print(list2)

    # insert 插入
    num_list = [1, 2, 3, 4]
    # 格式:列表.insert(要插入位置的索引, 要插入的对象)
    # 在insert中第一个参数是要插入位置的索引,所以如果插入了数,则该被插入数据的索引变为第一参数所显示的索引
    # 原来该位置的元素以及之后的元素下标+1(向后移动一位)
    # 如果使用insert进行 插入,可能会造成索引混乱,原来引用的索引发生错误
    # 在开发中除非明确所有的索引引用都修改完成,否则不要使用insert
    # append 插入数据,要比insert插入数据更安全
    num_list.insert(1, 5)
    print(num_list)

    # extend 和append 进行对比
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    # append将list2 当做一个元素追加到列表末尾
    # list1.append(list2)  # [1, 2, 3, 4, [5, 6, 7, 8]]
    # extend将list2 当做多个元素进行拆分后追加
    list1.extend(list2)  # [1, 2, 3, 4, 5, 6, 7, 8]
    print(list1)