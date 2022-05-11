import unittest
from sprint1_0.product.constants import GREY, WHITE
from sprint1_0.product.ficha import *

class TestFicha(unittest.TestCase):
    a=Ficha(1,2,GREY)
    def test_calcular_posicion(self):
        self.assertAlmostEqual()