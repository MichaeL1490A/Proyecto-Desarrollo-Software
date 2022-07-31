import pygame
from Piece import Piece
from Constant import C
from Table import Table

class Print():
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 20) 
    def draw_box(self, screen):
        for fil in range(7):
            self.board.append([])
            for col in range(7):
                self.board[fil].append(0)
                if C.valid_boxes[fil][col] == True:
                    pygame.draw.circle(
                        screen, C.BLACK, (fil*C.SIZE + C.SIZE//2, col*C.SIZE + C.SIZE//2), 15)

    # Draw the support lines on the board
    def draw_lines(self, screen):
        for line in C.game_lines:
            pygame.draw.rect(screen, C.BLACK, line)

    # Paint the screen
    # AC 5.1
    def draw_screen(self, screen):
        self.draw_lines(screen)
        self.draw_box(screen)
        for fil in range(7):
            for col in range(7):
                piece = self.board[fil][col]
                if piece != 0:
                    piece.draw(screen)