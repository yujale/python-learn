if __name__ == "__main__":
    # add 增加
    set1 = {1, 2, 3, 4}
    # set 在使用add命令后,不会产生新的数据,而是原集合中进行修改
    set1.add(5)
    print(set1)  # {1, 2, 3, 4, 5}

    # update 更新
    # TypeError: 'int' object is not iterable
    # update内部只能填写容器类型(数据序列)
    # set1.update(6)
    set1.update([6, 7])
    print(set1)  # {1, 2, 3, 4, 5, 6, 7}
    # 如果更新的数据已经存在,则去重
    set1.update([1, 2])
    print(set1)  # {1, 2, 3, 4, 5, 6, 7}