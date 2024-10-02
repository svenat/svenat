import pygame
from sys import exit

from pygame.examples.scrap_clipboard import screen
from pygame.examples.sprite_texture import clock

pygame.init()
scWidth = 800
scHeight = 600
mainSurface = pygame.display.set_mode((scWidth, scHeight))

pygame.display.set_caption('Memory Game')
fsPS = pygame.time.Clock()


creditSurface = pygame.Surface((scWidth, 50))
creditSurface.fill('white')

planetU = pygame.image.load('/Users/sventjallingii/PycharmProjects/svenat/IMAGES/Uranus.png')
planetStart = pygame.image.load('/Users/sventjallingii/PycharmProjects/svenat/IMAGES/STart the Game.png')




while True:



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()


	mainSurface.blit(planetStart, (-200, ))
	mainSurface.blit(creditSurface, (0, 550))

	pygame.display.update()
	clock.tick(60)
