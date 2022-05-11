import unittest
from sprint1_0.product.constants import *
from sprint1_0.product.ficha import *

class TestFicha(unittest.TestCase):
    def test_calcular_posicion(self):
        a = Ficha(3,2,GREY)
        x = SIZE * 2 + SIZE//2
        y = SIZE * 3 + SIZE//2
        self.assertAlmostEqual((x,y),(a.x,a.y))