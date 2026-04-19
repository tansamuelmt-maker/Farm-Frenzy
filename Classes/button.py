#Where class of button is built
from Classes.plant import plantInfoList
from Classes.text import Text
import pygame
class Button():
    def __init__(self, text, textColor, textSize, buttonBGDimension, buttonBGColor, buttonEdgeColor, buttonPos, funct, functArgs, functKwargs, hoverText, image, imagePos = None):
        self.text = text
        self.textColor = textColor
        self.textSize = textSize
        self.buttonBGDimension = buttonBGDimension
        self.buttonBGColor = buttonBGColor
        self.buttonEdgeColor = buttonEdgeColor
        self.buttonPos = buttonPos
        self.funct = funct
        self.functArgs = functArgs #Used AI for args and kwargs
        self.functKwargs = functKwargs
        self.hoverText = hoverText
        self.image = image
        self.imagePos = None if image is None else imagePos
        self.buttonText = Text(textSize, textColor, text, (buttonPos[0]+(buttonBGDimension[0]/2), buttonPos[1]+(buttonBGDimension[1]/2)))
        self.buttonSurf = pygame.Surface(buttonBGDimension)
        self.buttonRect = self.buttonSurf.get_rect(topleft=buttonPos)
        self.clicked = False
        self.mouseWasUp = False

    def displayButton(self,screen):
        pygame.draw.rect(screen, self.buttonBGColor, (self.buttonPos[0],self.buttonPos[1], self.buttonBGDimension[0],self.buttonBGDimension[1]))
        pygame.draw.rect(screen, self.buttonEdgeColor, (self.buttonPos[0],self.buttonPos[1],self.buttonBGDimension[0],self.buttonBGDimension[1]),3)
        mouse_pos = pygame.mouse.get_pos()
        self.buttonText.centerPosText()
        self.buttonText.displayStaticText(screen)
        if self.image != None:
            screen.blit(self.image,self.imagePos)
        if self.buttonRect.collidepoint(mouse_pos):
          if pygame.mouse.get_pressed()[0] == 0:
              self.clicked = False
              self.mouseWasUp = True
          elif pygame.mouse.get_pressed()[0] == 1 and not self.clicked and self.mouseWasUp:
              self.funct(*self.functArgs, **self.functKwargs)
              self.clicked = True
              self.mouseWasUp = False
        else:
          if pygame.mouse.get_pressed()[0] == 0:
              self.clicked = False

    def drawHoverText(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.hoverText is not None and self.buttonRect.collidepoint(mouse_pos):
            self.hoverText.displayDynamicTextBox(None, screen, mouse_pos[0], mouse_pos[1])
