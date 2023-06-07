if __name__ == "__main__":
    # 列表的嵌套: 在一个列表中包含其他的列表元素

    name_list = [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]

    # 需求:想要获取李四的值
    # 获取李四所在的子列表的索引,并通过索引获取该子列表值
    print(name_list[2])
    # 再从子列表中通过李四所在的索引获取其值
    print(name_list[2][1])

    # 如果我们想要获取嵌套列表中的每一个值,我们需要怎么做?
    # 如果进行一次循环,每次循环所得到的都一级列表中的元素,也就是每一个子列表
    for i in name_list:
        print(i)

    # 如果想要对嵌套后的列表进行输出,需要进行循环嵌套
    for sub_list in name_list:
        for name in sub_list:
            print(name)

    # 这样就可以进行所有名称的输出了

    # 如果当前的列表内的数据不都是子列表,有其他数据类型的数据,则不能直接使用循环嵌套,需要先进行类型判断