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
    # Incializamos la puntuacion a 0
    puntuacion = 50

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
        # Inicializacion de las fuentes de texto
        self.font = pygame.font.Font('resources/fonts/alatsi.ttf', 32)
        # Render del texto de marcador_puntos (un surface del texto)
        self.marcador_puntos = self.font.render(str(self.puntuacion), True, VERDE)
        # Render del texto de marcador_vidas (un surface del texto)
        self.marcador_vidas = self.font.render('-', True, VERDE)

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
        
        # Render del texto (un surface del texto)
        self.marcador_puntos = self.font.render(str(self.puntuacion), True, VERDE)
        # Pintamos el marcador_puntos
        self.pantalla.blit(self.marcador_puntos, (650,5))
        
        # Render del texto (un surface del texto)
        self.marcador_vidas = self.font.render(str(self.puntuacion), True, VERDE)
        # Pintamos el marcador_vidas
        self.pantalla.blit(self.marcador_vidas, (15,5))

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
            
            # Control de salida de partida por desgaste de vidas
            if self.nave.vidas == 0:
                print(f'NumVidas == 0 -> {self.nave.vidas}')
                self.game_over()

            # Llamamos al broker de eventos
            self.manejar_eventos()

            if contador == 500:  #Tiempo con el que no me ralentiza el juego... Preguntar!!
                self.crear_asteroides()
                contador = 0
            contador += 1
            
            # No borra
            # self.nave.test_colisiones_rocket(self.asteroideGroup)
            # Borra al elemento colisionado (saca del grupo)
            puntos = self.nave.test_colisiones_asteroides(self.asteroideGroup)
            if self.puntuacion > 0:
                self.puntuacion -= puntos * 10
                print(f'Puntuacon -> {self.puntuacion}')

            # Llamada a la funcion de repintado de pantalla.
            self.render(dt)


if __name__ == '__main__':
    pygame.init()
    juego = Juego()
    juego.main_loop()
    
    # link: "https://plataforma.keepcoding.io/courses/714386/lectures/13765431"
    # min:  2.26
