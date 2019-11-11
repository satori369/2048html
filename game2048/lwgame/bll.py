"""
    负责处理游戏核心逻辑模块

    步骤：
        1. 创建项目game2048,创建模块game_controller
        2. 将之前完成的面向过程的核心算法，移动到GameController类中．
            数据作为实例变量，操作作为实例方法.
        3. 在GameController类中，定义产生一个新数字的方法
            在随机的空白位置(零元素)上
            产生随机的数字(2的概率90%  4的概率10%)　

        4. 在GameController类中，定义判断游戏是否结束的方法
            如果有空位置不能结束
            如果水平方向，相邻具有相同元素，不能结束
            如果垂直方向，相邻具有相同元素，不能结束
            以上都不满足，游戏结束.

        5. 完成GameConsoleView
        6. 重构update方法
        7. 如果地图没有变化，则不生成新数字/更新界面
"""
import copy
import random

from game2048.lwgame.model import Location, MoveDirection


class GameController:
    """
        负责处理游戏核心逻辑
    """

    def __init__(self,array):
        self.__list_merge = [2, 16, 0, 4]
        # array = [
        #     [2, 8, 0, 2],
        #     [2, 2, 0, 4],
        #     [0, 4, 0, 4],
        #     [2, 2, 2, 0],
        # ]
        # array = [
        #     [2, 8, 16, 2],
        #     [128, 64, 2, 32],
        #     [4, 2048, 128, 4],
        #     [2, 1024, 2, 1024],
        # ]
        # array = array
        self.__list_empty_location = []
        self.__is_change = False

    @property
    def is_change(self):
        return self.__is_change

    # 只读属性
    # @property
    # def map(self):
    #     return array  # 缺点：类外仍然可以修改列表对象　
        # 缺点：每次读取数据，都会复制一份数据,内存占用过大．
        # return array[:]
        # return copy.deepcopy(array)

    # def get_map(self):
    #     return array
    # 对象.get_map()
    # 对象.map
    def __zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] *= 2
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __move_left(self,array):
        """
            向左移动
        """
        for line in array:
            self.__list_merge = line
            self.__merge()

    def __move_right(self,array):
        """
            向右移动
        """
        for line in array:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __move_up(self,array):
        """
            向上移动
        """
        self.__square_matrix_transpose(array)
        self.__move_left(array)
        self.__square_matrix_transpose(array)

    def __move_down(self,array):
        """
            向下移动
        """
        self.__square_matrix_transpose(array)
        self.__move_right(array)
        self.__square_matrix_transpose(array)

    def move(self,array, dir=MoveDirection.UP):
        # 移动前记录地图
        original_map = copy.deepcopy(array)

        if dir == MoveDirection.UP:
            self.__move_up(array)
        elif dir == MoveDirection.DOWN:
            self.__move_down(array)
        elif dir == MoveDirection.LEFT:
            self.__move_left(array)
        elif dir == MoveDirection.RIGHT:
            self.__move_right(array)

        # 移动后进行比较
        self.__is_change = array != original_map
        # true 表示有变化(不相等)  false 表示没变化(相等)

    def __square_matrix_transpose(self,array):
        for c in range(1, len(array)):
            for r in range(c, len(array)):
                array[r][c - 1], array[c - 1][r] = array[c - 1][r], array[r][c - 1]

    def generate_new_number(self,array):
        """
            生成新数字　
        """
        self.__calculate_empty_location(array)
        if len(self.__list_empty_location) == 0: return
        loc = random.choice(self.__list_empty_location)
        # array[location[0]][location[1]] = 4 if random.randint(0,10) ==1 else 2
        array[loc.r][loc.c] = self.__create_random_number()
        # self.__list_empty_location.remove(loc)

    def __create_random_number(self):
        return 4 if random.randint(0, 10) == 1 else 2

    def __calculate_empty_location(self,array):
        self.__list_empty_location.clear()
        for r in range(len(array)):
            for c in range(len(array[r])):
                if array[r][c] == 0:
                    # 记录r c
                    # self.__list_empty_location.append((r, c))
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self,array):
        """
            判断游戏是否结束
        :return: True 游戏结束　　False　游戏不结束
        """
        self.__calculate_empty_location(array)
        if len(self.__list_empty_location): return False

        # 水平方向判断　的同时　垂直方向判断
        for r in range(4):
            for c in range(3):
                if array[r][c] == array[r][c + 1] or array[c][r] == array[c + 1][r]:
                    return False
                elif array[r][c] == 0:
                    return False


        return True  # 以上条件都不满足，则游戏结束

        """
        # 水平方向
        for r in range(4):
            for c in range(3):
                if array[r][c] == array[r][c + 1]:
                    return False
        # 垂直方向
        for c in range(4):
            for r in range(3):
                if array[r][c] == array[r + 1][c]:
                    return False
        """


# 目的：不是主模块才执行测试代码
if __name__ == "__main__":
    controller = GameController()
    controller.__move_right()
    controller.__move_down()

    # controller.map = 100 #只读属性不能修改
    controller.map[0][0] = 100  # 通过属性返回对象地址，可以修改对象.

    print(controller.map)
    controller.generate_new_number()
    print(controller.map)

    print(controller.is_game_over())
