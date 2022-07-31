import pygame


class C():
    # Program Dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    FIL, COL = 7, 7
    SIZE = SCREEN_WIDTH // COL
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Colors
    GREY = (105, 101, 90)
    WHITE = (240, 240, 240)
    BLACK = (0, 0, 0)
    COLOR_TABLE = (247, 205, 102)
    RED = (204, 0, 0)

    # List of positions valid in the board.
    valid_boxes = [
        [True, False, False, True, False, False, True],
        [False, True, False, True, False, True, False],
        [False, False, True, True, True, False, False],
        [True, True, True, False, True, True, True],
        [False, False, True, True, True, False, False],
        [False, True, False, True, False, True, False],
        [True, False, False, True, False, False, True],
    ]

    # Dictionary of the valid adjacent points of each point of the board
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

    # Dictionary of all the possible ways to make a mill
    case_of_mill = {
        # (0, 0):[[[0, 0],[0, 0]],[[0, 3],[3, 0]],[[0, 6],[6, 0]]]
        (0, 0): [[[0, 0], [0, 3], [0, 6]], [[0, 0], [3, 0], [6, 0]]],
        (0, 3): [[[0, 3], [0, 0], [0, 6]], [[0, 3], [1, 3], [2, 3]]],
        (0, 6): [[[0, 6], [0, 3], [0, 0]], [[0, 6], [3, 6], [6, 6]]],
        (3, 0): [[[3, 0], [6, 0], [0, 0]], [[3, 0], [3, 1], [3, 2]]],
        (3, 6): [[[3, 6], [0, 6], [6, 6]], [[3, 6], [3, 5], [3, 4]]],
        (6, 6): [[[6, 6], [3, 6], [0, 6]], [[6, 6], [6, 3], [6, 0]]],
        (6, 3): [[[6, 3], [6, 6], [6, 0]], [[6, 3], [5, 3], [4, 3]]],
        (6, 0): [[[6, 0], [3, 0], [0, 0]], [[6, 0], [6, 3], [6, 6]]],
        (1, 1): [[[1, 1], [1, 3], [1, 5]], [[1, 1], [3, 1], [5, 1]]],
        (1, 3): [[[1, 3], [1, 1], [1, 5]], [[1, 3], [0, 3], [2, 3]]],
        (1, 5): [[[1, 5], [1, 3], [1, 1]], [[1, 5], [3, 5], [5, 5]]],
        (3, 5): [[[3, 5], [1, 5], [5, 5]], [[3, 5], [3, 4], [3, 6]]],
        (5, 5): [[[5, 5], [3, 5], [1, 5]], [[5, 5], [5, 1], [5, 3]]],
        (5, 3): [[[5, 3], [6, 3], [4, 3]], [[5, 3], [5, 5], [5, 1]]],
        (5, 1): [[[5, 1], [3, 1], [1, 1]], [[5, 1], [5, 3], [5, 5]]],
        (3, 1): [[[3, 1], [5, 1], [1, 1]], [[3, 1], [3, 0], [3, 2]]],
        (2, 2): [[[2, 2], [2, 3], [2, 4]], [[2, 2], [3, 2], [4, 2]]],
        (2, 3): [[[2, 3], [2, 2], [2, 4]], [[2, 3], [0, 3], [1, 3]]],
        (2, 4): [[[2, 4], [2, 3], [2, 2]], [[2, 4], [3, 4], [4, 4]]],
        (3, 4): [[[3, 4], [2, 4], [4, 4]], [[3, 4], [3, 5], [5, 6]]],
        (4, 4): [[[4, 4], [3, 4], [2, 4]], [[4, 4], [4, 3], [4, 2]]],
        (4, 3): [[[4, 3], [4, 4], [4, 2]], [[4, 3], [5, 3], [6, 3]]],
        (4, 2): [[[4, 2], [3, 2], [2, 2]], [[4, 2], [4, 3], [4, 4]]],
        (3, 2): [[[3, 2], [4, 2], [2, 2]], [[3, 2], [3, 1], [3, 0]]],
    }

    # Game frame
    width_line = 4
    game_lines = [
        (0*SIZE + SIZE//2, 0*SIZE + SIZE//2,
         width_line, SIZE*7 - 2*(0*SIZE + SIZE//2)),
        (1*SIZE + SIZE//2, 1*SIZE + SIZE//2,
         width_line, SIZE*7 - 2*(1*SIZE + SIZE//2)),
        (2*SIZE + SIZE//2, 2*SIZE + SIZE//2,
         width_line, SIZE*7 - 2*(2*SIZE + SIZE//2)),
        (7*SIZE - (1+0)*SIZE + SIZE//2, 0*SIZE + SIZE //
         2, width_line, SIZE*7 - 2*(0*SIZE + SIZE//2)),
        (7*SIZE - (1+1)*SIZE + SIZE//2, 1*SIZE + SIZE //
         2, width_line, SIZE*7 - 2*(1*SIZE + SIZE//2)),
        (7*SIZE - (1+2)*SIZE + SIZE//2, 2*SIZE + SIZE //
         2, width_line, SIZE*7 - 2*(2*SIZE + SIZE//2)),
        (0*SIZE + SIZE//2, 0*SIZE + SIZE//2, SIZE *
         7 - 2*(0*SIZE + SIZE//2), width_line),
        (1*SIZE + SIZE//2, 1*SIZE + SIZE//2, SIZE *
         7 - 2*(1*SIZE + SIZE//2), width_line),
        (2*SIZE + SIZE//2, 2*SIZE + SIZE//2, SIZE *
         7 - 2*(2*SIZE + SIZE//2), width_line),
        (0*SIZE + SIZE//2, 7*SIZE - (0*SIZE + SIZE//2),
         SIZE*7 - 2*(0*SIZE + SIZE//2), width_line),
        (1*SIZE + SIZE//2, 7*SIZE - (1*SIZE + SIZE//2),
         SIZE*7 - 2*(1*SIZE + SIZE//2), width_line),
        (2*SIZE + SIZE//2, 7*SIZE - (2*SIZE + SIZE//2),
         SIZE*7 - 2*(2*SIZE + SIZE//2), width_line),
        (SIZE//2, SIZE*3 + SIZE//2, SIZE*2, width_line),
        (SIZE//2 + SIZE*4, SIZE*3 + SIZE//2, SIZE*2, width_line),
        (SIZE*3 + SIZE//2, SIZE//2, width_line, SIZE*2),
        (SIZE*3 + SIZE // 2, 5*SIZE-SIZE//2, width_line, SIZE*2)
    ]
