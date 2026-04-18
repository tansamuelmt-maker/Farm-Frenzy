#Where class of button is built
import pygame
class Button():
    def __init__(self, buttonText, buttonBGDimension, buttonBGcolor, buttonBGPos, funct, functArgs, functKwargs, clicked = False):
        self.buttonText = buttonText
        self.buttonBGDimension = buttonBGDimension
        self.buttonBGcolor = buttonBGcolor
        self.buttonBGPos = buttonBGPos
        self.funct = funct
        self.functArgs = functArgs #Used AI for args and kwargs
        self.functKwargs = functKwargs
        self.buttonSurf = pygame.Surface(buttonBGDimension)
        self.buttonRect = self.buttonSurf.get_rect(center=buttonBGPos)
        self.clicked = clicked


    def createButton(self):
        self.buttonSurf.fill(self.buttonBGcolor)
    
    def displayButton(self,screen):
        screen.blit(self.buttonSurf, self.buttonRect)
        mouse_pos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mouse_pos):
          if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
               self.funct(*self.functArgs, **self.functKwargs)
               self.clicked = True
          if pygame.mouse.get_pressed()[0] == 0:
              self.clicked = False
        self.buttonText.centerPosText()
        self.buttonText.displayStaticText(screen)
