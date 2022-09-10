import pygame
from util.constants import Constants
class Ground:
    Width=37
    Height=128
    def __init__(self) -> None:
     self.groundImagePath="assets/images/ground.png"
     self.groundImage=pygame.image.load(self.groundImagePath)
     self.images=[self.groundImage.get_rect() for _ in range(Constants.TotalGroundImages)]   
     self.positions=list()  
     self.create_ground()
     
    def create_ground(self):
        delta=0
        for _ in range(Constants.TotalGroundImages):
         x = Ground.Width/2+ delta
         y = Constants.HEIGHT- Ground.Height/2
         self.positions.append((x,y))
         delta+=Ground.Width
        
    def display(self,screen):
        for i in range(Constants.TotalGroundImages):
         groundRect=self.images[i]
         groundRect.center=self.positions[i]
         screen.blit(self.groundImage,groundRect)
         
        