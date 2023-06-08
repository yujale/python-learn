# 文件读写,在使用的时候和我们正常使用文件一样
# 1.打开文件
# 2.操作文件
# 3.关闭文件

# 打开文件使用open函数即可
# 格式: open(file_name(文件路径), mode(读写模式)) 使用该函数会返回一个文件对象
# 文件路径:可以写相对路径, 也可以写绝对路径,路径需要以字符串形式传入
# 读写模式: r(只读)  w(写入)  a()追加
file = open('python.txt', 'r')
print(file)  # <_io.TextIOWrapper name='python.txt' mode='r' encoding='UTF-8'>  在windows中默认读写格式是gbk
print(type(file))  # <class '_io.TextIOWrapper'>
# 将读取出来的内容进行打印
print(file.read())
# 关闭文件
file.close()

# 为什么要关闭文件?
# 在文件打开状态是会保持连接,这种状态下会持续消耗内存,不利于服务器性能优化(内存泄漏)

# 关闭文件后,文件对象有没有被释放?
# 没有释放
print(file)  # <_io.TextIOWrapper name='python.txt' mode='r' encoding='UTF-8'>
# 文件关闭后,相当于与文件的连接状态消失了,但是文件对象没有发生变化
# 在文件关闭后,file对象不能进行任何读写操作,因为已经无法连接文件
# ValueError: I/O operation on closed file.  无法操作一个已经关闭的文件
print(file.read())