import pygame
from pygame.locals import *
import sys
import os
from random import choice, randint
from asteroides import *
from rocket import *
from menu import *

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
    nivel = 1
    # Condicion de salida bucle principal
    dentro_while = True
    


    def __init__(self):

        # Inicialización de la superficie de dibujo (display surface)
        self.display = pygame.display
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [700, 500]
        self.pantalla = pygame.display.set_mode(self.dimensiones)
        
        # Carga de archivo de audio
        pygame.mixer.music.load('resources/music/FASTER2019-01-02_-_8_Bit_Menu_-_David_Renda_-_FesliyanStudios.com.mp3')
        
        # Para reproducir, con parametro de repeticion.
        # pygame.mixer.music.play(5,0)

        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame -Jugando-')
        # Inserta evento personalizado en la cola de eventos
        pygame.time.set_timer(SUMA_SEGUNDO, 1000)
        # Utilizamos para capturar cada cuanto tiempo aumentamos el nivel
        pygame.time.set_timer(SUBIR_NIVEL, 1000 * 3)
        
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
        self.planeta = Rocket()
        # self.menu = Menu(opciones)

        # Creacion de grupos de Sprite
        self.naveGroup = pygame.sprite.Group()
        # Crear grupoAsteroides como pygame.sprite.Group()
        self.grupo_asteroides = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()
        # Agregamos al grupo al jugador
        self.naveGroup.add(self.nave)

        self.num_asteroides_creados = 0
        self.num_max_asteroides = 5
        self.tiempo_creacion_ultimo_Objet = FPS * 10
        self.tiempo_creacion_nuevo_Objet = FPS // 4
        self.tiempo_actual = 0

        self.allSprites.add(self.nave)

    # Configuracion de los asteroides
    def configurar_obstaculos(self, velocidad, dimesion_asteroide):
        # Creamos la instancia de Asteroides
        nuevo_asteroide = Asteroides(randint(636, 840), randint(0, 436),dimesion_asteroide)
        # Generamos velocidad random para cada nuevo objeto asteroide
        nuevo_asteroide.velocidad = velocidad
        # Agregamos al grupo de asteroides
        self.grupo_asteroides.add(nuevo_asteroide)
        # Contador num_asteroides_creados 
        self.num_asteroides_creados += 1
        # Actualizamos la bandera de tiempo para volver a contar el tiempo para la creacion de objetos...
        self.tiempo_creacion_ultimo_Objet = 0

    # Creacion de obstaculos, (asteroides), segun nivel de partida.
    def crear_asteroides(self, dt):
        self.tiempo_creacion_ultimo_Objet += dt
        if self.tiempo_creacion_ultimo_Objet >= self.tiempo_creacion_nuevo_Objet:
            if self.nivel >= 1 and self.nivel <= 5:
                self.configurar_obstaculos(randint(10,15),randint(128, 512))
            if self.nivel > 5 and self.nivel <= 10:
                self.num_max_asteroides = 8
                self.configurar_obstaculos(randint(8,12),randint(512, 768))
            if self.nivel > 10 and self.nivel <= 15:
                self.num_max_asteroides = 12
                self.configurar_obstaculos(randint(6,8),randint(512, 768))
            if self.nivel > 15:
                self.num_max_asteroides = 12
                self.configurar_obstaculos(randint(4,7),randint(512, 1024))
            # Contar puntos partida
            self.contador_puntos()

    def contador_puntos(self):
        # La puntuacion que se mostrará en marcador y con la cual se realizará el ranking de jugadores,
        # la voy a basar en la cantidad de tiempo en pantalla + el numero de asteroides creados.
        # El juego iniciara con 10 vidas para tratar de aterrizar, cada vida menos son 10 puntos
        vidas_inicio_partida = 10
        if vidas_inicio_partida < self.nave.vidas:
            self.puntuacion = self.cronometro + self.num_asteroides_creados - (self.nave.vidas - vidas_inicio_partida) * 10
        else:
            self.puntuacion = self.cronometro + self.num_asteroides_creados
        # print(self.puntuacion)

    def aterriza_nave(self):
        if self.cronometro == 15:
            pass

    def salir_del_juego(self):
        pygame.quit()
        # No Olvidar pasar 0 en sys.exit(0), sin el parametro -> "Exception has occurred: SystemExit"
        sys.exit(0)

    def manejar_eventos(self):
        # Manejador de eventos, un daemon o broker a la espera llamado desde bucle principal
        for evento in pygame.event.get():
            # Sí, pulsa Salir
            if evento.type == pygame.QUIT:
                self.salir_del_juego()
            if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                # Para Musica
                pygame.mixer.music.stop()
                # Vuelta a Menu.
                # Para reproducir, con parametro de repeticion.
                # pygame.mixer.music.play(5,0)
                self.dentro_while = False
            if evento.type == SUMA_SEGUNDO:
                self.cronometro += 1
                # print(f'Cronometro: {self.cronometro}')
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
        self.marcador_vidas = self.font.render(f'Vidas {str(self.nave.vidas)}', True, VERDE)
        self.marcador_cronometro = self.font.render(f'{str(self.cronometro)}\'s', True, AMARILLO)

        # Pintamos marcadores
        self.pantalla.blit(self.marcador_puntos, (490, 5))
        self.pantalla.blit(self.marcador_nivel, (15,5))
        self.pantalla.blit(self.marcador_vidas, (15, 450))
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

    def main_loop(self):
        contador = 0
        while self.dentro_while:
            # tiempo_transcurrido
            dt = self.clock.tick(FPS)
            # Control de salida de partida por desgaste de vidas
            if self.nave.vidas == 0 and not self.nave.nave_explotando:
                # print(f'NumVidas == 0 -> {self.nave.vidas}')
                # self.dentro_while = False
                # ranking = Ranking()
                # ranking.mostrar_ranking(puntos)
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
            if self.nave.nave_explotando == False:
                puntos = self.nave.test_colisiones_asteroides(self.grupo_asteroides,dt,self.puntuacion)

            # Llamada a la funcion de repintado de pantalla.
            self.render(dt)
