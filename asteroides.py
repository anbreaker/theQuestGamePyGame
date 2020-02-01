import pygame

# Variables de uso global
LARGO = 700
ANCHO = 500
# Fotogramas por segundo
FPS = 60


class Asteroides(pygame.sprite.Sprite):

    # Constructor de la clase
    def __init__(self,x,y):
        self.w = 128
        self.h = 128
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
        self.frames = [] # Lista con los asteroides
        self.index = 0
        self.num_imagenes = 0
        self.tiempo_animacion = FPS
        
        self.load_frames()
        
        # Cargamos la imagen
        self.tiempo_acutal = 0
        
        
    # Recortamos los asteroides y los guardamos en una lista
    def load_frames(self):
        self.sprite_sheet = pygame.image.load('resources/images/asteroides.png').convert_alpha()

        for fila in range(8):
            y = fila * self.h
            for columna in range(8):
                x = columna * self.w

                image = pygame.Surface((self.w, self.h), pygame.SRCALPHA).convert_alpha()
                image.blit(self.sprite_sheet, (0,0), (x, y, self.w, self.h))
                self.frames.append(image)

        self.num_imagenes = len(self.frames)
        self.image = self.frames[self.index]
            
    # Sobreescribimos el metodo update para las animaciones
    def update(self, dt):
        # Para las animaciones utilizamos lo que nos devuelve el clock
        self.tiempo_acutal += dt
        
        # Para acelerar o disminuir las animaciones.
        if self.tiempo_acutal > self.tiempo_animacion:
            # Actualizar tiempo para empezar a contar otro item
            self.tiempo_acutal = 0
            self.index += 1
            
            if self.index >= self.num_imagenes:
                self.index = 0
                
            self.image = self.frames[self.index]
        
            self.rect.x -= self.velocidad
            if self.rect.x == -120:
                self.rect.x = 760                
                # Incremetamos velociadd por cada llegada al final por ver...
                # self.velocidad += 1        
                
    def crear_asteroides(self):
        self.asteroideGroup.empty()
        self.allSprites.empty()
        
        for imagen in self.frames:
            imagen = Asteroides(i*50,128)
            self.asteroideGroup.add(imagen)
        
        self.allSprites.add(self.nave)
        self.allSprites.add(self.asteroides)