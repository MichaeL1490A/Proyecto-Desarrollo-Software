import pygame
from game import Game
from constants import *


def main():
    pygame.init()
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
