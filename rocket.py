import pygame

# Variables de uso global
ANCHO = 500


class Rocket(pygame.sprite.Sprite):
    pict_rocket = 'rocket.png'
    w_pict_rocket = 68
    h_pict_rocket = 40
    velocidad = 10
    vidas = 10

    # Constructor de la clase
    def __init__(self, x=0, y=(ANCHO/2)-h_pict_rocket):
        self.x = x
        self.y = y
        # Tamaño animacion nave
        self.w = 80

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
        
        # Sonidos para el rocket
        self.sonido_vida_menos = pygame.mixer.Sound('resources/music/vida-1.wav')

    def subir(self):
        # Utilizando la funcion (max/min) posicionamos limites del player
        self.rect.y = max(0, self.rect.y - self.velocidad)

        # print(f'Subir -> {self.rect.y}')
        # if self.rect.y >= 0:
        # self.rect.y = 0

    def bajar(self):
        self.rect.y = min(self.rect.y + self.velocidad,ANCHO-self.h_pict_rocket)

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

    def test_colisiones_asteroides(self, grupo):
        # rocket choca (self), choca contra grupo que entra en la fucncion (grupo_asteroides), saca al item del grupo (True)
        candidatos_a_colision = pygame.sprite.spritecollide(self, grupo, True)
        numero_candidatos = len(candidatos_a_colision)
        if numero_candidatos > 0:
            # print(f'Vidas Totales-> {self.vidas}')
            self.sonido_vida_menos.play()            
            self.vidas -= 1
            # print(f'Numero Vidas quedan-> {self.vidas}')
        return numero_candidatos

    # Recortamos los asteroides y los guardamos en una lista
    def load_frames(self):
        self.sprite_sheet = pygame.transform.scale((pygame.image.load('resources/images/rocket_explosion.png').convert_alpha()),(dimension,dimension))
        
        for fila in range(8):
            x = fila * self.w

            frame_nave = pygame.Surface((self.w, self.h), pygame.SRCALPHA).convert_alpha()
            # frame_asteroide_reescalado = pygame.transform.scale((frame_asteroide),(dimension,dimension))
            frame_nave.blit(self.sprite_sheet, (0, 0), (x, y, self.w, self.h))
            self.frames.append(frame_nave)

        self.num_imagenes = len(self.frames)
        print(self.num_imagenes)
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