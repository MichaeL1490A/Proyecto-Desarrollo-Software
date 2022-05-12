import pygame
from product.constants import SIZE
#CLASE FICHA
class Ficha():
    def __init__(self,fil,col,color):
        self.fil = fil
        self.col = col
        self.color = color 
        self.x = 0
        self.y = 0
        self.calcular_posicion()
    #Calcula la posicion en la pantalla
    def calcular_posicion(self):
        self.x = SIZE * self.col + SIZE//2
        self.y = SIZE * self.fil + SIZE//2
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),20)
    def move(self,fil,col):
        self.fil = fil
        self.col = col 
        self.calcular_posicion()
    def __repr__(self):
        return str(self.color)