import pygame
pygame.init()

#main variables
scWidth = 960
scHeight = 540
mainSurface = pygame.display.set_mode((scWidth, scHeight))
mainBackground = pygame.image.load('IMAGES/Black Background.jpg')
pygame.display.set_caption('TTTEST')
mainFont = pygame.font.Font('FONTS/SaucerFont.ttf', 50)

class BUTTON():

    def __init__(self, image, xPos, yPos, textInput):
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.rect = self.image.get_rect(center=(self.xPos, self.yPos))
        self.textInput = textInput
        self.text = mainFont.render(self.textInput, True, 'Red')
        self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("To be Continued-->")

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = mainFont.render(self.textInput, True,  'White')
        else:
            self.text = mainFont.render(self.textInput, True, 'Red')

buttonSurface = pygame.image.load('IMAGES/STart the Game.png')
buttonSurface = pygame.transform.scale(buttonSurface, (400, 200))
button = BUTTON(buttonSurface, 400, 300, "Click the earth")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())
    mainSurface.fill('white')
    button.update
    button.changeColor(pygame.mouse.get_pos())

    pygame.display.update

