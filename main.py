import pygame
from sys import exit

from pygame.examples.scrap_clipboard import screen
from pygame.examples.sprite_texture import clock

pygame.init()
scWidth = 960
scHeight = 540
mainSurface = pygame.display.set_mode((scWidth, scHeight))
mainBackground = pygame.image.load('IMAGES/Black Background.jpg')

pygame.display.set_caption('Memory Game')
fsPS = pygame.time.Clock()

startFont = pygame.font.Font('FONTS/SaucerFont.ttf', 50)
startText = startFont.render('Start The Game', False, 'Red')
startMovementText = 50
startMovementPlanet = 150

creditSurface = pygame.Surface((scWidth, 30))
creditSurface.fill('white')

planetU = pygame.image.load('IMAGES/Uranus.png')
planetStart = pygame.image.load('IMAGES/STart the Game.png')



while True:


#Main run Screen
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

#Starting Screen Background
	mainSurface.blit(mainBackground, (0, 0))
	mainSurface.blit(creditSurface, (0, 510))
#Starting Screen Toppings

#key buttons
	key = pygame.key.get_pressed()
	if key[pygame.K_SPACE] == True:
		while startMovementText > (-50):
			startMovementText -= 50
	if key[pygame.K_SPACE] == True:
		while startMovementPlanet < (540):
			startMovementPlanet += 50


	mainSurface.blit(startText, (360, startMovementText))

	mainSurface.blit(planetStart, (0, startMovementPlanet))




	pygame.display.update()
	clock.tick(60)
