if __name__ == "__main__":
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
    print(str1.find('python'))  # 6

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
    print(str1.count('h', 1, 9))  # 0
    print(str1.count('h', 9, 12))  # 1