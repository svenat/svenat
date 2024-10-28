import pygame
import sys

pygame.init()

scWidth = 960
scHeight = 540
mainSurface = pygame.display.set_mode((scWidth, scHeight))
mainBackground = pygame.image.load('IMAGES/Black Background.jpg')

planetStart = pygame.image.load('IMAGES/STart the Game.png')
fsPS = pygame.time.Clock()

while True:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    mainSurface.blit(planetStart, (0, 150))
    mainSurface.blit(mainBackground, (0, 0))




pygame.display.update()
clock.tick(60)
