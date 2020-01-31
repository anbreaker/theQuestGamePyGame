import pygame 
from pygame.locals import *
import sys, os

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
        
        # Entidades del juego, jugadores, obstaculos, enemigos.......................
        
        # Creamos la instancia del jugador
        self.player = Rocket()
        
        # Creacion de grupo de Sprite
        self.allSprintes = pygame.sprite.Group()
        # Agregamos al grupo al jugador
        self.allSprintes.add(self.player)
        

    def game_over(self):
        pygame.quit()
        # No Olvidar pasar 0 en sys.exit(0), sin el parametro -> "Exception has occurred: SystemExit"
        sys.exit(0)
        
        
    def manejar_eventos(self):
        # Manejador de eventos, un daemon o broker a la espera llamado desde bucle principal
        for evento in pygame.event.get():
            # Sí, pulsa Salir
            if evento.type == pygame.QUIT or evento.type == KEYDOWN and evento.key == K_ESCAPE:
                self.game_over()
            
            # Control de movimientos player
            if evento.type == KEYDOWN:
                if evento.key == K_UP:
                    self.player.subir()
                if evento.key == K_DOWN:
                    self.player.bajar()
                    
        # Control de pulsacion de teclas sostenida
        tecla_sostenida = pygame.key.get_pressed()
        
        if tecla_sostenida[K_UP]:
            self.player.subir()
        if tecla_sostenida[K_DOWN]:
            self.player.bajar()
                    
                
    
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
    # MINUTO 3.08