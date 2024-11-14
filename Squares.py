import pygame
pygame.init()

# Screen setup
scWidth = 960
scHeight = 540
mainSurface = pygame.display.set_mode((scWidth, scHeight))
pygame.display.set_caption("Colorful Squares")

# Define colors and positions for each square
square_size = 150
positions_and_colors = [
    ((20, 20), (255, 0, 0)),     # Red
    ((190, 20), (0, 255, 0)),    # Green
    ((360, 20), (0, 0, 255)),    # Blue
    ((530, 20), (255, 255, 0)),  # Yellow
    ((20, 200), (255, 0, 255)),  # Magenta
    ((190, 200), (0, 255, 255)), # Cyan
    ((360, 200), (255, 165, 0)), # Orange
    ((530, 200), (128, 0, 128))  # Purple
]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background with black
    mainSurface.fill((0, 0, 0))

    # Draw each square with a fixed position and color
    for position, color in positions_and_colors:
        pygame.draw.rect(mainSurface, color, (*position, square_size, square_size))

    # Update display
    pygame.display.update()

pygame.quit()
