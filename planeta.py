import pygame
from pygame.locals import *

FPS = 60


class Planeta(pygame.sprite.Sprite):

    velocidad = 1

    def __init__(self, x=800, y=-100):
        self.x = x
        self.y = y

        # Inicializamos el Sprite, (ver pygame.doc)
        pygame.sprite.Sprite.__init__(self)

        # Inicializacion de la imagen del player (es un rectangulo)
        self.image_planeta = pygame.image.load('resources/images/planet.png').convert_alpha()
        self.image = self.image_planeta

        # Convertimos la imagen en un rectangulo con x,y,w,h, -> devuelve (0,0,681,686)
        self.rect = self.image.get_rect()
        # Coordenadas de entrada para posicionamiento -> Pos(x,y)
        self.rect.x = x
        self.rect.y = y
        # Tamaño del "rectangulo" planeta, (ancho, alto)
        self.w = self.rect.w
        self.h = self.rect.h

    def update(self, dt):
        if self.rect.x > 500:
            self.rect.x = self.rect.x - self.velocidad