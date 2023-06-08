# 需求: 进行游戏
# 1/显示游戏信息
# 2/展示历史最高分
# 3/开始游戏

class Game(object):
    top_score = 100

    def __init__(self, name):
        self.name = name

    # 定义一个静态方法,与类和实例都没有关系
    @staticmethod
    def print_game_info():
        print('游戏信息展示')

    # 定义类方法,内部可以调用类属性和类方法,依赖于类
    @classmethod
    def show_top_score(cls):
        print(f'历史最高分数为{cls.top_score}')

    # 定义了一个实例方法,内部可以调用实例属性和实例方法,依赖于实例
    def start_game(self):
        print(f'{self.name}开始游戏')


Game.print_game_info()
Game.show_top_score()
# 实例方法必须使用实例进行调用
g1 = Game('xiaoming')
g1.start_game()