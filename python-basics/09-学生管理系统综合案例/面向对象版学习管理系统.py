import os

class StudetClass(object):
    def __init__(self):
        self.student_list = []  # list()
        print("全局变量:", id(self.student_list))

    # 显示功能菜单的函数
    def show_menu(self):
        print("-----学生管理系统v1.0-----")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 修改学生信息")
        print("4. 查询学生信息")
        print("5. 显示所有学生信息")
        print("6. 退出")


    # 添加学生
    def add_student(self):
        name = input("请输入学生的姓名:")
        age = input("请输入学生的年龄:")
        sex = input("请输入学生的性别:")

        # 定义学生字典类型的变量
        student_dict = {} # dict()
        # 把学生的信息使用字典进行存储
        student_dict["name"] = name
        student_dict["age"] = age
        student_dict["sex"] = sex

        # 把学生信息添加到学生列表中
        self.student_list.append(student_dict)


    # 显示所有学生信息
    def show_all_student(self):
        for index, student_dict in enumerate(self.student_list):
            # 学号和下标的关系
            student_no = index + 1

            print("学号:%d 姓名:%s 年龄:%s 性别:%s" % (student_no, student_dict["name"],
                                               student_dict["age"], student_dict["sex"]))


    # 删除学生信息
    def remove_student(self):
        student_no = int(input("请输入要删除学生的学号:"))
        # 获取学生字典信息的下标
        index = student_no - 1
        if index >= 0 and index < len(self.student_list):
            # 根据下标删除学生信息
            del self.student_list[index]
        else:
            print("请输入正确的学号")

    # 修改学生信息
    def modify_student(self):
        student_no = int(input("请输入要修改学生的学号:"))
        # 根据学号计算下标
        index = student_no - 1

        if index >= 0 and index < len(self.student_list):
            # 根据下标获取学生字典信息
            student_dict = self.student_list[index]

            name = input("请输入您修改后的名字:")
            age = input("请输入您修改后的年龄:")
            sex = input("请输入您修改后的性别:")

            student_dict["name"] = name
            student_dict["age"] = age
            student_dict["sex"] = sex
        else:
            print("请输入正确的学号")


    # 查询学生
    def search_student(self):
        name = input("请输入要查询的学生姓名:")

        # 遍历学生列表信息
        for index, student_dict in enumerate(self.student_list):
            # pass # 空实现
            if student_dict["name"] == name:
                student_no = index + 1
                # 说明找到了这个学生
                print("学号:%d 姓名:%s 年龄:%s 性别:%s" % (student_no, student_dict["name"],
                                                   student_dict["age"], student_dict["sex"]))
                break
        else:
            print("对不起，没有找到这个学生")


    # 保存学生列表数据到文件中
    def save_data(self):
        file = open("student_list.txt", "w", encoding="utf-8")
        # 把列表转成字符串
        student_list_str = str(self.student_list)
        # 把列表数据写入到文件中
        file.write(student_list_str)
        file.close()


    # 加载文件中的数据
    def load_data(self):
        result = os.path.exists("Test")
        print(result)
        # 判断文件或者文件夹是否存在
        if os.path.exists("student_list.data"):
            file = open("student_list.data", "r", encoding="utf-8")

            # 读取文件中的数据
            file_content = file.read()
            new_student_list = eval(file_content)
            print(new_student_list, type(new_student_list))
            # global student_list
            # student_list = new_student_list

            self.student_list.extend(new_student_list)
            print("全局变量:", id(self.student_list))

            file.close()

    # 程序启动的函数
    def run(self):

        # 加载文件中的数据
        self.load_data()

        while True:
            # 显示功能菜单
            self.show_menu()
            # 接收用户的指令
            menu_option = input("请输入您需要的功能选项:")

            if menu_option == "1":
                print("添加学生")
                self.add_student()
            elif menu_option == "2":
                print("删除学生")
                self.remove_student()
            elif menu_option == "3":
                print("修改学生信息")
                self.modify_student()
            elif menu_option == "4":
                print("查询学生信息")
                self.search_student()
            elif menu_option == "5":
                print("显示所有学生信息")
                self.show_all_student()
            elif menu_option == "6":
                # 保存数据到文件
                self.save_data()
                print("退出")
                break

# 执行程序启动的函数
s = StudetClass()
s.run()