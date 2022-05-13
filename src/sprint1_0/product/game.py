from turtle import circle
import pygame
import sys
from table import Table
from constants import BROWN, BLACK, GREY, screen, SIZE, valid_boxes, COLOR_TABLE
from ficha import Ficha

sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software")


def get_row_col_from_mouse(pos):
    x, y = pos
    circle_diameter = 20
    row = (y - SIZE//2 + circle_diameter) // SIZE
    col = (x - SIZE//2 + circle_diameter) // SIZE
    return row, col

# CLASE JUEGO


class Game():
    def __init__(self, screen):
        self._init()
        self.screen = screen

    def _init(self):
        self.table = Table()
        self.contador = 0
        # self.ficha = Ficha(1,1,BROWN) #PRUEBA
        self.turn = GREY
        self.player = "1"

    def update(self):
        self.table.draw_screen(screen)
        # self.ficha.draw(screen) #PRUEBA
        pygame.display.update()

    def cambiar_turno(self):
        if self.turn == GREY:
            self.turn = BROWN
            self.player = "2"
        else:
            self.turn = GREY
            self.player = "1"

    def colocar_ficha(self, fil, col):
        if valid_boxes[fil][col] == True and self.table.check_empty(fil, col) and self.contador < 18:
            ficha = Ficha(fil, col, self.turn)
            self.table.board[fil][col] = ficha
            self.cambiar_turno()
            self.contador = self.contador + 1  # Numero de fichas
            self.table.check_mill()

    def turn_text(self):
        # Muestra en texto al jugador que le toca
        font = pygame.font.SysFont("serif", 20)
        text = font.render("JUGADOR "+self.player, True, BLACK)
        center_x = SIZE*3 + SIZE//2 - text.get_width()//2
        center_y = 20 - text.get_height()//2
        screen.blit(text, [center_x, center_y])

    def process_events(self, screen):
        screen.fill(COLOR_TABLE)
        self.turn_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            '''
            MOVER UNA FICHA
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fil,col = get_row_col_from_mouse(pos)
                if valid_boxes[fil][col] == True:
                    self.ficha.move(fil,col)
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                fil, col = get_row_col_from_mouse(mouse)
                if fil >= 0 and col >= 0:
                    self.colocar_ficha(fil, col)
                '''if fil >= 0 and col >= 0:
                    if valid_boxes[fil][col] == True and self.table.board[fil][col] == 0 and self.contador < 18:
                        ficha = Ficha(fil, col, self.turn)
                        self.table.board[fil][col] = ficha
                        self.cambiar_turno()
                        self.contador = self.contador +1 #Numero de fichas
                        self.table.verificar_molino()'''
                # Implementacion de movimiento
                # if valid_boxes[fil][col] == True and self.table.board[fil][col] != 0  and self.contador >= 18 and self.:

        return False
