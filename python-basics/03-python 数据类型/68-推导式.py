if __name__ == "__main__":
    # 推导式
    # 格式: [要插入列表的表达式 for 临时变量 in 数据序列 if  条件]
    list5 = [i for i in range(1, 101) if i % 2 == 0]
    print(list5)

    # 练习:
    # 用推导式进行九九乘法表的生成,将所有的算式放入列表中
    list6 = []
    for i in range(1, 10):
        for j in range(1, i + 1):
            list6.append(f'{j} * {i} = {j * i}')

    print(list6)

    # 改写为推导式:
    list7 = [f'{j} * {i} = {j * i}' for i in range(1, 10) for j in range(1, i + 1)]
    print(list7)

    # 集合推导式
    # 集合推导式和列表推导式完全一致,只不过使用推导式时,外层用{}包裹,并且在序列中会去重
    set1 = {i for i in range(10)}
    print(set1)

    # 获取从1-10 的偶数集合
    set2 = {i for i in range(1, 11) if i % 2 == 0}
    print(set2)

    # 字典推导式
    keys = ['name', 'age', 'gender', 'id']
    values = ['xiaoming', 18, '女', '001']

    # 需求想将key 和value以一对应,形成一个字典
    dict1 = {}
    for i in range(len(keys)):
        dict1[keys[i]] = values[i]

    print(dict1)

    # 改写推导式
    # 格式:{要插入的键:要插入的值  for 临时变量 in 数据序列  if 条件}
    dict2 = {keys[i]: values[i] for i in range(len(keys))}
    print(dict2)

    # 所有的推导式都可以使用for循环改写,所以我们进行推导式的时候先不要急于求成,多改写几次就不用再改写了直接可以写出推导式