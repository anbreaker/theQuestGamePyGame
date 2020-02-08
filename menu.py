import pygame
from pygame.locals import *
import sys
import os
from mostrar_info import *


AMARILLO = (216, 229, 24)
NARANJA = (255, 124, 67)


class Menu():
    # Constructor de la clase Menu
    def __init__(self):
        pygame.font.init()
        self.pantalla = pygame.display.set_mode((700, 500))
        self.fondo_pantalla = pygame.image.load('resources/images/background.png').convert()
        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame')

        self.opciones = [
            ('· Mostrar Historia del juego', mostrar_historia),
            ('· Como jugar', mostrar_como_jugar),
            ('· Jugar a The Quest', iniciar_juego),
            ('· Acerca de:', acerca_de),
            ('· Salir', salir_del_juego)
        ]
        self.font = pygame.font.Font('resources/fonts/alatsi.ttf', 32)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False
        
        # Instancia de Juego.
        self.juego = Juego() 
           

    def opcion_elegida(self):
        # Altera el valor de 'self.seleccionado' con las flechas up/down
        tecla_pulsada = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if tecla_pulsada[K_UP]:
                self.seleccionado -= 1
            elif tecla_pulsada[K_DOWN]:
                self.seleccionado += 1
            elif tecla_pulsada[K_RETURN]:
                # Llamamos a la función asociada a las opciones.
                linea_menu, funcion = self.opciones[self.seleccionado]
                print(f'Opción seleccionada del menu-> {linea_menu}')
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = tecla_pulsada[K_UP] or tecla_pulsada[K_DOWN] or tecla_pulsada[K_RETURN]

    def mostrar_sms(self, pantalla):
        # Imprime sobre 'pantalla' el texto de cada opción del menú.

        total = self.total
        indice = 0
        altura_de_opcion = 40
        pos_texto_pantalla_x = 105
        pos_texto_pantalla_y = 125

        for (linea_menu, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = NARANJA
            else:
                color = AMARILLO

            texto_pantalla = self.font.render(linea_menu, 1, color)
            posicion_pantalla = (
                pos_texto_pantalla_x, pos_texto_pantalla_y + altura_de_opcion * indice)
            indice += 1
            pantalla.blit(texto_pantalla, posicion_pantalla)

    def render_menu(self):

        pantalla = pygame.display.set_mode((700, 500))
        fondo_pantalla = pygame.image.load('resources/images/background.png').convert()
        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame')

    def main_loop_menu(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    print(f'tecla-> {evento.key}')
                    salir_del_juego()

            self.pantalla.blit(self.fondo_pantalla, (0, 0))
            self.opcion_elegida()
            self.mostrar_sms(self.pantalla)

            pygame.display.flip()
            pygame.time.delay(10)


def mostrar_historia():
    print('Función que muestra un nuevo juego.')
    historia = Historia()
    historia.mostrar_historia()


def mostrar_como_jugar():
    print('Función que muestra otro menú de opciones.')
    historia = Historia()
    historia.como_jugar()
    
def iniciar_juego():
    print('Inicio del Juego...')
    # Instancia de Juego.
    juego = Juego() 
    juego.main_loop()


def acerca_de():
    print('Función que muestra acerca_de.')
    historia = Historia()
    historia.acerca_de()


def salir_del_juego():
    print('Gracias por jugar a The Quest.')
    pygame.quit()
    sys.exit(0)


# Main de pruebas rapido
if __name__ == '__main__':
    menu = Menu()
    menu.main_loop_menu()