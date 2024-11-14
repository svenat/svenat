print('hello world')
import pygame

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 500))
screen.fill('cadetblue1')
pygame.display.flip()

# Rectangles setup
red = pygame.Rect(20, 20, 150, 150)
blue = pygame.Rect(190, 20, 150, 150)
green = pygame.Rect(360, 20, 150, 150)
yellow = pygame.Rect(530, 20, 150, 150)
magenta = pygame.Rect(20, 200, 150, 150)
cyan = pygame.Rect(190, 200, 150, 150)
orange = pygame.Rect(360, 200, 150, 150)
purple = pygame.Rect(530, 200, 150, 150)

# Data to hold color, rectangle positions, and clicked state
rectData = [
    [pygame.Color(255, 0, 0), red, False],         # Red
    [pygame.Color(255, 255, 0), yellow, False],    # Yellow
    [pygame.Color(0, 0, 255), blue, False],        # Blue
    [pygame.Color(0, 255, 0), green, False],       # Green
    [pygame.Color(255, 0, 255), magenta, False],   # Magenta
    [pygame.Color(0, 255, 255), cyan, False],      # Cyan
    [pygame.Color(255, 165, 0), orange, False],    # Orange
    [pygame.Color(128, 0, 128), purple, False]     # Purple
]

# Main loop
run = True
while run:
    screen.fill('cadetblue1')

    # Draw rectangles and their small white squares if clicked
    for color, rect, clicked in rectData:
        pygame.draw.rect(screen, color, rect)
        if clicked:
            # Draw a small white square inside the clicked rectangle
            small_square = pygame.Rect(rect.x + 50, rect.y + 50, 50, 50)
            pygame.draw.rect(screen, 'white', small_square)

    # Draw the mouse pointer as a circle
    pygame.draw.circle(screen, 'gray100', pygame.mouse.get_pos(), 7)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
            mouse_pos = pygame.mouse.get_pos()
            # Check if any rectangle was clicked
            for data in rectData:
                color, rect, clicked = data
                if rect.collidepoint(mouse_pos):
                    # Toggle the clicked state
                    data[2] = not clicked

pygame.quit()


