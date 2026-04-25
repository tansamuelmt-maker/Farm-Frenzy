from Classes.tutorial import displayTutorial
from Game.init import (
    summerTime, autumnTime, winterTime, springTime,
    moneyGoal, timeLimit,
    shopMenu,
    endMenu, winText, lossText
)
#This function runs the game when the player clicks start game or play again button.
def runGame(background, floor1, floor2, shop, barn, gameState, timeText, moneyText, waterText, gameScreen, userKeyPress, currentTime, springTime, autumnTime, winterTime, summerTime):
    #farmer and plot array are assigned from the game state farmer and plot array, which contain the character object and plot array.
    farmer = gameState['farmer']
    plotArray = gameState['plotArray']
    #Displays the Background sky, and 2 floor environment images since 1 floor image is not long enough.
    background.displayImage(gameScreen, currentTime, summerTime, autumnTime,winterTime,springTime)
    floor1.displayImage(gameScreen, currentTime, summerTime, autumnTime, winterTime, springTime)
    floor2.displayImage(gameScreen, currentTime, summerTime, autumnTime, winterTime, springTime)
    shop.displayGraphic(gameScreen)
    barn.displayGraphic(gameScreen)
    #Starts displaying character and walking character before other functions so that character rect is calculated for further use.
    farmer.displayCharacter(gameScreen)
    farmer.walkCharacter(userKeyPress)
    
    #
    for plot in plotArray:
        if plot.isEmpty == False:
            plot.plant.growPlant()
            plot.plant.displayPlant(gameScreen)
        plot.displayPlot(gameScreen)

    farmer.plantSeed(userKeyPress,gameScreen, plotArray)
    farmer.HarvestFruit(userKeyPress, gameScreen, plotArray)

    for inventorySlot in list(farmer.inventory):
        inventorySlot.drawInvSlot(gameScreen)
    farmer.updateWater(summerTime, autumnTime, winterTime, currentTime)

    moneyText.displayDynamicText(gameScreen, f'Money: {farmer.money}')
    waterText.displayDynamicText(gameScreen, f'Water: {farmer.water} / 30')
    farmer.accessInv(userKeyPress)
    timeText.displayDynamicText(gameScreen, f'Time : {currentTime}')

    farmer.accessShop(userKeyPress, gameScreen, shop.rect, shopMenu)

    if gameState['tutorialActive']:
        displayTutorial(gameState, gameScreen, userKeyPress)

    if farmer.money >= moneyGoal or currentTime >= timeLimit:
        gameState['gameStarted'] = False
        gameState['gameEnded'] = True

def endGame(gameState, currentTime, screen, winText, lossText):
    farmer = gameState['farmer']
    if farmer.money >= moneyGoal:
        endMenu.updateMenuText(winText)
        endMenu.displayMenu(screen)
    elif currentTime >= timeLimit:
        endMenu.updateMenuText(lossText)
        endMenu.displayMenu(screen)
