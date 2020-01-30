import pygame
from pygame.locals import *

# Variables de uso global
LARGO = 700
ANCHO = 500

# Definimos algunos colores
VERDE = (30, 186, 22)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (216, 229, 24)

# Fotogramas por segundo
FPS = 60

class Juego:
    clock = pygame.time.Clock()
    
    def__init__(self,LARGO,ANCHO):
        # Inicialización de la superficie de dibujo (display surface)
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [LARGO, ANCHO]
        self.pantalla = pygame.display.set_mode(self.dimensiones)
        
        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame')
        
        # Inicializacion de la imagen de fondo de la pantalla (sin efecto alpha)
        self.fondo_pantalla = pygame.image.load('resources/background.png').convert()
