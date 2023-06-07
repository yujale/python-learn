if __name__ == "__main__":
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