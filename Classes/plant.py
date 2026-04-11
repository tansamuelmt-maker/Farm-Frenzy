#This is where the class of plants is built
import pygame
class Plant():
    def __init__(self, plantPos, growthTime,plantedTime = int(pygame.time.get_ticks()/1000), growthImage1 = pygame.Surface((30,30)), growthImage2 = pygame.Surface((30,50)), growthImage3 = pygame.Surface((30,70)), plantImage = "not chosen yet", plantRect = "not initialized yet"):
        self.plantPos = plantPos
        self.growthTime = growthTime
        self.plantedTime = plantedTime
        self.growthImage1 = growthImage1
        self.growthImage2 = growthImage2
        self.growthImage3 = growthImage3
        self.plantImage = plantImage
        self.plantRect = plantRect
    def growPlant(self):
        elapsedTime = (pygame.time.get_ticks() / 1000) - self.plantedTime
        if elapsedTime > self.growthTime:
            self.plantImage = self.growthImage3
        elif elapsedTime > (0.5*self.growthTime):
            self.plantImage = self.growthImage2
        elif elapsedTime < (0.5*self.growthTime):
            self.plantImage = self.growthImage1
    def displayPlant(self, screen):
        self.plantImage.fill('green')
        self.plantRect = self.plantImage.get_rect(midbottom = self.plantPos)
        screen.blit(self.plantImage, self.plantRect)
