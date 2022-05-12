import pygame

# Program Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FIL, COL = 7, 7
SIZE = (SCREEN_WIDTH) // COL
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Colors
WHITE = (255, 255, 255)
GREY = (85, 81, 70)
BROWN = (240, 240, 240)
BLACK = (0, 0, 0)
COLOR_TABLE = (247, 205, 102)

#
valid_boxes = [
    [True, False, False, True, False, False, True],
    [False, True, False, True, False, True, False],
    [False, False, True, True, True, False, False],
    [True, True, True, False, True, True, True],
    [False, False, True, True, True, False, False],
    [False, True, False, True, False, True, False],
    [True, False, False, True, False, False, True],
]
