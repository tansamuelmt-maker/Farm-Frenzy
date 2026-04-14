#This is where the plot class is built
import pygame
from Classes.plant import Plant
class Plot():
    def __init__(self, plotXPos, plant, plotYPos = 350, isEmpty = True, plotImage = pygame.Surface((40, 10)), plotRect ="Not created yet"):
        self.plotXPos = plotXPos
        self.plant = plant      
        self.plotYPos = plotYPos
        self.isEmpty = isEmpty
        self.plotImage = plotImage
        self.plotRect = self.plotImage.get_rect(midbottom = (self.plotXPos, self.plotYPos))
    def displayPlot(self, screen):
        self.plotImage.fill('brown')
        screen.blit(self.plotImage, self.plotRect)
    def plantedSeed(self):
        self.isEmpty = False
        self.plant = Plant(self.plotXPos, self.plotYPos, 10)
     
    def harvestedPlant(self):
        self.isEmpty = True
        self.plant = "None"
def createPlotArray():
    newPlotArray = []
    startingXPos = 100
    for x in range(12):
        newPlot = Plot(startingXPos, "None")
        newPlotArray.append(newPlot)
        startingXPos += 45
        if x == 5:
            startingXPos += 200
    return newPlotArray