## 1、循环中的else

- for...else...
- while...esle...
- 如果循环正常结束，则执行else中的代码，如果循环异常结束，不执行else中的代码
  - break 可以打破循环造成循环异常结束
  - continue不会造成循环异常结束

```python
# 语法结构
'''
while 循环条件:
    条件满足,则循环执行此代码
else:
    循环条件不成立执行此代码,执行后循环结构终止
'''

# 需求: 下载一个视频  从0% - 100%,下载完成后,显示下载完成 否则不显示
# 循环条件成立,则反复执行循环体中的代码,如果循环条件不成立,则执行else中的代码
# break打破了循环结构,循环异常终止,没有执行到循环条件不成立的那一刻,所以else不会被执行
# continue没有打破循环结构,循环正常进入循环条件不成立的状态后才会终止,此时执行else中的命令

i = 0
while i <= 100:
    if i == 60:
        print('下载非法文件,已经将你举报,下载终止')
        # break  # 会造成循环异常终止,不会执行else中的代码
        i += 1
        continue  # 不会造成循环异常终止,会执行else中的代码
    print(f'下载进度:{i}%')
    i += 1
else:
    print('下载完成')
```

```python
# 语法结构
'''
for 临时变量  in 数据序列(容器):
    循环执行的代码
else:
    所有元素遍历完成后执行的代码
'''

# 需求: 下载一个视频  从0% - 100%,下载完成后,显示下载完成 否则不显示
for i in range(0, 101):
    if i == 60:
        # print('别下了,网费用光了')
        # break  # 打破循环,造成循环异常结束,不会执行else 中的命令
        print('丢包,这里没有下载好继续下载别的吧')
        continue # 结束本次循环,进入下一次循环,不会造成循环异常结束,会执行else中的命令
    print(f'下载进度:{i}%')
else:
    print('下载完成')
```

## 2、字符串的定义以及输入输出

- 字符串定义方式
  - 一对单引号
  - 一对双引号
  - 三对单引号
  - 三对双引号
- 如果我们想输出单引号或者双引号，直接在最外层包裹其他的字符串定义形式即可
- 输入： input
- 输出：print
- 字符串可以进行格式化处理： f-string   传统占位符形式拼接

```python
# 字符串的定义方式
# 单引号
str1 = 'hello world!!!'  # <class 'str'>
print(type(str1))
# 双引号
str2 = "hello python"  # <class 'str'>
print(type(str2))
# 三对单引号
str3 = '''hello bigdata'''  # <class 'str'>
print(type(str3))
# 三对双引号
str4 = """hello china"""  # <class 'str'>
print(type(str4))


# 一对引号和三对引号的区别
# 在一对引号内部进行手动换行,无法修改其字符串的格式,必须使用转义字符\n \t等
str1 = 'hello ' \
       'world'
print(str1)

# 在三对引号内进行手动换行,可以在打印时输出换行格式,无需使用转义字符
str3 = '''hello 
bigdata'''
print(str3)

str4 = """
弃我去者昨日之日不可留
乱我心者今日之日多烦忧
长风万里送秋雁
对此可以酣高楼
......
"""

# 三对引号可以作为多行注释


# 需求 : 输出  I'm Jake.
# 如果字符串被双引号包裹,则内部可以单独使用单引号
print("I'm jake")
# 需求:输出"鲁迅说:I'm a 周树人"
print('''"孔子说:I'm a 文豪"''')
```

```python
# 输入 input
user_name = input('请输入你的用户名')

# 输出
print(f'您的用户名是{user_name}')
print('您输入的用户名是%s' % user_name)
```

## 3、字符串索引

- 索引就是系统给字符串中每一个元素的编号
  - 正数索引：从0开始，从左至右依次递增
  - 负数索引：从-1来时，从右至左依次递减
- 使用索引可以获取字符串中的元素
  - 字符串[元素的索引]

