import pygame
import sys
from ranking import *

# Variables de uso global
ANCHO = 500
FPS = 60


class Rocket(pygame.sprite.Sprite):
    pict_rocket = 'rocket.png'
    w_pict_rocket = 68
    h_pict_rocket = 40
    velocidad = 10
    vidas = 3

    # Constructor de la clase
    def __init__(self, x=0, y=(ANCHO/2)-h_pict_rocket):
        self.x = x
        self.y = y
        # Tamaño animacion nave
        self.w = 100
        self.h = 80

        # Girar la nave para aterrizar
        self.girando = False

        # Inicializamos el Sprite, (ver pygame.doc)
        pygame.sprite.Sprite.__init__(self)

        self.nave_explotando = False
        # Inicializacion de la imagen del player (es un rectangulo)
        self.image_nave = pygame.image.load(f'resources/images/{self.pict_rocket}').convert_alpha()
        self.image = self.image_nave
        # Convertimos la imagen en un rectangulo con x,y,w,h, -> devuelve (0,0,68,40)
        self.rect = self.image.get_rect()
        # Coordenadas de entrada para posicionamiento -> Pos(x,y)
        self.rect.x = x
        self.rect.y = y
        # Tamaño del "rectangulo" player, (ancho, alto)
        self.w_pict_rocket = self.rect.w
        self.h_pict_rocket = self.rect.h

        # Sonidos para el rocket
        self.sonido_vida_menos = pygame.mixer.Sound('resources/music/vida-1.wav')
        self.sonido_sin_vidas = pygame.mixer.Sound('resources/music/explosion_final.wav')

        # Preparacion de los frames
        # Alamacenamos los frames en una lista
        self.frames = []
        self.index = 0
        self.num_imagenes = 0
        self.tiempo_animacion = FPS * 2

        # Cargamos la imagen
        self.load_frames()
        self.tiempo_acutal = 0

    def subir(self):
        # Utilizando la funcion (max/min) posicionamos limites del player
        self.rect.y = max(0, self.rect.y - self.velocidad)

    def bajar(self):
        self.rect.y = min(self.rect.y + self.velocidad,ANCHO-self.h_pict_rocket)

    def test_colisiones_rocket(self, grupo_asteroides):
        # rocket choca (self), choca contra grupo que entra en la fucncion (grupo_asteroides), no saca el item del grupo (False)
        candidatos_a_colision = pygame.sprite.spritecollide(self, grupo_asteroides, False)
        if len(candidatos_a_colision) > 0:
            print(f'Colision-> {candidatos_a_colision}')
            # print(f'NumVidas->{self.vidas}')
            # self.vidas -= 1

    def test_colisiones_asteroides(self, grupo, dt, puntos):
        # rocket choca (self), choca contra grupo que entra en la fucncion (grupo_asteroides), saca al item del grupo (True)
        candidatos_a_colision = pygame.sprite.spritecollide(self, grupo, True)
        numero_candidatos = len(candidatos_a_colision)
        if numero_candidatos > 0 and self.girando == False:
            # print(f'Vidas Totales-> {self.vidas}')
            if self.vidas > 1:
                self.sonido_vida_menos.play()
            self.vidas -= 1

        if self.vidas == 0:
            # Llamada a metodo sobreescrito para animacin explosion.
            self.sonido_sin_vidas.play()
            self.update(dt)
            self.nave_explotando = True
            # print(f'Numero Vidas quedan-> {self.vidas}')
            # ranking = Ranking()
            # ranking.mostrar_ranking(puntos)
        return numero_candidatos

    def load_frames(self):
        sprite_sheet = pygame.image.load('resources/images/nave_explosion.png').convert_alpha()

        for fila in range(4):
            y = fila * self.h
            for columna in range(4):
                x = columna * self.w
                image = pygame.Surface((self.w, self.h), pygame.SRCALPHA).convert_alpha()
                image.blit(sprite_sheet, (0,0), (x, y, self.w, self.h))
                self.frames.append(image)

        self.num_imagenes = len(self.frames)
        self.image = self.frames[self.index]

    # Sobreescribimos el metodo update para las animaciones
    def update(self, dt):
        # Condicion para la sobreescritura del método
        if self.nave_explotando:
            # Para las animaciones utilizamos lo que nos devuelve el clock
            self.tiempo_acutal += dt

            # Para acelerar o disminuir las animaciones.
            if self.tiempo_acutal > self.tiempo_animacion:
                # Actualizar tiempo para empezar a contar otro item
                self.tiempo_acutal = 0
                self.index += 1

                if self.index >= self.num_imagenes:
                    self.index -= 1
                    self.nave_explotando = False

                self.image = self.frames[self.index]
        else:
            self.image = self.image_nave