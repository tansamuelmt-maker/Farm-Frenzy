#This is the initialize file, this is where the messy work of instantiaing all the classes (start and end menus),
#graphics, etc and the class of start game
#Eventually, this will be turned into a function that will initialize the game when the game button is pressed
import pygame
from Classes.character import Character
from Classes.gameSettings import gameSettings
from Classes.environment import environment
from Classes.text import Text
from Classes.plot import plotArray
from Classes.button import Button
from Classes.scaleImage import scaleImg

farmer = Character()

gameClock = pygame.time.Clock()
FFsettings = gameSettings((1200,500), 30)


background = environment(scaleImg(pygame.image.load('images/background_summer.png'),2), scaleImg(pygame.image.load('images/background_autumn.jpeg'), 2), scaleImg( pygame.image.load('images/background_winter.png'), 2) ,scaleImg(pygame.image.load('images/background_spring.png'), 2), (0,0))
floor1 = environment(pygame.image.load('images/ground_summer.png'), pygame.image.load('images/ground_autumn.png'), pygame.image.load('images/ground_winter.png'), pygame.image.load('images/ground_spring.png'), (0,350))
floor2 = environment(pygame.image.load('images/ground_summer.png'), pygame.image.load('images/ground_autumn.png'), pygame.image.load('images/ground_winter.png'), pygame.image.load('images/ground_spring.png'), (600,350))

for inventorySlot in farmer.inventory:
    inventorySlot.quantityText.topLeftPosText()
    inventorySlot.keyMappingText.topLeftPosText()
    inventorySlot.selectedText.centerPosText()

    
moneyText = Text(20,'black', f'Money: {farmer.money}',(1100, 50))
moneyText.topLeftPosText()
waterText = Text(20 ,'black', f'water: {farmer.water} / 30', (1100, 70))
waterText.topLeftPosText()
timeText = Text(20, 'black', 'none', (1100,90))
timeText.topLeftPosText()

summerTime = range(0,100)
autumnTime = range(101,200)
winterTime = range(201,300)
springTime = range(301,400)

tempTexts = []
buttonPosition = (900, 100)
def buttonFunction():
    print("button is pressed")
printButtonText = Text(20, 'black', 'Press this button', buttonPosition)
printButton = Button(printButtonText, (200,80), 'yellow', buttonPosition, buttonFunction, (), {})
printButton.createButton()