#This is where the class of plants is built
import pygame
from Classes.scaleImage import scaleImg
class Plant():
    def __init__(self, plantXPos, plantYPos):
        self.plantXPos = plantXPos
        self.plantYPos = plantYPos
        self.plantedTime = int(pygame.time.get_ticks() / 1000)
        self.isFruiting = False
        self.plantImage = None
        self.plantRect = None
        self.growthImage1 = pygame.Surface((30,30))
        self.growthImage2 = pygame.Surface((30,50)) 
        self.growthImage3 = pygame.Surface((30,70))
        self.growthTime = 10

    def growPlant(self):
        elapsedTime = (pygame.time.get_ticks() / 1000) - self.plantedTime
        if elapsedTime > self.growthTime:
            self.plantImage = self.growthImage3
            self.isFruiting = True
        elif elapsedTime > (0.5*self.growthTime):
            self.plantImage = self.growthImage2
        elif elapsedTime < (0.5*self.growthTime):
            self.plantImage = self.growthImage1
        self.plantRect = self.plantImage.get_rect(midbottom = (self.plantXPos, self.plantYPos))

    def displayPlant(self, screen):
        screen.blit(self.plantImage, self.plantRect)

class Apple(Plant):
 def __init__(self, plantXPos, plantYPos):  
     super().__init__(plantXPos, plantYPos)
     self.plantedTime = int(pygame.time.get_ticks() / 1000)
     self.isFruiting = False
     self.plantImage = None
     self.plantRect = None
     self.growthImage1 = scaleImg(pygame.image.load('images/apple_stage1_seedling.png').convert_alpha(), 0.2)
     self.growthImage2 = scaleImg(pygame.image.load('images/apple_stage2_sapling.png').convert_alpha(), 0.2)
     self.growthImage3 = scaleImg(pygame.image.load('images/apple_stage4_fruiting.png').convert_alpha(), 0.2)
     self.growthTime = 20
class Pear(Plant):
 def __init__(self, plantXPos, plantYPos):  
     super().__init__(plantXPos, plantYPos)
     self.plantedTime = int(pygame.time.get_ticks() / 1000)
     self.isFruiting = False
     self.plantImage = None
     self.plantRect = None
     self.growthImage1 = scaleImg(pygame.image.load('images/pear_stage1_seedling.png').convert_alpha(), 0.2)
     self.growthImage2 = scaleImg(pygame.image.load('images/pear_stage2_sapling.png').convert_alpha(), 0.2)
     self.growthImage3 = scaleImg(pygame.image.load('images/pear_stage4_fruiting.png').convert_alpha(), 0.2)
     self.growthTime = 16
class Banana(Plant):
 def __init__(self, plantXPos, plantYPos):  
     super().__init__(plantXPos, plantYPos)
     self.plantedTime = int(pygame.time.get_ticks() / 1000)
     self.isFruiting = False
     self.plantImage = None
     self.plantRect = None
     self.growthImage1 = scaleImg(pygame.image.load('images/banana_stage1_seedling.png').convert_alpha(), 0.15)
     self.growthImage2 = scaleImg(pygame.image.load('images/banana_stage2_stem.png').convert_alpha(), 0.1)
     self.growthImage3 = scaleImg(pygame.image.load('images/banana_stage3_fruiting.png').convert_alpha(), 0.1)
     self.growthTime = 8
class Watermelon(Plant):
 def __init__(self, plantXPos, plantYPos):  
     super().__init__(plantXPos, plantYPos)
     self.plantedTime = int(pygame.time.get_ticks() / 1000)
     self.isFruiting = False
     self.plantImage = None
     self.plantRect = None
     self.growthImage1 = scaleImg(pygame.image.load('images/watermelon_stage1_seedling.png').convert_alpha(), 0.15)
     self.growthImage2 = scaleImg(pygame.image.load('images/watermelon_stage2_vine.png').convert_alpha(), 0.1)
     self.growthImage3 = scaleImg(pygame.image.load('images/watermelon_stage3_fruiting.png').convert_alpha(), 0.1)
     self.growthTime = 20
class Corn(Plant):
 def __init__(self, plantXPos, plantYPos):  
     super().__init__(plantXPos, plantYPos)
     self.plantedTime = int(pygame.time.get_ticks() / 1000)
     self.isFruiting = False
     self.plantImage = None
     self.plantRect = None
     self.growthImage1 = scaleImg(pygame.image.load('images/corn_stage1_seedling.png').convert_alpha(), 0.15)
     self.growthImage2 = scaleImg(pygame.image.load('images/corn_stage2_stem.png').convert_alpha(), 0.1)
     self.growthImage3 = scaleImg(pygame.image.load('images/corn_stage3_mature.png').convert_alpha(), 0.1)
     self.growthTime = 10
class Wheat(Plant):
 def __init__(self, plantXPos, plantYPos):  
     super().__init__(plantXPos, plantYPos)
     self.plantedTime = int(pygame.time.get_ticks() / 1000)
     self.isFruiting = False
     self.plantImage = None
     self.plantRect = None
     self.growthImage1 = scaleImg(pygame.image.load('images/wheat_stage1_seedling.png').convert_alpha(), 0.15)
     self.growthImage2 = scaleImg(pygame.image.load('images/wheat_stage2_stem.png').convert_alpha(), 0.1)
     self.growthImage3 = scaleImg(pygame.image.load('images/wheat_stage3_mature.png').convert_alpha(), 0.1)
     self.growthTime = 7


