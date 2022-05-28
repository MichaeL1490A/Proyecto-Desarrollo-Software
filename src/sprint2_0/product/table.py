from asyncio.windows_events import NULL
import pygame
from ficha import Piece
from constants import valid_boxes, BLACK, SIZE, GREY, WHITE, RED, next_to_piece


class Table():
    def __init__(self):
        self.board = []  # Fichas en juego
        self.remove = False  # Pinta las fichas que se pueden remover, si es True
        self.paint = NULL  # le damos el valor de lista de las fichas que se pueden remover
    # Dibuja las posiciones válidas en el tablero

    def draw_box(self, screen):
        for fil in range(7):
            self.board.append([])
            for col in range(7):
                self.board[fil].append(0)
                if valid_boxes[fil][col] == True:
                    pygame.draw.circle(
                        screen, BLACK, (fil*SIZE + SIZE//2, col*SIZE + SIZE//2), 15)

    # Dibuja las líneas de apoyo en el tablero
    def draw_lines(self, screen):
        width_line = 4
        for column in range(3):
            pygame.draw.rect(screen, BLACK, (column*SIZE + SIZE
                                             // 2, column*SIZE + SIZE//2, width_line, SIZE*7 - 2*(column*SIZE + SIZE//2)))
            pygame.draw.rect(screen, BLACK, (7*SIZE - (1+column)*SIZE+SIZE//2, column
                                             * SIZE + SIZE//2, width_line, SIZE*7 - 2*(column*SIZE + SIZE//2)))
        for row in range(3):
            pygame.draw.rect(screen, BLACK, (row*SIZE + SIZE
                                             // 2, row*SIZE + SIZE//2, SIZE*7 - 2*(row*SIZE + SIZE//2), width_line))
            pygame.draw.rect(screen, BLACK, (row*SIZE + SIZE//2, 7*SIZE - (row
                                             * SIZE + SIZE//2), SIZE*7 - 2*(row*SIZE + SIZE//2), width_line))

        pygame.draw.rect(screen, BLACK, (SIZE//2, SIZE
                                         * 3 + SIZE//2, SIZE*2, width_line))
        pygame.draw.rect(screen, BLACK, (SIZE//2+SIZE
                                         * 4, SIZE*3 + SIZE//2, SIZE*2, width_line))
        pygame.draw.rect(screen, BLACK, (SIZE*3 + SIZE
                                         // 2, SIZE//2, width_line, SIZE*2))
        pygame.draw.rect(screen, BLACK, (SIZE*3 + SIZE
                                         // 2, 5*SIZE-SIZE//2, width_line, SIZE*2))

    # Pinta la pantalla
    # AC 5.1
    def draw_screen(self, screen):
        self.draw_lines(screen)
        self.draw_box(screen)
        for fil in range(7):
            for col in range(7):
                piece = self.board[fil][col]
                if piece != 0:
                    piece.draw(screen)

    def check_nexto(self, fil, col, newfil, newcol):
        for place in next_to_piece[(fil, col)]:
            if newfil == place[0] and newcol == place[1]:
                return True
        return False

    # This method checks for each places of the board if a mill has been built

    def check_mill(self, fil, col):
        colors = (GREY, WHITE)
        for color in colors:
            # Cuadrado Grande
            if fil == 0 and col == 0:
                if self.board[0][0].__repr__() == str(color) and self.board[0][3].__repr__() == str(color) and self.board[0][6].__repr__() == str(color):
                    return True
                if self.board[0][0].__repr__() == str(color) and self.board[3][0].__repr__() == str(color) and self.board[6][0].__repr__() == str(color):
                    return True
            if fil == 0 and col == 3:
                if self.board[0][3].__repr__() == str(color) and self.board[0][0].__repr__() == str(color) and self.board[0][6].__repr__() == str(color):
                    return True
                if self.board[0][3].__repr__() == str(color) and self.board[1][3].__repr__() == str(color) and self.board[2][3].__repr__() == str(color):
                    return True
            if fil == 0 and col == 6:
                if self.board[0][6].__repr__() == str(color) and self.board[0][3].__repr__() == str(color) and self.board[0][0].__repr__() == str(color):
                    return True
                if self.board[0][6].__repr__() == str(color) and self.board[3][6].__repr__() == str(color) and self.board[6][6].__repr__() == str(color):
                    return True
            if fil == 3 and col == 6:
                if self.board[3][6].__repr__() == str(color) and self.board[0][6].__repr__() == str(color) and self.board[6][6].__repr__() == str(color):
                    return True
                if self.board[3][6].__repr__() == str(color) and self.board[3][5].__repr__() == str(color) and self.board[3][4].__repr__() == str(color):
                    return True
            if fil == 6 and col == 6:
                if self.board[6][6].__repr__() == str(color) and self.board[3][6].__repr__() == str(color) and self.board[0][6].__repr__() == str(color):
                    return True
                if self.board[6][6].__repr__() == str(color) and self.board[6][3].__repr__() == str(color) and self.board[6][0].__repr__() == str(color):
                    return True
            if fil == 6 and col == 3:
                if self.board[6][3].__repr__() == str(color) and self.board[6][6].__repr__() == str(color) and self.board[6][0].__repr__() == str(color):
                    return True
                if self.board[6][3].__repr__() == str(color) and self.board[5][3].__repr__() == str(color) and self.board[4][3].__repr__() == str(color):
                    return True
            if fil == 6 and col == 0:
                if self.board[6][0].__repr__() == str(color) and self.board[3][0].__repr__() == str(color) and self.board[0][0].__repr__() == str(color):
                    return True
                if self.board[6][0].__repr__() == str(color) and self.board[6][3].__repr__() == str(color) and self.board[6][6].__repr__() == str(color):
                    return True
            if fil == 3 and col == 0:
                if self.board[3][0].__repr__() == str(color) and self.board[6][0].__repr__() == str(color) and self.board[0][0].__repr__() == str(color):
                    return True
                if self.board[3][0].__repr__() == str(color) and self.board[3][1].__repr__() == str(color) and self.board[3][2].__repr__() == str(color):
                    return True
            # Cuadrado Mediano
            if fil == 1 and col == 1:
                if self.board[1][1].__repr__() == str(color) and self.board[1][3].__repr__() == str(color) and self.board[1][5].__repr__() == str(color):
                    return True
                if self.board[1][1].__repr__() == str(color) and self.board[3][1].__repr__() == str(color) and self.board[5][1].__repr__() == str(color):
                    return True
            if fil == 1 and col == 3:
                if self.board[1][3].__repr__() == str(color) and self.board[1][1].__repr__() == str(color) and self.board[1][5].__repr__() == str(color):
                    return True
                if self.board[1][3].__repr__() == str(color) and self.board[0][3].__repr__() == str(color) and self.board[2][3].__repr__() == str(color):
                    return True
            if fil == 1 and col == 5:
                if self.board[1][5].__repr__() == str(color) and self.board[1][3].__repr__() == str(color) and self.board[1][1].__repr__() == str(color):
                    return True
                if self.board[1][5].__repr__() == str(color) and self.board[3][5].__repr__() == str(color) and self.board[5][5].__repr__() == str(color):
                    return True
            if fil == 3 and col == 5:
                if self.board[3][5].__repr__() == str(color) and self.board[1][5].__repr__() == str(color) and self.board[5][5].__repr__() == str(color):
                    return True
                if self.board[3][5].__repr__() == str(color) and self.board[3][4].__repr__() == str(color) and self.board[3][6].__repr__() == str(color):
                    return True
            if fil == 5 and col == 5:
                if self.board[5][5].__repr__() == str(color) and self.board[3][5].__repr__() == str(color) and self.board[1][5].__repr__() == str(color):
                    return True
                if self.board[5][5].__repr__() == str(color) and self.board[5][3].__repr__() == str(color) and self.board[5][1].__repr__() == str(color):
                    return True
            if fil == 5 and col == 3:
                if self.board[5][3].__repr__() == str(color) and self.board[5][5].__repr__() == str(color) and self.board[5][1].__repr__() == str(color):
                    return True
                if self.board[5][3].__repr__() == str(color) and self.board[6][3].__repr__() == str(color) and self.board[4][3].__repr__() == str(color):
                    return True
            if fil == 5 and col == 1:
                if self.board[5][1].__repr__() == str(color) and self.board[3][1].__repr__() == str(color) and self.board[1][1].__repr__() == str(color):
                    return True
                if self.board[5][1].__repr__() == str(color) and self.board[5][3].__repr__() == str(color) and self.board[5][5].__repr__() == str(color):
                    return True
            if fil == 3 and col == 1:
                if self.board[3][1].__repr__() == str(color) and self.board[5][1].__repr__() == str(color) and self.board[1][1].__repr__() == str(color):
                    return True
                if self.board[3][1].__repr__() == str(color) and self.board[3][0].__repr__() == str(color) and self.board[3][2].__repr__() == str(color):
                    return True
            # CUADRADO PEQUEÑO
            if fil == 2 and col == 2:
                if self.board[2][2].__repr__() == str(color) and self.board[2][3].__repr__() == str(color) and self.board[2][4].__repr__() == str(color):
                    return True
                if self.board[2][2].__repr__() == str(color) and self.board[3][2].__repr__() == str(color) and self.board[4][2].__repr__() == str(color):
                    return True
            if fil == 2 and col == 3:
                if self.board[2][3].__repr__() == str(color) and self.board[2][2].__repr__() == str(color) and self.board[2][4].__repr__() == str(color):
                    return True
                if self.board[2][3].__repr__() == str(color) and self.board[0][3].__repr__() == str(color) and self.board[1][3].__repr__() == str(color):
                    return True
            if fil == 2 and col == 4:
                if self.board[2][4].__repr__() == str(color) and self.board[2][3].__repr__() == str(color) and self.board[2][2].__repr__() == str(color):
                    return True
                if self.board[2][4].__repr__() == str(color) and self.board[3][4].__repr__() == str(color) and self.board[4][4].__repr__() == str(color):
                    return True
            if fil == 3 and col == 4:
                if self.board[3][4].__repr__() == str(color) and self.board[2][4].__repr__() == str(color) and self.board[4][4].__repr__() == str(color):
                    return True
                if self.board[3][4].__repr__() == str(color) and self.board[3][5].__repr__() == str(color) and self.board[3][6].__repr__() == str(color):
                    return True
            if fil == 4 and col == 4:
                if self.board[4][4].__repr__() == str(color) and self.board[3][4].__repr__() == str(color) and self.board[2][4].__repr__() == str(color):
                    return True
                if self.board[4][4].__repr__() == str(color) and self.board[4][3].__repr__() == str(color) and self.board[4][2].__repr__() == str(color):
                    return True
            if fil == 4 and col == 3:
                if self.board[4][3].__repr__() == str(color) and self.board[4][4].__repr__() == str(color) and self.board[4][2].__repr__() == str(color):
                    return True
                if self.board[4][3].__repr__() == str(color) and self.board[5][3].__repr__() == str(color) and self.board[6][3].__repr__() == str(color):
                    return True
            if fil == 4 and col == 2:
                if self.board[4][2].__repr__() == str(color) and self.board[3][2].__repr__() == str(color) and self.board[2][2].__repr__() == str(color):
                    return True
                if self.board[4][2].__repr__() == str(color) and self.board[4][3].__repr__() == str(color) and self.board[4][4].__repr__() == str(color):
                    return True
            if fil == 3 and col == 2:
                if self.board[3][2].__repr__() == str(color) and self.board[4][2].__repr__() == str(color) and self.board[2][2].__repr__() == str(color):
                    return True
                if self.board[3][2].__repr__() == str(color) and self.board[3][1].__repr__() == str(color) and self.board[3][0].__repr__() == str(color):
                    return True
    # AC 1.1 1.2

    def check_empty(self, fil, col):
        if self.board[fil][col] == 0:
            return True
        else:
            return False
    # AC 1.4

    def valid_place(self, fil, col):
        return valid_boxes[fil][col]

    def create_piece(self, fil, col, turn):
        piece = Piece(fil, col, turn)
        self.board[fil][col] = piece

    def delete_piece(self, fil, col):
        self.board[fil][col] = 0

    def move_piece(self, fil, col, newfil, newcol):
        self.board[newfil][newcol] = self.board[fil][col]
        self.board[fil][col].move(newfil, newcol)
        self.board[fil][col] = 0
