import pygame
from pygame.locals import *

FPS = 60


class Planeta(pg.sprite.Sprite):

    velocidad = 1

    def __init__(self, x=800, y=-50):
        self.x = x
        self.y = y

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('resources/images/planet.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h

    def update(self, dt):
        if self.rect.x > 500:
            self.rect.x = self.rect.x - self.velocidad
