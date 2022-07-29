import pygame
import unittest
import sys
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software\src\sprint2_0")
from product.piece import Piece
from product.table import *




class TestTable(unittest.TestCase):
    def test_molino_True(self):
        screen = pygame.display.set_mode([1000, 1000])
        self.table = Table()
        self.table.draw_screen(screen)
        self.table.board[0][0] = Piece(0, 0, GREY)
        self.table.board[0][3] = Piece(0, 3, GREY)
        self.table.board[0][6] = Piece(0, 6, GREY)
        self.assertTrue(self.table.check_mill(0, 0))

    def test_molino_False(self):
        screen = pygame.display.set_mode([1000, 1000])
        self.table = Table()
        self.table.draw_screen(screen)
        self.table.board[0][0] = Piece(0, 0, GREY)
        self.table.board[0][3] = Piece(0, 3, GREY)
        self.table.board[0][6] = Piece(0, 6, WHITE)
        self.assertFalse(self.table.check_mill(0, 0))

    def test_molino_True2(self):
        screen = pygame.display.set_mode([1000, 1000])
        self.table = Table()
        self.table.draw_screen(screen)
        self.table.board[2][2] = Piece(2, 2, WHITE)
        self.table.board[3][2] = Piece(3, 2, WHITE)
        self.table.board[4][2] = Piece(4, 2, WHITE)
        self.assertTrue(self.table.check_mill(2, 2))

    def test_molino_False2(self):
        screen = pygame.display.set_mode([1000, 1000])
        self.table = Table()
        self.table.draw_screen(screen)
        self.table.board[1][5] = Piece(1, 5, WHITE)
        self.table.board[3][6] = Piece(3, 6, WHITE)
        self.table.board[5][5] = Piece(5, 5, WHITE)
        self.assertFalse(self.table.check_mill(1, 5))
 