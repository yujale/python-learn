# write 写入
# 当文件读写模式时 'w',可以使用文件的写入操作
# 当文件执行写入模式打开时,如果被打开的文件不存在,则重新创建一个新的文件,不会报错
# file = open('test.txt', 'w')
# 当文件执行写入模式打开时,如果被打开的文件存在,则会将源文件内的字符清空
# 如果使用windows电脑进行开发,在写入文件时,需要制定编码格式为'utf-8'
# 如果使用linux 或者mac 默认是utf-8编码 不需要转码
file = open('python.txt', 'w', encoding='utf-8')
# 当完成文件的读写操作时,我们写入文件  和读取文件所使用的编码格式必须一致
# UnicodeDecodeError: 'gbk' codec can't decode byte 0x89 in position 14: illegal multibyte sequence
print(file)  # <_io.TextIOWrapper name='python.txt' mode='w' encoding='UTF-8'>
# 写入操作
# file.write('我爱北京天安门,天安门上太阳升')
# 如果写入的字符串时三对引号包过内部的换行符会不会写入呢?  会写入格式
# file.write("""
# 我爱北京天安门,
# 天安门上太阳升
# """)

# writelines 是配合readlines进行使用的,可以将一个由字符串元素组成的列表一次性写入文件
# file.writelines('我爱北京天安门')
lines = ['吴丝蜀桐张高秋\n', '空山凝云颓不流\n', '举头望明月\n', '低头思故乡\n']
file.writelines(lines)

file.close()