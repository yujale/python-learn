if __name__ == "__main__":
    # 集合: 集合是一个无序,不重复的数据序列
    # 无序: 程序员无法控制其排不顺序,  程序员无法使用索引查找或修改数据
    # 不重复:没有办法在字典中放入相同的值,会自动去重,类似于字典的键

    # 无序:
    set1 = {1, 2, 5, 6, 3, 4}
    # 程序员无法利用其顺序,有顺序也无用
    # 了解:在集合中会使用数据的值计算哈希值,根据哈希值顺序进行排序
    print(set1)  # {1, 2, 3, 4, 5, 6}

    # 不重复
    set2 = {1, 2, 3, 4, 5, 6, 7, 2, 3}
    # set会自动去重
    print(set2)  # {1, 2, 3, 4, 5, 6, 7}

    # 定义空集合
    set3 = set()
    # {} 是定义空字典的
    print(set3)

    # 集合中能够储存什么数据?
    # 布尔值在进行计算时  True == 1 Fasle == 0
    # 基础数据类型 int  float  bool  字符串 都可以用集合储存
    set4 = {1, 12.3, True, 0, False, ''}
    print(set4)

    # TypeError: unhashable type: 'list'
    # 列表数据无法用集合储存
    # set5 = {1, 12.3, True, 0, False, '', [1, 2]}
    # print(set5)

    # 元组类型可以放入集合内储存
    set6 = {1, 12.3, True, 0, False, '', (1, 2)}
    print(set6)

    # TypeError: unhashable type: 'dict'
    # 字典类型无法用集合储存
    # set6 = {1, 12.3, True, 0, False, '', {1:2}}

    # TypeError: unhashable type: 'set'
    # 集合类型同样不能使用集合嵌套
    # set6 = {1, 12.3, True, 0, False, '', {1,2}}

    # 结论:列表  字典  集合,不能放入集合中,作为元素出现

    # 拓展:不能作为集合元素的数据类型,同样不能作为字典的键出现
    dict1 = {(1, 2): 3}
    print(dict1)
    # TypeError: unhashable type: 'list'
    # 列表 字典 集合不能作为字典的键出现
    dict2 = {[1, 2]: 3}
    print(dict2)