import pygame
import sys
from ranking import *

# Variables de uso global
ANCHO = 500
FPS = 60


class Planet(pygame.sprite.Sprite):
    pict_planet = 'planet.png'
    w_pict_planet = 681
    h_pict_planet = 686
    velocidad = 1

    # Constructor de la clase
    def __init__(self, x=0, y=(ANCHO/2)-h_pict_planet):
        self.x = x
        self.y = y

        # Inicializamos el Sprite, (ver pygame.doc)
        pygame.sprite.Sprite.__init__(self)

        # Inicializacion de la imagen del player (es un rectangulo)
        self.image = pygame.image.load(f'resources/images/{self.pict_planet}').convert_alpha()
        # Convertimos la imagen en un rectangulo con x,y,w,h, -> devuelve (0,0,681,686)
        self.rect = self.image.get_rect()
        # Coordenadas de entrada para posicionamiento -> Pos(x,y)
        self.rect.x = x
        self.rect.y = y
        # Tamaño del "rectangulo" player, (ancho, alto)
        self.w_pict_planet = self.rect.w
        self.h_pict_planet = self.rect.h
        
        self.tiempo_animacion = FPS // 4

        self.tiempo_acutal = 0

    def aparece_planeta(self):
        # Utilizando la funcion posicionamos el planeta y dado cierta condicion iniciara aparacion.
        
        self.rect.x -= self.velocidad





