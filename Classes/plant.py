#This is where the class of plants is built
import pygame
class Plant():
    def __init__(self, plantXPos, plantYPos, growthTime, plantedTime = None, growthImage1 = pygame.Surface((30,30)), growthImage2 = pygame.Surface((30,50)), growthImage3 = pygame.Surface((30,70)), isFruiting = False):
        self.plantXPos = plantXPos
        self.plantYPos = plantYPos
        self.growthTime = growthTime
        self.plantedTime = int(pygame.time.get_ticks() / 1000) if plantedTime is None else plantedTime
        self.growthImage1 = growthImage1
        self.growthImage2 = growthImage2
        self.growthImage3 = growthImage3
        self.plantImage = self.growthImage1
        self.plantRect = self.plantImage.get_rect(midbottom = (self.plantXPos, self.plantYPos))
        self.isFruiting = isFruiting

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
        self.plantImage.fill('green')
        screen.blit(self.plantImage, self.plantRect)

