#This is where the plot class is built
import pygame
from Classes.plant import Plant
#This plot class instantiates all necessary attributes needed for a plot and methods the plot can do.
class Plot():
    def __init__(self, plotXPos):
        #Only unique information is the x position, to ensure plots don't overlap and can be customizably placed.
        self.plotXPos = plotXPos  
        #All plots have Y position 350, ensuring it is displayed above ground.
        self.plotYPos = 350
        #Starting conditions of plot is that no plant is planted on the plot. Hence the plot is empty
        self.plant = None
        self.isEmpty = True
        #Plot is a brown rectangle with 60x10 pixel dimension
        self.plotImage = pygame.Surface((60, 10))
        #Rectangle is used for precise location display.
        self.plotRect = self.plotImage.get_rect(midbottom = (self.plotXPos, self.plotYPos))

    #Displays the plot with its brown color on the screen
    def displayPlot(self, screen):
        self.plotImage.fill('brown')
        screen.blit(self.plotImage, self.plotRect)

    #Adds the unique seed into the plant attribute, while changing the plot into a not empty plot.
    def plantedSeed(self, plant):
        self.isEmpty = False
        self.plant = plant
     
    #removes the plant from the plant attribute, effectively deleting it from the game. Turns the plot into an empty plot for future planting
    def harvestedPlant(self):
        self.isEmpty = True
        self.plant = "None"

#This method creates 12 individiual plots, each at a unique position and with the starting attributes.
def createPlotArray():
    #Plots are stored in an array for easy access and unpacking for indeterminate amount of plots
    newPlotArray = []
    #starting value gets incremented after every new plot is instantiated to ensure each plot has a unique position and doesn't overlap.
    startingXPos = 100
    for x in range(12):
        #Plot is instantiated with its x position
        newPlot = Plot(startingXPos)
        #Plot is added to plot array
        newPlotArray.append(newPlot)
        startingXPos += 65
        #Extra positioning space between plots 1-6 and 7-12 to ensure that a barn fits in the middle
        if x == 5:
            startingXPos += 200
    return newPlotArray
#Plot array is called, creating the plot array into variable plotArray
plotArray = createPlotArray()