# Simple pygame program

# Import and initialize the pygame library
from pickle import STOP
from util.constants import Constants
import pygame
pygame.init()

COLOR_BLACK=(0, 0, 0)
# Set up the drawing window
bacgroundImagePath="assets/images/background.png"
backgroundImage=pygame.image.load(bacgroundImagePath)

#imgWidth=backgroundImage.get_width()
#imgHeight=backgroundImage.get_height()
#imgCenter=imgWidth//2,imgHeight//2
screen = pygame.display.set_mode([Constants.WIDTH,Constants.HEIGHT])

# Run until the user asks to quit
STOP = False
while not STOP:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STOP = False
    screen.blit(backgroundImage,backgroundImage.get_rect())
    pygame.display.flip()
    # Fill the background with white
    screen.fill(COLOR_BLACK)

    
pygame.quit()
