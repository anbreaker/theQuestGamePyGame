import pygame

# Variables de uso global
LARGO = 700
ANCHO = 500
# Fotogramas por segundo
FPS = 60


class Rocket(pygame.sprite.Sprite):
    pict_rocket = 'rocket.png'
    w_pict_rocket = 68
    h_pict_rocket = 40
    velocidad = 10

    # Constructor de la clase
    def __init__(self, x=0, y=(ANCHO/2)-h_pict_rocket):
        self.x = x
        self.y = y
        
        # Inicializamos el Sprite, (ver pygame.doc)
        pygame.sprite.Sprite.__init__(self)
        
        # Inicializacion de la imagen del player (es un rectangulo)
        self.image = pygame.image.load(f'resources/images/{self.pict_rocket}').convert_alpha()
        # Convertimos la imagen en un rectangulo con x,y,w,h, -> devuelve (0,0,68,40)
        self.rect = self.image.get_rect()
        # Coordenadas de entrada para posicionamiento -> Pos(x,y)
        self.rect.x = x
        self.rect.y = y
        # Tamaño del "rectangulo" player, (ancho, alto)
        self.w_pict_rocket = self.rect.w
        self.h_pict_rocket = self.rect.h
        
    def subir(self):
        # Utilizando la funcion (max/min) posicionamos limites del player
        self.rect.y = max(0, self.rect.y - self.velocidad)
        print(f'Subir -> {self.rect.y}')
        # if self.rect.y >= 0:
            # self.rect.y = 0
        
    def bajar(self):    
        self.rect.y = min(self.rect.y + self.velocidad, ANCHO-self.h_pict_rocket)
        print(f'Bajar -> {self.rect.y}')
        # if self.rect.y >= 0:
            # self.rect.y = 0

class Asteroides(pygame.sprite.Sprite):

    # Constructor de la clase
    def __init__(self):
        self.w = 128
        self.h = 128
        self.velocidad = 5
        pict_asteroides = 'asteroides.png'

        # Inicializamos el Sprite, (ver pygame.doc)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.w, self.h), pygame.SRCALPHA, 32)
        # Inicializacion de la imagen de los asteroides (es un rectangulo)
        self.image = pygame.image.load(f'resources/images/{self.pict_asteroides}').convert_alpha()
        # Convertimos la imagen en un rectangulo con x,y,w,h, -> devuelve (0,0,68,40)
        self.rect = self.image.get_rect()
        # Coordenadas de entrada para posicionamiento -> Pos(x,y)
        self.rect.x = x
        self.rect.y = y
        # Tamaño del "rectangulo" player, (ancho, alto)
        self.w_pict_asteroides = self.rect.w
        self.h_pict_asteroides = self.rect.h
        
        # Preparacion de los frames
        # Alamacenamos los frames en una lista
        self.frames = [] # Lista con los asteroides
        self.index = 0
        self.num_imagenes = 0
        self.tiempo_animacion = FPS 
        
        # Cargamos la imagen
        self.load_frames()
        self.tiempo_acutal = 0
        
        
        # Recortamos los asteroides y los guardamos en una lista
        def load_frames(self):
            sprite_sheet = pygame.image.load('resources/asteroides.png').convert_alpha()

            for fila in range(4):
                y = fila * self.h
                for columna in range(4):
                    x = columna * self.w

                    image = pygame.Surface((self.w, self.h), pygame.SRCALPHA).convert_alpha()
                    image.blit(self.sprite_sheet, (0,0), (x, y, self.w, self.h))
                    self.frames.append(image)

            self.num_imagenes = len(self.frames)
            self.image = self.frames[self.index]
            
        