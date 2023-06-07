if __name__ == "__main__":
    # 通过索引修改字典中的键值对
    dict1 = {'name': '小明', 'age': 18}
    dict1['name'] = '小红'
    print(dict1)

    # update
    # 可以进行制定字段值的修改
    # dict1.update(name='小绿')
    dict1.update({'name': '小绿'})
    print(dict1)