import pygame

pygame.init()

# main variables
scWidth = 960
scHeight = 540
mainSurface = pygame.display.set_mode((scWidth, scHeight))
mainBackground = pygame.image.load('IMAGES/Black Background.jpg')
pygame.display.set_caption('TTTEST')
mainFont = pygame.font.Font('FONTS/SaucerFont.ttf', 20)


class BUTTON():

    def __init__(self, image, xPos, yPos, textInput):
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.rect = self.image.get_rect(center=(self.xPos, self.yPos))
        self.textInput = textInput
        self.text = mainFont.render(self.textInput, True, 'Red')
        self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))

    def update(self):
        mainSurface.blit(self.image, self.rect)
        mainSurface.blit(self.text, self.textRect)

    def checkForInput(self, position):
        # Print message if button is clicked
        if self.rect.collidepoint(position):
            print("To be Continued-->")

    def changeColor(self, position):
        # Change color when hovered
        if self.rect.collidepoint(position):
            self.text = mainFont.render(self.textInput, True, 'White')
        else:
            self.text = mainFont.render(self.textInput, True, 'Red')

    def update(self, surface):
        # Draw button and text on the main surface
        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.textRect)

# Load and set up button image
buttonSurface = pygame.image.load('IMAGES/STart the Game.png')
buttonSurface = pygame.transform.scale(buttonSurface, (scWidth, 500))
button = BUTTON(buttonSurface, 480, 270, "Click the earth")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())

    mainSurface.blit(mainBackground, (100, 100))

    button.changeColor(pygame.mouse.get_pos())
    BUTTON.update()

    pygame.display.update()