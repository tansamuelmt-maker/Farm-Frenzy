#This is where the plot class is built
import pygame
from Classes.plant import Plant
class Plot():
    def __init__(self, plotXPos):
        self.plotXPos = plotXPos  
        self.plotYPos = 350
        self.plant = None
        self.isEmpty = True
        self.plotImage = pygame.Surface((60, 10))
        self.plotRect = self.plotImage.get_rect(midbottom = (self.plotXPos, self.plotYPos))
    def displayPlot(self, screen):
        self.plotImage.fill('brown')
        screen.blit(self.plotImage, self.plotRect)
    def plantedSeed(self, plant):
        self.isEmpty = False
        self.plant = plant
     
    def harvestedPlant(self):
        self.isEmpty = True
        self.plant = "None"
def createPlotArray():
    newPlotArray = []
    startingXPos = 100
    for x in range(12):
        newPlot = Plot(startingXPos)
        newPlotArray.append(newPlot)
        startingXPos += 65
        if x == 5:
            startingXPos += 200
    return newPlotArray