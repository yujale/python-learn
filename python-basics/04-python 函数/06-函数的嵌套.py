if __name__ == "__main__":
    # 函数的嵌套,就是在一个函数的内部嵌套了另一个函数的调用

    def function2():
        print('我是func2-----')
        function1()
        print('我是func2-----')


    def function1():
        print('func1执行开始')
        print('func1执行结束')


    # def function2():
    #     print('我是func2-----')
    #     function1()
    #     print('我是func2-----')

    function2()

    # 执行顺序,只要函数在调用之前被定义即可,定义函数的顺序不做规定