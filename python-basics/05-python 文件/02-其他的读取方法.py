# 除了read外还有一些读取方式
# 文件打开
file = open('python.txt', 'r')
# 文件操作
# readline  使用这种方式读取文件,每次读取一行以\n为分隔符,并且在文件打开状态下,会持续向下读取,直到所有文件被读取完成后,会读取空字符串""
# while True:
#     content = file.readline()
#     if content == '':
#         break
#     print(content,end='')

# readlines 读取所有的文件以\n为分隔符,将所有的行以字符串元素的方式保存到列表当中进行返回
# ['吴丝蜀桐张高秋\n', '空山凝云颓不流\n', '举头望明月\n', '低头思故乡\n']
content = file.readlines()

print(content)
# 文件关闭
file.close()