# 方法:
# 1.判断用户键入的数字,执行不同的命令
# 2.添加学员
# 3.删除学员
# 4.修改学员
# 5.查询学员
# 6.展示所有学员
# 7.退出程序
# 8.展示信息
from student import Student


class StudentManager(object):

    def __init__(self):
        self.students_list = []

    @staticmethod
    def show_info():
        print('请选择如下功能-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    def choose_option(self, num):
        if num == 1:
            self.add_student_info()
        elif num == 2:
            self.delete_student_info()
        elif num == 3:
            self.modify_student_info()
        elif num == 4:
            self.search_student_info()
        elif num == 5:
            self.show_all_student_info()
        elif num == 6:
            self.save_student_info()
        elif num == 7:
            self.exit_program()
        else:
            print('数据有误')

    def add_student_info(self):
        """添加学员信息"""
        # 获取要添加的学员id
        student_id = input('请输入您要添加的学员id:')
        # 判断学员id是否存在
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                print('该id已经存在,无法添加')
                return
        else:
            name = input('请输入您要添加的学员姓名:')
            age = input('请输入您要添加的学员年龄:')
            s1 = Student(student_id, name, age)
            self.students_list.append(s1)
            print('学员添加成功')

    def delete_student_info(self):
        """删除学员信息"""
        # 获取要删除的学员id
        student_id = input('请输入您要删除的学员id:')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                self.students_list.remove(student_info)
                print('学员删除成功')
                return
        else:
            print('此学员不存在')

    def modify_student_info(self):
        """修改学员信息"""
        # 获取要修改的学员的id
        student_id = input('请输入您要修改的学员id')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                name = input('请输入您要修改为的姓名')
                age = input('请输入您要修改为的年龄')
                student_info.name = name
                student_info.age = age
                print('学员信息修改完成')
                return
        else:
            print('查无此学员')

    def search_student_info(self):
        """查询学员信息"""
        # 获取要查询学员的id
        student_id = input('请输入要查询学员的id')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                # 由于已经重写对了__str__方法,所以打印对象就可以输出信息
                print(student_info)
                return
        else:
            print('要查询的学员不存在')

    def show_all_student_info(self):
        for student_info in self.students_list:
            print(student_info)

    def save_student_info(self):
        """保存学员信息"""
        # 打开文件  如果要依次写入,我们使用a模式
        file = open('student_info.txt', 'a')
        # 遍历学员列表依次将学员信息写入, 学员对象.__dict__
        for student_info in self.students_list:
            file.write(str(student_info.__dict__) + '\n')
        # 关闭文件
        file.close()

    def load_student_info(self):
        """加载学员信息"""
        # 打开文件
        file = open('student_info.txt', 'r')
        # 将学员信息读取出来
        while True:
            content = file.readline()
            # 将字典类型的字符串转换为字典
            if content == '':
                break
            dict1 = eval(content)
            # 创建一个student对象
            # 字典前面+ ** 可以转换为  key = 值的 这种关键字参数赋值形式
            # 将学员信息赋值给对象
            s1 = Student(**dict1)
            self.students_list.append(s1)

        # 关闭文件
        file.close()

    def exit_program(self):
        """退出程序"""
        self.save_student_info()
        exit()