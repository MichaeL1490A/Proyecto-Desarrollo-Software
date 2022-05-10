import pygame
from constants import *
#CLASE FICHA
class Ficha():
    def __init__(self,fil,col,color):
        self.fil = fil
        self.col = col
        self.color = color 
        self.x = 0
        self.y = 0