```python
# 什么是字符串索引?
# 就是保存字符串时,将所有字符依次存入字符串所在空间,并且按照顺序将元素依次存放, 为了方便存取数据,我们讲元素进行编号,从0开始依次递增
# 通过下标索引,可以获取元素,或者进行切片等操作

str1 = 'itheima'
# 通过索引获取元素的格式:  字符串[元素索引]
# 需求:想获取第5个元素
print(str1[4])
# 需求:获取t
print(str1[1])

'''
i  t  h  e  i  m  a
# 正数索引
0  1  2  3  4  5  6
# 负数索引
-7 -6 -5 -4 -3 -2 -1
'''
# 结论:字符串中的索引,正数索引从0开始,从左至右依次递增, 负数索引,从-1开始从右至左依次递减
# 需求:使用负数索引取 m
print(str1[-2])
print(str1[-4])
```

## 4、字符串切片

- 字符串切片就是讲字符串中的一部分数据按照指定规则进行分隔得到的新的字符串
- 字符串切片的格式

```python
字符串[起始位置索引：终止位置索引：步长]
```

- 起始位置可以省略：
  - 步长为正：起始位置默认为字符串开始
  - 步长为负：起始位置默认为字符串结束
- 终止位置可以省略：
  - 步长为正：终止位置默认为字符串结束
  - 步长为负：终止位置默认为字符串开始
- 步长可以省略，省略后默认为1，并且可以省略冒号
- 复制字符串：str[:]
- 反转字符串：str[::-1]
- 注意：如果步长为正，则起始位置在终止位置左侧，如果步长为负，则起始位置在终止位置右侧

```python
# 切片:就是按照一定的索引位置和步长将字符串分割出一部分就是切片
# 切片的格式:数据序列[起始位置索引:结束位置索引:步长]   字符串,列表,元组,都可以进行切片

str1 = 'itheima'
# 需求:将the切片出来
# 字符串切片以及其他容器类型的切片操作,都会重新生成一个新的数据序列,不会对原有数据序列产生影响
str2 = str1[1:4:1]
print(str2)

# 切片逻辑
# 起始位置: 字符串切片的起点(包含)
# 结束位置:字符串切片的终点(不包含)
# 在开发中绝大多数范围区间是左闭右开区间,其余内容单独记忆(例如 randint是一个闭区间)
# 步长:步长就是每一次查找数据的间隔(相邻两个索引的差值就是步长)

str2 = '我爱北京天安门,天安门上太阳升!'
# 获取"北京天安门"
print(str2[2:7:1])
# 如果步长为1 可以被省略
# 步长省略后,:也可以省略
print(str2[2:7])

# 起始位置也可以省略
# 如果起始位置省略,步长为正数,则起始位置为字符串开始
print(str2[:7:1])  # 我爱北京天安门
# 如果起始位置省略,步长为负数,则起始位置为字符串末尾
print(str2[:7:-1])  # !升阳太上门安天
# 为什么为空?  字符串切片起点 是索引为2 的位置, 步长是-1  切片区间[2,7),此时从2的位置从右向左步长为1 切片此区域没有数据.
print(str2[2:7:-1]) # 空字符串
# 结论: 如果步长是负数,开始位置要在结束位置右侧,否则没有数据

# 结束位置可以省略
# 如果结束位置省略,步长为正数,则结束位置为字符串末尾
print(str2[8::1])  # 天安门上太阳升!
# 下方表达式和上一行是否含义相同? 不相同,因为结束位置写-1不包含结束位置
print(str2[8:-1:1])  # 天安门上太阳升


# 如果结束位置省略,步长为负数,则结束位置为字符串开始
print(str2[8::-1])  # 天,门安天京北爱我
# 如果结束位置写0  含义也不相同
print(str2[8:0:-1])  # 天,门安天京北爱我

# 需求:在字符串中截取"天门天门"
print(str2[4: 11: 2])  # 天门天门
# 在使用字符串切片进行非1步长书写时,要注意起始位置和结束位置,并且查看间隔

# Python中优雅的字符串反转方式
print(str2[::-1])  # !升阳太上门安天,门安天京北爱我

# python中复制数据序列的方法
str3 = str2[:]
print(str3)  # 我爱北京天安门,天安门上太阳升!
```

