# 需求拆分:
"""
1.展示学生管理系统的功能有哪些,引导用户键入序号选择功能
2.获取用户键入的功能
3.分析具体要执行哪一项功能
4.执行功能
"""


def print_all_option():
    """用户功能界面展示"""
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员信息')
    print('2: 删除学员信息')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 遍历输出所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


def choose_option(num):
    """分析要执行哪一项功能"""
    if num == '1':
        # 添加学员函数
        add_student_info()
    elif num == '2':
        # 删除学员函数
        delete_student_info()
    elif num == '3':
        # 修改学员函数
        modify_student_info()
    elif num == '4':
        # 查询学员函数
        search_student_info()
    elif num == '5':
        # 展示所有学员函数
        show_students_info()
    elif num == '6':
        # 退出程序函数
        exit_program()
    else:
        print('无此选项,请重新输入')


def add_student_info():
    """添加学员信息"""
    # 1.用户输入学员信息
    # 1.1当用户输入的id值已经存在时,则不让其继续输入,警告,该id已经存在
    stu_id = input('请输入要添加学员的id:')
    # 获取students_list中所有学员的id值(推导式)
    students_id = [i['id'] for i in students_list]
    # 1.2 比对id是否存在,存在则不允许运行
    if stu_id in students_id:
        print('该id值已经存在,无法添加学员')
    else:
        name = input('请输入要添加学员的姓名:')
        age = input('请输入要添加学员的年龄:')
        mobile = input('请输入要添加学员的手机号:')
        # 2.将学员信息添加到students_list当中
        students_list.append({'id': stu_id, 'name': name, 'age': int(age), 'mobile': mobile})
        print('学员添加完成')


def delete_student_info():
    """删除学员信息"""
    # 1.获取要删除学员的id值
    stu_id = input('请输入要删除学员的id:')
    # 2.判断该学员是否存在,如果存在则删除该学员,如果不存在,则提示该学员不存在
    for stu_info in students_list:
        # 判断是否是要删除的学员
        if stu_info['id'] == stu_id:
            # 删除学员并跳出函数
            students_list.remove(stu_info)
            print('该学员已删除')
            return
    else:
        # 执行该命令警告用户没有该学员
        print('该学员不存在,无法删除')


def modify_student_info():
    """修改学员信息"""
    # 1.输入要修改的学员的id值
    stu_id = input('请输入您要修改学员的id:')
    # 2.如果学员存在就修改学员信息,如果不存在则进行提示,学员不存在
    for stu_info in students_list:
        if stu_info['id'] == stu_id:
            # 学员信息修改
            name = input('请输入您要修改为的名字:')
            age = input('请输入您要修改为的年龄')
            mobile = input('请输入您要修改为的手机号:')
            stu_info['name'] = name
            stu_info['age'] = age
            stu_info['mobile'] = mobile
            print('学员信息修改完成')
            return
    else:
        print('该学员不存在,修改失败')


def search_student_info():
    """查询学员信息"""
    # 1.输入要查询学员的id值
    stu_id = input('请输入要查询学员的id:')
    # 2.判断id值是否存在,如果存在则展示,如果不存在,则警告学员不存在
    for stu_info in students_list:
        if stu_info['id'] == stu_id:
            print(
                f'学员的学号是:{stu_info["id"]}, 学员的姓名是:{stu_info["name"]}, 学员的年龄是:{stu_info["age"]}, 学员的手机号是:{stu_info["mobile"]}')
            return
    else:
        print('该学员不存在,查询失败')


def show_students_info():
    """展示所有学员信息"""
    for stu_info in students_list:
        print(
            f'学员的学号是:{stu_info["id"]}, 学员的姓名是:{stu_info["name"]}, 学员的年龄是:{stu_info["age"]}, 学员的手机号是:{stu_info["mobile"]}'
        )


# def exit_program():
#     # import sys
#     # # 退出当前程序,结束进程
#     # sys.exit()
#     exit()

def exit_program():
    """结束程序"""
    # 通过控制变量结束死循环
    global is_stop
    # 在修改之前需要进行声明 ,修改的变量为全局变量
    is_stop = True


# # 展示功能界面
# print_all_option()
#
# # 引导用户输入功能序号,并获取序号
# option = input('请输入您要执行功能的序号:')
#
# # 根据获取的序号分析要执行哪些功能
# chose_option(option)


# 思考:学生管理系统,是不是需要输入6  才能退出 不然就一直询问您要输入的选项
# 这中情况下建议使用 while True 构造死循环

students_list = [
    {'id': '001', 'name': 'xiaoming', 'age': 18, 'mobile': '13833838338'},
    {'id': '002', 'name': 'xiaohong', 'age': 18, 'mobile': '13900000000'}
]
is_stop = False

while not is_stop:
    # 展示功能界面
    print_all_option()

    # 引导用户输入功能序号,并获取序号
    option = input('请输入您要执行功能的序号:')

    # 根据获取的序号分析要执行哪些功能
    choose_option(option)
    # 方便展示,显示所有学员信息,开发完成后删除
    # print(students_list)
    input()

# 死循环的退出方式有哪些?
# break
# return
# exit()
# 控制变量
...