import pygame
from constants import tablita, BLACK, SIZE, GREY, BROWN


class Table():
    def __init__(self):
        self.board = []  # Fichas en juego
        self.brown_left = self.white_left = 9  # Numero de fichas que quedan

    # Dibuja las posiciones válidas en el tablero
    def draw_box(self, screen):
        for fil in range(7):
            self.board.append([])
            for col in range(7):
                self.board[fil].append(0)
                if tablita[fil][col] == True:
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
    def draw_screen(self, screen):
        self.draw_lines(screen)
        self.draw_box(screen)
        for fil in range(7):
            for col in range(7):
                ficha = self.board[fil][col]
                if ficha != 0:
                    ficha.draw(screen)

    # Revisa si se a formado un molino
    def check_mill(self):
        # Horizontal
        if (self.board[0][0].__repr__() == str(GREY) and self.board[0][3].__repr__() == str(GREY) and self.board[0][6].__repr__() == str(GREY)) or (self.board[0][0].__repr__() == str(BROWN) and self.board[0][3].__repr__() == str(BROWN) and self.board[0][6].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if (self.board[1][1].__repr__() == str(GREY) and self.board[1][3].__repr__() == str(GREY) and self.board[1][5].__repr__() == str(GREY)) or (self.board[1][1].__repr__() == str(BROWN) and self.board[1][3].__repr__() == str(BROWN) and self.board[1][5].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if (self.board[2][2].__repr__() == str(GREY) and self.board[2][3].__repr__() == str(GREY) and self.board[2][4].__repr__() == str(GREY)) or (self.board[2][2].__repr__() == str(BROWN) and self.board[2][3].__repr__() == str(BROWN) and self.board[2][4].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if ((self.board[3][0].__repr__() == str(GREY) and self.board[3][1].__repr__() == str(GREY) and self.board[3][2].__repr__() == str(GREY)) or (self.board[3][4].__repr__() == str(GREY) and self.board[3][5].__repr__() == str(GREY) and self.board[3][6].__repr__() == str(GREY))) or ((self.board[3][0].__repr__() == str(BROWN) and self.board[3][1].__repr__() == str(BROWN) and self.board[3][2].__repr__() == str(BROWN)) or (self.board[3][4].__repr__() == str(BROWN) and self.board[3][5].__repr__() == str(BROWN) and self.board[3][6].__repr__() == str(BROWN))):
            print("Molino")
            return True
        if (self.board[4][2].__repr__() == str(GREY) and self.board[4][3].__repr__() == str(GREY) and self.board[4][4].__repr__() == str(GREY)) or (self.board[4][2].__repr__() == str(BROWN) and self.board[4][3].__repr__() == str(BROWN) and self.board[4][4].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if (self.board[5][1].__repr__() == str(GREY) and self.board[5][3].__repr__() == str(GREY) and self.board[5][5].__repr__() == str(GREY)) or (self.board[5][1].__repr__() == str(BROWN) and self.board[5][3].__repr__() == str(BROWN) and self.board[5][5].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if (self.board[6][0].__repr__() == str(GREY) and self.board[6][3].__repr__() == str(GREY) and self.board[6][6].__repr__() == str(GREY)) or (self.board[6][0].__repr__() == str(BROWN) and self.board[6][3].__repr__() == str(BROWN) and self.board[6][6].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if (self.board[0][0].__repr__() == str(GREY) and self.board[3][0].__repr__() == str(GREY) and self.board[6][0].__repr__() == str(GREY)) or (self.board[0][0].__repr__() == str(BROWN) and self.board[3][0].__repr__() == str(BROWN) and self.board[6][0].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if (self.board[1][1].__repr__() == str(GREY) and self.board[3][1].__repr__() == str(GREY) and self.board[5][1].__repr__() == str(GREY)) or (self.board[1][1].__repr__() == str(BROWN) and self.board[3][1].__repr__() == str(BROWN) and self.board[5][1].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if (self.board[2][2].__repr__() == str(GREY) and self.board[3][2].__repr__() == str(GREY) and self.board[4][2].__repr__() == str(GREY)) or (self.board[2][2].__repr__() == str(BROWN) and self.board[3][2].__repr__() == str(BROWN) and self.board[4][2].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if ((self.board[0][3].__repr__() == str(GREY) and self.board[1][3].__repr__() == str(GREY) and self.board[2][3].__repr__() == str(GREY)) or (self.board[4][3].__repr__() == str(GREY) and self.board[5][3].__repr__() == str(GREY) and self.board[6][3].__repr__() == str(GREY))) or ((self.board[0][3].__repr__() == str(BROWN) and self.board[1][3].__repr__() == str(BROWN) and self.board[2][3].__repr__() == str(BROWN)) or (self.board[4][3].__repr__() == str(BROWN) and self.board[5][3].__repr__() == str(BROWN) and self.board[6][3].__repr__() == str(BROWN))):
            print("Molino")
            return True
        if (self.board[2][4].__repr__() == str(GREY) and self.board[3][4].__repr__() == str(GREY) and self.board[4][4].__repr__() == str(GREY)) or (self.board[2][4].__repr__() == str(BROWN) and self.board[3][4].__repr__() == str(BROWN) and self.board[4][4].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if (self.board[1][5].__repr__() == str(GREY) and self.board[3][5].__repr__() == str(GREY) and self.board[5][5].__repr__() == str(GREY)) or (self.board[1][5].__repr__() == str(BROWN) and self.board[3][5].__repr__() == str(BROWN) and self.board[5][5].__repr__() == str(BROWN)):
            print("Molino")
            return True
        if (self.board[0][6].__repr__() == str(GREY) and self.board[3][6].__repr__() == str(GREY) and self.board[6][6].__repr__() == str(GREY)) or (self.board[0][6].__repr__() == str(BROWN) and self.board[3][6].__repr__() == str(BROWN) and self.board[6][6].__repr__() == str(BROWN)):
            print("Molino")
            return True
        else:
            return False
