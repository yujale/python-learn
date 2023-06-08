# 'a'模式写入:追加模式
# 在追加模式下可以进行文件字符的追加,在原有数据的末尾添加 新的字符
# 在追加模式下打开文件,如果文件存在,则不会讲源文件清空
# file = open('python.txt', 'a', encoding='utf-8')
# 在追加模式下打开文件,如果文件不存在,则新建一个文件
# 打开文件
file = open('bigdata.txt', 'a', encoding='utf-8')
# 进行追加操作(注意:没有append方法,追加操作也是使用write进行写入,只不过不会清空源文件)
file.write('乱我心者今日之日多烦忧')
# 关闭文件
file.close()