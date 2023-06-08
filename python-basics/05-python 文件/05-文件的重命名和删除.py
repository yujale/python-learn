# 如果想要使用这两个方法,就要去进行模块导入
import os

# rename  重命名  >>>类似于linux命令中的mv
# 格式:os.rename(旧文件路径,新文件路径)
# 需求:将Python.txt重命名为 abc.txt
# rename可以对文件进行重命名
# rename中源文件路径必须存在
# os.rename('bigdata.txt', 'abcd.txt')
# 文件可以通过rename进行移动,移动的位置根据新文件路径决定,移动后同样可以修改名称
# os.rename('abcd.txt', '文件/abcd.txt')
# 文件移动时必须有文件名称,否则无法移动,移动后可以改名
# os.rename('abc.txt', '文件/a.txt')


# remove  删除文件  >>> 类似于linux里的rm
# 可以删除文件,但是不会有任何提示,但是也不会出现在回收站中,误删后无法回复,删除需谨慎
# os.remove('bigdata[备份].txt')
# 可以删除指定路径下的文件
# 如果被删除的路径不存在,则报错  (路径可以使用绝对路径,和相对路径)
# os.remove('文件/a.txt')
# os.remove('python[备份].txt')
# PermissionError: [Errno 1] Operation not permitted: '文件'
# 使用remove不能删除文件夹
os.remove('文件')