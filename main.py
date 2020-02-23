#!/usr/bin/env python
# Para crear un script autoejecutable del juego en el entorno virtual de python 
# instalando requirements.txt
# chmod +x main.py

import pygame
from pygame.locals import *
from menu import *


if __name__ == '__main__':
    pygame.init()
    menu = Menu()
    menu.main_loop_menu()
