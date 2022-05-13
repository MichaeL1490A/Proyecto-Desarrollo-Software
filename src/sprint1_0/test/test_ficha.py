import sys
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software\src\sprint1_0")
import unittest
from product.constants import SIZE,GREY
from product.ficha import Ficha
class TestFicha(unittest.TestCase):
    def test_calcular_posicion(self):
        a = Ficha(3,2,GREY)
        x = 285
        y = 399
        self.assertEqual((x,y),(a.x,a.y))
    def test_move(self):
        a = Ficha(3,2,GREY)
        a.move(4,5)
        x = 627
        y = 513
        self.assertEqual((x,y),(a.x,a.y))