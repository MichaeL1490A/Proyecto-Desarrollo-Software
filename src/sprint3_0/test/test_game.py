from product.constants import GREY, WHITE
from product.game import *
import sys
import unittest
import pygame
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software\src\sprint2_0")


class TestGame(unittest.TestCase):

    def test_get_row_col_from_pos(self):
        g = Game(screen)
        row, col = g.get_row_col_from_mouse((500, 500))
        self.assertEqual((4, 4), (row, col))

    # First acceptance requirement for 1 user history
    # Proving you can't place any piece on a place where already a piece is

    def test_place_piece1(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        g.place_piece(2, 2)
        # Trying to place a piece on the same place we already did with GREY
        self.assertFalse(g.place_piece(2, 2))
        g.change_turn()
        # Trying again with WHITE
        self.assertFalse(g.place_piece(2, 2))

    # Second acceptance requirement for 1 user history
    # Confirming you can place a piece on a empty place

    def test_place_piece2(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Placing a piece on a empty place
        g.place_piece(2, 2)
        self.assertTrue(g.table.board[2][2] != 0)

    # Third acceptance requirement for 7 user history
    # You can't place more pieces after placing the 18 pieces required

    def test_place_piece3(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Placing the 18 pieces for each player
        g.place_piece(0, 0)
        g.place_piece(0, 3)
        g.place_piece(0, 6)
        g.place_piece(3, 0)
        g.place_piece(6, 0)
        g.place_piece(3, 6)
        g.place_piece(6, 6)
        g.place_piece(3, 4)
        g.place_piece(3, 5)
        g.change_turn()
        g.place_piece(1, 3)
        g.place_piece(2, 3)
        g.place_piece(5, 3)
        g.place_piece(4, 3)
        g.place_piece(6, 3)
        g.place_piece(3, 1)
        g.place_piece(3, 2)
        g.place_piece(1, 5)
        g.place_piece(5, 1)
        g.change_turn()
        # Trying to place another piece
        g.place_piece(5, 5)
        # Expecting it didn't place
        self.assertFalse(g.table.board[5][5] != 0)

    # Fourth acceptance requirement for 1 user history
    # Proving you can't place any piece on a place outside of the table

    def test_place_piece4(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Trying to place a piece on an invalid place
        g.place_piece(0, 1)
        self.assertFalse(g.table.board[0][1] != 0)

    # First acceptance requirement for 2 user history
    # Proving that you can't move a piece to a place that is already fill

    def test_move_piece1(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Placing 2 pieces one next to other
        g.place_piece(0, 0)
        g.place_piece(0, 3)
        # Trying to move the first piece to the place already the 2nd one is on
        g.move_piece(0, 3, (0, 0))
        # Expecting to return to select mode since there was no change
        self.assertEqual("Select", g.modo)

    # Second acceptance requirement for 2 user history
    # Proving that you can't move a piece to a place that is not next to you

    def test_move_piece2(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Placing a piece
        g.place_piece(0, 0)
        # Back to GREY
        g.change_turn()
        # Trying to move the piece to a place outside of it's range to move
        g.move_piece(0, 6, (0, 0))
        # Expecting to return to select mode since there was no change
        self.assertEqual("Select", g.modo)

    # Third acceptance requirement for 2 user history
    # Placing a piece and doing a mill

    def test_move_piece3(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Placing a piece
        g.place_piece(0, 0)
        # Back to GREY
        g.change_turn()
        g.place_piece(0, 3)
        g.change_turn()
        # Placing the piece we want to move to a mill
        g.place_piece(3, 6)
        g.change_turn()
        # Moving the piece to a place that does a mill
        g.move_piece(0, 6, (3, 6))
        # Expecting we change mode to Remove since we did a mill and that there is a piece on the place we moved the piece
        self.assertEqual("Remove", g.modo)
        self.assertTrue(g.table.board[0][6] != 0)

    # Fourth acceptance requirement for 2 user history
    # Moving a piece to a place outside of the table

    def test_move_piece4(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Placing a piece
        g.place_piece(0, 0)
        # Back to GREY
        g.change_turn()
        # Moving the piece to a valid place
        g.move_piece(0, 2, (0, 0))
        # Expecting to return to select mode since there was no change because is invalid
        self.assertEqual("Select", g.modo)

    # Second acceptance requirement for 7 user history
    # Proving that you can remove a piece

    def test_remove_piece1(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Piece from GREY placed
        g.place_piece(2, 2)
        # Proving if you can remove the piece of GREY while being in WHITE
        g.remove_piece(2, 2)
        self.assertTrue(g.table.board[2][2] == 0)

    # First acceptance requirement for 7 user history
    # Proving that you can't remove a piece from yours in your own turn

    def test_remove_piece2(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Piece from GREY placed
        g.place_piece(2, 2)
        # Turn back to GREY
        g.change_turn()
        # Trying to remove piece while being on GREY turn
        g.remove_piece(2, 2)
        self.assertFalse(g.table.board[2][2] == 0)

    # Third acceptance requirement for 7 user history
    # Proving that you can't remove a piece from enemy if it is on a mill

    def test_remove_piece3(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        # Making a mill for GREY
        g.place_piece(0, 0)
        g.change_turn()
        g.place_piece(0, 3)
        g.change_turn()
        g.place_piece(0, 6)
        # Trying to remove a GREY piece that is on a mill while being on WHITE turn
        g.remove_piece(0, 0)
        self.assertFalse(g.table.board[0][0] == 0)

    # First acceptance requirement for 4 user history
    # When you are on turn of GREY and finish your move you change to WHITE

    def test_change_turn1(self):
        screen = pygame.display.set_mode([800, 800])
        # You start on GREY
        g = Game(screen)
        # Trying to change turn to WHITE
        g.change_turn()
        # Proving
        self.assertEqual(g.turn, WHITE)

    # Seccond acceptance requirement for 4 user history
    # When you are on turn of WHITE and finish your move you change to GREY

    def test_change_turn2(self):
        screen = pygame.display.set_mode([800, 800])
        # You start on GREY
        g = Game(screen)
        # Changing turn to WHITE
        g.change_turn()
        # Trying to change turn to GREY
        g.change_turn()
        # Proving
        self.assertEqual(g.turn, GREY)
