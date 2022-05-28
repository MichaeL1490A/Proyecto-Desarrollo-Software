import pygame

# Program Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FIL, COL = 7, 7
SIZE = SCREEN_WIDTH // COL
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Colors
GREY = (85, 81, 70)
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
COLOR_TABLE = (247, 205, 102)
RED = (204, 0, 0)
# Tabla de posiciones válidas
valid_boxes = [
    [True, False, False, True, False, False, True],
    [False, True, False, True, False, True, False],
    [False, False, True, True, True, False, False],
    [True, True, True, False, True, True, True],
    [False, False, True, True, True, False, False],
    [False, True, False, True, False, True, False],
    [True, False, False, True, False, False, True],
]

next_to_piece = {
    (0, 0): [[0, 3], [3, 0]],
    (0, 3): [[0, 0], [0, 6], [1, 3]],
    (0, 6): [[3, 6], [0, 3]],
    (3, 0): [[6, 0], [0, 0], [3, 1]],
    (3, 6): [[0, 6], [6, 6], [3, 5]],
    (6, 6): [[3, 6], [6, 3]],
    (6, 3): [[6, 6], [6, 0], [5, 3]],
    (6, 0): [[6, 3], [3, 0]],
    (1, 1): [[1, 3], [3, 1]],
    (1, 3): [[1, 1], [1, 5], [2, 3], [0, 3]],
    (1, 5): [[1, 3], [3, 5]],
    (3, 5): [[1, 5], [3, 4], [3, 6], [5, 5]],
    (5, 5): [[5, 3], [3, 5]],
    (5, 3): [[5, 5], [4, 3], [5, 1], [6, 3]],
    (5, 1): [[5, 3], [3, 1]],
    (3, 1): [[5, 1], [3, 2], [1, 1], [3, 0]],
    (2, 2): [[2, 3], [3, 2]],
    (2, 3): [[2, 4], [1, 3], [2, 2]],
    (2, 4): [[3, 4], [2, 3]],
    (3, 4): [[4, 4], [2, 4], [3, 5]],
    (4, 4): [[3, 4], [4, 3]],
    (4, 3): [[4, 4], [4, 2], [5, 3]],
    (4, 2): [[4, 3], [3, 2]],
    (3, 2): [[4, 2], [2, 2], [3, 1]]
}
