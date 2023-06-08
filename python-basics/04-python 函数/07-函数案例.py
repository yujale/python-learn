if __name__ == "__main__":
    def sum_three(num1, num2, num3):
        """求三个数的和"""
        return num1 + num2 + num3


    def average(num1, num2, num3):
        """求三个数的平均值"""
        return sum_three(num1, num2, num3) / 3


    print(average(1, 2, 3))