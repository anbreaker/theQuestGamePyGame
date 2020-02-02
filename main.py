import pygame
from pygame.locals import *
import sys
import os
from random import choice, randint
from asteroides import *
from rocket import *
import time

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

        # Entidades del juego, jugadores, obstaculos..., .......................

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

    # Preguntar como mierda poner esto en la clae asteroides!!!!!!!!

    def crear_asteroides(self):
        # Vaciamos la lista de asteroides
        self.asteroideGroup.empty()
        self.lista_asteroides = []
        for i in range(randint(1, 11)):
            # Creamos la instancia de Asteroides
            self.asteroides = Asteroides(randint(636, 840), randint(0, 436))
            self.lista_asteroides.append(self.asteroides)

        self.asteroideGroup.add(self.lista_asteroides)
        self.allSprites.add(self.lista_asteroides)
        print(f'Numero Asteroides en pantalla -> {len(self.lista_asteroides)}')


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
        # Limpia la pantalla y establece el fondo
        self.pantalla.blit(self.fondo_pantalla, (0, 0))

        # Actualizar los asteroides
        self.asteroideGroup.update(dt)

        # Actualizamos todos los sprite del grupo
        # Hacemos la llamada del metodo update de Sprite
        self.allSprites.update(dt)
        # Pintamos todos los Sprite del grupo general actualizados
        self.allSprites.draw(self.pantalla)

        # Actualizamos la pantalla con lo dibujado.
        pygame.display.flip()

    def main_loop(self):
        contador = 0
        while True:
            # tiempo_transcurrido
            dt = self.clock.tick(FPS)

            # Llamamos al broker de eventos
            self.manejar_eventos()

            if contador == 500:  #Tiempo con el que no me ralentiza el juego... Preguntar!!
                self.crear_asteroides()
                contador = 0
            contador += 1
            
            self.nave.test_colisiones(self.asteroideGroup)

            # Llamada a la funcion de repintado de pantalla.
            self.render(dt)


if __name__ == '__main__':
    pygame.init()
    juego = Juego()
    juego.main_loop()
