"""
    游戏入口
"""
from game2048.lwgame.usl import GameConsoleView

# 目的：必须是主模块才执行游戏逻辑
if __name__ == "__main__":
    view = GameConsoleView()
    view.start()
    view.update()