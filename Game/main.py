#This is the main file, where the main function of the code is added, dictating the sequence of the code
import pygame
from sys import exit
pygame.init()
pygame.display.set_mode((1200, 500))
from Game.init import( FFsettings, gameClock,
background, floor1, floor2, moneyText,
waterText, timeText,
shop, barn, runGame,
startMenu, endGame,
gameState)
gameScreen = FFsettings.startScreen()
while True:
    userKeyPress = pygame.key.get_pressed()
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          exit()
       
    currentTime = int(pygame.time.get_ticks() / 1000 - gameState['startTime'])
    
    if gameState['gameStarted'] == False and gameState['gameEnded'] == False:
       startMenu.displayMenu(gameScreen)
    elif gameState['gameStarted'] == True and gameState['gameEnded'] == False:
       runGame(background, floor1, floor2, shop, barn, gameState, timeText, moneyText, waterText, gameScreen, userKeyPress, currentTime)
    elif gameState['gameStarted'] == False and gameState['gameEnded'] == True:
       endGame(gameState, currentTime, gameScreen)

    FFsettings.startClock(gameClock)
    pygame.display.update()
    
