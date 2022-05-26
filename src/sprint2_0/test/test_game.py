import sys
import unittest
import pygame
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software\src\sprint2_0")
from product.game import *
from product.constants import GREY, WHITE

class TestGame(unittest.TestCase):
    def test_cambiar_turno(self):
        screen = pygame.display.set_mode([1000, 1000])
        g = Game(screen)
        g.change_turn()
        self.assertEqual(g.turn, WHITE)

    def test_cambiar_turno2(self):
        screen = pygame.display.set_mode([1000, 1000])
        g = Game(screen)
        g.change_turn()
        g.change_turn()
        self.assertEqual(g.turn, GREY)

    def test_get_row_col_from_pos(self):
        row, col = get_row_col_from_mouse((500, 500))
        self.assertEqual((4, 4), (row, col))

    def test_place_piece(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        g.place_piece(2, 2)
        self.assertTrue(g.table.board[2][2] != 0)
        self.assertFalse(g.table.board[0][0] != 0)
    
    def test_remove_piece(self):
        screen = pygame.display.set_mode([1000, 1000])
        g = Game(screen)
        g.update()
        g.place_piece(2, 2)
        g.change_turn()
        g.remove_piece(2, 2)
        self.assertTrue(g.table.board[2][2] == 0)

    def test_remove_piece2(self):
        screen = pygame.display.set_mode([1000, 1000])
        g = Game(screen)
        g.update()
        g.place_piece(2, 2)
        g.remove_piece(2, 2)
        self.assertFalse(g.table.board[2][2] == 0)