## 5、字符串查询

- index：查找字符串中子字符串所在位置i，如果有该字符串，查询其==从左至右==第一次出现的位置的正数索引，==否则报错==。
- find：查找字符串中子字符串所在位置i，如果有该字符串，查询其==从左至右==第一次出现的位置的正数索引，==否则返回-1==。
- rindex：查找字符串中子字符串所在位置i，如果有该字符串，查询其==从右至左==第一次出现的位置的正数索引，==否则报错==。
- rfind：查找字符串中子字符串所在位置i，如果有该字符串，查询其==从右至左==第一次出现的位置的正数索引，==否则返回-1==。
- count：查询子字符串在指定字符串中出现的次数。

```python
str1 = 'hello python'
# index
# 需求:查找p所在的索引位置
# 格式: 字符串.index(self(不用传值), sub(子字符串), start(起始位置), end(结束位置))
print(str1.index('p'))  # 6
# 如果字符串中含有多个子字符串,则会返回指定范围内的从左至右的第一个查找到的子字符串位置索引
print(str1.index('o'))  # 4
# 查询指定范围内的字符串,虽然指定了范围,但是计算索引是从左至右依次递增的
print(str1.index('o', 5, 12))  # 10
# ValueError: substring not found
# 结论:找不到对应的子字符串,则会报错,如果能够查找到数据返回当前子字符串的正数索引
# 指定查找范围是左闭右开区间
# print(str1.index('o', 5, 10))  # 10
print(str1.index('o', 10, 12))  # 10

# find
str1 = 'hello python'
# 需求:查找p所在的索引位置
# 格式: 字符串.find(self(不用传值), sub(子字符串), start(起始位置), end(结束位置))
print(str1.find('p'))  # 6
# 如果字符串中含有多个子字符串,则会返回指定范围内的从左至右的第一个查找到的子字符串位置索引
print(str1.find('o'))  # 4
# 指定范围查找
# 需求:查找o 指定范围为  5,10   10,12
# 结论:使用find进行查询时,如果查询的子字符串不存在,则返回-1,如果存在则返回指定正数索引
# find的查询范围是左闭右开区间
print(str1.find('o', 5, 10))
print(str1.find('o', 10, 12))
# 查询的子字符串可以是单个字符可以是多个字符
print(str1.find('python')) # 6

# rfind
# 和find使用方式完全相同,只是在查询时,从右至左查询,返回第一次查询到的字符索引,返回的依然是正数索引
print(str1.rfind('o'))  # 10
# rindex
# 和index使用方式完全相同,只是在查询时,从右至左查询,返回第一次查询到的字符索引,返回的依然是正数索引
print(str1.rindex('o'))

# 结论:index 和 find 使用方法完全一致,只是,index 在查询不到子字符串时会报错,find会返回-1

# count() 计数
# 使用count 可以返回当前子字符串在指定字符串中出现的次数
# 需求:查询o在str1 中出现的多少次
# 提示:在大多数编程语言中,  计数从1开始数,  索引或编号,从0开始编号
# 格式: 字符串.count(self(不用传值, x(要查询个数的子字符串), start(开始位置), end(结束位置)))
print(str1.count('o'))
# 需求,查询指定范围内h的个数   从1-9  9-12
# 结论:1.count查询的范围是一个左闭右开区间
#     2.如果没有查询到子字符串则返回0  不会报错
print(str1.count('h', 1, 9)) # 0
print(str1.count('h', 9, 12)) # 1
```

## 6、字符串替换

- replace：将旧值替换指定字符串中的新值

