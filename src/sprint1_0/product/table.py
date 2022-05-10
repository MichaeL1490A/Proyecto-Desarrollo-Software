import pygame
from constants import tablita,WHITE,SIZE
class Table():
    def __init__(self):
        self.board = [] # Fichas en juego
        self.brown_left = self.white_left = 9 # Numero de fichas que quedan
    def draw_cubes(self,screen):
        for row in range(7):
            for col in range(7):
                if tablita[row][col] == True:
                    pygame.draw.circle(screen,WHITE,(row*SIZE+SIZE//2,col*SIZE+SIZE//2),30)
