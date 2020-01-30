import pygame

# Variables de uso global
LARGO = 700
ANCHO = 500

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


def main():
    # Inicialización de la superficie de dibujo (display surface)
    # Establecemos el largo y ancho de la pantalla.
    dimensiones = [LARGO, ANCHO]
    pantalla = pygame.display.set_mode(dimensiones)

    # Inicializacion de la imagen de fondo de la pantalla (sin efecto alpha)
    fondo_pantalla = pygame.image.load('resources/background.png').convert()

    # Titulo de la barra de la aplicacion
    pygame.display.set_caption('The Quest Juego pyGame')

    # Fuente para el texto que aparecerá en pantalla (tamaño 30 y 22)
    fuente_titulo = pygame.font.Font('resources/fonts/alatsi.ttf', ALTO_TEXTO_TITULOS)
    fuente_descripciones = pygame.font.Font('resources/fonts/alatsi.ttf', ALTO_TEXTO_DESCRIPCIONES)
    
    # Devuelve la altura en píxeles para distancia "ideal" entre líneas de texto con la fuente.
    fd_linesize = fuente_descripciones.get_linesize()
    
    # Iteramos hasta que el usuario haga click sobre el botón de salida.
    # Condicion de salida del bucle principal
    salir = False

    # Gestionamos como de rápido actualiza la pantalla
    reloj = pygame.time.Clock()

    mostrar_instrucciones = True  # Bandera para condicion
    pagina_de_instrucciones = 1   # Bandera

    # Bucle de las Páginas de Instrucciones -----------
    while not salir and mostrar_instrucciones:
        for evento in pygame.event.get():   # El usuario hace algo
            if evento.type == pygame.QUIT:  # Si el usuario hace click en cerrar
                # Cambio del Flag, rompe la condicion del bucle y sale.
                salir = True
            if evento.type == pygame.MOUSEBUTTONDOWN:  # El usuario presiona click derecho sobre screen
                pagina_de_instrucciones += 1  # Aumentamos contador para forzar el cambio de pantalla
                if pagina_de_instrucciones == 3:  # Esperando evento que fuerce el ultimo cambio de pantalla
                    # Cambio del flag para dejar de mostarar pantallas de instrucciones
                    mostrar_instrucciones = False

        # Limpia la pantalla y establece el fondo
        pantalla.blit(fondo_pantalla, (0, 0))

        if pagina_de_instrucciones == 1:
            # Instrucciones de dibujo, página 1
            # Podría cargar una imagen realizada por cualquier otro programa.
            # de esta forma sería más fácil y flexible.
            
            # Texto por lineas y posicion en pantalla, (Head)
            linea_head = fuente_titulo.render(
                'Bienvenidos a El juego: The quest!', True, VERDE)
            # Para centrar el texto mido su tamaño con esta funcion que devuelve w,h
            ancho_linea_head = linea_head.get_rect().width
            # Calculo del posicionamiento de linea_texto1
            posicion_centrada = (LARGO/2)-(ancho_linea_head/2)
            # Presentacion del texto en pantalla
            pantalla.blit(linea_head, [posicion_centrada, 20])

            # Introduccion al juego:
            # Texto por lineas y posicion en pantalla
            linea_texto1 = fuente_descripciones.render('Historia del juego:', True, BLANCO)
            pantalla.blit(linea_texto1, [10, ALTO_TEXTO_TITULOS + 10 + fd_linesize])

            linea_texto2 = fuente_descripciones.render('La búsqueda comienza en un planeta tierra moribundo por el cambio', True, BLANCO)
            pantalla.blit(linea_texto2, [32, ALTO_TEXTO_TITULOS + 10 + fd_linesize * 2])
            
            linea_texto3 = fuente_descripciones.render('climático. Partiremos a la búsqueda de un planeta compatible ', True, BLANCO)
            pantalla.blit(linea_texto3, [32, ALTO_TEXTO_TITULOS + 10 + fd_linesize * 3])
            
            linea_texto4 = fuente_descripciones.render('con la vida humana para colonizarlo. Esquiva los obstaculos,', True, BLANCO)
            pantalla.blit(linea_texto4, [32, ALTO_TEXTO_TITULOS + 10 + fd_linesize * 4])

            linea_texto5 = fuente_descripciones.render('hazte con el control de la nave y logra aterrizar!', True, BLANCO)
            pantalla.blit(linea_texto5, [32, ALTO_TEXTO_TITULOS + 10 + fd_linesize * 5])

            # Texto por lineas y posicion en pantalla, (footer)
            linea_footer = fuente_titulo.render('Click derecho para continuar', True, AMARILLO)
            # Para centrar el texto mido su tamaño con esta funcion que devuelve w,h
            ancho_linea_footer = linea_footer.get_rect().width
            # Calculo del posicionamiento de linea_texto1
            alineacion_izquierda = (LARGO - ancho_linea_footer -10)
            # Presentacion del texto en pantalla
            pantalla.blit(linea_footer, [alineacion_izquierda, ANCHO - 50])
                        
            
        if pagina_de_instrucciones == 2:
            # Instrucciones de dibujo, página 2
            linea_texto1 = fuente_titulo.render(
                'Pantalla de instrucciones', True, BLANCO)
            pantalla.blit(linea_texto1, [10, 10])

            # Texto por lineas y posicion en pantalla
            linea_texto2 = fuente_titulo.render('Página 2', True, BLANCO)
            pantalla.blit(linea_texto2, [10, 44])

        # Limitamos a 20 fotogramas por segundo.
        # reloj.tick(20)
        # Actualizamos la pantalla con lo que hemos dibujado.
        pygame.display.flip()

    # Bucle Principal del Programa -----------
    while not salir:
        for evento in pygame.event.get():  # El usuario hace algo
            if evento.type == pygame.QUIT:  # Si el usuario hace click en cerrar
                salir = True
        # Limpia la pantalla y coloca el fondo
        pantalla.blit(fondo_pantalla, (0, 0))

    # Para salir correctamente de la aplicacion y cierre todos los procesos
    pygame.quit()


if __name__ == '__main__':
    # Inicialización de Pygame
    pygame.init()
    main()
