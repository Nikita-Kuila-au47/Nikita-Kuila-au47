# Simple pygame program

# Import and initialize the pygame library
from pickle import STOP
import pygame
pygame.init()
WIDTH=500
HEIGHT=500
COLOR_BLACK=(0, 0, 0)
# Set up the drawing window
screen = pygame.display.set_mode([WIDTH,HEIGHT])

# Run until the user asks to quit
STOP = False
while not STOP:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STOP = False

    # Fill the background with white
    screen.fill(COLOR_BLACK)

    
pygame.quit()
