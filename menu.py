import pygame
import sys
from pygame.locals import *

AMARILLO = (216, 229, 24)
NARANJA = (255, 124, 67)


class Menu():
    # Constructor de la clase Menu
    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font('resources/fonts/alatsi.ttf', 32)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def opcion_elegida(self):
        # Altera el valor de 'self.seleccionado' con las flechas up/down

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                print ("Selecciona la opción '%s'." %(titulo))
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def mostrar_sms(self, pantalla):
        # Imprime sobre 'pantalla' el texto de cada opción del menú.

        total = self.total
        indice = 0
        altura_de_opcion = 40
        pos_texto_pantalla_x = 205
        pos_texto_pantalla_y = 125
        
        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = NARANJA
            else:
                color = AMARILLO

            texto_pantalla = self.font.render(titulo, 1, color)
            posicion_pantalla = (pos_texto_pantalla_x, pos_texto_pantalla_y + altura_de_opcion * indice)
            indice += 1
            pantalla.blit(texto_pantalla, posicion_pantalla)


def mostrar_historia():
    print ('Función que muestra un nuevo juego.')

def mostrar_como_jugar():
    print ('Función que muestra otro menú de opciones.')

def creditos():
    print ('Función que muestra los creditos del programa.')

def juego():
    print ('Juego...')

def salir_del_juego():
    print ('Gracias por jugar a The Quest.')
    sys.exit(0)


if __name__ == '__main__':
    
    salir_del_menu = False
    opciones = [
        ('Mostrar Historia del juego', mostrar_historia),
        ('Como jugar', mostrar_como_jugar),
        ('Creditos', creditos),
        ('Jugar a The Quest', juego),
        ('Salir', salir_del_juego)
    ]

    pygame.font.init()
    pantalla = pygame.display.set_mode((700, 500))
    fondo_pantalla = pygame.image.load('resources/images/background.png').convert()
    # Titulo de la barra de la aplicacion
    pygame.display.set_caption('The Quest Juego pyGame')
    menu = Menu(opciones)

    while not salir_del_menu:

        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir = True

        pantalla.blit(fondo_pantalla, (0, 0))
        menu.opcion_elegida()
        menu.mostrar_sms(pantalla)

        pygame.display.flip()
        pygame.time.delay(10)    