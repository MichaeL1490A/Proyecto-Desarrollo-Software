from constants import *
from game import Game
import pygame
import sys
sys.path.append(
    "D:\Programas\Pygame\Proyecto Software\Proyecto-Desarrollo-Software - Test")


def main():
    pygame.init()
    pygame.display.set_caption("Nine Men's Morris")
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    done = False
    clock = pygame.time.Clock()
    game = Game(screen)
    while not done:
        done = game.process_events(screen)
        game.update()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
