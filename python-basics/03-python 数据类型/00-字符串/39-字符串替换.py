if __name__ == "__main__":
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