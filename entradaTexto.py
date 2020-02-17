import pygame
from pygame.locals import *
import sys

VERDE = (30, 186, 22)

class Entrada():

    def __init__(self):
        pygame.font.init()
        self.pantalla = pygame.display.set_mode((700, 500))
        self.fondo_pantalla = pygame.image.load('resources/images/background.png').convert()
        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame -Hall of Fame-')
                
        self.caracteres = ['']
        self.font = pygame.font.Font('resources/fonts/alatsi.ttf', 32)
        self.distancia = 28
        self.pos_x = 300
        self.pos_y = 200
        self.max_caracteres = 0

    def teclas(self, evento):
            for accion in evento:
                if accion.type == KEYDOWN:
                    if accion.key == K_RETURN:
                        self.caracteres.append('')
                        self.lineas += 1
                    elif accion.key == K_ESCAPE:
                        sys.exit(0)
                    elif accion.key == K_BACKSPACE:
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
                            self.caracteres[self.lineas] = str(self.caracteres[self.lineas] + accion.unicode)
                            # print(f'Max_car -> {self.max_caracteres}')
                            self.max_caracteres += 1

    def mensaje(self, superficie):
        # superficie.fill((0, 0, 0))
        self.pantalla.blit(self.fondo_pantalla, (0, 0))
        for self.lineas in range(len(self.caracteres)):
            nick = self.font.render(self.caracteres[self.lineas], True, VERDE)
            superficie.blit(nick, (self.pos_x, self.pos_y + self.distancia))


def entrada_texto():
    pantalla = pygame.display.set_mode((700, 500))
    fondo_pantalla = pygame.image.load('resources/images/background.png').convert()
    pygame.display.set_caption('Escribir en pygame')
    salir = False

    entrar_texto = Entrada()

    while not salir:
        eventos = pygame.event.get()
        for accion in eventos:
            if accion.type == pygame.QUIT:
                salir = True

        entrar_texto.teclas(eventos)
        entrar_texto.mensaje(pantalla)
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    entrada_texto()
    