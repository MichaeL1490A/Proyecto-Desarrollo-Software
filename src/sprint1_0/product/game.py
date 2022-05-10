import pygame, sys
from table import Table
from constants import BROWN,WHITE,screen,SIZE,tablita
from ficha import Ficha

sys.path.append("..\\..\\Proyecto-Desarrollo-Software")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y - SIZE //2)//SIZE
    col = (x - SIZE//2)//SIZE 
    return row,col


#CLASE JUEGO
class Game():
    def __init__(self, screen):
        self._init()
        self.screen = screen
    def _init(self):
        self.table = Table()
        self.ficha = Ficha(1,1,BROWN) #PRUEBA
        self.turn = WHITE
    def update(self):
        self.table.draw_cubes(screen)
        self.ficha.draw(screen) #PRUEBA
        pygame.display.update()
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fil,col = get_row_col_from_mouse(pos)
                if tablita[fil][col] == True:
                    self.ficha.move(fil,col)
        return False