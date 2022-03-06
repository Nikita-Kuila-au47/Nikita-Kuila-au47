import pygame
from util.constants import Constants
class Ground:
    def __init__(self) -> None:
     self.groundImagePath="assets/images/ground.png"
     self.groundImage=pygame.image.load(self.groundImagePath)
     groundWidth=128
     groundHeight=37
     self.groundImage=[self.groundImage.get_rect()for _ in range(Constants.TotalGroundImages)]     
    counter=0
    def display(self,screen):
        for i in range(Constants.TotalGroundImages):
         groundRect=self.groundImage[i]
         groundRect.centery=(groundRect.centery)+Constants.WIDTH-self.groundImage 
         groundRect.centerx=self.groundWidth+ counter
         screen.blit(self.groundImage[i],groundRect)
         counter+=self.groundWidth
        