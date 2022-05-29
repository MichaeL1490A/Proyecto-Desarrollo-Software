from asyncio.windows_events import NULL
from tabnanny import check
from matplotlib.pyplot import table
import pygame
import sys
from table import Table
from constants import valid_boxes, BLACK, GREY, screen, SIZE, COLOR_TABLE, WHITE, RED

sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software")


# Function to transform from cartesian coordinate
# system to a matrix of 7x7 that represent the board game
def get_row_col_from_mouse(pos):
    x, y = pos
    circle_diameter = 20
    row = (y - SIZE//2 + circle_diameter) // SIZE
    col = (x - SIZE//2 + circle_diameter) // SIZE
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
        self.turn = GREY
        self.player = "1"
        self.pieces = 18
        self.modo = "Place"
        self.memory = 0

    # Historia de usuario 5

    # Update method shows the new actions that happen with the board game and the pieces in the GUI
    def update(self):
        self.table.draw_screen(screen)
        pygame.display.update()

    # This method changes the turn to its opponent
    def change_turn(self):
        if self.turn == GREY:
            self.turn = WHITE
            self.player = "2"
        else:
            self.turn = GREY
            self.player = "1"

    # AC 1.3
    # This method subtracts the pieces each time the player place a pieces in baord
    def pieces_left_add(self, num):
        self.pieces = self.pieces - num

    # This method checks remaining pieces
    def pieces_left(self):
        if self.pieces > 0:
            return True
        else:
            return False

    # This method helps to change the game mode

    def check_mode(self):
        if self.pieces > 0:
            self.modo = "Place"
        else:
            self.modo = "Select"
    # Historia de usuario 1

    def place_piece(self, fil, col):
        if self.table.check_empty(fil, col) and self.pieces_left() and valid_boxes[fil][col]:
            self.table.create_piece(fil, col, self.turn)
            self.pieces_left_add(1)
            self.check_mode()
            # Check if a mill has been built if not change turn
            if self.table.check_mill(fil, col):
                self.modo = "Remove"
            else:
                self.change_turn()

    # Historia de usuario 7

    def remove_piece(self, fil, col):
        if not self.table.board[fil][col].__repr__() == str(self.turn) and not self.table.check_empty(fil, col) and not self.table.check_mill(fil, col):
            self.table.delete_piece(fil, col)
            self.change_turn()
            self.check_mode()

    # Historia de usuario 2

    def move_piece(self, fil, col, memory):
        if self.table.check_empty(fil, col) and self.table.check_nexto(memory[0], memory[1], fil, col):
            self.table.move_piece(memory[0], memory[1], fil, col)
            # Check if a mill has been built
            if self.table.check_mill(fil, col):
                self.modo = "Remove"
                return 0
            else:
                self.change_turn()
        self.modo = "Select"

    # This method show in the windows the player's number that is playing
    def turn_text(self):
        font = pygame.font.SysFont("serif", 20)
        text = font.render("JUGADOR "+self.player, True, BLACK)
        center_x = SIZE*3 + SIZE//2 - text.get_width()//2
        center_y = 20 - text.get_height()//2
        screen.blit(text, [center_x, center_y])

    # Retorna una lista con las fichas que se pueden remover

    def process_events(self, screen):
        screen.fill(COLOR_TABLE)
        self.turn_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse pos in cartesian coordinate of the windows
                mouse = pygame.mouse.get_pos()

                # Function to transformate from cartesian coordinate to rows and cols of a matrix 7x7
                fil, col = get_row_col_from_mouse(mouse)
                if fil >= 0 and col >= 0 and valid_boxes[fil][col]:
                    # If the game is in Place Mode the player place pieces in the board and it checks if a mill has been build
                    if self.modo == "Place":
                        self.place_piece(fil, col)

                    # If the game is in Remove Mode the player just can remove pieces from the opponent
                    elif self.modo == "Remove":
                        self.remove_piece(fil, col)

                    # In Select Mode the player select which piece of him he is going to move
                    elif self.modo == "Select":
                        self.memory = 0
                        if self.table.board[fil][col].__repr__() == str(self.turn) and not self.table.check_empty(fil, col) and self.table.valid_place(fil, col):
                            self.memory = (fil, col)
                            self.modo = "Move"

                    # Move Select just move the piece to the new place selected and check if a mill has ben built
                    elif self.modo == "Move":
                        self.move_piece(fil, col, self.memory)
        return False
