from Classes.tutorial import displayTutorial
from Game.init import (
    summerTime, autumnTime, winterTime, springTime,
    moneyGoal, timeLimit,
    shopMenu,
    endMenu, winText, lossText
)
#This function runs the game when the player clicks start game or play again button.
def runGame(background, floor1, floor2, shop, barn, gameState, timeText, moneyText, waterText, gameScreen, userKeyPress, currentTime, springTime, autumnTime, winterTime, summerTime):
    #Added by AI: farmer and plot array are assigned from the game state farmer and plot array, which contain the character object and plot array.
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
    #Allows the user to access inventory based on key press.
    farmer.accessInv(userKeyPress)

    #Checks each plot for collisions, grows every plant from each plot, and finally displays the plant while growing it and the plot.
    for plot in plotArray:
        if plot.isEmpty == False:
            plot.plant.growPlant()
            plot.plant.displayPlant(gameScreen)
        plot.displayPlot(gameScreen)
    #Farmer actions for harvesting and planting the seeds, which activate based on conditions that can be taken from user, farmer, and plot array)
    farmer.plantSeed(userKeyPress,gameScreen, plotArray)
    farmer.HarvestFruit(userKeyPress, gameScreen, plotArray)
    
    #Displays every inventory slot 
    for inventorySlot in list(farmer.inventory):
        inventorySlot.drawInvSlot(gameScreen)
    #Resets the water every season for user to plant new seeds and earn money.
    farmer.updateWater(summerTime, autumnTime, winterTime, currentTime)

    #Written after background, allows for display of changing utilities based on game state of the character and game.
    moneyText.displayDynamicText(gameScreen, f'Money: {farmer.money}')
    waterText.displayDynamicText(gameScreen, f'Water: {farmer.water} / 30')
    timeText.displayDynamicText(gameScreen, f'Time : {currentTime}')
    
    #References shopmenu without changing the shop menu
    farmer.accessShop(userKeyPress, gameScreen, shop.rect, shopMenu)
    
    #Displays tutorial at the start of the game only once, once tutorial is finished, tutorial active is no longer true, and tutorial stops
    if gameState['tutorialActive']:
        displayTutorial(gameState, gameScreen, userKeyPress)
    
    #Ends the game if win or loss condition has been reached.
    if farmer.money >= moneyGoal or currentTime >= timeLimit:
        gameState['gameStarted'] = False
        gameState['gameEnded'] = True

#Displays a win or loss screen based on if the user has won or lost the game.
def endGame(gameState, currentTime, screen, winText, lossText):
    farmer = gameState['farmer']
    if farmer.money >= moneyGoal:
        endMenu.updateMenuText(winText)
        endMenu.displayMenu(screen)
    elif currentTime >= timeLimit:
        endMenu.updateMenuText(lossText)
        endMenu.displayMenu(screen)
