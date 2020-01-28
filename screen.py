import pygame

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
FPS = 60  # Fotogramas por segundo


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    # Establecemos el largo y ancho de la pantalla.
    dimensiones = [700,500]
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("Pantalla de Instrucciones")
    
    
    background_img = pg.image.load('resources/background.png').convert()

    # Iteramos hasta que el usuario haga click sobre le botón de salida.
    # Condicion de salida del bucle principal
    salir = False
    
    #  Gestionamos como de rápido actualiza la pantalla
    reloj = pygame.time.Clock()
    
    # Posición de partida del rectángulo
    rect_x = 50
    rect_y = 50
 
    # Velocidad y dirección del rectángulo
    rect_cambio_x = 5
    rect_cambio_y = 5

    # Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
    fuente = pygame.font.Font('resources/fonts/alatsi.ttf', 36)
    
    mostrar_instrucciones = True
    pagina_de_instrucciones = 1

    # Bucle de la Página de Instrucciones -----------
    while not salir and mostrar_instrucciones:
        for evento in pygame.event.get():   # El usuario hace algo
            if evento.type == pygame.QUIT:  # Si el usuario hace click en cerrar
                salir = True # Cambio del Flag, rompe la condicion del bucle y sale.
            if evento.type == pygame.MOUSEBUTTONDOWN: # El usuario presiona click derecho sobre screen
                pagina_de_instrucciones += 1
    pygame.quit()

if __name__ == "__main__":
    main()