from Constant import C
from Game import Game
import pygame
import pygame_menu


class AppRunner():
    pygame.init()

    def startGame(self):
        pygame.display.set_caption("Nine Men's Morris")
        done = False
        clock = pygame.time.Clock()
        game = Game(C.screen)
        while not done:
            done = game.process_events(C.screen)
            game.update()
            clock.tick(60)
        self.quitApp

    def quitApp():
        pygame.quit()

    def run(self):
        menu = pygame_menu.Menu(
            'Welcome', C.SCREEN_WIDTH, C.SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_SOLARIZED)
        menu.add.button('Play', self.startGame)
        menu.add.button('Quit', self.quitApp)
        menu.mainloop(C.screen)
