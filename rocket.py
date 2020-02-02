import pygame

# Variables de uso global
ANCHO = 500


class Rocket(pygame.sprite.Sprite):
    pict_rocket = 'rocket.png'
    w_pict_rocket = 68
    h_pict_rocket = 40
    velocidad = 10
    vidas = 5

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

        # print(f'Subir -> {self.rect.y}')
        # if self.rect.y >= 0:
        # self.rect.y = 0

    def bajar(self):
        self.rect.y = min(self.rect.y + self.velocidad, ANCHO-self.h_pict_rocket)

        # print(f'Bajar -> {self.rect.y}')
        # if self.rect.y >= 0:
        # self.rect.y = 0
        
        
    def test_colisiones_rocket(self, grupo_asteroides):
        # rocket choca (self), choca contra grupo que entra en la fucncion (grupo_asteroides), no saca el item del grupo (False)
        candidatos_a_colision = pygame.sprite.spritecollide(self, grupo_asteroides, False)
        if len(candidatos_a_colision) > 0:
            print(f'Colision-> {candidatos_a_colision}')
            # print(f'NumVidas->{self.vidas}')
            # self.vidas -= 1
            
    def test_colisiones_asteroides (self, grupo):
        # rocket choca (self), choca contra grupo que entra en la fucncion (grupo_asteroides), saca al item del grupo (True)
        candidatos_a_colision =pygame.sprite.spritecollide(self, grupo, True)
        numero_candidatos = len(candidatos_a_colision)
        if numero_candidatos > 0:
            print(f'Vidas Totales->{self.vidas}')
            self.vidas -= 1
            print(f'Numero Vidas quedan->{self.vidas}')
        return numero_candidatos
