if __name__ == "__main__":
    # break:跳出循环,终止此次循环之后的所有循环

    # 吃苹果案例   吃到第三个 吃出半条虫子,后续无心再吃
    i = 1
    while i <= 5:
        print(f'我吃了{i}个苹果')
        if i == 3:
            print('吃不下了 虫子个太大吃撑了')
            # break之后的所有代码均不执行
            break
        i += 1

    print('吃苹果完成')

    # 输出1-10 十个数字
    # 在循环体中,break所在的分支中,break之后不要写任何代码,不可能执行
    # i = 1
    # while i <= 10:
    #     print(i)
    #     break
    #     i += 1