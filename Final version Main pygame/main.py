import pygame
import time

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((700, 450))  # Set up a 700x400 pixel display
pygame.display.set_caption("Pygame Memory Game")  # Set the window caption
screen.fill('cadetblue1')  # Fill the screen with a light blue color
pygame.display.flip()  # Update the display to reflect changes

def create_squares():
    """Initialize squares with their colors, positions, and click states."""
    # Define square positions using pygame.Rect (x, y, width, height)
    red = pygame.Rect(20, 20, 150, 150)
    blue = pygame.Rect(190, 20, 150, 150)
    green = pygame.Rect(360, 20, 150, 150)
    yellow = pygame.Rect(530, 20, 150, 150)
    magenta = pygame.Rect(20, 200, 150, 150)
    cyan = pygame.Rect(190, 200, 150, 150)
    orange = pygame.Rect(360, 200, 150, 150)
    purple = pygame.Rect(530, 200, 150, 150)

    # Return a list of squares with their associated colors and states
    return [
        [pygame.Color(255, 0, 0), red, False, 0],         # Red square
        [pygame.Color(255, 255, 0), yellow, False, 0],    # Yellow square
        [pygame.Color(0, 0, 255), blue, False, 0],        # Blue square
        [pygame.Color(0, 255, 0), green, False, 0],       # Green square
        [pygame.Color(255, 0, 255), magenta, False, 0],   # Magenta square
        [pygame.Color(0, 255, 255), cyan, False, 0],      # Cyan square
        [pygame.Color(255, 165, 0), orange, False, 0],    # Orange square
        [pygame.Color(128, 0, 128), purple, False, 0]     # Purple square
    ]

def handle_button_click(rect_data, mouse_pos):
    """
    Check if any square is clicked and toggle its clicked state.
    Args:
        rect_data: List of square data (color, rect, clicked, clicked_time).
        mouse_pos: Position of the mouse click (x, y).
    """
    for data in rect_data:
        color, rect, clicked, clicked_time = data
        if rect.collidepoint(mouse_pos):  # Check if mouse click is within the square
            data[2] = True  # Set clicked state to True
            data[3] = time.time()  # Record the time of the click

# Initialize variables
rect_data = create_squares()  # Create the squares and store their data
run = True  # Game loop control variable
show_grey_screen = False  # Track whether the grey screen is active


# Define a font and size
font = pygame.font.Font(None, 48)  # Use default font with size 48

# Render the text
text = font.render("Show Colors Screen, click space to return", True, 'black')  # Render the text in black
text_rect = text.get_rect(center=(350, 200))  # Center the text at (350, 200)

font_small_red = pygame.font.Font(None, 30)  # Smaller font size for the "Space to start" text
start_text = font_small_red.render("Space to start", True, 'red')
start_rect = start_text.get_rect(center=(350, 390))  # Position the text in the middle of the space

# Main game loop
while run:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handle window close event
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Spacebar pressed
                show_grey_screen = not show_grey_screen  # Toggle the grey screen state
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            handle_button_click(rect_data, mouse_pos)  # Check for square clicks

    if show_grey_screen:
        # Fill the screen with a grey color for the "memory game" mode
        screen.fill('grey')
        screen.blit(text, text_rect)  # Render the text on the grey screen
    else:
        # Fill the screen with a darker grey background for normal gameplay
        screen.fill('grey50')

        # Draw the squares and handle click states
        current_time = time.time()
        for data in rect_data:
            color, rect, clicked, clicked_time = data
            pygame.draw.rect(screen, color, rect)  # Draw the square

            if clicked:  # If the square is clicked
                # Draw a smaller white square inside the clicked square
                small_square = pygame.Rect(rect.x + 10, rect.y + 10, rect.width - 20, rect.height - 20)
                pygame.draw.rect(screen, 'white', small_square)

                # Reset the clicked state after 0.5 seconds
                if current_time - clicked_time >= 0.5:
                    data[2] = False

        # Add the small red text "Space to start" between the squares and the bottom bar
        screen.blit(start_text, start_rect)  # Render the text

    # Draw the mouse pointer as a small gray circle
    pygame.draw.circle(screen, 'gray100', pygame.mouse.get_pos(), 7)

    # Draw a white rectangle at the bottom as a status bar
    bottom_bar = pygame.Rect(0, 430, 700, 20)
    pygame.draw.rect(screen, 'white', bottom_bar)

    # Display game credits text on the bottom bar
    font_small = pygame.font.Font(None, 24)  # Default font with size 24
    credits_text = font_small.render("Memory Game made by: Sven Tjallingii", True, 'black')
    credits_rect = credits_text.get_rect(center=(350, 440))  # Center the text
    screen.blit(credits_text, credits_rect)

    # Update the display to show changes
    pygame.display.flip()

# Quit Pygame
pygame.quit()

