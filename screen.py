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

    # Iteramos hasta que el usuario haga click sobre le botón de salida.
    # Condicion de salida del bucle principal
    salir = False





    pygame.quit()

if __name__ == "__main__":
    main()