
if __name__ == '__main__':
    str1 = 'python'

    # rjust 右对齐
    # 字符在右侧,不足位置用空格补齐
    # 如果不指定填充字符,则自动用空格补齐
    print(str1.rjust(10))  # python
    # 格式:字符串.rjust(self(不用传值), width(字符宽度), fillchar(填充字符))
    # 指定填充字符 为$
    print(str1.rjust(10, '$'))  # $$$$python

    # ljust 左对齐
    # 和rjust使用方式一致,只不过字符在左侧
    print(str1.ljust(10))  # python
    print(str1.ljust(10, '$'))  # python$$$$

    # center 居中对齐
    # 格式: center(self(不用传值), width(字符宽度), fillchar(填充字符))
    print(str1.center(10))  # python
    print(str1.center(10, '*'))  # **python**

    # 练习: 计算 1-10000中出现7的次数 (例如 77  就计算两次  777 就计算三次.... )
    sum1 = 0
    for i in range(1, 10001):
        sum1 += str(i).count('7')

    print(sum1)

    print(str(list(range(1, 10001))).count('7'))

    sum1 = 0
    for i in range(1, 10001):
        if i % 10 == 7:
            sum1 += 1
        if i % 100 // 10 == 7:
            sum1 += 1
        if i % 1000 // 100 == 7:
            sum1 += 1
        if i // 1000 == 7:
            sum1 += 1
    print(sum1)