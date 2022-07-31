from constants import *
from AppRunner import AppRunner
import pygame
import sys
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software - Test")

class NineMenMorris:
    def main(self):
        A=AppRunner()
        A.run()



if __name__ == "__main__":
    game = NineMenMorris()
    game.main()
