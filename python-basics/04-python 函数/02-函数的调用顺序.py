if __name__ == "__main__":
    # NameError: name 'sing' is not defined
    # 函数需要先定义后调用否则会报错
    # sing()
    # 定义一个唱歌方法
    def sing():
        print('我再唱青藏高原')


    # 定义一个跳舞方法
    def dance():
        print('我再跳广场舞')


    sing()
    dance()

    # 执行顺序: 先讲所有函数的函数名执行一遍将其储存到缓存中的方法列表中,后续调用函数时去方法列表中查询,如果函数名存在,则调用函数内部的代码,如果函数名不存在将报错
