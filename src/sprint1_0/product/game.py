import pygame, sys
from table import Table
from constants import BROWN,WHITE,GREY,screen,SIZE,tablita
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
        self.contador = 0
        #self.ficha = Ficha(1,1,BROWN) #PRUEBA
        self.turn = GREY
    def update(self):
        self.table.dibujar(screen)
        #self.ficha.draw(screen) #PRUEBA
        pygame.display.update()
    def cambiar_turno(self):
        if self.turn == GREY:
            self.turn = BROWN
        else:
            self.turn = GREY
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            '''
            MOVER UNA FICHA
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fil,col = get_row_col_from_mouse(pos)
                if tablita[fil][col] == True:
                    self.ficha.move(fil,col)
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fil,col = get_row_col_from_mouse(pos)
                if fil >= 0 and col >= 0:
                    if tablita[fil][col] == True and self.table.board[fil][col] == 0 and self.contador < 18:
                        ficha = Ficha(fil,col,self.turn)
                        self.table.board[fil][col]=ficha
                        self.cambiar_turno()
                        self.contador = self.contador +1 #Numero de fichas
                        self.table.verificar_molino()
        return False
    
