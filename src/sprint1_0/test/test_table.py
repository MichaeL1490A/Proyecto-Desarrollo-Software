from product.ficha import Ficha
from product.table import *
import unittest
import sys
import pygame

sys.path.append("..")


class TestTable(unittest.TestCase):
    def test_molino_True(self):
        screen = pygame.display.set_mode([1000, 1000])
        self.table = Table()
        self.table.draw_screen(screen)
        self.table.board[0][0] = Ficha(0, 0, GREY)
        self.table.board[0][3] = Ficha(0, 3, GREY)
        self.table.board[0][6] = Ficha(0, 6, GREY)
        self.assertTrue(self.table.check_mill())

    def test_molino_False(self):
        screen = pygame.display.set_mode([1000, 1000])
        self.table = Table()
        self.table.draw_screen(screen)
        self.table.board[0][0] = Ficha(0, 0, GREY)
        self.table.board[0][3] = Ficha(0, 3, GREY)
        self.table.board[0][6] = Ficha(0, 6, BROWN)
        self.assertFalse(self.table.check_mill())

    def test_molino_True2(self):
        screen = pygame.display.set_mode([1000, 1000])
        self.table = Table()
        self.table.draw_screen(screen)
        self.table.board[2][2] = Ficha(2, 2, BROWN)
        self.table.board[3][2] = Ficha(3, 2, BROWN)
        self.table.board[4][2] = Ficha(4, 2, BROWN)
        self.assertTrue(self.table.check_mill())

    def test_molino_False2(self):
        screen = pygame.display.set_mode([1000, 1000])
        self.table = Table()
        self.table.draw_screen(screen)
        self.table.board[1][5] = Ficha(1, 5, BROWN)
        self.table.board[3][6] = Ficha(3, 6, BROWN)
        self.table.board[5][5] = Ficha(5, 5, BROWN)
        self.assertFalse(self.table.check_mill())
