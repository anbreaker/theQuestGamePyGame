import pygame
import sqlite3
from menu import *
from juego_niveles import *

# Definicion tamaños de textos
ALTO_TEXTO_TITULOS = 30
ALTO_TEXTO_DESCRIPCIONES = 22

# Definimos algunos colores
VERDE = (30, 186, 22)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (216, 229, 24)
NARANJA = (245, 150, 34)

class Ranking():
    # Constructor de la clase Menu
    # Para implementar las llamadas a la BBDD
    # ranking = Ranking()
    # ranking.mostrar_ranking()


    # Constructor de la clase Ranking
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
        pygame.display.set_caption('The Quest Juego pyGame -Ranking-')
        
        # Limpia la pantalla y coloca el fondo
        self.pantalla.blit(self.fondo_pantalla, (0, 0))

        # Fuente para el texto que aparecerá en pantalla (tamaño 30 y 22)
        self.fuente_titulo = pygame.font.Font('resources/fonts/alatsi.ttf', ALTO_TEXTO_TITULOS)
        self.fuente_descripciones = pygame.font.Font('resources/fonts/alatsi.ttf', ALTO_TEXTO_DESCRIPCIONES)
        
        # Devuelve la altura en píxeles para distancia "ideal" entre líneas de texto con la fuente.
        self.fd_linesize = self.fuente_descripciones.get_linesize()

        # Gestionamos como de rápido actualiza la pantalla
        self.reloj = pygame.time.Clock()
        
    
    def mostrar_ranking(self):
        # Texto por lineas y posicion en pantalla
        self.linea_texto1 = self.fuente_descripciones.render('Ranking puntuaciones The Quest:', True, BLANCO)
        self.pantalla.blit(self.linea_texto1, [10, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize])

        self.linea_texto2 = self.fuente_descripciones.render('JLC - 306', True, BLANCO)
        self.pantalla.blit(self.linea_texto2, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 2])
        
        self.linea_texto3 = self.fuente_descripciones.render('STF - 304', True, BLANCO)
        self.pantalla.blit(self.linea_texto3, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 3])
        
        self.linea_texto4 = self.fuente_descripciones.render('JNP - 290', True, BLANCO)
        self.pantalla.blit(self.linea_texto4, [32, ALTO_TEXTO_TITULOS + 10 + self.fd_linesize * 4])

        self.linea_texto5 = self.fuente_descripciones.render('FJA - 281', True, BLANCO)
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
        
        self.main_loop_ranking()





    def main_loop_ranking(self):
        # Bucle Principal del Programa y condicion de salida del bucle
        dentro_while = True
        while dentro_while:
            for evento in pygame.event.get():  # El usuario hace algo
                # Si el usuario hace click en cerrar
                if evento.type == pygame.QUIT:
                    juego = Juego()
                    juego.salir_del_juego()
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    dentro_while = False        

    '''
    1.- Control de errores
    Cuando hagáis accesos a la base de datos deberéis controlar el error en acceso 
    a datos (por ejemplo inserciones con clave duplicada) o bloqueo de la base de 
    datos porque estéis haciendo inserciones desd SQLite Browser. La forma ya la conocéis.
    try:
        dbQuery(consulta, parametros)
        except sqlite3.Error as e:
    <procesar error>
    Este <procesar error> puede ser:
    form.errors['general'] = ['Error en acceso a base de datos: {}'.format(e)]
    return render_template('vuestro.html', form)
    
    En pygame, mostrar un error bien en la consola (terminal)
    lblError.config(text='Errorn en acceso a base de datos: {}'.format(e)) 
    #algo así en tkinter siempre que lblError sea una label que muestra los errores o usando messagebox
    print('Error en acceso a base de datos: {}'.format(e))
    #algo así en pygame. A no ser que queráis mostrarlo en la propia pantalla del juego    

    def create_table(self,c):
        c.execute("CREATE TABLE IF NOT EXISTS `ranking` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `user` TEXT NOT NULL, `point` INTEGER NOT NULL)")
    
    def data_entry(self,c,conn):
        c.execute("INSERT INTO ranking (user, point) VALUES('SJA',650)")
        conn.commit()
        c.close()
        conn.close()

    def mostrar_ranking(self):
        
        conn = sqlite3.connect('ranking.db')
        c = conn.cursor()
        
        self.create_table(c)
        self.data_entry(c,conn)
'''        