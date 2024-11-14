import pygame


pygame.init()

scWidth = 800
scHeight = 600
window = pygame.display.set_mode((scWidth, scHeight))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run == True:

    pygame.draw.rect(window, (225, 0, 0), player)
	 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False



pygame.display.update()
pygame.quit()