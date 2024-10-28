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

#Basics of the text on main menu
startFont = pygame.font.Font('FONTS/SaucerFont.ttf', 50)
startText = startFont.render('Start The Game', False, 'Red')
clickFont = pygame.font.Font('FONTS/SaucerFont.ttf', 15)
clickText = clickFont.render('click space ._. ', False, 'Red')



def MainMenu():

	#top corner name
	pygame.display.set_caption('Game Main Menu')

	#frames per second update
	fsPS = pygame.time.Clock()

	creditSurface = pygame.Surface((scWidth, 30))
	creditSurface.fill('white')

	planetU = pygame.image.load('IMAGES/Uranus.png')
	planetStart = pygame.image.load('IMAGES/STart the Game.png')



	while True:

		# Starting Screen Background
		mainSurface.blit(mainBackground, (0, 0))
		mainSurface.blit(creditSurface, (0, 510))

	#Main run Screen
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()



		#key buttons
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE] == True:
				while startMovementText > (-50):
					startMovementText -= 4
				while startMovementPlanet < (540):
					startMovementPlanet += 3
				while clickMovementText > (-50):
					startMovementPlanet -= 3


		mainSurface.blit(startText, (360, 110))
		mainSurface.blit(planetStart, (0, 150))
		mainSurface.blit(clickText, (390, 110))

	pygame.display.update()
	clock.tick(60)

MainMenu()
