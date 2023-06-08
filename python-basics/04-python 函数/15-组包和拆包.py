# 组包:就是讲多个值进行组合,打包为一个容器类型的过程
# 拆包:就是讲一个容器类型,拆分成多个数据,分别赋值给多个变量的过程

# 组包
def func1():
    return 1, 2, 3, 4


# func1返回了多个数据,Python自动将其打包为一个元组,这个过程就是组包
print(func1())  # (1, 2, 3, 4)
# 将多个数据打包整合为一个容器,赋值给变量,这个就是组包过程
a = 1, 2, 3, 4
print(a)

# 拆包(解包)
# 将等号右侧的列表,拆分为四个数据元素,分别赋值给a,b,c,d这个过程就是拆包
a, b, c, d = [1, 2, 3, 4]
print(a, b, c, d)

# 之前我们在循环汇总用过拆包过程
list1 = [1, 2, 3, 4]
for index, value in enumerate(list1):
    print(index, value)

dict1 = {'name': 'xiaoming', 'age': 18}
for key, value in dict1.items():
    print(key, value)

# 同时应用组包和拆包的案例

a = 1
b = 2
# 需求:将a, b进行互换值
# 这个互换过程,是先讲a,b的值提取出来,组包为一个元组,然后进行拆包,将元组内的两个数据分别赋值给,a,b变量
a, b = b, a
print(a, b)

# 注意:字典可以拆包么?可以
dict1 = {'a': 1, 'b': 2, 'c': 3}
# 对字典进行拆包,得到的是字典的键
char1, char2, char3 = dict1
print(char1, char2, char3)

# 集合可以拆包么?  可以
# 对于集合进行拆包,没有任何问题,但是一般不会这样做,因为赋值顺序无法指定
set1 = {'Tom', 'Bob', 'Rose'}
a, b, c = set1
print(a, b, c)