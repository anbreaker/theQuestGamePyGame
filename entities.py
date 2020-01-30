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

    def __init__(self, x=0, y=(ANCHO/2)-h_pict_rocket):
        self.x = x
        self.y = y
        
        # Obtiene el rectangulo (preguntar bien que hace)
        pygame.sprite.Sprite.__init__(self)
        
        # Inicializacion de la imagen del player (es un rectangulo)
        self.image = pygame.image.load(f'resources/{self.pict_rocket}').convert_alpha()
        # Convertimos la imagen en un rectangulo con w,h, -> devuelve (0,0,68,40)
        self.rect = self.image.get_rect()
        # Coordenadas de entrada para posicionamiento -> Pos(x,y)
        self.rect.x = x
        self.rect.y = y
        
    def subir(self):
        self.rect.y = max(0, self.rect.y - self.velocidad)
        print(f'Subir -> {self.rect.y}')
        # if self.rect.y >= 0:
            # self.rect.y = 0
        
    def bajar(self):    
        print(f'Bajar -> {self.rect.y}')
        self.rect.y = min(self.rect.y + self.velocidad, 460)
        # if self.rect.y >= 0:
            # self.rect.y = 0

