if __name__ == "__main__":
    # 字典的遍历
    dict1 = {'name': '小明', 'age': 18, 'gender': '男', 'id': '001'}

    # 使用for循环对字典进行遍历,默认获取的是字典的每一个键
    for i in dict1:
        print(i)
    '''
    name
    age
    gender
    id
    '''
    # 获取的是字典的每一个键
    for i in dict1.keys():
        print(i)
    '''
    name
    age
    gender
    id
    '''

    # 获取的是字典的每一个值
    for i in dict1.values():
        print(i)
    '''
    小明
    18
    男
    001
    '''

    # 获取的是字典中每一个键值对组成的元组
    for i in dict1.items():
        print(i)
    '''
    ('name', '小明')
    ('age', 18)
    ('gender', '男')
    ('id', '001')
    '''
    # 有没有办法可以分别拿到字典的键和值呢?

    for i in dict1:
        print(i, dict1[i])

    for key, value in dict1.items():
        print(key, value)