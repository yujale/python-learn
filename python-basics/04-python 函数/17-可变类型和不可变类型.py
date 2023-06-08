# 传参或者变量的传递是进行了值的传递 还是进行了引用地址的传递呢?

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
#  id的值,我们称呼他为引用地址,list1 和list2 的引用地址不相同
print(id(list1))  # 140652966394496
print(id(list2))  # 140652968507776

# 如果我向list1 中添加以数字,次数list2 中的值为多少? [1,2,3,4]
list1.append(5)
print(list1)
print(list2)
# 在list1中添加了数据,那list1的引用地址会发生变化么? 不会变化
# list1,在使用append方法时,是将内存空间中的值进行了变化,没有修改内存地址,所以id值不变
print(id(list1))  # 140652966394496

# 如果我们使用list1 = list2,list1的引用地址发生变化了么?  变化
list1 = list2
# 在对list1赋值时,list2 将list1中的内存地址赋值给了list1,此时,list1和list2指向同一块内存空间
print(id(list1))  # 140652968507776

# 如果在list1中删除下标为1的元素,list2 会发生变化么? 会变化
# list1  和list2 指向同一块内存空间,所以内存空间中的数据发生了改变,list1 和list2 均发生了变化
list1.pop(1)
print(list1)  # [1, 3, 4]
print(list2)  # [1, 3, 4]

# list 内存空间中的数据可以发生改变,这种数据类型我们称之为可变数据类型

# 练习:
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list1 = [1, 2, 3, 4, 5]
list2 = list1
list1.pop(2)
list1 + list2
# list1 和list2  分别是多少
print(list1)
print(list2)

# 练习:
str1 = '12345'
str2 = '12345'
str1 = str2
str1 = '123'
str2 + str1
print(str1)
print(str2)

str1 = '123'
str2 = '123'
print(id(str1))  # 140509725727984
print(id(str2))  # 140509725727984

# 我么可以修改str内部的元素么?  不可以
# TypeError: 'str' object does not support item assignment
# str1[0] = '2'
# 既然内部元素不可修改,系统定义其值相同时,数据引用地址也相同

# 我么称这种内存空间中的数据无法被修改的值为不可变数据类型


# 结论:
# 可变数据类型:  列表,集合,字典
# 不可变数据类型: 字符串,元组,整型,浮点型,布尔型

# 结论:在数据的传递过程中,是引用传递,不是值的传递