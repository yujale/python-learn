"""
需求:
1.
创建phone类
Phone
2.
在类中添加方法, 充电
听歌
打电话
玩游戏
3.
每个手机都有初始的电量, 并且在创建对象时可以手动输入电量
4.
充电可以输入充电时长, 充电1小时获得20个单位的电量
5.
听歌(15)
打电话(10)
玩游戏(30)
都会消耗电量
6.
电量最高100
最低
0
充电到100
就就会结束, 使用手机, 如果电量不足以支撑完成操作则警告, 并自动关机
"""

# 分析:
'''
1.
在上述需求中有哪些类?  一个
Phone
2.
在上述类中有哪些属性?  一个
电量
3.
在上述类中有哪些方法?  四个
充电
听歌
打电话
玩游戏
4.
有哪些数值判断: 在使用手机
和充电过程中, 让电量范围保持在0 - 100
之间
'''


# 定义类
class Phone(object):

    def __init__(self, power):
        """初始化对象的方法,在定义对象时,需要输入电量"""
        if power >= 100:
            self.power = 100
        elif power <= 0:
            self.power = 0
        else:
            self.power = power

    def add_power(self, time):
        """充电方法"""
        print(f'充电开始,共充电{time}小时')
        # 对于对象中的电量进行增加
        self.power += 20 * time
        if self.power > 100:
            self.power = 100
            print('充满电了,赶紧收起来吧不然充坏了')
        else:
            # 输出电量
            print(f'充电结束,当前电量为{self.power}')

    def music(self):
        """听音乐"""
        print('音乐真好听呀,再来一首大河向东流')
        self.power -= 15
        if self.power > 0:
            print(f'听歌结束,剩余电量为{self.power}')
        else:
            # 在手机没电时需要将电量赋值为0,防止出现负数电量
            self.power = 0
            print(f'手机没电了赶紧充电吧,别听歌了')

    def call(self):
        """打电话"""
        print('给女朋友打个电话,希望还没睡觉')
        self.power -= 10
        if self.power > 0:
            print(f'电话打完了,成功分手,剩余电量为{self.power}')
        else:
            # 在手机没电时需要将电量赋值为0,防止出现负数电量
            self.power = 0
            print(f'手机没电了赶紧充电吧,别打电话了')

    def play_game(self):
        """玩游戏"""
        print('我最爱玩游戏了,每次都赢没办法,就是这么厉害')
        self.power -= 30
        if self.power > 0:
            print(f'游戏打完了,打游戏太爽了,我打游戏,舍友打我,剩余电量{self.power}')
        else:
            # 在手机没电时需要将电量赋值为0,防止出现负数电量
            self.power = 0
            print('手机没电了,赶紧充电吧,别玩游戏了')


p1 = Phone(20)
p1.music()
p1.call()
p1.play_game()
p1.add_power(4)
p1.add_power(4)
print(p1.power)