#This is the initialize file, this is where the messy work of instantiaing all the classes (start and end menus),
#graphics, etc and the class of start game
#Eventually, this will be turned into a function that will initialize the game when the game button is pressed
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
from Classes.tutorial import displayTutorial
farmer = Character()

gameClock = pygame.time.Clock()
FFsettings = gameSettings((1200,500), 30)
gameScreen = FFsettings.startScreen()

plotArray = createPlotArray()

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

gameStarted = False
gameEnded = False
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

summerTime = range(0,100)
autumnTime = range(101,200)
winterTime = range(201,300)
springTime = range(301,400)

tempText = Text(30, 'red', "displays texts temporarily", (600, 150))
tempText.centerPosText()
buyButtonsList = []
buttonPosition = (900, 100)
def createbuyButtonList(buttonsList):
    startingXPos = 365
    startingYPos = 100
    for index in range(len(plantInfoList)):
        newButton = Button(f"Click here to buy {plantInfoList[index][0]} seeds for ${plantInfoList[index][1]}", 
                           'white', 12, (200,50), (241, 195, 145), (213, 126, 106), 
                           (startingXPos, startingYPos),
                             farmer.buySeed, [index],{}, shopInfoTextBoxList[index], plantInfoList[index][6], (startingXPos,startingYPos))
        startingYPos += 50
        buttonsList.append(newButton)
createbuyButtonList(buyButtonsList)
sellButton = Button("Press here to sell all your fruits", 'white', 15, (200,50), (241, 195, 145), (213, 126, 106),
                   (590, 100), farmer.sellFruits,[], {}, None, None)
exitButton = Button("Press here to exit shop", 'white', 15, (200,50), (241, 195, 145), (213, 126, 106),
                   (590, 180), farmer.exitShop,[], {}, None, None)
shopButtonsList = buyButtonsList + [sellButton, exitButton]
shop = Graphics(scaleImg(pygame.image.load('images/shop.png').convert_alpha(), 0.1), (1100,350))
barn = Graphics(scaleImg(pygame.image.load('images/barn.png').convert_alpha(), 0.50), (550,350))

shopMenu = Menu("Shop Menu", 'yellow', (450,80), scaleImg(pygame.image.load('images/shop_menu_bg.png'), 2), shopButtonsList, (300,30))

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
timeLimit = springTime[-1]
moneyGoal = 600
def runGame(background, floor1, floor2, shop, barn, gameState, timeText, moneyText, waterText, gameScreen, userKeyPress, currentTime):
    farmer = gameState['farmer']
    plotArray = gameState['plotArray']
    background.displayImage(gameScreen, currentTime, summerTime, autumnTime,winterTime,springTime)
    floor1.displayImage(gameScreen, currentTime, summerTime, autumnTime, winterTime, springTime)
    floor2.displayImage(gameScreen, currentTime, summerTime, autumnTime, winterTime, springTime)
    shop.displayGraphic(gameScreen)
    barn.displayGraphic(gameScreen)
    farmer.displayCharacter(gameScreen)
    farmer.walkCharacter(userKeyPress)

    for plot in plotArray:
       if plot.isEmpty == False:
        plot.plant.growPlant()
        plot.plant.displayPlant(gameScreen)
       plot.displayPlot(gameScreen)

    farmer.plantSeed(userKeyPress,gameScreen, plotArray)
    farmer.HarvestFruit(userKeyPress, gameScreen, plotArray)

    for inventorySlot in list(farmer.inventory):
       inventorySlot.drawInvSlot(gameScreen)
    farmer.updateWater(summerTime, autumnTime, winterTime, springTime, currentTime)

    moneyText.displayDynamicText(gameScreen, f'Money: {farmer.money}')
    waterText.displayDynamicText(gameScreen, f'Water: {farmer.water} / 30')
    farmer.accessInv(userKeyPress)
    timeText.displayDynamicText(gameScreen, f'Time : {currentTime}')

    farmer.accessShop(userKeyPress, gameScreen, shop.rect, shopMenu)

    if gameState['tutorialActive']:
        displayTutorial(gameState, gameScreen, userKeyPress)

    if farmer.money > moneyGoal or currentTime >= timeLimit:
        gameState['gameStarted'] = False
        gameState['gameEnded'] = True

def startStartMenu(gameState):
    gameState['gameStarted'] = False
    gameState['gameEnded'] = False

def exitGame():
    pygame.quit()
    exit()

startGameButton = Button("Start Game", 'white', 45, (300,100), (110, 117, 112), (220, 230, 223),
                   (450, 200), startGame, [gameState], {}, None, None)
replayGameButton = Button("Play Again", 'white', 45, (300,100), (110, 117, 112), (220, 230, 223),
                   (450, 200), startGame, [gameState], {}, None, None)
returnToStartMenuButton = Button("Return to start menu", 'white', 45, (300,100), (110, 117, 112), (220, 230, 223),
                   (450, 350), startStartMenu, [gameState], {}, None, None)
exitGameButton = Button("End Game", 'white', 45, (300,100), (110, 117, 112), (220, 230, 223),
                   (450, 350), exitGame,[], {}, None, None)

startButtonsList = [startGameButton, exitGameButton]
endButtonsList = [replayGameButton, returnToStartMenuButton]
startMenu = Menu("Farm Frenzy", 'Red', (600,150), scaleImg(pygame.image.load('images/start_menu_bg.png'), 2), startButtonsList, (0,0))

winText = "You Won! Congrats"
lossText = "You Lost! Better luck next time"
endMenu = Menu(winText, 'Green', (600,150), scaleImg(pygame.image.load('images/end_menu_bg.png'), 2), endButtonsList, (0,0))
def endGame(gameState, currentTime, screen):
    farmer = gameState['farmer']
    if farmer.money >= moneyGoal:
        endMenu.updateMenuText(winText)
        endMenu.displayMenu(screen)
    if currentTime >= timeLimit:
        endMenu.updateMenuText(lossText)
        endMenu.displayMenu(screen)


        

