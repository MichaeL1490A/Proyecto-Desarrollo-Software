import pygame
from constants import tablita,WHITE,SIZE
class Table():
    def __init__(self):
        self.board = [] # Fichas en juego
        self.brown_left = self.white_left = 9 # Numero de fichas que quedan
    def dibujar_casillas(self,screen):
        for fil in range(7):
            self.board.append([])
            for col in range(7):
                self.board[fil].append(0)
                if tablita[fil][col] == True:
                    pygame.draw.circle(screen,WHITE,(fil*SIZE+SIZE//2,col*SIZE+SIZE//2),30)
    def dibujar(self,screen):
        self.dibujar_casillas(screen)
        for fil in range(7):
            for col in range(7):
                ficha = self.board[fil][col]
                if ficha != 0:
                    ficha.draw(screen)
