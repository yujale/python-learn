# 定义学员类,并且在创建学员对象的时候添加学员信息

class Student(object):
    def __init__(self, student_id, name, age):
        """在创建学员对象时,传入学员信息"""
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        """在打印学员对象时,展示学员信息"""
        return f'学员的名字是{self.name}, 今年{self.age}岁, 学号是{self.student_id}'