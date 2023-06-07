
if __name__ == '__main__':
    # 元组:可以储存多个数据,但是元组内的数据不能被修改(元定义后只能被查询)
    # 元组的定义:变量 = (数据1, 数据2, 数据3......)
    tuple1 = (1, 2, 3, 4)
    # 打印后可以展示元组中的全部信息
    print(tuple1)  # (1, 2, 3, 4)
    # 查询数据类型
    print(type(tuple1))  # <class 'tuple'>

    # 如果元组中只有一个元素怎么办? 在单一元素后添加逗号
    tuple2 = (10)
    print(type(tuple2))  # <class 'int'>

    tuple3 = ('10')
    print(type(tuple3))  # <class 'str'>

    tuple4 = (10,)
    print(type(tuple4))  # <class 'tuple'>

    # 如果小括号包裹单一元素数据不添加逗号,则小括号的意义是提升算术运算符优先级

    # 在定义元素或者传值时,元组的括号可以省略

    tuple5 = 1, 2, 3, 4, 5
    print(tuple5)  # (1, 2, 3, 4, 5)
    print(type(tuple5))  # <class 'tuple'>

    tuple6 = 5,
    print(tuple6)  # (5,)
    print(type(tuple6))

    tuple7 = (1, 2, 3,)
    print(tuple7)