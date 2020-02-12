import pygame
from pygame.locals import *
import sys

VERDE = (30, 186, 22)

class Entrada():

    def __init__(self):
        pygame.font.init()
        self.caracteres = ['']
        self.fuente = pygame.font.Font(None, 38)
        self.distancia = 28
        self.pos_x = 300
        self.pos_y = 200
        self.max_caracteres = 0
    def teclas(self, evento):
        
        for accion in evento:
            if accion.type == KEYDOWN:                
                if accion.key == K_ESCAPE:
                    sys.exit(0)
                else:
                    if self.max_caracteres < 3:
                        self.caracteres[0] = str(self.caracteres[0] + accion.unicode)
                        self.max_caracteres += 1

    def mensaje(self, superficie):
        superficie.fill((0, 0, 0))
        for self.lineas in range(len(self.caracteres)):
            nick = self.fuente.render(self.caracteres[self.lineas], True, VERDE)
            superficie.blit(nick, (self.pos_x, self.pos_y + self.distancia))


def entrada_texto():
    pantalla = pygame.display.set_mode((700, 500))
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
    