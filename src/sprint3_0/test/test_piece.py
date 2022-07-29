import unittest
import sys
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software - Test\src\sprint3_0\product")
from product.constants import SIZE, GREY
from product.piece import Piece

class TestPiece(unittest.TestCase):
    def test_calcular_posicion(self):
        a = Piece(3, 2, GREY)
        x = 285
        y = 399
        self.assertEqual((x, y), (a.x, a.y))

    def test_move(self):
        a = Piece(3, 2, GREY)
        a.move(4, 5)
        x = 627
        y = 513
        self.assertEqual((x, y), (a.x, a.y))
