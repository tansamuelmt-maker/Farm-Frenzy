import pygame
pygame.font.init()
class Text():
    def __init__(self, fontSize, fontColor, text, fontPos):
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.text = text
        self.fontPos = fontPos
        self.fontstyle = 'images/Jersey10-Regular.ttf'
        self.font = pygame.font.Font(self.fontstyle, fontSize)
        self.textSurf = self.font.render(text, False, fontColor)
        self.textRect = None
        self.createdTime = pygame.time.get_ticks()


    def centerPosText(self):
        self.textRect = self.textSurf.get_rect(center=self.fontPos)

    def topLeftPosText(self):
        self.textRect = self.textSurf.get_rect(topleft=self.fontPos)

    def displayStaticText(self, screen):
        screen.blit(self.textSurf, self.textRect)
    
    def displayDynamicText(self, screen, newText):
        if newText != None:
          self.text = newText
          self.textSurf = self.font.render(self.text, False, self.fontColor)
        screen.blit(self.textSurf, self.textRect)

    def displayTemp(self, screen, newText):
          elapsedTime = (pygame.time.get_ticks() - self.createdTime) / 1000
          if elapsedTime < 2:
             return True
          else:
             return False
    

