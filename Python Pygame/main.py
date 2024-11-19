import pygame
import time

pygame.init()

# Screen setup
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Interactive Squares")
screen.fill('cadetblue1')
pygame.display.flip()

def create_squares():
    """Initialize squares with their colors and positions."""
    red = pygame.Rect(20, 20, 150, 150)
    blue = pygame.Rect(190, 20, 150, 150)
    green = pygame.Rect(360, 20, 150, 150)
    yellow = pygame.Rect(530, 20, 150, 150)
    magenta = pygame.Rect(20, 200, 150, 150)
    cyan = pygame.Rect(190, 200, 150, 150)
    orange = pygame.Rect(360, 200, 150, 150)
    purple = pygame.Rect(530, 200, 150, 150)

    return [
        [pygame.Color(255, 0, 0), red, False, 0],         # Red
        [pygame.Color(255, 255, 0), yellow, False, 0],    # Yellow
        [pygame.Color(0, 0, 255), blue, False, 0],        # Blue
        [pygame.Color(0, 255, 0), green, False, 0],       # Green
        [pygame.Color(255, 0, 255), magenta, False, 0],   # Magenta
        [pygame.Color(0, 255, 255), cyan, False, 0],      # Cyan
        [pygame.Color(255, 165, 0), orange, False, 0],    # Orange
        [pygame.Color(128, 0, 128), purple, False, 0]     # Purple
    ]

def handle_button_click(rect_data, mouse_pos):
    """Check if a square is clicked and toggle its state."""
    for data in rect_data:
        color, rect, clicked, clicked_time = data
        if rect.collidepoint(mouse_pos):
            data[2] = True  # Set clicked state to True
            data[3] = time.time()  # Record the current time


def algorithm():
    current_time = time.time()
    for data in rect_data:
        color, rect, clicked, clicked_time = data
        pygame.draw.rect(screen, color, rect)



    # Draw a small white square inside the clicked rectangle
    small_square = pygame.Rect(rect.x + 10, rect.y + 10, rect.width - 20, rect.height - 20)
    pygame.draw.rect(screen, 'white', small_square)
    # Reset clicked state after 0.5 seconds
    if current_time - clicked_time >= 0.5:
        data[2] = False


# Initialize squares
expList = []
rect_data = create_squares()

# Main loop
run = True
while run:
    screen.fill('grey50')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:  # Check if spacebar is pressed
        screen.fill('grey50')
        for expList in range(10:
            for data in rect_data:
                color, rect, clicked, clicked_time = data
                pygame.draw.rect(screen, color, rect)

    # Draw rectangles and their small white squares if clicked
    current_time = time.time()
    for data in rect_data:
        color, rect, clicked, clicked_time = data
        pygame.draw.rect(screen, color, rect)

        # Show white square if clicked
        if clicked:
            # Draw a small white square inside the clicked rectangle
            small_square = pygame.Rect(rect.x + 10, rect.y + 10, rect.width - 20, rect.height - 20)
            pygame.draw.rect(screen, 'white', small_square)
            # Reset clicked state after 0.5 seconds
            if current_time - clicked_time >= 0.5:
                data[2] = False

    # Draw the mouse pointer as a circle
    pygame.draw.circle(screen, 'gray100', pygame.mouse.get_pos(), 7)

    # Draw the white rectangle at the bottom
    bottom_bar = pygame.Rect(0, 380, 700, 20)
    pygame.draw.rect(screen, 'white', bottom_bar)

    # Render text on the bottom bar
    font = pygame.font.Font(None, 24)  # Default font with size 24
    text = font.render("Memory Game made by: Sven Tjallingii", True, 'black')
    text_rect = text.get_rect(center=(350, 390))
    screen.blit(text, text_rect)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
            mouse_pos = pygame.mouse.get_pos()
            handle_button_click(rect_data, mouse_pos)

pygame.quit()
