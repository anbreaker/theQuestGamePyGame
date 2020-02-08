import pygame
from juego_niveles import *

# Variables de uso global
ANCHO = 500
LARGO = 700

# Definicion tamaños de textos
ALTO_TEXTO_TITULOS = 30
ALTO_TEXTO_DESCRIPCIONES = 22

# Definimos algunos colores
VERDE = (30, 186, 22)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (216, 229, 24)

# Fotogramas por segundo
FPS = 60

class Historia():
    
    def mostrar_historia(self):
        # Inicialización de la superficie de dibujo (display surface)
        self.display = pygame.display
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [700, 500]
        self.pantalla = pygame.display.set_mode((700,500))

        # Inicializacion de la imagen de fondo de la pantalla (sin efecto alpha)
        self.fondo_pantalla = pygame.image.load('resources/images/background.png').convert()

        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('The Quest Juego pyGame')
        
        # Limpia la pantalla y coloca el fondo
        self.pantalla.blit(self.fondo_pantalla, (0, 0))

        # Fuente para el texto que aparecerá en pantalla (tamaño 30 y 22)
        self.fuente_titulo = pygame.font.Font('resources/fonts/alatsi.ttf', ALTO_TEXTO_TITULOS)
        self.fuente_descripciones = pygame.font.Font('resources/fonts/alatsi.ttf', ALTO_TEXTO_DESCRIPCIONES)
        
        # Devuelve la altura en píxeles para distancia "ideal" entre líneas de texto con la fuente.
        self.fd_linesize = self.fuente_descripciones.get_linesize()

        # Gestionamos como de rápido actualiza la pantalla
        self.reloj = pygame.time.Clock()

        # Introduccion al juego:
        # Texto por lineas y posicion en pantalla
        self.linea_texto1 = self.fuente_descripciones.render('Historia del juego:', True, BLANCO)
        self.pantalla.blit(self.linea_texto1, [10, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize])

        self.linea_texto2 = self.fuente_descripciones.render('La búsqueda comienza en un planeta tierra moribundo por el cambio', True, BLANCO)
        self.pantalla.blit(self.linea_texto2, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 2])
        
        self.linea_texto3 = self.fuente_descripciones.render('climático. Partiremos a la búsqueda de un planeta compatible ', True, BLANCO)
        self.pantalla.blit(self.linea_texto3, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 3])
        
        self.linea_texto4 = self.fuente_descripciones.render('con la vida humana para colonizarlo. Esquiva los obstaculos,', True, BLANCO)
        self.pantalla.blit(self.linea_texto4, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 4])

        self.linea_texto5 = self.fuente_descripciones.render('hazte con el control de la nave y logra aterrizar!', True, BLANCO)
        self.pantalla.blit(self.linea_texto5, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 5])

        # Texto por lineas y posicion en pantalla, (footer)
        self.linea_footer = self.fuente_titulo.render('Click derecho para continuar', True, AMARILLO)
        # Para centrar el texto mido su tamaño con esta funcion que devuelve w,h
        self.ancho_linea_footer = self.linea_footer.get_rect().width
        # Calculo del posicionamiento de linea_texto1
        self.alineacion_izquierda = (LARGO - self.ancho_linea_footer -10)
        # Presentacion del texto en pantalla
        self.pantalla.blit(self.linea_footer, [self.alineacion_izquierda, ANCHO - 50])

        # Limitamos a 20 fotogramas por segundo.
        # reloj.tick(20)

        # Actualizamos la pantalla con lo dibujado.
        pygame.display.flip()                

        self.main_loop_mostrar_info()
    
    def main_loop_mostrar_info(self):
        # Bucle Principal del Programa y condicion de salida del bucle
        self.salir = False
        while not self.salir:
            juego = Juego()
            juego.manejar_eventos()
            for evento in pygame.event.get():  # El usuario hace algo
                if evento.type == pygame.QUIT:  # Si el usuario hace click en cerrar
                    self.salir = True

        # Para salir correctamente de la aplicacion y cierre todos los procesos
        pygame.quit()


# Main de pruebas rapido
if __name__ == '__main__':
    # Inicialización de Pygame
    pygame.init()
    historia = Historia()
    historia.mostrar_historia()