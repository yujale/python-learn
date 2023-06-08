# 将数字1所在空间的引用地址赋值给了a
# a = 1
# 将a所保存的引用你地址给了b
# b = a


def func(num_list):
    print(id(num_list))  # 140490414045760
    num_list.append(2)
    return num_list


# 在进行参数传递时,是进行了地址传递,将list1 的引用地址传递给了num_list,num_list 修改内存空间中的数据时,list1,也会发生变化
list1 = [1, 2, 3, 4]


# print(id(list1))  # 140490414045760
# print(func(list1))
# print(list1)

def func2(num_list):
    print(id(num_list))  # 140326362233472
    # 无论什么情况下,使用=赋值运算,就是讲等号右侧数据的引用地址,赋值给等号左侧的变量
    num_list = [1, 2, 3, 4, 5]
    print(id(num_list))  # 140466340833664
    return num_list


print(id(list1))  # 140326362233472
print(func2(list1))  # [1, 2, 3, 4, 5]
print(list1)  # [1, 2, 3, 4]


# 不可变数据类型
def func1(char1):
    print(id(char1))  # 140228523715632
    # 不可变数据类型,在进行参数传递时,也是引用传递,但是他无法修改原有数据空间内的数据,如果想要修改只能改变引用地址,重新赋值(只有=才有改变引用的功能)
    char1.replace('a', 'b')
    return char1


str1 = 'abc'
print(id(str1))  # 140228523715632
print(func1(str1))  # abc
print(str1)  # abc