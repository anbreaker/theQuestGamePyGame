import pygame
from pygame.locals import *
import sys
import os
from random import choice, randint
from asteroides import *
from rocket import *
from menu import *
import time

# Variables de uso global

# Definimos algunos colores
VERDE = (30, 186, 22)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (216, 229, 24)
NARANJA = (255, 124, 67)

# Fotogramas por segundo
FPS = 60

# Variables para el menu
MOSTRAR_HISTORIA = 1
COMO_JUGAR = 2
INICIAR_JUEGO = 3
SALIR = 0

# Eventos personalizados (por cada nuevo evento una bandera)
SUMA_SEGUNDO = pygame.USEREVENT
SUBIR_NIVEL = pygame.USEREVENT + 1

class Juego:
    clock = pygame.time.Clock()
    # Incializamos la puntuacion a 0
    puntuacion = 0
    # Inicializamos el cronometro a 0
    cronometro = 0
    # Numero nivel / dificultad
    nivel = 0
    

    def __init__(self):

        # Inicialización de la superficie de dibujo (display surface)
        self.display = pygame.display
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [700, 500]
        self.pantalla = pygame.display.set_mode(self.dimensiones)

        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame')
        # Inserta evento personalizado en la cola de eventos
        pygame.time.set_timer(SUMA_SEGUNDO, 1000)
        # Utilizamos para capturar cada cuanto tiempo aumentamos el nivel
        pygame.time.set_timer(SUBIR_NIVEL, 3000)
        
        # Inicializacion de la imagen de fondo de la pantalla (sin efecto alpha)
        self.fondo_pantalla = pygame.image.load('resources/images/background.png').convert()
        # Inicializacion de las fuentes de texto
        self.font = pygame.font.Font('resources/fonts/alatsi.ttf', 32)

        # Render de textos de marcadores (un surface del texto)
        self.marcador_puntos = self.font.render(str(self.puntuacion), True, VERDE)
        self.marcador_nivel = self.font.render('-', True, VERDE)
        self.marcador_cronometro = self.font.render(str(self.cronometro), True, VERDE)

        # Entidades del juego, jugadores, obstaculos..., .......................
        # Creamos la instancia del jugador
        self.nave = Rocket()
        # self.menu = Menu(opciones)

        # Creacion de grupos de Sprite
        self.naveGroup = pygame.sprite.Group()
        # Crear grupoAsteroides como pygame.sprite.Group()
        self.grupo_asteroides = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()
        # Agregamos al grupo al jugador
        self.naveGroup.add(self.nave)

        self.num_asteroides_creados = 0
        self.num_max_asteroides = 7
        self.tiempo_creacion_ultimo_Objet = FPS * 10
        self.tiempo_creacion_nuevo_Objet = FPS // 4
        self.tiempo_acutal = 0

        self.allSprites.add(self.nave)

    def crear_asteroides(self, dt):
        self.tiempo_creacion_ultimo_Objet += dt
        if self.tiempo_creacion_ultimo_Objet >= self.tiempo_creacion_nuevo_Objet:
            
            # Generacion random de tamaños por asteroide.
            dimesion_asteroide = randint(256, 1024)
            # Creamos la instancia de Asteroides
            nuevo_asteroide = Asteroides(randint(636, 840), randint(0, 436),dimesion_asteroide)
            # Generamos velocidad random para cada nuevo objeto asteroide
            nuevo_asteroide.velocidad = (randint(5, 15))
            # Agregamos al grupo de asteroides
            self.grupo_asteroides.add(nuevo_asteroide)
            # Actualizamos la bandera de tiempo para volver a contar el tiempo para la creacion de objetos...
            self.tiempo_creacion_ultimo_Objet = 0

    def salir_del_juego(self):
        pygame.quit()
        # No Olvidar pasar 0 en sys.exit(0), sin el parametro -> "Exception has occurred: SystemExit"
        sys.exit(0)

    def manejar_eventos(self):
        # Manejador de eventos, un daemon o broker a la espera llamado desde bucle principal
        for evento in pygame.event.get():
            # Sí, pulsa Salir
            if evento.type == pygame.QUIT or evento.type == KEYDOWN and evento.key == K_ESCAPE:
                self.salir_del_juego()
            if evento.type == SUMA_SEGUNDO:
                self.cronometro += 1
                print(f'Cronometro: {self.cronometro}')
            if evento.type == SUBIR_NIVEL:
                self.nivel += 1
                    

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

        # Render del textos marcadores puntos (un surface del texto)
        self.marcador_puntos = self.font.render(f'Puntuacion: {str(self.puntuacion)}', True, VERDE)
        self.marcador_nivel = self.font.render(f'Nivel {str(self.nivel)}', True, VERDE)
        self.marcador_cronometro = self.font.render(f'{str(self.cronometro)}\'s', True, AMARILLO)

        # Pintamos marcadores
        self.pantalla.blit(self.marcador_puntos, (490, 5))
        self.pantalla.blit(self.marcador_nivel, (15,5))
        self.pantalla.blit(self.marcador_cronometro, (630,450))

        # Actualizar los asteroides
        self.grupo_asteroides.update(dt)

        # Actualizamos todos los sprite del grupo
        # Hacemos la llamada del metodo update de Sprite
        self.allSprites.update(dt)
        # Pintamos todos los Sprite del grupo general actualizados
        self.grupo_asteroides.draw(self.pantalla)
        self.allSprites.draw(self.pantalla)
        
        # Actualizamos la pantalla con lo dibujado.
        pygame.display.flip()
        
        # Agrego un delay
        pygame.time.delay(10)
        

    def contador_puntos(self):
        # La puntuacion que se mostrará en marcador y con la cual se realizará el ranking de jugadores,
        # la voy a basar en la cantidad de tiempo en pantalla x el numero de asteroides creados.
        
        # self.puntuacion =
        pass

    def main_loop(self):
        contador = 0
        while True:
            # tiempo_transcurrido
            dt = self.clock.tick(FPS)
            # Control de salida de partida por desgaste de vidas
            if self.nave.vidas == 0:
                # print(f'NumVidas == 0 -> {self.nave.vidas}')
                self.salir_del_juego()

            # Llamamos al broker de eventos
            self.manejar_eventos()

            objetos_en_pantalla = len(self.grupo_asteroides)
            if objetos_en_pantalla < self.num_max_asteroides:
                self.crear_asteroides(dt)
                # print(f'Asteroides en pantalla-> {objetos_en_pantalla}')

            # No borra
            # self.nave.test_colisiones_rocket(self.grupo_asteroides)
            # Borra al elemento colisionado (saca del grupo)
            puntos = self.nave.test_colisiones_asteroides(self.grupo_asteroides)
            if self.puntuacion > 0:
                self.puntuacion -= puntos * 10
                # print(f'Puntuacon -> {self.puntuacion}')

            # Llamada a la funcion de repintado de pantalla.
            self.render(dt)
