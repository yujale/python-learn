if __name__ == "__main__":
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
