if __name__ == "__main__":
    # f-string是Python3.6以后推出的格式化方式
    name = 'xiaoming'
    age = 18
    height = 1.85
    weight = 69.5
    score = 98
    id = 12345678

    # 格式化拼接上述变量
    # 传统拼接方式
    print('学员的姓名是%s, 学员的年龄是%d, 学员的身高是%f, 学员的体重是%f, 学员的分数是%d%%, 学员的学号是%d' % (
    name, age, height, weight, score, id))
    # 使用f-string进行字符串拼接
    # 格式:f'要输出的内容{变量}'
    print(
        F'学员的姓名是{name}, 学员的年龄是{age}, 学员的身高是{height}, 学员的体重是{weight}, 学员的分数是{score}%%, 学员的学号是{id}')

    # 修改格式:
    print('学员的姓名是%s, 学员的年龄是%d, 学员的身高是%.2f, 学员的体重是%.3f, 学员的分数是%d%%, 学员的学号是%06d' % (
    name, age, height, weight, score, id))
    # 如果需要调整精度
    # {整数型变量:06d} 整型占六位,不足位用0补齐 d可以省略
    # {浮点型变量:.2f} 浮点型保留两位小数, 四舍五入
    # %可以单独输出
    print(
        F'学员的姓名是{name}, 学员的年龄是{age}, 学员的身高是{height:.2f}, 学员的体重是{weight:.3f}, 学员的分数是{score}%, 学员的学号是{id:06d}')
    print(
        F'学员的姓名是{name}, 学员的年龄是{age}, 学员的身高是{height:.2f}, 学员的体重是{weight:.3f}, 学员的分数是{score}%, 学员的学号是{id:06}')

    # 练习:
    # 输出自己的信息包括,姓名,年龄,身高(保留两位小数),学号(保留6位,不足位用0补齐),使用f-string进行拼接