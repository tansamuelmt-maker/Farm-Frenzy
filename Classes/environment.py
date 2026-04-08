#Where class of environment is built
import pygame
class environment():
    def __init__(self, envDim, envCol, envPos, envImage = "Null"):
        self.envDim = envDim
        self.envCol = envCol
        self.envPos = envPos
        self.envImage = envImage
    def createEnv(self):
        self.envImage = pygame.Surface(self.envDim)
        self.envImage.fill(self.envCol)
    def displayImage(self, screen):
        screen.blit(self.envImage, self.envPos)
