import pygame 
from pygame.locals import *
import sys, os
from random import choice, randint
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
        self.display = pygame.display
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [700, 500]
        self.pantalla = pygame.display.set_mode(self.dimensiones)
        
        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame')
        
        # Inicializacion de la imagen de fondo de la pantalla (sin efecto alpha)
        self.fondo_pantalla = pygame.image.load('resources/images/background.png').convert()
        
        # Entidades del juego, jugadores, obstaculos, enemigos.......................
        
        # Creamos la instancia del jugador
        self.nave = Rocket()
        
        # Creacion de grupos de Sprite
        self.naveGroup = pygame.sprite.Group()
        self.asteroideGroup = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()
                
        # Agregamos al grupo al jugador
        self.naveGroup.add(self.nave)
        
        # Llamo la funcion
        self.crear_asteroides()
        
        self.allSprites.add(self.nave)
        
    def crear_asteroides(self):
        # Creamos la instancia de los Asteroides
        self.asteroides = []
        for i in range(4):
            self.asteroides.append(Asteroides(700, randint(0,372)))
            self.asteroideGroup.add(self.asteroides[i])
            self.allSprites.add(self.asteroides[i])

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
            
            # Control de movimientos nave
            if evento.type == KEYDOWN:
                if evento.key == K_UP:
                    self.nave.subir()
                if evento.key == K_DOWN:
                    self.nave.bajar()
                    
        # Control de pulsacion de teclas sostenida
        tecla_sostenida = pygame.key.get_pressed()
        
        if tecla_sostenida[K_UP]:
            self.nave.subir()
        if tecla_sostenida[K_DOWN]:
            self.nave.bajar()


    def render(self, dt):
        # Actualizamos todos los sprite del grupo
        # Hacemos la llamada del metodo update de Sprite
        self.allSprites.update(dt)
        # Pintamos los Sprite del grupo actualizados
        self.allSprites.draw(self.pantalla)
        
        # Pintar los asteroides
        

        # Actualizamos la pantalla con lo dibujado.
        # self.pantalla.flip()                
    
    def main_loop(self):
        while True:
            # tiempo_transcurrido
            dt = self.clock.tick(FPS)
            
            # Llamamos al broker de eventos
            self.manejar_eventos()
            
            # Limpia la pantalla y establece el fondo
            self.pantalla.blit(self.fondo_pantalla, (0,0))
            
            # Actualizamos y pintamos los grupos de Sprite para mostrarlos en pantalla
            self.allSprites.update(dt)
            self.allSprites.draw(self.pantalla)
            
            # Funcion para pintar la pantalla
            self.render(dt)
            
            # Actualizamos la pantalla con lo dibujado.
            pygame.display.flip()
            

if __name__ ==  '__main__':
    pygame.init()
    juego = Juego()
    juego.main_loop()

    
    # https://plataforma.keepcoding.io/courses/714386/lectures/13745010
    # MINUTO 3.08