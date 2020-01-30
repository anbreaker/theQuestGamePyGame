import pygame 
from pygame.locals import *
import sys

from entities import *

# Variables de uso global

# Definimos algunos colores
VERDE = (30, 186, 22)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (216, 229, 24)

# Fotogramas por segundo
FPS = 60


class Juego:
    clock = pygame.time.Clock()
    
    def __init__(self):
        # Inicialización de la superficie de dibujo (display surface)
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [700, 500]
        self.pantalla = pygame.display.set_mode(self.dimensiones)
        
        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame')
        
        # Inicializacion de la imagen de fondo de la pantalla (sin efecto alpha)
        self.fondo_pantalla = pygame.image.load('resources/background.png').convert()
        
        # Creamos la instancia del jugador
        self.player = Rocket()
        
        # Creacion de grupo de Sprite
        self.allSprintes = pygame.sprite.Group()
        # Agregamos al grupo al jugador
        self.allSprintes.add(self.player)

    def game_over(self):
        pygame.quit()
        
        
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.game_over()
            if evento.type == MOUSEBUTTONDOWN:
                self.game_over()
                
    
    def main_loop(self):
        while True:
            # tiempo_transcurrido
            dt = self.clock.tick(FPS)
            
            # Llamamos al broker de eventos
            self.manejar_eventos()
            
            # Limpia la pantalla y establece el fondo
            self.pantalla.blit(self.fondo_pantalla, (0,0))
            
            # Actualizamos y pintamos los grupos de Sprite para mostrarlos en pantalla
            self.allSprintes.update(dt)
            self.allSprintes.draw(self.pantalla)
            
            
            # Actualizamos la pantalla con lo dibujado.
            pygame.display.flip()
            

if __name__ ==  '__main__':
    pygame.init()
    juego = Juego()
    juego.main_loop()
    
    # https://plataforma.keepcoding.io/courses/714386/lectures/13745010
    # MINUTO 2.45