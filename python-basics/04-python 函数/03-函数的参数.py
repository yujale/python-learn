if __name__ == "__main__":
    # 定义一个eat方法,通过传入不同的参数,可以输出不同的生物吃不同的食物

    def eat_cat():
        print('猫吃鱼')


    def eat_dog():
        print('狗吃肉')


    def eat_person():
        print('人吃藕')


    # 上述函数定义方法不太方便,因为如果有更多的生物去吃不同的东西,就要重复书写函数不利于函数的复用

    # 改进 >> 传参
    # 通过传入参数,可以控制函数体内部的执行结果发生变化,让函数更加灵活
    def eat(who, food):  # 在定义时传入的参数叫做形参,只能在函数体内部使用
        print(f'{who}吃{food}')


    # 在调用的时候传入的参数叫做实参,会传入到函数内部被形参接收
    eat('猫', '🐟')
    eat('狗', '肉')
    eat('人', '藕')

    # TypeError: eat() missing 1 required positional argument: 'food'
    # 进行传值时需要保证传参数量满足要求,否则会报错
    # eat('人')
