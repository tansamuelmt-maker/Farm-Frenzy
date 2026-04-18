#This is the main file, where the main function of the code is added, dictating the sequence of the code
import pygame
from sys import exit
pygame.init()
pygame.display.set_mode((1200, 500))
from Game.init import( FFsettings, gameClock,
background,floor1, floor2, farmer, moneyText,
waterText, timeText, tempTexts, plotArray,
 printButton, springTime, summerTime, winterTime, autumnTime)
gameScreen = FFsettings.startScreen()
while True:
    userKeyPress = pygame.key.get_pressed()
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          exit()
       if event.type == pygame.KEYDOWN:
          farmer.accessInv(event.key)
    currentTime = int(pygame.time.get_ticks() / 1000)
      
    background.displayImage(gameScreen, currentTime, summerTime, autumnTime,winterTime,springTime)
    floor1.displayImage(gameScreen, currentTime, summerTime, autumnTime, winterTime, springTime)
    floor2.displayImage(gameScreen, currentTime, summerTime, autumnTime, winterTime, springTime)

    for plot in plotArray:
       if plot.isEmpty == False:
        plot.plant.growPlant()
        plot.plant.displayPlant(gameScreen)
       plot.displayPlot(gameScreen)
    farmer.plantSeed(userKeyPress, tempTexts, plotArray)
    farmer.HarvestSeed(userKeyPress, tempTexts, plotArray)
    
    for text in list(tempTexts):
       if text.textLifeCycle(3) == True:
         text.displayStaticText(gameScreen)
       else:
          tempTexts.remove(text)

    for inventorySlot in list(farmer.inventory):
       inventorySlot.drawInvSlot(gameScreen)

    printButton.displayButton(gameScreen)

    farmer.displayCharacter(gameScreen)
    farmer.walkCharacter(userKeyPress)

    moneyText.displayDynamicText(gameScreen, f'Money: {farmer.money}')
    waterText.displayDynamicText(gameScreen, f'Water: {farmer.water} / 30')
    timeText.displayDynamicText(gameScreen, f'Time : {currentTime}')

    FFsettings.startClock(gameClock)
    pygame.display.update()
    
