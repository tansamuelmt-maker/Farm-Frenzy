import pygame
pygame.font.init()
class Text():
    def __init__(self, fontSize, fontColor, text, fontPos, textSurf ="not created yet" ,font = "not created yet", fontstyle=None):
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.text = text
        self.fontPos = fontPos
        self.textSurf = textSurf
        self.font = font
        self.fontstyle = fontstyle
    
    def createFont(self):
       self.font = pygame.font.Font(self.fontstyle, self.fontSize)

    def displayStaticText(self, screen):
        self.textSurf = self.font.render(self.text, False, self.fontColor)
        screen.blit(self.textSurf, self.fontPos)
    
    def displayDynamicText(self, screen, newText):
        self.text = newText
        self.textSurf = self.font.render(self.text, False, self.fontColor)
        screen.blit(self.textSurf, self.fontPos)