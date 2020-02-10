import pygame
from pygame.locals import *
from menu import *


if __name__ == '__main__':
    pygame.init()
    menu = Menu()
    menu.main_loop_menu()
