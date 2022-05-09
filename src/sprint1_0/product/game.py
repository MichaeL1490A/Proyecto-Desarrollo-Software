import pygame, sys
from board import *
from constants import *
from ficha import *
sys.path.append('C:\\Users\\Hitee\\Desktop\\ProyectoNinMenMorris\\Proyecto-Desarrollo-Software')


#asdsa


#CLASE JUEGO
class Game(object):
    def __init__(self):
        #CREAMOS EL SPRITE TABLA
        self.all_sprites_list = pygame.sprite.Group()
        self.table =Table()
        self.all_sprites_list.add(self.table)

        self.ficha = Ficha()
        self.all_sprites_list.add(self.ficha)
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.ficha.move()
        return False
    def run_logic(self):
        pass
    def display_frame(self, screen):
        screen.fill(WHITE)
        self.all_sprites_list.draw(screen)
        pygame.display.flip()

#FUNCION PRINCIPAL
def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    done = False 
    clock = pygame.time.Clock()
    #Inicializa la clase Juego
    game = Game()
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
