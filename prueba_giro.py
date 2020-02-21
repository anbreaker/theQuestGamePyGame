from pygame.locals import *
import pygame
import sys

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('giro de nave')
screen = pygame.display.set_mode((700, 500), 0, 32)

image_nave = pygame.image.load('resources/images/rocket.png')

image_nave_180 = 0

while True:

    screen.fill((0, 0, 0))

    if image_nave_180 < 180:
        image_nave_180 += 1

    image_nave_copia = image_nave.copy()

    image_nave_copia = pygame.transform.rotate(image_nave_copia, image_nave_180)
    screen.blit(image_nave_copia, (200, 200))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)

    pygame.display.update()
    mainClock.tick(60)
