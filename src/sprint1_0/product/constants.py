import pygame
#Dimensiones del programa
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 1020
FIL,COL=7,7
SIZE = SCREEN_WIDTH//COL
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
#Colores
WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (115,0,0)
tablita =[
            [True,False,False,True,False,False,True],
            [False,True,False,True,False,True,False],
            [False,False,True,True,True,False,False],
            [True,True,True,False,True,True,True],
            [False,False,True,True,True,False,False],
            [False,True,False,True,False,True,False],
            [True,False,False,True,False,False,True],
        ]