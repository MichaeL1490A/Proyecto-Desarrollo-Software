import pygame
import sys
from constants import SIZE
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software")


class Piece():
    def __init__(self, fil, col, color):
        self.fil = fil
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = SIZE*self.col + SIZE//2
        self.y = SIZE*self.fil + SIZE//2

    def move(self, fil, col):
        self.fil = fil
        self.col = col
        self.calculate_position()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 20)

    def __repr__(self):
        return str(self.color)
