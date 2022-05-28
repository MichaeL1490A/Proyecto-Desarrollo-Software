import sys
import unittest
import pygame
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software\src\sprint2_0")
from product.game import *
from product.constants import GREY, WHITE

class TestGame(unittest.TestCase):
    def test_cambiar_turno(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.change_turn()
        self.assertEqual(g.turn, WHITE)

    def test_cambiar_turno2(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.change_turn()
        g.change_turn()
        self.assertEqual(g.turn, GREY)

    def test_get_row_col_from_pos(self):
        row, col = get_row_col_from_mouse((500, 500))
        self.assertEqual((4, 4), (row, col))

    #First acceptance requirement for 1 user history
    #Proving you can't place any piece on a place where already a piece is

    def test_place_piece(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        g.place_piece(2,2)
        #Trying to place a piece on the same place we already did with GREY
        self.assertFalse(g.place_piece(2,2))
        g.change_turn()
        #Trying again with WHITE
        self.assertFalse(g.place_piece(2,2))

    #Second acceptance requirement for 1 user history
    #Confirming you can place a piece on a empty place

    def test_place_piece2(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        #Placing a piece on a empty place
        g.place_piece(2,2)
        self.assertTrue(g.table.board[2][2]!=0)

    #Second acceptance requirement for 7 user history
    #Proving if you can remove a piece when is not yours

    def test_remove_piece1(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        #Piece from GREY placed
        g.place_piece(2,2)
        #Changing to WHITE
        g.change_turn()
        #Proving if you can remove the piece of GREY while being in WHITE
        g.remove_piece(2,2)
        self.assertTrue(g.table.board[2][2] == 0)

    #Third acceptance requirement for 7 user history
    #You can't place more pieces after placing the 18 required

    def test_remove_piece1(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        #Piece from GREY placed
        g.place_piece(2,2)
        #Changing to WHITE
        g.change_turn()
        #Proving if you can remove the piece of GREY while being in WHITE
        g.remove_piece(2,2)
        self.assertTrue(g.table.board[2][2] == 0)

    #First acceptance requirement for 7 user history
    #Proving that you can't remove a piece from yours in your own turn

    def test_remove_piece2(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        #Piece from GREY placed
        g.place_piece(2,2)
        #Trying to remove piece while being on GREY turn
        g.remove_piece(2,2)
        self.assertFalse(g.table.board[2][2] == 0)

    #Third acceptance requirement for 7 user history
    #Proving that you can't remove a piece from enemy if it is on a mill

    def test_remove_piece3(self):
        screen = pygame.display.set_mode([800, 800])
        g = Game(screen)
        g.update()
        #Making a mill for GREY
        g.place_piece(0,0)
        g.place_piece(0,3)
        g.place_piece(0,6)
        #Changing turn to WHITE
        g.change_turn()
        #Trying to remove a GREY piece that is on a mill while being on WHITE turn 
        g.remove_piece(0,0)
        self.assertFalse(g.table.board[0][0] == 0)