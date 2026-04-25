#This is the main file, where the main function of the code is added, dictating the sequence of the code
import pygame
from sys import exit
pygame.init()
#Sets the resolution to 1200 by 500.
pygame.display.set_mode((1200, 500))
#Imports all necessary functions, variables and constants for reference and use.
from Game.init import (FFsettings, gameClock,
    background, floor1, floor2, moneyText,
    waterText, timeText,
    shop, barn,
    startMenu,
    gameState, winText, lossText, springTime, summerTime, winterTime, autumnTime)
from Game.gameProcesses import runGame, endGame
#Declares the game screen for all surfaces to be displayed on.
gameScreen = FFsettings.startScreen()
#While loop continually updates screen, user actions, and clock
while True:
    #Takes all user key presses
    userKeyPress = pygame.key.get_pressed()
    #Allows for the game to exit safely.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Calculates current time, updating after every iteration.
    currentTime = int(pygame.time.get_ticks() / 1000 - gameState['startTime'])
    
    #Displays start menu, game, and end menu depending on game conditions
    if gameState['gameStarted'] == False and gameState['gameEnded'] == False:
        startMenu.displayMenu(gameScreen)
    elif gameState['gameStarted'] == True and gameState['gameEnded'] == False:
        runGame(background, floor1, floor2, shop, barn, gameState, timeText, moneyText, waterText, gameScreen, userKeyPress, currentTime, springTime, autumnTime, winterTime, summerTime)
    elif gameState['gameStarted'] == False and gameState['gameEnded'] == True:
        endGame(gameState, currentTime, gameScreen, winText, lossText)
    
    #Updates clock and display
    FFsettings.startClock(gameClock)
    pygame.display.update()
    
