if __name__ == "__main__":
    # 字典:储存多个数据,以键值对形式存储,方便快速存取
    # 字典的键要见名知意

    # 字典定义格式: 变量 = {键1:值1, 键2:值2.....}
    dict1 = {'name': 'xiaoming', 'age': 18, 'gender': '女'}
    # 使用print打印可以显示字典中的所有数据
    print(dict1)
    # 查看字典类型
    print(type(dict1))  # <class 'dict'>

    # 空字典定义方法
    dict2 = {}
    # 或者
    dict3 = dict()
    print(dict2, dict3)
    print(type(dict2), type(dict3))

    # 见名知意的重要性
    # 需求: 使用字典保存一个人的信息  xiaoming  18   男  001
    # 保存方式一:
    # dict4 = {'name': 'xiaoming', 'age': 18, 'gender': '男', '学号': '001'}
    # print(dict4)
    # 保存方式二:
    # 字典的优势是快速存取,注意命名键的时候要见名知意,并且易于记忆
    # 字典占用空间远大于列表,使用字典存储数据本来就是牺牲空间确保时间,所以要尽量利用字典快速存取的特性,而不要想空间的节省
    # dict5 = {'xiaoming':18, '男':'001'}  # 不建议这样写

    # 定义字典时 ,不能有重复的键,否则后定义的键值对会覆盖先定义的

    dict6 = {'name': 'xiaoming', 'age': 18, 'name': 'rose'}
    # 字典中的键是惟一的,后定义的内容值会覆盖先定义的
    print(dict6)

    # 字典中键是唯一的但是值可以随意重复
    dict7 = {'name': '小明', 'age': 18, 'id': 18}
    print(dict7)