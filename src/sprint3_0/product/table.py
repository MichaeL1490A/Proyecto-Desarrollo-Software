import pygame
from piece import Piece
from constants import valid_boxes, BLACK, SIZE, GREY, WHITE, next_to_piece, case_of_mill, game_lines


class Table():
    def __init__(self):
        self.board = []  # Pieces in play

    def draw_positions_valids_of_game(self, screen):
        for fil in range(7):
            self.board.append([])
            for col in range(7):
                self.board[fil].append(0)
                if valid_boxes[fil][col] == True:
                    pygame.draw.circle(
                        screen, BLACK, (fil*SIZE + SIZE//2, col*SIZE + SIZE//2), 15)

    # Draw the support lines on the board
    def draw_lines_of_game(self, screen):
        for line in game_lines:
            pygame.draw.rect(screen, BLACK, line)

    # Draw the pieces in game
    def draw_pieces_in_game(self, screen):
        for fil in range(7):
            for col in range(7):
                piece = self.board[fil][col]
                if piece != 0:
                    piece.draw(screen)

    # AC 5.1: Paint the screen
    def draw_screen(self, screen):
        self.draw_lines_of_game(screen)
        self.draw_positions_valids_of_game(screen)
        self.draw_pieces_in_game(screen)

    # Check if the move is a consecutive position
    def check_nexto(self, fil, col, newfil, newcol):
        for place in next_to_piece[(fil, col)]:
            if newfil == place[0] and newcol == place[1]:
                return True
        return False

    # This method checks for each places of the board if a mill has been built
    def check_mill(self, fil, col):
        colors = (GREY, WHITE)
        for color in colors:
            for i in case_of_mill[(fil, col)]:
                if self.board[i[0][0]][i[0][1]].__repr__() == str(color) and self.board[i[1][0]][i[1][1]].__repr__() == str(color) and self.board[i[2][0]][i[2][1]].__repr__() == str(color):
                    return True
        return False

    # AC 1.1 1.2: Check if the position where you want to put the pieces is empty
    def check_empty(self, fil, col):
        return self.board[fil][col] == 0

    # AC 1.4: Check if the selected position is valid
    def valid_place(self, fil, col):
        return valid_boxes[fil][col]

    # Create a piece
    def create_piece(self, fil, col, turn):
        piece = Piece(fil, col, turn)
        self.board[fil][col] = piece

    # Delete a piece
    def delete_piece(self, fil, col):
        self.board[fil][col] = 0

    # Move a piece
    def move_piece(self, fil, col, newfil, newcol):
        self.board[newfil][newcol] = self.board[fil][col]
        self.board[fil][col].move(newfil, newcol)
        self.board[fil][col] = 0
