





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

	creditSurface = pygame.Surface((scWidth, 200))
	creditSurface.fill('white')

	planetU = pygame.image.load('IMAGES/Uranus.png')
	planetStart = pygame.image.load('IMAGES/STart the Game.png')



	while True:

		# Starting Screen Background

		mainSurface.fill('Black')
		mainSurface.blit(creditSurface, (0, 0))

	#Main run Screen
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()



		#key buttons



		mainSurface.blit(startText, (360, 110))
		mainSurface.blit(planetStart, (0, 150))
		mainSurface.blit(clickText, (390, 110))

	pygame.display.update()


MainMenu()
