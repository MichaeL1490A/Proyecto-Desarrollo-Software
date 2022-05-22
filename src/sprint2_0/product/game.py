from os import remove
import pygame
import sys
from table import Table
from constants import BROWN, BLACK, GREY, screen, SIZE, valid_boxes, COLOR_TABLE
from ficha import Ficha
import time
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
        self.modo = "Colocar"  # Prueba
        self.memory = 0

    # Historia de usuario 5

    def update(self):
        self.table.draw_screen(screen)
        # self.ficha.draw(screen) #PRUEBA
        pygame.display.update()

    def change_turn(self):
        if self.turn == GREY:
            self.turn = BROWN
            self.player = "2"
        else:
            self.turn = GREY
            self.player = "1"

    # AC 1.3

    def pieces_left_add(self, num):
        self.contador = self.contador + num

    def pieces_left(self):
        if self.contador < 18:
            return True
        else:
            return False
    # Historia de usuario 1

    def set_piece(self, fil, col):
        if self.table.valid_place(fil, col) == True and self.table.check_empty(fil, col):
            self.table.create_piece(fil, col, self.turn)
            self.pieces_left_add(1)
            if self.contador < 18:
                self.modo = "Colocar"
            else:
                self.modo = "Cojer"
    # Historia de usuario 7

    def remove_piece(self, fil, col):
        if self.table.valid_place(fil, col) == True:
            self.table.delete_piece(fil, col)
            self.change_turn()
            if self.contador < 18:
                self.modo = "Colocar"
            else:
                self.modo = "Cojer"

    # Historia de usuario 2
    def move_piece(self, fil, col, memory):
        if self.table.valid_place(fil, col) == True:
            self.table.delete_piece(memory[0], memory[1])
            self.table.create_piece(fil, col, self.turn)
            #self.table.board[memory[0]][memory[1]].move(fil, col)
            self.change_turn()

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
            # SET PIECES
            if event.type == pygame.MOUSEBUTTONDOWN and self.modo == "Colocar":
                mouse = pygame.mouse.get_pos()
                fil, col = get_row_col_from_mouse(mouse)
                if fil >= 0 and col >= 0 and self.table.check_empty(fil, col) and self.table.valid_place(fil, col) and self.pieces_left():
                    self.set_piece(fil, col)
                    if self.table.check_mill(fil, col):
                        self.modo = "Quitar"
                    else:
                        self.change_turn()
            # REMOVE PIECES
            elif event.type == pygame.MOUSEBUTTONDOWN and self.modo == "Quitar":
                mouse = pygame.mouse.get_pos()
                fil, col = get_row_col_from_mouse(mouse)
                print("Quitando")
                if fil >= 0 and col >= 0 and not self.table.board[fil][col].__repr__() == str(self.turn) and not self.table.check_empty(fil, col) and not self.table.check_mill(fil, col) and self.table.valid_place(fil, col):
                    self.remove_piece(fil, col)
            # MOVE PIECES
            elif event.type == pygame.MOUSEBUTTONDOWN and self.modo == "Cojer":
                mouse = pygame.mouse.get_pos()
                fil, col = get_row_col_from_mouse(mouse)
                if fil >= 0 and col >= 0 and self.table.board[fil][col].__repr__() == str(self.turn) and not self.table.check_empty(fil, col) and self.table.valid_place(fil, col):
                    self.memory = (fil, col)
                    self.modo = "Mover"
            elif event.type == pygame.MOUSEBUTTONDOWN and self.modo == "Mover":
                mouse = pygame.mouse.get_pos()
                fil, col = get_row_col_from_mouse(mouse)
                if fil >= 0 and col >= 0 and self.table.check_empty(fil, col) and self.table.valid_place(fil, col):
                    self.move_piece(fil, col, self.memory)
                    if self.table.check_mill(fil, col):
                        self.modo = "Quitar"
                    self.memory = 0
                    self.modo = "Cojer"
        return False
