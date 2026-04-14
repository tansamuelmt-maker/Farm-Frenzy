#This is the main file, where the main function of the code is added, dictating the sequence of the code
import pygame
from sys import exit
from Game.init import( FFsettings, gameClock, 
background,floor, farmer, moneyText, 
waterText, timeText, tempTexts, plotArray, InvMapping, InvKeys)
pygame.init()
gameScreen = FFsettings.startScreen()
while True:
    userKeyPress = pygame.key.get_pressed()
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          exit()
       if event.type == pygame.KEYDOWN:
          farmer.accessInv(event.key, InvMapping, InvKeys)
    currentTime = int(pygame.time.get_ticks() / 1000)
      
       

    background.displayImage(gameScreen)
    floor.displayImage(gameScreen)

    for plot in plotArray:
       if plot.isEmpty == False:
        plot.plant.growPlant()
        plot.plant.displayPlant(gameScreen)
       plot.displayPlot(gameScreen)
       farmer.plantSeed(userKeyPress, plot)
       farmer.HarvestSeed(userKeyPress, tempTexts, plot)
    
    for text in list(tempTexts):
       if text.textLifeCycle(3) == True:
         text.displayStaticText(gameScreen)
       else:
          tempTexts.remove(text)

    for inventorySlot in list(farmer.inventory):
       inventorySlot.drawInvSlot(gameScreen)

    farmer.displayCharacter(gameScreen)
    farmer.walkCharacter(userKeyPress)

    moneyText.displayDynamicText(gameScreen, f'Money: {farmer.money}')
    waterText.displayDynamicText(gameScreen, f'Water: {farmer.money}')
    timeText.displayDynamicText(gameScreen, f'time : {currentTime}')

    FFsettings.startClock(gameClock)
    pygame.display.update()
    
