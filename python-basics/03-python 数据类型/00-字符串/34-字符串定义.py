if __name__ == "__main__":
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