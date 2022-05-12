import unittest
import sys
sys.path.append("..")
from product.constants import SIZE,GREY
from product.ficha import Ficha

class TestFicha(unittest.TestCase):
    def test_calcular_posicion(self):
        a = Ficha(3,2,GREY)
        x = 355
        y = 497
        self.assertEqual((x,y),(a.x,a.y))
    def test_move(self):
        a = Ficha(3,2,GREY)
        a.move(4,5)
        x = 781
        y = 639
        self.assertEqual((x,y),(a.x,a.y))