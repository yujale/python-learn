# 需求:批量修改指定目录下所有文件的文件名
'''
1.修改时可以通过参数控制是增加,还是删除字符
2.传入指定字符用于增加或者删除
3.使用rename进行重命名
'''

# 导入os模块
import os

# 定义一个控制增加还是删除的变量,True是增加 False 是删除
flag = False
# 指定字符的定义
str1 = '[黑马出品]'


# 构造多个文件:要在文件目录下构造 test1-test10 十个文件
# for i in range(1, 11):
#     open('文件/test' + str(i), 'w')

# 定义函数
def modify_files_name(flag, str1, path):
    # 切换工作目录为指定的目录path
    os.chdir(path)
    # 遍历指定路径下的所有文件名称
    for file_name in os.listdir():
        # 判断时增加字符还是删除字符
        if flag:
            # 重命名添加文件前缀
            os.rename(file_name, str1 + file_name)
        else:
            # 重命名删除文件名中指定的字符
            os.rename(file_name, file_name.replace(str1, ''))


# 将文件目录下所有的文件添加[黑马出品]的前缀
# modify_files_name(flag, str1, '文件')
modify_files_name(flag, str1, '文件')