```python
# replace
str1 = 'hello python'
# 需求: 将o 替换为 $
# 格式: replace(self(不用传值), old(旧值), new(新值), count(替换次数))
print(str1.replace('o', '$'))  # hell$ pyth$n
# 指定替换次数
# 如果不指定替换次数,默认将所有的制定字符全部替换
print(str1.replace('o', '$', 1))  # hell$ python
# 如果指定的替换次数大于出现的次数,则也是只替换出现的次数
print(str1.replace('o', '$', 10))  # hell$ python
```

## 7、字符串的拆分和合并

- split：字符串按照指定分隔符进行拆分
  - 拆分后得到的结果是有拆分后的字符串组成的一个列表
  - 拆分后，所有的分隔符消失
- join：将字符串序列（容器类型中所有元素均为字符串）按照指定分隔符进行合并

```python
# split 字符串拆分
str1 = 'I love Python and java and c and lixiaolong'
# 需求: 将所有的单词按照空格为分隔符进行拆分,拆分为多个字符串
# split 会按照指定分隔符进行拆分,拆分完成后 会将所有的拆分后的结果以字符串形式保存到列表中
# split(self(不用传值), sep(分隔符), maxsplit(最大分割次数))
print(str1.split())  # ['I', 'love', 'Python', 'and', 'java', 'and', 'c', 'and', 'lixiaolong']
# 指定最大分割次数
# 可以把split看成一把刀,字符串看成一条线,砍一刀分成两份,砍两刀分成3分以此类推
print(str1.split(' ', 3))  # ['I', 'love', 'Python', 'and java and c and lixiaolong']

# 需求:按照以'a'为分割符进行拆分,将str1 最大拆分次数60次
# 使用谁作为分隔符,则拆分后该分隔符消失,
# 最大拆分次数如果超过可以拆分的上限,则保持拆分上线即可,不会报错
print(str1.split('a', 60))  # ['I love Python ', 'nd j', 'v', ' ', 'nd c ', 'nd lixi', 'olong']



# join 字符串合并
list1 = str1.split()
list2 = [1,2,3,4,'abc']
print(list1)
# 将list1  按照指定分隔符❤  合并为一个字符串
# 格式:分隔符.join(iterable(可迭代类型))
print('❤'.join(list1))  # I❤love❤Python❤and❤java❤and❤c❤and❤lixiaolong
# 进行join合并时,要注意可迭代类型中全部元素都要是字符串类型,否则无法合并
print('❤'.join(list2))  # TypeError: sequence item 0: expected str instance, int found
```

## 8、字符串转换

- capitalize：将字符串首字母大写，其余字母小写
- title： 将字符串中每个单词首字母大写（任何非字母字符都可以作为单词分隔符）
- upper：将字符全部变为大写
- lower：将字符全部变为小写

```python
# 字符串中各种大小写转换
str1 = 'hello woRld aNd Python'
# capitalize  将字符串的第一个字母大写,同时讲其余全部字母小写,  对数字和汉字等不做处理
print(str1.capitalize())  # Hello world and python

# title  将所有的单词首字母大写,其余字母变为小写
# 在Python中怎样对单词进行辨别, 非字母字符都可以作为分隔符
str2 = 'hello中国python'
print(str1.title())  # Hello World And Python
print(str2.title())  # Hello中国Python

# upper()将数据全部变为大写
print(str1.upper())  # HELLO WORLD AND PYTHON
# lower()将字符全部变为小写
print(str1.lower())  # hello world and python
```

## 9、字符串两侧指定字符删除

- strip：删除字符串两侧的指定字符
- rstrip：删除字符串右侧的制定字符
- lstrip：删除字符串左侧的指定字符

