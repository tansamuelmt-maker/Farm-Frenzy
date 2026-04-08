#This is the initialize file, this is where the messy work of instantiaing all the classes (start and end menus),
#graphics, etc and the class of start game
import pygame
from Classes.character import Character
from Classes.gameSettings import gameSettings
from Classes.environment import environment

gameClock = pygame.time.Clock()
FFsettings = gameSettings((1200,500), 30)

background = environment((1200, 350), 'blue', (0,0))
background.createEnv()
floor = environment((1200,150), 'green', (0,350))
floor.createEnv()

farmer = Character()