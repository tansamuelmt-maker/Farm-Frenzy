import pygame
class gameSettings():
    def __init__(self, resolution, clockTime):
        self.resolution= resolution
        self.clockTime= clockTime
    def startScreen(self):
        screen = pygame.display.set_mode(self.resolution)
        return screen

    def startClock(self, clock):
        clock.tick(self.clockTime)
 
        