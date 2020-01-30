import pygame

# Variables de uso global
LARGO = 700
ANCHO = 500
# Fotogramas por segundo
FPS = 60


class Rocket(pygame.sprite.Sprite):
    pict_rocket = 'resources/rocket.png'
    w_pict_rocket = 68
    h_pict_rocket = 40

    def __init__(self, x=0, y=(ANCHO/2)-h_pict_rocket):
