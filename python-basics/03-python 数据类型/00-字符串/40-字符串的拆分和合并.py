if __name__ == "__main__":
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
    list2 = [1, 2, 3, 4, 'abc']
    print(list1)
    # 将list1  按照指定分隔符❤  合并为一个字符串
    # 格式:分隔符.join(iterable(可迭代类型))
    print('❤'.join(list1))  # I❤love❤Python❤and❤java❤and❤c❤and❤lixiaolong
    # 进行join合并时,要注意可迭代类型中全部元素都要是字符串类型,否则无法合并
    print('❤'.join(list2))  # TypeError: sequence item 0: expected str instance, int found
