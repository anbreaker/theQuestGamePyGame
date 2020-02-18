import pygame
import sqlite3
from menu import *
from juego_niveles import *
from entradaTexto import *

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

    # Constructor de la clase Ranking
    def __init__(self):
        pygame.font.init()
        # Inicialización de la superficie de dibujo (display surface)
        self.display = pygame.display
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [700, 500]
        self.pantalla = pygame.display.set_mode((700, 500))

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
        
        # lista_ranking
        self.lista_ranking = []

    def mostrar_ranking_textos_pantalla(self, lista_ranking):
        # Texto por lineas y posicion en pantalla
        self.linea_texto1 = self.fuente_descripciones.render(f'{lista_ranking[0]}', True, BLANCO)
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
        self.alineacion_izquierda = (LARGO - self.ancho_linea_footer - 10)
        # Presentacion del texto en pantalla
        self.pantalla.blit(self.linea_footer, [self.alineacion_izquierda, ANCHO - 50])


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
                    pygame.quit()
                    sys.exit(0)
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    dentro_while = False

    def create_table(self, cursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS `ranking` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `user` TEXT NOT NULL, `point` INTEGER NOT NULL)")

    def data_entry(self, cursor, conn, puntos, name):
        try:
            cursor.execute("INSERT INTO ranking (user, point) VALUES(?,?)", (name, puntos))
            conn.commit()
        except sqlite3.Error as error_e:
            print(f'Se ha producido el error {error_e}')
            print('En este momento no se puede guardar el record')

    def ranking_jugadores(self, cursor, conexion, puntos):
        entrada = Entrada()
        self.create_table(cursor)
        query = "SELECT user, point FROM ranking order by point desc"
        cursor.execute("SELECT count(*) FROM ranking ")
        # Para obtener un solo elemento, usamos fetchone():
        count = cursor.fetchone()
        filas = cursor.execute(query)

        iniciales = entrada.entrada_texto_loop()

        # self.ver_base_datos(cursor)
        
        if count[0] > 0:
            for fila in filas:
                if count[0] >= 5:
                    if fila[1] < puntos:
                        query = "DELETE FROM ranking WHERE id IN (SELECT id FROM ranking ORDER BY point ASC LIMIT 1)"
                        cursor.execute(query)
                        self.data_entry(cursor, conexion, puntos, iniciales[0])
                        break
                else:
                    self.data_entry(cursor, conexion, puntos, iniciales[0])
                    break
        else:
            self.data_entry(cursor, conexion, puntos, iniciales[0])


    def mostrar_ranking(self, puntos):
        conexion = sqlite3.connect('ranking.db')
        cursor = conexion.cursor()
        self.ranking_jugadores(cursor, conexion, puntos)

    def ver_base_datos(self, cursor):
        print('llamada')
        self.lista_ranking = cursor.fetchall()
        # lista_ranking = cursor.execute("SELECT * FROM ranking ")
        for registros in self.lista_ranking:
            print(f'Registros BBDD-> {registros}')
        # self.mostrar_ranking_textos_pantalla(self.lista_ranking)
        return self.lista_ranking