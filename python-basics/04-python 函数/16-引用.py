# 在Python中所有的数据分为三个维度: 值(判断==), 数据类型(int...float...), 唯一标识(id)

# 值相等的数据,唯一标识和数据类型不一定相等
bool1 = False
int1 = 0
# 0 和False的值相等
print(bool1 == int1)  # True
# 数据类型不等
print(type(bool1) == type(int1))  # False
# 唯一标识不等
# id 判断数据是否是同一内存空间中的数据(同一内存空间中的数据必相等)
print(id(bool1) == id(int1))  # False

# 值和数据类型相等的,唯一标识不一定相等
list1 = [1, 2, 3]
list2 = [1, 2, 3]
# list1 和list2 值相等
print(list1 == list2)  # True
# list1和list2 数据类型相等
print(type(list1) == type(list2))  # True
# list1 和list2 的唯一标识不等,也就是说,其所在的内存空间不一致
print(id(list1) == id(list2))  # False

# 唯一标识相等的, 值和数据类型必然相等
# 在同一内存空间中只能储存同一个值
str1 = 'abc'
str2 = 'abc'
# str1 和str2 的唯一标识相等
print(id(str1) == id(str2))  # True
# 数据类型相等
print(type(str1) == type(str2))  # True
# 数据值相等
print(str1 == str2)  # True

# 怎样判断id  唯一标识是否相等呢?  is关键字
# 使用is可以判断是否为同一个内存空间中的数据
print(list1 is list2)  # False
print(str1 is str2)  # True