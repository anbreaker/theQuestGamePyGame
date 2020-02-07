import pygame
from random import choice, randint

# Variables de uso global
LARGO = 700
ANCHO = 500
# Fotogramas por segundo
FPS = 60


class Asteroides(pygame.sprite.Sprite):

    # Constructor de la clase
    def __init__(self, x, y,dimesion):
        # La dimension la paso al instanciar el objeto y la divido por el num de imagenes de la composicion.
        self.w = dimesion / 8
        self.h = dimesion / 8
        self.velocidad = 5

        # Inicializamos el Sprite, (ver pygame.doc)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((self.w, self.h), pygame.SRCALPHA, 32) 
        # Inicializacion de la imagen de los asteroides (es un rectangulo)
        # Convertimos la imagen en un rectangulo con x,y,w,h, -> devuelve (0,0,68,40)
        self.rect = self.image.get_rect()
        # Coordenadas de entrada para posicionamiento -> Pos(x,y)
        self.rect.x = x
        self.rect.y = y
        # Tamaño del "rectangulo" player, (ancho, alto)
        # self.w_pict_asteroides = self.rect.w
        # self.h_pict_asteroides = self.rect.h

        # Preparacion de los frames
        # Alamacenamos los frames en una lista
        self.frames = []  # Lista con los asteroides
        self.index = 0
        self.num_imagenes = 0
        self.tiempo_animacion = FPS

        # Cargamos la imagen
        self.load_frames(dimesion)

        self.tiempo_acutal = 0

    # Recortamos los asteroides y los guardamos en una lista
    def load_frames(self,dimension):
        self.sprite_sheet = pygame.transform.scale((pygame.image.load('resources/images/asteroides_128.png').convert_alpha()),(dimension,dimension))
        
        for fila in range(8):
            y = fila * self.h
            for columna in range(8):
                x = columna * self.w

                frame_asteroide = pygame.Surface((self.w, self.h), pygame.SRCALPHA).convert_alpha()
                # frame_asteroide_reescalado = pygame.transform.scale((frame_asteroide),(dimension,dimension))
                frame_asteroide.blit(self.sprite_sheet, (0, 0), (x, y, self.w, self.h))
                
                self.frames.append(frame_asteroide)

        self.num_imagenes = len(self.frames)
        self.image = self.frames[self.index]


    # Sobreescribimos el metodo update para las animaciones
    def update(self, dt):
        # Para las animaciones utilizamos lo que nos devuelve el clock
        self.tiempo_acutal += dt
        # print(f'tiempo_acutal -> {self.tiempo_acutal}')
        # Para acelerar o disminuir las animaciones.
        if self.tiempo_acutal > self.tiempo_animacion:
            # Actualizar tiempo para empezar a contar otro item
            self.tiempo_acutal = 0
            
            self.index += 1

            if self.index >= self.num_imagenes:
                self.index = 0

            self.image = self.frames[self.index]

            self.rect.x -= self.velocidad
            
            if self.rect.x <= - self.w: # Al salir del ancho de pantalla
                self.kill() # Remueve la instancia de cualquier grupo (los saca del grupo)
                del self # destruye la instancia del objeto de memoria (es decir borra la instancia del asteroide
