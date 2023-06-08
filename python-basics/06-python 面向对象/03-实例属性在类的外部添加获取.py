# 在类的外部可以添加或获取实例属性
# 格式:
# 实例属性添加:对象.属性名 = 值
# 实例属性获取:对象.属性名

# 定义类
class Person(object):
    def eat(self):
        print('早饭吃了油条和包子,血糖110')


# 实例化属性
p1 = Person()
# 给p1添加实例属性
p1.name = 'xiaoming'
# 调用实例属性
print(p1.name)  # xiaoming

# 如果我们再创建一个对象,其实例属性name是否存在?  不存在
p2 = Person()
p2.age = 18
# AttributeError: 'Person' object has no attribute 'name'
# print(p2.name)
# print(p1.age)
# 结论:对象被创建后,添加实例属性,对其他的对象不产生影响

# 如果我们对同一个实例属性添加两次值会怎样?
p1.name = 'Rose'
print(p1.name)
# 对象名.属性名 = 值,  如果当前对象的该属性名存在,则重新赋值,如果不存在,则新建一个属性
# 类似于dict

# 扩展  __dict__
# 可以通过__dict__去查询对象的属性,该属性以字典形式保存
# 在计算机底层,对象的属性,保存在一个字典结构的空间内,多以多次赋值会覆盖原来的值,给新的属性赋值,会增加属性数量
print(p1.__dict__)

# 对象属性删除del(扩展)
del p1.name
# AttributeError: 'Person' object has no attribute 'name'
print(p1.name)