import pygame, sys
from table import Table
from constants import *
from ficha import Ficha
sys.path.append("..\\..\\Proyecto-Desarrollo-Software")
#CLASE JUEGO
class Game():
    def __init__(self, screen):
        self.screen = screen
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
    def display_frame(self, screen):
        screen.fill(WHITE)
        pygame.display.flip()