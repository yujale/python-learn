if __name__ == "__main__":
    # 直接使用key进行查询
    dict1 = {'name': '小明', 'age': 18, 'gender': '男', 'id': '001'}
    # 查询学员的名称?
    print(dict1['name'])

    # get查询
    # 如果我们查询的键不存在会真么样??? 报错
    # KeyError: 'apple'  会出现keyerror  表示查询的键不存在  报错
    # print(dict1['apple'])
    # 使用get进行查询,只需要在get中传入对应的键即可
    # 如果使用get查询的键不存在,则不会报错,会默认返回一个None
    print(dict1.get('name'))  # 小明
    print(dict1.get('apple'))  # None
    # 如果查询的键不存在,get可以自定义默认返回值
    # 格式 字典.get(要查询的键, 查询的键不存在时返回的数据)
    print(dict1.get('apple', '小刚'))
    print(dict1.get('apple', 9))

    # keys 获取当前字典中所有的键
    print(dict1.keys())  # dict_keys(['name', 'age', 'gender', 'id'])
    # keys返回的内容不是列表,而是dict_keys,该数据类型不能直接使用索引查询数据,但是可以进行for遍历
    print(type(dict1.keys()))  # <class 'dict_keys'>
    keys_1 = dict1.keys()
    #  不能使用索引查询
    # TypeError: 'dict_keys' object is not subscriptable
    # print(keys_1[1])
    # 可以被迭代
    for i in keys_1:
        print(i)

    # values 获取当前字典中所有的值
    print(dict1.values())  # dict_values(['小明', 18, '男', '001'])
    # dict_values不能使用索引查询,但是可以迭代
    print(type(dict1.values()))  # <class 'dict_values'>

    # items 获取当前字典中所有的键值对,键值对以元组形式展示
    print(dict1.items())  # dict_items([('name', '小明'), ('age', 18), ('gender', '男'), ('id', '001')])
    # dict_items不能使用索引查询,但是可以迭代
    print(type(dict1.items()))  # <class 'dict_items'>