if __name__ == "__main__":
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