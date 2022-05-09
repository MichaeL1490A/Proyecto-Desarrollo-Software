import pygame
class Table(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("table.jpeg").convert()
        self.rect = self.image.get_rect()