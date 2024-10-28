import pygame
from sys import exit

from pygame.examples.scrap_clipboard import screen
from pygame.examples.sprite_texture import clock


# Starting Screen Background
pygame.init()
scWidth = 960
scHeight = 540
mainSurface = pygame.display.set_mode((scWidth, scHeight))
mainBackground = pygame.image.load('IMAGES/Black Background.jpg')

creditSurface = pygame.Surface((scWidth, 30))
creditSurface.fill('white')



def playScreen():
	pygame.display.set_caption('Game On')


	mainSurface.blit(mainBackground, (0, 0))

	mainSurface.blit(creditSurface, (0, 510))

	while True:


	#Main run Screen
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()




	pygame.display.update()
	clock.tick(60)

playScreen()
