#This is the main file, where the main function of the code is added, dictating the sequence of the code
import pygame
from sys import exit
from Game.init import( FFsettings, gameClock, 
background,floor, farmer, moneyText, 
waterText, timeText, plantsPlanted, tempTexts)
pygame.init()
gameScreen = FFsettings.startScreen()
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          exit()
    userKeyPress = pygame.key.get_pressed()
    currentTime = int(pygame.time.get_ticks() / 1000)

    background.displayImage(gameScreen)
    floor.displayImage(gameScreen)
    
    for plant in plantsPlanted:
       plant.growPlant()
       plant.displayPlant(gameScreen)
    
    for text in list(tempTexts):
       if text.textLifeCycle(3) == True:
         text.displayStaticText(gameScreen)
       else:
          tempTexts.remove(text)

    farmer.displayCharacter(gameScreen)
    farmer.walkCharacter(userKeyPress)
    farmer.plantSeed(userKeyPress, plantsPlanted)
    farmer.HarvestSeed(userKeyPress, plantsPlanted, tempTexts)

    moneyText.displayDynamicText(gameScreen, f'Money: {farmer.money}')
    waterText.displayDynamicText(gameScreen, f'Water: {farmer.money}')
    timeText.displayDynamicText(gameScreen, f'time : {currentTime}')

    FFsettings.startClock(gameClock)
    pygame.display.update()
    
