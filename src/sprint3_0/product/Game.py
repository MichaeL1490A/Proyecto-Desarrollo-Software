from statistics import mode
import pygame
import sys
from Table import Table
from Constant import C
from Print import Print

sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software - Test")


# Function to transform from cartesian coordinate
# system to a matrix of 7x7 that represent the board game
def get_row_col_from_mouse(pos):
    x, y = pos
    circle_diameter = 20
    row = (y - C.SIZE//2 + circle_diameter) // C.SIZE
    col = (x - C.SIZE//2 + circle_diameter) // C.SIZE
    return row, col


# Class Game() has the job to run the logic of the program as
# when turn has to change, also when place, move, remove pieces
# And always check if a mill has been created

class Game():
    def __init__(self, screen):
        self._init()
        self.screen = screen

    def _init(self):
        self.table = Table()
        self.turn = C.GREY
        self.pieces = 18
        self.modo = "Place"
        self.memory = 0
        self.grey = 0
        self.white = 0

    # User history 5: This method shows the new actions that happen with the board game and the pieces in the GUI
    def update(self):
        if self.modo == "Remove":
            Print.draw_pieces_remove(C.screen, self.table, self.turn)
        Print.draw_screen(C.screen, self.table.board)
        pygame.display.update()

    # This method changes the turn to its opponent
    def change_turn(self):
        self.turn = C.WHITE if self.turn == C.GREY else C.GREY

    # AC 1.3: This method subtracts the remaining pieces each time the player places a piece on the board
    def decrease_remaining_pieces(self, num):
        self.pieces = self.pieces - num

    # Increase the number of pieces we have by color
    def add_pieces_by_color(self):
        self.grey += 1 * int(self.turn == C.GREY)
        self.white += 1 * int(self.turn == C.WHITE)

    # Reduce the number of pieces per color
    def delete_pieces_by_color(self):
        self.grey -= 1 * int(self.turn == C.WHITE)
        self.white -= 1 * int(self.turn == C.GREY)

    # This method checks remaining pieces
    def remaining_pieces(self):
        return self.pieces > 0

    # This method helps to change the game mode
    def check_mode(self):
        self.modo = "Place" if self.remaining_pieces() else "Select"

    # Check if a mill has been built if not change turn
    def check_mill_to_set_game_mode(self, fil, col):
        if self.table.check_mill(fil, col):
            self.modo = "Remove"
            return 0
        else:
            self.change_turn()

    # User history 1: This method adds a piece to the board
    def place_piece(self, fil, col):
        if self.table.is_space_available(fil, col) and self.remaining_pieces() and self.table.is_space_on_board(fil, col):
            self.table.create_piece(fil, col, self.turn)
            self.decrease_remaining_pieces(1)
            self.add_pieces_by_color()
            self.check_mode()
            self.check_mill_to_set_game_mode(fil, col)

    # User history 7: This method removes a piece
    def remove_piece(self, fil, col):
        if not self.table.board[fil][col].__repr__() == str(self.turn) and not self.table.is_space_available(fil, col) and not self.table.check_mill(fil, col):
            self.table.delete_piece(fil, col)
            self.delete_pieces_by_color()
            self.change_turn()
            self.check_mode()
            self.winner()

    # User history 2: This method moves one piece
    def move_piece(self, fil, col, memory):
        if (self.turn == C.GREY and self.grey > 3) or (self.turn == C.WHITE and self.white > 3):
            if self.table.is_space_available(fil, col) and self.table.check_nexto(memory[0], memory[1], fil, col):
                self.table.move_piece(memory[0], memory[1], fil, col)
                if self.table.check_mill(fil, col):
                    self.modo = "Remove"
                    return 0
                else:
                    self.change_turn()
        elif (self.turn == C.GREY and self.grey == 3) or (self.turn == C.WHITE and self.white == 3):
            if self.table.is_space_available(fil, col):
                self.table.move_piece(memory[0], memory[1], fil, col)
                if self.table.check_mill(fil, col):
                    self.modo = "Remove"
                    return 0
                else:
                    self.change_turn()
        self.modo = "Select"

    # This method calculates the winner of the game
    def winner(self):
        if self.pieces == 0:
            if self.grey == 2 or self.white == 2:
                self.modo = "Win"
                self.change_turn()

    # Shows the status of the game on the screen
    def text_in_screen(self):
        font = pygame.font.SysFont("serif", 25, bold=True)

        if self.modo == "Place":
            game_action = "COLOCA"
            color_action = C.GREEN
        elif self.modo == "Remove":
            game_action = "COME"
            color_action = C.RED
        elif self.modo == "Select" or self.modo == "Move":
            game_action = "MUEVE"
            color_action = C.BLUE
        elif self.modo == "Win":
            game_action = "VENCE"
            color_action = C.GREEN

        action_screen = font.render(game_action, True, color_action)
        center_x = C.SIZE*2.85 - action_screen.get_width()//2
        center_y = 19 - action_screen.get_height()//2
        C.screen.blit(action_screen, [center_x, center_y])

        font = pygame.font.SysFont("serif", 20, bold=True)
        player = "NEGRO" if self.turn == C.GREY else "BLANCO"
        player_screen = font.render(" EL JUGADOR "+player, True, C.BLACK)
        center_x = C.SIZE*3.8 + C.SIZE//2 - player_screen.get_width()//2
        center_y = 20 - player_screen.get_height()//2
        C.screen.blit(player_screen, [center_x, center_y])

    # Constantly called method for the game process
    def process_events(self, screen):
        screen.fill(C.COLOR_TABLE)
        self.text_in_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse pos in cartesian coordinate of the windows
                mouse = pygame.mouse.get_pos()
                # We convert the mouse coordinates to positions of board
                fil, col = get_row_col_from_mouse(mouse)

                if fil >= 0 and col >= 0 and self.table.is_space_on_board(fil, col):
                    # If the game is in Place Mode the player place pieces in the board and it checks if a mill has been build
                    if self.modo == "Place":
                        self.place_piece(fil, col)

                    # If the game is in Remove Mode the player just can remove pieces from the opponent
                    elif self.modo == "Remove":
                        self.remove_piece(fil, col)

                    # In Select Mode the player select which piece of him he is going to move
                    elif self.modo == "Select":
                        self.memory = 0
                        if self.table.board[fil][col].__repr__() == str(self.turn) and not self.table.is_space_available(fil, col) and self.table.is_space_on_board(fil, col):
                            self.memory = (fil, col)
                            self.modo = "Move"

                    # Move Select just move the piece to the new place selected and check if a mill has ben built
                    elif self.modo == "Move":
                        self.move_piece(fil, col, self.memory)

                    elif self.modo == "Win":
                        pass
        return False
