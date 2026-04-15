import pygame
pygame.font.init()
class Text():
    def __init__(self, fontSize, fontColor, text, fontPos):
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.text = text
        self.fontPos = fontPos
        self.textSurf = None
        self.font = None
        self.fontstyle = 'images/Jersey10-Regular.ttf'
        self.textRect = None
        self.createdTime = pygame.time.get_ticks() 

    def createFont(self):
       self.font = pygame.font.Font(self.fontstyle, self.fontSize)
       self.textSurf = self.font.render(self.text, False, self.fontColor)

    def centerPosText(self):
        self.textRect = self.textSurf.get_rect(center=self.fontPos)

    def topLeftPosText(self):
        self.textRect = self.textSurf.get_rect(topleft=self.fontPos)

    def displayStaticText(self, screen):
        screen.blit(self.textSurf, self.textRect)
    
    def displayDynamicText(self, screen, newText):
        self.text = newText
        self.textSurf = self.font.render(self.text, False, self.fontColor)
        screen.blit(self.textSurf, self.textRect)

    
    def textLifeCycle(self, lifeSpan):
        elapsedTime = (pygame.time.get_ticks() - self.createdTime) / 1000
        if elapsedTime < lifeSpan:
            return True
        else:
            return False