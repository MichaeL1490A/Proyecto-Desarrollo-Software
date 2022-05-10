import pygame, sys
from table import Table
from constants import BROWN,WHITE,screen
from ficha import Ficha

sys.path.append("..\\..\\Proyecto-Desarrollo-Software")
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
        return False