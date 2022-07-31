from constants import SCREEN_HEIGHT, SCREEN_WIDTH, screen
from game import Game
import pygame
import pygame_menu

class AppRunner():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def main(self):
        pygame.display.set_caption("Nine Men's Morris")
        done = False
        clock = pygame.time.Clock()
        game = Game(screen)
        while not done:
            done = game.process_events(screen)
            game.update()
            clock.tick(60)
        pygame.quit()
    def start_the_game(self):
        self.main()
    def run(self):
        menu = pygame_menu.Menu('Welcome', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_SOLARIZED)
        menu.add.button('Play', self.start_the_game)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(screen)
