import sys
import unittest
import pygame
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software\src\sprint1_0")
from product.game import *
from product.constants import GREY, BROWN

class TestGame(unittest.TestCase):
    def test_cambiar_turno(self):
        screen = pygame.display.set_mode([1000, 1000])
        g = Game(screen)
        g.cambiar_turno()
        self.assertEqual(g.turn, BROWN)

    def test_cambiar_turno2(self):
        screen = pygame.display.set_mode([1000, 1000])
        g = Game(screen)
        g.cambiar_turno()
        g.cambiar_turno()
        self.assertEqual(g.turn, GREY)

    def test_get_row_col_from_pos(self):
        row, col = get_row_col_from_mouse((500, 500))
        self.assertEqual((4, 4), (row, col))

    def test_colocar_ficha(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        g.colocar_ficha(2, 2)
        self.assertTrue(g.table.board[2][2] != 0)
        self.assertFalse(g.table.board[0][0] != 0)