```python
# strip 去重字符串左右两侧指定字符
str1 = '    hello  python\t \n     '
# strip中如果不传参数,则去除字符串左右两侧的空白(包括空格,换行,制表位等)
print(str1.strip())  # hello  python
# 格式:字符串.strip(self(不传值), chars(可以传一个字符或多个字符))
str2 = '$$$hello Python$$$'
# 删除字符串左右两侧的$符号
# 删除一个指定字符
print(str2.strip('$'))  # hello Python
# 删除多个指定字符
str3 = '13214123123hello Python12314123123123'
print(str3.strip('12'))  # 314123123hello Python12314123123123
print(str3.strip('123'))  # 4123123hello Python12314
print(str3.strip('4231'))  # hello Python
# 结论:如果在strip中填写多个字符,等号左右两侧出现的字符如果在传入的字符串中,则删除,否则保留
# 传入多个字符时,和传入的顺序没有任何关系,只要是传入的字符就不能出现在指定字符串左右两侧,直到出现不属于其内容的字符删除结束

# rstrip 删除字符串右侧指定的字符
print(str3.rstrip('1234'))
# lstrip 删除字符串左侧指定的字符
print(str3.lstrip('1234'))
# TypeError: lstrip arg must be None or str
# strip, lstrip, rstrip 只能接收str类型参数或者None
# print(str3.lstrip(1234))
```

## 10、字符串对齐

- rjust：右对齐
- ljust：左对齐
- cneter： 居中对齐

```python
str1 = 'python'

# rjust 右对齐
# 字符在右侧,不足位置用空格补齐
# 如果不指定填充字符,则自动用空格补齐
print(str1.rjust(10))  #     python
# 格式:字符串.rjust(self(不用传值), width(字符宽度), fillchar(填充字符))
# 指定填充字符 为$
print(str1.rjust(10, '$'))  #$$$$python

# ljust 左对齐
# 和rjust使用方式一致,只不过字符在左侧
print(str1.ljust(10))  # python
print(str1.ljust(10, '$'))  # python$$$$

# center 居中对齐
# 格式: center(self(不用传值), width(字符宽度), fillchar(填充字符))
print(str1.center(10))  #   python
print(str1.center(10, '*'))  # **python**
```

## 11、字符串判断

- 所有的字符串判断结果都是布尔型数据
- isalnum：判断是否都为字母或数字
- isalpha：判断是否都为字母
- isdigit：判断是否都为数字
- isspace：判断是否都为空格
- endswith：是否以。。结尾
- startswith：是否以。。开头
- 其余内容自己测试学习

```python
# 判断字符串内的数据是否符合某种规则

str1 = 'hello itcast'
# startswith 判断是否以...开头
# 需求:判断当前字符串是否以he开头
# 结果是布尔值
print(str1.startswith('he'))  # True
print(str1.startswith('al'))  # False
# 指定范围  左闭右开区间
print(str1.startswith('he', 6, 12))  # False
print(str1.startswith('it', 6, 12))  # True

# endswith 判断是否以...结尾
print(str1.endswith('st'))  # True
print(str1.endswith('al'))  # False
# 指定范围的方式与startswith一致,不在赘述

# is 判断
# isalnum 判断是否全部为数字或字母  不能有空格
print(str1.isalnum())  # False
# isspace  判断是否全部为空格
str2 = ' '
print(str2.isspace())  # True
# isnumeric  isdecimal isdigit  都是判断是否为数字的
str3 = '1234'
print(str3.isnumeric())  # True
print(str3.isdecimal())  # True
print(str3.isdigit())  # True

# 判断中文数字
str4 = '123四肆④亖零〇'
print(str4.isnumeric())  # True  这个方法可以判断中文数字和罗马数字和阿拉伯数字
print(str4.isdecimal())  # False
print(str4.isdigit())  # False

# isidentifier判断是否为标识符
str5 = '2abc'
str6 = 'apple'
print(str5.isidentifier())  # False
print(str6.isidentifier())  # True

# isalpha 判断是否全部为字母
print(str6.isalpha())  # True
print(str5.isalpha())  # False
str7 = 'abc中国'
# 默认将中文当做字母来看
print(str7.isalpha())  # True
# 如果强制判断字母和汉字区分开(了解即可)
print(str7.encode('utf-8').isalpha())  # False
print(str6.encode('utf-8').isalpha())  # True
```

