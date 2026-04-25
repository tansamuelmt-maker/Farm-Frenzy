#This is the initialize file, this is where the messy work of instantiaing all the classes (start and end menus),
#graphics, etc and the class of start game
import pygame
from Classes.character import Character
from Classes.gameSettings import gameSettings
from Classes.environment import environment
from Classes.text import Text
from Classes.button import Button
from Classes.scaleImage import scaleImg
from Classes.textbox import shopInfoTextBoxList
from Classes.plant import plantInfoList
from Classes.graphics import Graphics
from Classes.menu import Menu
from Classes.plot import createPlotArray

#Re-structured by AI.

#Initializes the settings of refresh rate and screen dimension
# --- Core Display Setup ---
gameClock = pygame.time.Clock()
FFsettings = gameSettings((1200,500), 30)
gameScreen = FFsettings.startScreen()

#Initializes the constants of seasonal range, the time limit being the last second of spring and the goal to earn $600
# --- Game Constants ---
summerTime = range(0,100)
autumnTime = range(100,200)
winterTime = range(200,300)
springTime = range(300,401)
timeLimit = springTime[-1]
moneyGoal = 600

#Instantiates the character and the plot arrays that will be displayed
# --- Core Game Objects ---
farmer = Character()
plotArray = createPlotArray()

#Added by AI: These are the conditions that have occured in the game, like if the game has started, if it has ended, when the game starts, tutorials, etc.
# --- Game State ---
gameState = {
    'farmer': farmer,
    'plotArray': plotArray,
    'gameStarted': False,
    'gameEnded': False,
    'startTime': 0,
    'tutorialActive': True,
    'tutorialIndex': 0,
    'tKeyWasUp': True
}

#This changes the conditions to start the game
# --- Game Functions ---
def startStartMenu(gameState):
    gameState['gameStarted'] = False
    gameState['gameEnded'] = False

#This exits the game
def exitGame():
    pygame.quit()
    exit()

#Created by AI: This initializes the game, with new time, characters, initializing the inventory, sets the function of sell and exit buttons in shop.
def startGame(gameState):
    gameState['gameStarted'] = True
    gameState['gameEnded'] = False
    gameState['farmer'] = Character()
    gameState['plotArray'] = createPlotArray()
    gameState['startTime'] = pygame.time.get_ticks() / 1000
    gameState['tutorialActive'] = True
    gameState['tutorialIndex'] = 0
    gameState['tKeyWasUp'] = True
    for inventorySlot in gameState['farmer'].inventory:
        inventorySlot.quantityText.topLeftPosText()
        inventorySlot.keyMappingText.topLeftPosText()
        inventorySlot.selectedText.centerPosText()
    newFarmer = gameState['farmer']
    sellButton.funct = newFarmer.sellFruits
    exitButton.funct = newFarmer.exitShop
    for button in buyButtonsList:
        button.funct = newFarmer.buySeed

#Instantiates the background and floor with their position and seasonal background.
# --- Environment ---
background = environment(scaleImg(pygame.image.load('images/background_summer.png'),2),
                         scaleImg(pygame.image.load('images/background_autumn.jpeg'), 2),
                         scaleImg( pygame.image.load('images/background_winter.png'), 2) ,
                         scaleImg(pygame.image.load('images/background_spring.png'), 2),
                         (0,0))
floor1 = environment(pygame.image.load('images/ground_summer.png'),
                     pygame.image.load('images/ground_autumn.png'),
                     pygame.image.load('images/ground_winter.png'),
                     pygame.image.load('images/ground_spring.png'),
                     (0,350))
floor2 = environment(pygame.image.load('images/ground_summer.png'),
                      pygame.image.load('images/ground_autumn.png'),
                      pygame.image.load('images/ground_winter.png'),
                      pygame.image.load('images/ground_spring.png'),
                      (600,350))

#Loads the graphics that have little functionality, hence their own class.
# --- Static Graphics ---
shop = Graphics(scaleImg(pygame.image.load('images/shop.png').convert_alpha(), 0.1), (1100,350))
barn = Graphics(scaleImg(pygame.image.load('images/barn.png').convert_alpha(), 0.50), (550,350))

