import pygame, sys
from table import Table
from constants import *
from ficha import Ficha
sys.path.append("..\\..\\Proyecto-Desarrollo-Software")
#CLASE JUEGO
class Game():
    def __init__(self, screen):
        self._init()
        self.screen = screen
    def _init(self):
        self.table = Table()
        self.turn = WHITE
    def update(self):
        self.table.draw_cubes(screen)
        pygame.display.update()
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False