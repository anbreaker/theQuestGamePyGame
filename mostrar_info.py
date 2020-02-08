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
NARANJA = (245, 150, 34)

# Fotogramas por segundo
FPS = 60

class Historia():
    # Constructor de la clase Menu
    def __init__(self):
        pygame.font.init()
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

    def mostrar_historia(self):

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
        self.linea_footer = self.fuente_titulo.render('Pulsa "Escape" para volver al Menu', True, AMARILLO)
        # Para alinear el texto mido su tamaño con esta funcion que devuelve w,h
        self.ancho_linea_footer = self.linea_footer.get_rect().width
        # Calculo del posicionamiento de ancho_linea_footer
        self.alineacion_izquierda = (LARGO - self.ancho_linea_footer -10)
        # Presentacion del texto en pantalla
        self.pantalla.blit(self.linea_footer, [self.alineacion_izquierda, ANCHO - 50])

        # Limitamos a 20 fotogramas por segundo.
        # reloj.tick(20)

        # Actualizamos la pantalla con lo dibujado.
        pygame.display.flip()                

        self.main_loop_mostrar_info()

    def como_jugar(self):

        # Introduccion al juego:
        # Texto por lineas y posicion en pantalla
        self.linea_texto1 = self.fuente_titulo.render('Dinamica del juego, que hacer:', True, VERDE)
        self.pantalla.blit(self.linea_texto1, [10, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize])

        self.linea_texto2 = self.fuente_descripciones.render('Utiliza las teclas de control arriba (↑) o abajo (↓) del teclado', True, BLANCO)
        self.pantalla.blit(self.linea_texto2, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 3])
        
        self.linea_texto3 = self.fuente_descripciones.render('para desplazar la nave y esquivar asteroides!.', True, BLANCO)
        self.pantalla.blit(self.linea_texto3, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 4])

        self.linea_texto5 = self.fuente_descripciones.render('Aguanta todo lo posible, controla el tiempo y el nivel', True, BLANCO)
        self.pantalla.blit(self.linea_texto5, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 6])
        
        self.linea_texto5 = self.fuente_descripciones.render('de dificultad con los marcadores.', True, BLANCO)
        self.pantalla.blit(self.linea_texto5, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 7])
      
        self.linea_texto5 = self.fuente_descripciones.render('Hazte con el control de la nave durante el tiempo necesario y aterriza!', True, BLANCO)
        self.pantalla.blit(self.linea_texto5, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 9])

        # Texto por lineas y posicion en pantalla, (footer)
        self.linea_footer = self.fuente_titulo.render('Pulsa "Escape" para volver al Menu', True, AMARILLO)
        # Para alinear el texto mido su tamaño con esta funcion que devuelve w,h
        self.ancho_linea_footer = self.linea_footer.get_rect().width
        # Calculo del posicionamiento de ancho_linea_footer
        self.alineacion_izquierda = (LARGO - self.ancho_linea_footer -10)
        # Presentacion del texto en pantalla
        self.pantalla.blit(self.linea_footer, [self.alineacion_izquierda, ANCHO - 50])

        # Limitamos a 20 fotogramas por segundo.
        # reloj.tick(20)

        # Actualizamos la pantalla con lo dibujado.
        pygame.display.flip()                

        self.main_loop_mostrar_info()
        
    def acerca_de(self):

        # Texto por lineas y posicion en pantalla, (Titulo)
        self.linea_titulo1 = self.fuente_titulo.render('Proyecto fin Bootcamp,', True, NARANJA)
        # Para alinear el texto mido su tamaño con esta funcion que devuelve w,h
        self.ancho_linea_titulo1 = self.linea_titulo1.get_rect().width
        # Calculo del posicionamiento de ancho_linea_footer
        self.alineacion_centrada = (LARGO / 2 - (self.ancho_linea_titulo1 /2))
        # Presentacion del texto en pantalla
        self.pantalla.blit(self.linea_titulo1, [self.alineacion_centrada, 70])
        
        
        # Texto por lineas y posicion en pantalla, (Titulo)
        self.linea_titulo2 = self.fuente_titulo.render('Aprender a programar desde cero', True, NARANJA)
        # Para alinear el texto mido su tamaño con esta funcion que devuelve w,h
        self.ancho_linea_titulo2 = self.linea_titulo2.get_rect().width
        # Calculo del posicionamiento de ancho_linea_footer
        self.alineacion_centrada = (LARGO / 2 - (self.ancho_linea_titulo2 /2))
        # Presentacion del texto en pantalla
        self.pantalla.blit(self.linea_titulo2, [self.alineacion_centrada, self.fd_linesize * 4])
        
        
        self.linea_texto1 = self.fuente_descripciones.render('Autor del juego: Francisco Javier Antúnez Durán', True, BLANCO)
        self.pantalla.blit(self.linea_texto1, [62, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 5])
        
        self.linea_texto1 = self.fuente_descripciones.render('Tecnologia empleada, Python 3.7 libreria pyGame 1.9.3', True, BLANCO)
        self.pantalla.blit(self.linea_texto1, [62, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 6])
       
        self.linea_texto1 = self.fuente_descripciones.render('Fecha: 23-02-2020', True, BLANCO)
        self.pantalla.blit(self.linea_texto1, [62, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 7])

        self.linea_texto1 = self.fuente_descripciones.render('Tutor del proyecto: Ramón Maldonado', True, BLANCO)
        self.pantalla.blit(self.linea_texto1, [62, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 8])




        # Texto por lineas y posicion en pantalla, (footer)
        self.linea_footer = self.fuente_titulo.render('Pulsa "Escape" para volver al Menu', True, AMARILLO)
        # Para alinear el texto mido su tamaño con esta funcion que devuelve w,h
        self.ancho_linea_footer = self.linea_footer.get_rect().width
        # Calculo del posicionamiento de ancho_linea_footer
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
        while True:
            for evento in pygame.event.get():  # El usuario hace algo
                # Si el usuario hace click en cerrar
                if evento.type == pygame.QUIT:
                    juego = Juego()
                    juego.salir_del_juego()
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    menu = Menu()
                    menu.main_loop_menu()
                    

        # Para salir correctamente de la aplicacion y cierre todos los procesos
        pygame.quit()


# Main de pruebas rapido
if __name__ == '__main__':
    # Inicialización de Pygame
    pygame.init()
    historia = Historia()
    # historia.mostrar_historia()
    historia.acerca_de()
    # menu = Menu()
    # menu.main_loop_menu()