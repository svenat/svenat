import pygame
import random


red = pygame.Rect(20, 20, 150, 150)
blue = pygame.Rect(190, 20, 150, 150)
green = pygame.Rect(360, 20, 150, 150)
yellow = pygame.Rect(530, 20, 150, 150)
magenta = pygame.Rect(20, 200, 150, 150)
cyan = pygame.Rect(190, 200, 150, 150)
orange = pygame.Rect(360, 200, 150, 150)
purple = pygame.Rect(530, 200, 150, 150)

sQ1 = red
sQ2 = blue
sQ3 = green
sQ4 = yellow
sQ5 = magenta
sQ6 = cyan
sQ7 = orange
sQ8 = purple



# Initialize an empty list


expandableList = [sQ1, ]
clickedList = []
gLevel = 1
if tLevel is True
    gLevel = gLevel + 1
    print("You have reached level:", tLevel + 1)

# Function to expand the list with a random number between 1 and 8
def expand_list(lst):
    new_number = random.randint(1, 8)  # Generate a random number between 1 and 8
    lst.append(new_number)  # Add the number to the list
    for _ in range(gLevel):
        print(expandable_list)
    return lst

# Example usage

