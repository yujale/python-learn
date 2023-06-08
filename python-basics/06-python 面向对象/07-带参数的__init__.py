# 每次我们创建对象时,如果使用init方法,是不是只能添加同一个值的属性呢?
# 如果我们能够将参数传递到init方法中,是不是就可以在创建对象时,动态添加属性值了呢?
# 我们怎样给init进行传参呢?
# 面临的问题: 1.我们不需要手动调用init  在哪里给他传参呢?  2.我们传参时到底传什么参数给init方法呢?

# 在实例化对象时,类名(参数1, 参数2....)这些参数会传递给init方法,进行使用

# class Person(object):
#     def __init__(self, name, age):
#         print(name, age)


# TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
# p1 = Person()
# 既然我们给init方法中添加了参数,就必须传值,否则就会报错
# 在Person的括号中传参,就可以传递到init方法中,传参的数量,就是init方法中除了self之外的位置参数的数量
# p1 = Person('Jack', 18)  # Jack 18
# 结论: 在Person类创建对象时,在()内添加参数,可以被init接收但是,传参数量和inti方法中的形参必须一致

# 怎样实现动态的实例属性添加呢?

class Person(object):
    def __init__(self, name, age):
        # self.属性名 = 参数  将函数外部传递进来的参数赋值给对象,创建实例属性
        self.name = name
        self.age = age


# 实例化对象时要正确传参
p1 = Person('Rose', 17)
print(p1.name, p1.age)
# 创建第二个对象,查看属性是否动态传递成功
p2 = Person('Jack', 18)
print(p2.name, p2.age)

# 通过这种方式,我们在创建对象时可以指定其不同对象属性的值不同,但是所有的对象包含的属性类别相同
# 这种形式下一定要给每一个对象单独赋值,或者给init方法中的属性一些默认值,否则会报错