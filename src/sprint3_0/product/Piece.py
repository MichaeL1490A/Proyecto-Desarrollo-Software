from Constant import C
import sys

sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software - Test")


class Piece():
    def __init__(self, fil, col, color):
        self.fil = fil
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = C.SIZE*self.col + C.SIZE//2
        self.y = C.SIZE*self.fil + C.SIZE//2

    def move(self, fil, col):
        self.fil = fil
        self.col = col
        self.calculate_position()

    def __repr__(self):
        return str(self.color)
