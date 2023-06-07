if __name__ == "__main__":
    # 增  使用新的键 = 值的形式增加键值对
    dict1 = {'name': 'xiaoming', 'age': 18}
    # 使用新的键= 值
    # 格式:字典变量[key] = 值  如果为新增,则key在原字典中不存在
    dict1['gender'] = '男'
    print(dict1)  # {'name': 'xiaoming', 'age': 18, 'gender': '男'}

    # 如果原字典中存在该key 则为修改原key所对应的值
    dict1['name'] = 'xiaowang'
    print(dict1)  # {'name': 'xiaowang', 'age': 18, 'gender': '男'}

    # update
    # 一般用于两个字典间的拼接
    # 如果update中添加的键已经存在则修改原有的值
    dict1.update({'id': '001', 'color': 'yellow', 'name': 'rose'})
    print(dict1)