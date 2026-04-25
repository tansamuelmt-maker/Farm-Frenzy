import pygame
#Initializes the font functions
pygame.font.init()

#Text class allows for customizeable text to be displayed.
#Text is used in inventory, text box, butten, menus, utilties, etc.
class Text():
    #Attributes of text that is allowed to change are the size, color, the text content and the position of the text.
    def __init__(self, fontSize, fontColor, text, fontPos):
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.text = text
        self.fontPos = fontPos
        #Standardised pixel art font to create game/cartoon feel.
        self.fontstyle = 'images/Jersey10-Regular.ttf'
        #pygame functions to create the style of the font and the text within the font.
        self.font = pygame.font.Font(self.fontstyle, fontSize)
        self.textSurf = self.font.render(text, False, fontColor)
        #Rectangle is an attribute that allows for precise positioning
        self.textRect = None

    #Allows for simple english call to center the text at the given position.
    #This is useful for buttons, menu, textbox, etc.
    def centerPosText(self):
        self.textRect = self.textSurf.get_rect(center=self.fontPos)
    
    #Allows for simple english call to display the top left of the text at the font position.
    #This is useful for utilities text.
    def topLeftPosText(self):
        self.textRect = self.textSurf.get_rect(topleft=self.fontPos)

    #This displays the text only statically without change or new input.
    #This is helpful for buttons.
    def displayStaticText(self, screen):
        screen.blit(self.textSurf, self.textRect)

    #Dynamic display allows for the same text to be changed and display a new text.
    def displayDynamicText(self, screen, newText):
        #Edited by AI to render the text again with new text.
        if newText != None:
          self.text = newText
          self.textSurf = self.font.render(self.text, False, self.fontColor)
        screen.blit(self.textSurf, self.textRect)

