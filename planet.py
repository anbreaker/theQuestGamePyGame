import pygame
import sys

# Variables de uso global
ANCHO = 500
FPS = 60

class Planeta(pygame.sprite.Sprite):
    pict_planet = 'planet.png'
    w_pict_planet = 681
    h_pict_planet = 686
    velocidad_aparicion_planeta = 1

    # Constructor de la clase
    def __init__(self, x=800, y=-80):
        self.x = x
        self.y = y

        # Condicion de aparicion del planeta
        self.aparece_planeta = False

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

    def update(self,dt):
        if self.aparece_planeta == True:
            # Utilizando la funcion posicionamos el planeta y dado cierta condicion iniciara aparacion.        
            if self.rect.x > 600:
                self.rect.x -= self.velocidad_aparicion_planeta





