"""
    用户界面
"""
import copy
import os

from game2048.lwgame.bll import GameController
from game2048.lwgame.model import MoveDirection


class GameConsoleView:
    """
        负责处理界面逻辑
    """

    def __init__(self,array):
        self.__controller = GameController(array)

    def start(self,array):
        array.clear()
        array.append([0, 0, 0, 0])
        array.append([0, 0, 0, 0])
        array.append([0, 0, 0, 0])
        array.append([0, 0, 0, 0])
        self.__controller.generate_new_number(array)
        self.__controller.generate_new_number(array)
        # self.__print_map()
        return array

    def __print_map(self):
        # 在终端中可以 清空界面
        # os.system("clear")

        # for line in self.__controller.map:
        #     for item in line:
        #         print(item, end=" ")
        #     print()
        # return self.__controller.map
        pass
    def update(self,str_input,array):
            self.__move_map(str_input,array)
            # 如果地图没有变化,则跳过
            if not self.__controller.is_change:
                return '没有变化'
            self.__controller.generate_new_number(array)
            if self.__controller.is_game_over(array):
                print("游戏结束喽")
                over = copy.deepcopy(array)
                over.append('over')
                return over
            return array

    def __move_map(self, str_input,array):
        if str_input == "w":
            self.__controller.move(array,MoveDirection.UP)
        elif str_input == "s":
            self.__controller.move(array,MoveDirection.DOWN)
        elif str_input == "a":
            self.__controller.move(array,MoveDirection.LEFT)
        elif str_input == "d":
            self.__controller.move(array,MoveDirection.RIGHT)

