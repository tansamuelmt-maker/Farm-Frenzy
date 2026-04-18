import pygame
from Classes.text import Text
class TextBox():
    def __init__(self, textList, bgBodyColor, bgEdgeColor, textBoxXPos,textBoxYPos):
     self.textList = textList
     self.bgBodyColor = bgBodyColor
     self.bgEdgeColor = bgEdgeColor
     self.textBoxXPos = textBoxXPos
     self.textBoxYPos = textBoxYPos
     self.width = 20
     self.height = 30
     self.textObjects = []
   
    def initializeText(self):
       textPos = (self.textBoxXPos + 5, self.textBoxYPos + 5)
       if isinstance(self.textList, list):  
        for text in self.textList:
          newText = Text(10, "white", text, textPos)
          newText.topLeftPosText()
          self.textObjects.append(newText)
       else:
          newText = Text(10, "white", self.textList, textPos)
          newText.topLeftPosText()
          self.textObjects.append(newText)

    def calculateSize(self):
       for text in self.textList:
          self.height += text.get_height() + 3
          if text.get_width() > self.width:
             self.width += text.get_width() 
         
    def drawTextBox(self, screen):
     pygame.draw.rect(screen, self.bgBodyColor, (self.bgXPos, self.bgYPos, self.width, self.height))
     pygame.draw.rect(screen, self.bgEdgeColor, (self.bgXPos, self.bgYPos, self.width, self.height), 5)
     for text in self.textObjects:
        text.displayStaticText(screen)

    def updateTextBox(self, newTextList, newXPos, newYPos):
       if newTextList != None:
          self.TextList = newTextList
       if newXPos != None and newYPos != None :
          self.textBoxXPos = newXPos
          self.textBoxYPos = newYPos

HarvText = TextBox(None, (237, 147, 69), (240, 182, 132), None, None)
plantText = TextBox("Press E to Plant a seed", (237, 147, 69), (240, 182, 132), 0,0)
plantText.initializeText()
shopInfoText = TextBox(None, (241, 195, 145), (213, 126, 106),None, None)

