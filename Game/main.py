#This is the main file, where the main function of the code is added, dictating the sequence of the code
import pygame
from sys import exit
from Game.init import FFsettings, gameClock, background,floor, farmer
gameScreen = FFsettings.startScreen()
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          exit()
    userKeyPress = pygame.key.get_pressed()

    background.displayImage(gameScreen)
    floor.displayImage(gameScreen)

    farmer.displayCharacter(gameScreen)
    farmer.walkCharacter(userKeyPress)

    FFsettings.startClock(gameClock)
    pygame.display.update()