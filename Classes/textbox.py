import pygame
from Classes.text import Text
from Classes.plant import plantInfoList

class TextBox():
    def __init__(self, textList, textsize, bgBodyColor, bgEdgeColor, textBoxXPos, textBoxYPos, image, imagePos=None):
        self.textList = textList
        self.baseTextList = textList  # Never changes — used for dynamic display comparison
        self.textSize = textsize
        self.bgBodyColor = bgBodyColor
        self.bgEdgeColor = bgEdgeColor
        self.textBoxXPos = textBoxXPos
        self.textBoxYPos = textBoxYPos
        self.image = image
        self.imagePos = None if image is None else imagePos
        self.width = 20
        self.height = 30
        self.textObjects = []
        self.tempDisplayStart = None
        self.tempText = None
        if textList is not None:
            self.initializeText()

    def initializeText(self):
        # Clear previous state and recompute dimensions from rendered surfaces
        self.textObjects = []
        self.width = 20
        self.height = 10
        currentY = self.textBoxYPos + 5
        texts = self.textList if isinstance(self.textList, list) else [self.textList]
        for text in texts:
            newText = Text(self.textSize, "white", str(text), (self.textBoxXPos + 5, currentY))
            newText.topLeftPosText()
            self.textObjects.append(newText)
            textH = newText.textSurf.get_height()
            textW = newText.textSurf.get_width()
            self.height += textH + 3
            if textW + 10 > self.width:
                self.width = textW + 10
            currentY += textH + 3

    def drawTextBox(self, screen):
        pygame.draw.rect(screen, self.bgBodyColor, (self.textBoxXPos, self.textBoxYPos, self.width, self.height))
        pygame.draw.rect(screen, self.bgEdgeColor, (self.textBoxXPos, self.textBoxYPos, self.width, self.height), 5)
        if self.image != None:
            screen.blit(self.image, self.imagePos)
        for text in self.textObjects:
            text.displayStaticText(screen)

    def updateTextBox(self, newTextList, newXPos, newYPos):
        changed = False
        if newTextList is not None and newTextList != self.textList:
            self.textList = newTextList
            changed = True
        if newXPos is not None and newYPos is not None:
            if self.textBoxXPos != newXPos or self.textBoxYPos != newYPos:
                self.textBoxXPos = newXPos
                self.textBoxYPos = newYPos
                changed = True
        if changed:
            self.initializeText()

    def displayDynamicTextBox(self, tempText, screen, newXPos, newYPos):
        if tempText != self.baseTextList:
            # Start or continue timer for temporary text
            if self.tempDisplayStart is None or self.tempText != tempText:
                self.tempDisplayStart = pygame.time.get_ticks()
                self.tempText = tempText
            elapsedTime = (pygame.time.get_ticks() - self.tempDisplayStart) / 1000
            if elapsedTime < 1:
                self.updateTextBox(tempText, newXPos, newYPos)
                self.drawTextBox(screen)
            else:
                # Timer expired — revert to base text
                self.tempDisplayStart = None
                self.tempText = None
                self.updateTextBox(self.baseTextList, newXPos, newYPos)
                self.drawTextBox(screen)
        else:
            self.tempDisplayStart = None
            self.tempText = None
            self.updateTextBox(self.baseTextList, newXPos, newYPos)
            self.drawTextBox(screen)


HarvText = TextBox("Press R to harvest a seed", 20, (237, 147, 69), (240, 182, 132), 0, 0, None)
plantText = TextBox("Press E to Plant a seed", 20, (237, 147, 69), (240, 182, 132), 0, 0, None)
shopText = TextBox("Press G to access shop", 20, (237, 147, 69), (240, 182, 132), 1000, 200, None)
shopInfoTextBoxList = []

for index in range(len(plantInfoList)):
    infoText1 = f"Time to grow: {plantInfoList[index][1]}              water cost to plant: {plantInfoList[index][4]}"
    infoText2 = f"seed price: ${plantInfoList[index][2]}               fruit sells for: ${plantInfoList[index][3]}"
    infoTextList = [infoText1, infoText2]
    shopInfoText = TextBox(infoTextList, 20, (241, 195, 145), (213, 126, 106), 0, 0, None)
    shopInfoTextBoxList.append(shopInfoText)