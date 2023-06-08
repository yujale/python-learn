# 不定长参数主要就是在定义函数时,不确定参数的个数时即可进行不定长参数的书写

'''
位置不定长参数的定义格式:
def 参数名(*args):
    函数体
'''


# def func(*args):
#     print(*args)  # 相当于书写内容为  print(1,2,3)
#
#
# func(1, 2, 3)
# print(1, 2, 3)

# args变量到底内部是什么样子的?
# def func(*args):
#     return args

# 数据传入函数内部时,将传入的多个数据进行打包,转换为一个元组,被args接收.并且在函数体内部可以使用该元组参与运算
# print(func(1, 2, 3))  # (1, 2, 3)


# 案例:
# 输入不确定数量的多个值,判断其中的最大值

def max1(*args):
    max_num = args[0]  # 如果max_num = 0 这个时候我们所有值都没负的时候会判断出错
    for i in args:
        if i > max_num:
            max_num = i
    return max_num


print(max1(1, 4, 5, 3, 6, 12, 3))

# 如果输入的数值全部为负呢?
print(max1(-1, -2, -5))