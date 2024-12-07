import numpy as np
import random as rn
from enum import Enum


class Dirs(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Map:
    def __init__(self):
        self.game_map = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
                            [0, 0, 1, 1, 0, 1, 1, 0, 1, 0],
                            [0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                            [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
                            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]])


        while True:
            x = rn.randint(0, 9)
            y = rn.randint(0, 9)
            if self.game_map[x, y] != 0:
                self.coord = [x, y]
                self.game_map[x, y] = 2
                break

    def generation(self, monnum, itemnum):
        self.monnum = monnum
        self.itemnum = itemnum
        if self.monnum + self.itemnum <= 49:
            while self.monnum != 0:
                mx = rn.randint(0, 9)
                my = rn.randint(0, 9)
                if self.game_map[mx, my] != (0 and 2):
                    self.game_map[mx, my] = 3
                    self.monnum -= 1
            while self.itemnum != 0:
                mx = rn.randint(0, 9)
                my = rn.randint(0, 9)
                if self.game_map[mx, my] != (0 and 2 and 3):
                    self.game_map[mx, my] = 4
                    self.itemnum -= 1
        else:
            print("Генерация мира по вашим параметрам невозможна, попробуйте снова")

    def show_map(self):
        print(self.game_map)

    def move(self, dirnum):
        try:
            direc = Dirs(dirnum)
        except ValueError:
            print("Не сущесвует такого направления, выберите снова")
            return
        x, y = self.coord
        if direc == Dirs.UP:
            new_x, new_y = x - 1, y
        elif direc == Dirs.DOWN:
            new_x, new_y = x + 1, y
        elif direc == Dirs.LEFT:
            new_x, new_y = x, y - 1
        elif direc == Dirs.RIGHT:
            new_x, new_y = x, y + 1
        else:
            print("Некорректное направление")
            return

        if 0 <= new_x < 10 and 0 <= new_y < 10 and self.game_map[new_x, new_y] != 0:
            self.game_map[x, y] = 1
            self.coord = [new_x, new_y]
            old_num = self.game_map[new_x, new_y]
            self.game_map[new_x, new_y] = 2
            print(old_num)
            return old_num
        else:
            return 0
