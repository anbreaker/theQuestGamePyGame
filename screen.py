import pygame

# Variables de uso global
LARGO = 700
ANCHO = 500

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

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
    pygame.display.set_caption("The Quest Juego pyGame")

    # Fuente para el texto que aparecerá en pantalla (tamaño 30)
    fuente = pygame.font.Font('resources/fonts/alatsi.ttf', 30)

    # Iteramos hasta que el usuario haga click sobre le botón de salida.
    # Condicion de salida del bucle principal
    salir = False

    #  Gestionamos como de rápido actualiza la pantalla
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

        # Limpia la pantalla y establece su color de fondo
        pantalla.blit(fondo_pantalla, (0, 0))

        if pagina_de_instrucciones == 1:
            # Instrucciones de dibujo, página 1
            # También podría cargar una imagen realizada por cualquier otro programa.
            # De esta forma sería más fácil y flexible.

            # Texto por lineas y posicion en pantalla
            linea_texto1 = fuente.render(
                "Bienvenido al Juego The Quest:", True, BLANCO)
            # Para centrar el texto mido su tamaño con esta funcion que devuelve w,h
            ancho_linea_texto1 = linea_texto1.get_rect().width
            # Calculo del posicionamiento de linea_texto1
            posicion_centrada = (LARGO/2)-(ancho_linea_texto1/2)
            # Presentacion del texto
            pantalla.blit(linea_texto1, [posicion_centrada, 10])
            

            # Texto por lineas y posicion en pantalla
            linea_texto2 = fuente.render(
                "Historia del juego: La búsqueda comienza en un planeta tierra moribundo por el cambio climático. Partiremos a la búsqueda de un planeta compatible con la vida humana para colonizarlo.", True, BLANCO)
            pantalla.blit(linea_texto2, [10, 44])

        if pagina_de_instrucciones == 2:
            # Instrucciones de dibujo, página 2
            linea_texto1 = fuente.render(
                "Pantalla de instrucciones", True, BLANCO)
            pantalla.blit(linea_texto1, [10, 10])

            # Texto por lineas y posicion en pantalla
            linea_texto2 = fuente.render("Página 2", True, BLANCO)
            pantalla.blit(linea_texto2, [10, 44])

        # # Limitamos a 20 fotogramas por segundo.
        # reloj.tick(20)
        # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
        pygame.display.flip()

    # Bucle Principal del Programa -----------
    while not salir:
        for evento in pygame.event.get():  # El usuario hace algo
            if evento.type == pygame.QUIT:  # Si el usuario hace click en cerrar
                salir = True
        # Limpia la pantalla y establece su color de fondo
        pantalla.blit(fondo_pantalla, (0, 0))

    # Para salir correctamente de la aplicacion y cierre todos los procesos
    pygame.quit()


if __name__ == "__main__":
    # Inicialización de Pygame
    pygame.init()
    main()
