#Where class of environment is built
import pygame
#Environment class used to map the seasonal background and floor to the game.
class environment():
    #Attributes of the position that the environment will be displayed in and the image of that environment based on the season.
    def __init__(self, summerImg, autumnImg, winterImg, springImg, envPos):
        self.summerImg = summerImg
        self.autumnImg = autumnImg
        self.winterImg = winterImg
        self.springImg = springImg
        self.envPos = envPos
    #Using the pre-defined seaso9n ranges to display the correct seasonal image.
    def displayImage(self, screen, gameTime, summerRange, autumnRange, winterRange, springRange):
        if gameTime in summerRange:
            screen.blit(self.summerImg, self.envPos)
        elif gameTime in autumnRange:
            screen.blit(self.autumnImg, self.envPos)
        elif gameTime in winterRange:
            screen.blit(self.winterImg, self.envPos)
        elif gameTime in springRange:
            screen.blit(self.springImg, self.envPos)
        
