import unittest
import sys

sys.path.append("..")

from product.constants import GREY, BROWN
from product.game import *

class TestGame(unittest.TestCase):
    def test_cambiar_turno(self):
        screen = pygame.display.set_mode([1000,1000])
        g=Game(screen)
        g.cambiar_turno()
        self.assertEqual(g.turn,BROWN)
    def test_cambiar_turno2(self):
        screen = pygame.display.set_mode([1000,1000])
        g=Game(screen)
        g.cambiar_turno()
        g.cambiar_turno()
        self.assertEqual(g.turn,GREY)