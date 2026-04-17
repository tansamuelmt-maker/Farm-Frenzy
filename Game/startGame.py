import pygame
from Classes.character import Character
from Classes.gameSettings import gameSettings
from Classes.environment import environment
from Classes.text import Text
from Classes.plot import Plot, createPlotArray
from Classes.button import Button
from Classes.scaleImage import scaleImg
farmer = "object of character"
startTime = "Time point at which game has started"

def startGame(currentTime):
    farmer = Character()
    startTime = pygame.time.get_ticks() / 1000
    currentTime = currentTime - startTime
    plotArray = createPlotArray