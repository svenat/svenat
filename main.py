import pygame
from sys import exit

from pygame.examples.scrap_clipboard import screen
from pygame.examples.sprite_texture import clock

pygame.init()
scWidth = 960
scHeight = 540
mainSurface = pygame.display.set_mode((scWidth, scHeight))

pygame.display.set_caption('Memory Game')
fsPS = pygame.time.Clock()

startFont = pygame.font.Font('FONTS/SaucerFont.ttf', 50)
startText = startFont.render('Start The Game', False, 'Red')

creditSurface = pygame.Surface((scWidth, 30))
creditSurface.fill('white')

planetU = pygame.image.load('IMAGES/Uranus.png')
planetStart = pygame.image.load('IMAGES/STart the Game.png')




while True:



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()


	mainSurface.blit(planetStart, (0, 150))
	mainSurface.blit(creditSurface, (0, 510))
	mainSurface.blit(startText, (360, 50))

	pygame.display.update()
	clock.tick(60)
