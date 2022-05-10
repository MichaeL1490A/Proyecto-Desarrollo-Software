import pygame
from constants import tablita,WHITE,SIZE,GREY,BROWN
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
    def verificar_molino(self):
        #Horizontal
        if (self.board[0][0].__repr__() == str(GREY) and self.board[0][3].__repr__() == str(GREY) and self.board[0][6].__repr__() == str(GREY)) or (self.board[0][0].__repr__() == str(BROWN) and self.board[0][3].__repr__() == str(BROWN) and self.board[0][6].__repr__() == str(BROWN)):
            print("Molino")
        if (self.board[1][1].__repr__() == str(GREY) and self.board[1][3].__repr__() == str(GREY) and self.board[1][5].__repr__() == str(GREY)) or (self.board[1][1].__repr__() == str(BROWN) and self.board[1][3].__repr__() == str(BROWN) and self.board[1][5].__repr__() == str(BROWN)):
            print("Molino")
        if (self.board[2][2].__repr__() == str(GREY) and self.board[2][3].__repr__() == str(GREY) and self.board[2][4].__repr__() == str(GREY)) or (self.board[2][2].__repr__() == str(BROWN) and self.board[2][3].__repr__() == str(BROWN) and self.board[2][4].__repr__() == str(BROWN)):
            print("Molino")
        if ((self.board[3][0].__repr__() == str(GREY) and self.board[3][1].__repr__() == str(GREY) and self.board[3][2].__repr__() == str(GREY)) or (self.board[3][4].__repr__() == str(GREY) and self.board[3][5].__repr__() == str(GREY) and self.board[3][6].__repr__() == str(GREY))) or ((self.board[3][0].__repr__() == str(BROWN) and self.board[3][1].__repr__() == str(BROWN) and self.board[3][2].__repr__() == str(BROWN)) or (self.board[3][4].__repr__() == str(BROWN) and self.board[3][5].__repr__() == str(BROWN) and self.board[3][6].__repr__() == str(BROWN))):
            print("Molino")
        if (self.board[4][2].__repr__() == str(GREY) and self.board[4][3].__repr__() == str(GREY) and self.board[4][4].__repr__() == str(GREY)) or (self.board[4][2].__repr__() == str(BROWN) and self.board[4][3].__repr__() == str(BROWN) and self.board[4][4].__repr__() == str(BROWN)):
            print("Molino")
        if (self.board[5][1].__repr__() == str(GREY) and self.board[5][3].__repr__() == str(GREY) and self.board[5][5].__repr__() == str(GREY)) or (self.board[5][1].__repr__() == str(BROWN) and self.board[5][3].__repr__() == str(BROWN) and self.board[5][5].__repr__() == str(BROWN)):
            print("Molino")
        if (self.board[6][0].__repr__() == str(GREY) and self.board[6][3].__repr__() == str(GREY) and self.board[6][6].__repr__() == str(GREY)) or (self.board[6][0].__repr__() == str(BROWN) and self.board[6][3].__repr__() == str(BROWN) and self.board[6][6].__repr__() == str(BROWN)):
            print("Molino")
        #Vertical
        if (self.board[0][0].__repr__() == str(GREY) and self.board[3][0].__repr__() == str(GREY) and self.board[6][0].__repr__() == str(GREY)) or (self.board[0][0].__repr__() == str(BROWN) and self.board[3][0].__repr__() == str(BROWN) and self.board[6][0].__repr__() == str(BROWN)):
            print("Molino")
        if (self.board[1][1].__repr__() == str(GREY) and self.board[3][1].__repr__() == str(GREY) and self.board[5][1].__repr__() == str(GREY)) or (self.board[1][1].__repr__() == str(BROWN) and self.board[3][1].__repr__() == str(BROWN) and self.board[5][1].__repr__() == str(BROWN)):
            print("Molino")
        if (self.board[2][2].__repr__() == str(GREY) and self.board[3][2].__repr__() == str(GREY) and self.board[4][2].__repr__() == str(GREY)) or (self.board[2][2].__repr__() == str(BROWN) and self.board[3][2].__repr__() == str(BROWN) and self.board[4][2].__repr__() == str(BROWN)):
            print("Molino")
        if ((self.board[0][3].__repr__() == str(GREY) and self.board[1][3].__repr__() == str(GREY) and self.board[2][3].__repr__() == str(GREY)) or (self.board[4][3].__repr__() == str(GREY) and self.board[5][3].__repr__() == str(GREY) and self.board[6][3].__repr__() == str(GREY))) or ((self.board[0][3].__repr__() == str(BROWN) and self.board[1][3].__repr__() == str(BROWN) and self.board[2][3].__repr__() == str(BROWN)) or (self.board[4][3].__repr__() == str(BROWN) and self.board[5][3].__repr__() == str(BROWN) and self.board[6][3].__repr__() == str(BROWN))):
            print("Molino")
        if (self.board[2][4].__repr__() == str(GREY) and self.board[3][4].__repr__() == str(GREY) and self.board[4][4].__repr__() == str(GREY)) or (self.board[2][4].__repr__() == str(BROWN) and self.board[3][4].__repr__() == str(BROWN) and self.board[4][4].__repr__() == str(BROWN)):
            print("Molino")
        if (self.board[1][5].__repr__() == str(GREY) and self.board[3][5].__repr__() == str(GREY) and self.board[5][5].__repr__() == str(GREY)) or (self.board[1][5].__repr__() == str(BROWN) and self.board[3][5].__repr__() == str(BROWN) and self.board[5][5].__repr__() == str(BROWN)):
            print("Molino")
        if (self.board[0][6].__repr__() == str(GREY) and self.board[3][6].__repr__() == str(GREY) and self.board[6][6].__repr__() == str(GREY)) or (self.board[0][6].__repr__() == str(BROWN) and self.board[3][6].__repr__() == str(BROWN) and self.board[6][6].__repr__() == str(BROWN)):
            print("Molino")