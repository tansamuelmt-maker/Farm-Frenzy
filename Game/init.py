#This is the initialize file, this is where the messy work of instantiaing all the classes (start and end menus),
#graphics, etc and the class of start game
#Eventually, this will be turned into a function that will initialize the game when the game button is pressed
import pygame
from Classes.character import Character
from Classes.gameSettings import gameSettings
from Classes.environment import environment
from Classes.text import Text
from Classes.plot import Plot, createPlotArray
gameClock = pygame.time.Clock()
FFsettings = gameSettings((1200,500), 30)

background = environment((1200, 350), 'blue', (0,0))
background.createEnv()
floor = environment((1200,150), 'green', (0,350))
floor.createEnv()

farmer = Character()

moneyText = Text(20,'black', f'Money: {farmer.money}',(1100, 50))
moneyText.createFont()
waterText = Text(20,'black', f'water: {farmer.water} / 30', (1100, 70))
waterText.createFont()
timeText = Text(20, 'black', 'none', (1100,90))
timeText.createFont()

summerTime = range(1,250)
autumnTime = range(251,500)
winterTime = range(501,750)
springTime = range(751,1000)

plotArray = createPlotArray()
InvMapping = {
    pygame.K_1: 0,
    pygame.K_2: 1,
    pygame.K_3: 2,
    pygame.K_4: 3,
    pygame.K_5: 4,
    pygame.K_6: 5,
    pygame.K_7: 6,
    pygame.K_8: 7,
    pygame.K_9: 8,
    pygame.K_0 : 9,
    pygame.K_MINUS: 10,
    pygame.K_EQUALS: 11 #Used AI as I was unfamiliar with the keyboard mappings
}
InvKeys = InvMapping.keys()
tempTexts = []