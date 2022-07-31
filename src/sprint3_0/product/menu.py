from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from main import main

import pygame
import pygame_menu
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def start_the_game():
    main()

menu = pygame_menu.Menu('Welcome', SCREEN_WIDTH, SCREEN_HEIGHT,
                       theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)