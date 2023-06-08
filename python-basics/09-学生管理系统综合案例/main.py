# 主程序入口
# 一般开发中 文件夹会使用大驼峰命名法, 包和模块都是下划线分割法
from student_manager import StudentManager


def main():
    # 需求:循环输入,直到用户选择7 则退出
    s1 = StudentManager()
    s1.load_student_info()
    while True:
        # 提示用户输入信息 调用静态方法
        StudentManager.show_info()
        # 接收用户输入的信息
        num = int(input('请输入您要执行的功能:'))
        # 判断要执行的功能并且执行
        s1.choose_option(num)
        input()


main()