if __name__ == "__main__":
    # del
    # 使用del删除键值对,先要找到dict所对应的键,进行删除
    # 注意,在字典中键值对是成对出现的,删除键值也就消失了,不能出现单独的键或者单独的值
    dict1 = {'name': 'xiaoming', 'age': 18}
    del dict1['age']
    print(dict1)  # {'name': 'xiaoming'}

    # clear() 清空字典
    # 使用clear将字典所对应的内存空间中的数据进行了清空
    dict1.clear()
    print(dict1)  # {}

    # 通过之前的学习经验我们猜测 pop是删除简直对用的
    dict2 = {'name': 'xiaoming', 'age': 18, 'gender': '男'}
    # 使用pop可以根据指定的key删除键值对
    # 使用pop删除键值对后会将其键对应的值进行返回
    # print(dict2.pop('name'))  # xiaoming
    # print(dict2)  # {'age': 18, 'gender': '男'}

    # 猜测:popitem也是删除键值对使用的
    # 随机删除一个键值对,一般都是删除最后一个
    # 删除后会将我们所删除的键值对以元组的形式进行返回
    print(dict2.popitem())  # ('gender', '男')
    print(dict2.popitem())  # ('age', 18)
    print(dict2)  # {'name': 'xiaoming'}

    # dict  无序的  因为其不能通过索引进行键值对的获取(了解)
    # Python3.5以后,字典中键值对的顺序和我们插入键值对的顺序保持一致,但是该顺序没法被利用(了解)