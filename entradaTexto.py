import pygame
from pygame.locals import *
import sys

# Variables de uso global
ANCHO = 500
LARGO = 700

# Definicion tamaños de textos
ALTO_TEXTO_TITULOS = 30

# Definimos algunos colores
VERDE = (30, 186, 22)
AMARILLO = (216, 229, 24)
NARANJA = (245, 150, 34)

class Entrada():

    def __init__(self):
        pygame.font.init()
        # Inicialización de la superficie de dibujo (display surface)
        self.display = pygame.display
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [LARGO, ANCHO]
        self.pantalla = pygame.display.set_mode(self.dimensiones)
        # Inicializacion de la imagen de fondo de la pantalla (sin efecto alpha)
        self.fondo_pantalla = pygame.image.load('resources/images/background.png').convert()
        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame -Hall of Fame-')
        # Fuente para el texto que aparecerá en pantalla (tamaño 30 y 22)
        self.fuente_titulo = pygame.font.Font('resources/fonts/alatsi.ttf', 32)

        self.caracteres = ['']
        self.font = pygame.font.Font('resources/fonts/alatsi.ttf', 84)
        self.distancia = 76
        self.pos_x = 285
        self.pos_y = 100
        self.max_caracteres = 0

    def teclas(self, eventos):
            for evento in eventos:
                if evento.type == KEYDOWN:
                    if evento.key == K_RETURN:
                        self.caracteres.append('')
                        self.lineas += 1
                    elif evento.key == K_ESCAPE:
                        self.salir = True
                    elif evento.key == K_BACKSPACE:
                        if self.caracteres[self.lineas] == '' and self.lineas > 0:
                            self.caracteres = self.caracteres[0:-1]
                            self.lineas -= 1
                        else:
                            self.caracteres[self.lineas] = self.caracteres[self.lineas][0:-1]
                            if self.max_caracteres > 0:
                                self.max_caracteres -= 1
                                # print(f'Max_car -> {self.max_caracteres}')
                    else:
                        if self.max_caracteres < 3:
                            self.caracteres[self.lineas] = str(self.caracteres[self.lineas] + evento.unicode)
                            # print(f'Max_car -> {self.max_caracteres}')
                            self.max_caracteres += 1
                        if self.max_caracteres == 3 and evento.key == K_SPACE:
                            print(f'nick... {self.caracteres}')
                            self.salir = True
                            return self.caracteres

    def mensaje(self, superficie):
        # Limpia la pantalla y coloca el fondo
        self.pantalla.blit(self.fondo_pantalla, (0, 0))
        for self.lineas in range(len(self.caracteres)):
            nick = self.font.render(self.caracteres[self.lineas], True, VERDE)
            superficie.blit(nick, (self.pos_x, self.pos_y + self.distancia))

        # Texto por lineas y posicion en pantalla, (footer)
        self.linea_nick = self.fuente_titulo.render('Escribe tu nick de tres caracteres:', True, NARANJA)
        # Para alinear el texto mido su tamaño con esta funcion que devuelve w,h
        self.ancho_linea_nick = self.linea_nick.get_rect().width
        # Calculo del posicionamiento de ancho_linea_footer
        self.alineacion_derecha = (LARGO / 4 - (self.ancho_linea_nick / 4))
        # Presentacion del texto en pantalla
        self.pantalla.blit(self.linea_nick, [self.alineacion_derecha, 100])

        self.linea_footer = self.fuente_titulo.render('Pulsa "Espacio" para guardar y volver al Menú', True, AMARILLO)
        # Para alinear el texto mido su tamaño con esta funcion que devuelve w,h
        self.ancho_linea_footer = self.linea_footer.get_rect().width
        # Calculo del posicionamiento de ancho_linea_footer
        self.alineacion_izquierda = (LARGO - self.ancho_linea_footer -10)
        # Presentacion del texto en pantalla
        self.pantalla.blit(self.linea_footer, [self.alineacion_izquierda, ANCHO - 50])

    def entrada_texto_loop(self):
        salir = True
        entrar_texto = Entrada()

        while salir:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    self.salir = True

            # iniciales sera None siempre y cuando no se haya llegado al final de la introducción de 3 caracteres, 
            iniciales = entrar_texto.teclas(eventos)
            if iniciales is not None:
                print(f'Las Iniciales -> {iniciales}')
                salir = False
            entrar_texto.mensaje(self.pantalla)
            pygame.display.update()

        return iniciales

