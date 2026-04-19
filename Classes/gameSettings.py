import pygame
#This class allows for easy changes to the resolution and framerate/ticks of the game that only requires the change
#of the class instead of the change of many pygame functions 
class gameSettings():
    def __init__(self, resolution, clockTime):
        self.resolution= resolution
        self.clockTime= clockTime
    #Displays the screen with the intended game resolution
    def startScreen(self):
        screen = pygame.display.set_mode(self.resolution)
        return screen
    #instantiates the clock ticks based on the determined clock speed.
    def startClock(self, clock):
        clock.tick(self.clockTime)
 
        