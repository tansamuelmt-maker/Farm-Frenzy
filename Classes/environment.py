#Where class of environment is built
import pygame
class environment():
    def __init__(self, summerImg, autumnImg, winterImg, springImg, envPos):
        self.summerImg = summerImg
        self.autumnImg = autumnImg
        self.winterImg = winterImg
        self.spring = springImg
        self.envPos = envPos
    def displayImage(self, screen, gameTime, summerRange, autumnRange, winterRange, springRange):
        if gameTime in summerRange:
            screen.blit(self.summerImg, self.envPos)
        elif gameTime in autumnRange:
            screen.blit(self.autumnImg, self.envPos)
        elif gameTime in winterRange:
            screen.blit(self.winterImg, self.envPos)
        elif gameTime in springRange:
            screen.blit(self.spring, self.envPos)
        