#Loads the text of the inventory.
# --- HUD ---
for inventorySlot in farmer.inventory:
    inventorySlot.quantityText.topLeftPosText()
    inventorySlot.keyMappingText.topLeftPosText()
    inventorySlot.selectedText.centerPosText()

#Creates the utilities text to display utilities based on the game's conditions.
moneyText = Text(20,'black', f'Money: {farmer.money}',(1100, 50))
moneyText.topLeftPosText()
waterText = Text(20 ,'black', f'water: {farmer.water} / 30', (1100, 70))
waterText.topLeftPosText()
timeText = Text(20, 'black', 'none', (1100,90))
timeText.topLeftPosText()
tempText = Text(30, 'red', "displays texts temporarily", (600, 150))
tempText.centerPosText()

#Creates the shop menu
# --- Shop ---
#Creates the list for all buttons to be displayed
buyButtonsList = []
#This function adds all the buy buttons to a button list, each having a function to buy different plants, display different text, and be displayed at different locations
def createbuyButtonList(buttonsList):
    startingXPos = 365
    startingYPos = 100
    for index in range(len(plantInfoList)):
        newButton = Button(f"Click here to buy {plantInfoList[index][0]} seeds for ${plantInfoList[index][2]}",
                           'white', 12, (200,50), (241, 195, 145), (213, 126, 106),
                           (startingXPos, startingYPos),
                             farmer.buySeed, [index],{}, shopInfoTextBoxList[index], plantInfoList[index][6], (startingXPos,startingYPos))
        startingYPos += 50
        buttonsList.append(newButton)
#Calls buy button function
createbuyButtonList(buyButtonsList)
#Instantiates button to exit shop and button to sell all fruits
sellButton = Button("Press here to sell all your fruits", 'white', 15, (200,50), (241, 195, 145), (213, 126, 106),
                   (590, 100), farmer.sellFruits,[], {}, None, None)
exitButton = Button("Press here to exit shop", 'white', 15, (200,50), (241, 195, 145), (213, 126, 106),
                   (590, 180), farmer.exitShop,[], {}, None, None)
#Combines all shop buttons to one list.
shopButtonsList = buyButtonsList + [sellButton, exitButton]
#Instantiates the shop menu, with yellow title, shop background, shop button list, and position to display the menu background.
shopMenu = Menu("Shop Menu", 'yellow', (450,80), scaleImg(pygame.image.load('images/shop_menu_bg.png'), 2), shopButtonsList, (300,30))

#Creates the buttons, constants and lists for the start and end menus.
# --- Menus ---
#Text to be displayed if user wins / losses the game.
winText = "You Won! Congrats"
lossText = "You Lost! Better luck next time"
#Instantiates the buttons for the start and end menu
startGameButton = Button("Start Game", 'white', 45, (300,100), (110, 117, 112), (220, 230, 223),
                   (450, 200), startGame, [gameState], {}, None, None)
replayGameButton = Button("Play Again", 'white', 45, (300,100), (110, 117, 112), (220, 230, 223),
                   (450, 200), startGame, [gameState], {}, None, None)
returnToStartMenuButton = Button("Return to start menu", 'white', 45, (300,100), (110, 117, 112), (220, 230, 223),
                   (450, 350), startStartMenu, [gameState], {}, None, None)
exitGameButton = Button("End Game", 'white', 45, (300,100), (110, 117, 112), (220, 230, 223),
                   (450, 350), exitGame,[], {}, None, None)
#Combines the buttons into lists format for access by menu class
startButtonsList = [startGameButton, exitGameButton]
endButtonsList = [replayGameButton, returnToStartMenuButton]
#Instantiates start and end menu
startMenu = Menu("Farm Frenzy", 'Red', (600,150), scaleImg(pygame.image.load('images/start_menu_bg.png'), 2), startButtonsList, (0,0))
endMenu = Menu(winText, 'Green', (600,150), scaleImg(pygame.image.load('images/end_menu_bg.png'), 2), endButtonsList, (0,0))
