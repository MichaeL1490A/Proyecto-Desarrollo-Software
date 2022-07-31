import pygame
#from Piece import Piece
from Constant import C
#from Table import Table


class Print():

    def draw_pieces(self, screen, piece):
        pygame.draw.circle(screen, piece.color, (piece.x, piece.y), 20)

    def draw_positions_valids_of_game(self, screen, board):
        for fil in range(7):
            board.append([])
            for col in range(7):
                board[fil].append(0)
                if C.valid_boxes[fil][col] == True:
                    pygame.draw.circle(
                        screen, C.BLACK, (fil*C.SIZE + C.SIZE//2, col*C.SIZE + C.SIZE//2), 15)

    # Draw the support lines on the board
    def draw_lines_of_game(self, screen):
        for line in C.game_lines:
            pygame.draw.rect(screen, C.BLACK, line)

    # Draw the pieces in game
    def draw_pieces_in_game(self, screen, board):
        for fil in range(7):
            for col in range(7):
                piece = board[fil][col]
                if piece != 0:
                    self.draw_pieces(self, screen, piece)

    # AC 5.1: Paint the screen
    @classmethod
    def draw_screen(self, screen, board):
        self.draw_lines_of_game(self, screen)
        self.draw_positions_valids_of_game(self, screen, board)
        self.draw_pieces_in_game(self, screen, board)

    # Shows the pieces that can be removed when making a mill
    @classmethod
    def draw_pieces_remove(self, screen, table, turn):
        for fil in range(7):
            for col in range(7):
                if not table.board[fil][col].__repr__() == str(turn) and not table.is_space_available(fil, col) and not table.check_mill(fil, col):
                    pygame.draw.circle(
                        screen, C.RED, (col*C.SIZE + C.SIZE//2, fil*C.SIZE + C.SIZE//2), 25)
