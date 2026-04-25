import pygame
from Classes.text import Text
from Classes.plant import plantInfoList

#Almost all code has been added/fixed by AI.
#Text boxes display text in its own rectangle, thus making the text more readable and eye-catching.
class TextBox():
    def __init__(self, textList, textsize, bgBodyColor, bgEdgeColor, textBoxXPos, textBoxYPos, image, imagePos=None):
        #Allows for large and indeterminant amounts of text through storing all text in a list.
        self.textList = textList
        #Added by AI, stores the base text list that the text box reverts to after dynamic actions.
        self.baseTextList = textList  # Never changes — used for dynamic display comparison.
        self.textSize = textsize
        self.bgBodyColor = bgBodyColor
        self.bgEdgeColor = bgEdgeColor
        self.textBoxXPos = textBoxXPos
        self.textBoxYPos = textBoxYPos
        self.image = image
        #This allows the program to not add another attribute for text position if image itself is not added.
        self.imagePos = None if image is None else imagePos
        self.width = 20
        self.height = 30
        self.textObjects = []
        self.tempDisplayStart = None
        self.tempText = None
        #Initializes the text during instantiation, removing need to instantiate text.
        if textList is not None:
            self.initializeText()

    def initializeText(self):
        # Clear previous state and recompute dimensions from rendered surfaces
        self.textObjects = []
        self.width = 20
        self.height = 10
        currentY = self.textBoxYPos + 5
        #Checks whether or not texts is list.
        texts = self.textList if isinstance(self.textList, list) else [self.textList]
        #calculates the necessary width and height of the text box to fit all the text within it.
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
    #Displays the text box and image with the text box if necessary.
    def drawTextBox(self, screen):
        pygame.draw.rect(screen, self.bgBodyColor, (self.textBoxXPos, self.textBoxYPos, self.width, self.height))
        pygame.draw.rect(screen, self.bgEdgeColor, (self.textBoxXPos, self.textBoxYPos, self.width, self.height), 5)
        if self.image != None:
            screen.blit(self.image, self.imagePos)
        for text in self.textObjects:
            text.displayStaticText(screen)

    #Modified by AI: Updates the text box's text content and position.
    def updateTextBox(self, newTextList, newXPos, newYPos):
        changed = False
        #Changes textlist if there is a new and unique text list to add.
        if newTextList is not None and newTextList != self.textList:
            self.textList = newTextList
            changed = True
        #Changes the text box's psoition if there is a new and unique position.
        if newXPos is not None and newYPos is not None:
            if self.textBoxXPos != newXPos or self.textBoxYPos != newYPos:
                self.textBoxXPos = newXPos
                self.textBoxYPos = newYPos
                changed = True
        #Recalculates text and initializes text if the text box has been changed.
        if changed:
            self.initializeText()
    #This displays the text box based on the position it has to be at and the text is has to display.
    def displayDynamicTextBox(self, tempText, screen, newXPos, newYPos):
        if tempText != self.baseTextList:
            #Start or continue timer for temporary text.
            if self.tempDisplayStart is None or self.tempText != tempText:
                self.tempDisplayStart = pygame.time.get_ticks()
                self.tempText = tempText
                #Displays the temporary text for a duration of 1 second.
            elapsedTime = (pygame.time.get_ticks() - self.tempDisplayStart) / 1000
            if elapsedTime < 1:
                self.updateTextBox(tempText, newXPos, newYPos)
                self.drawTextBox(screen)
            else:
                #Timer expired — revert to base text.
                self.tempDisplayStart = None
                self.tempText = None
                self.updateTextBox(self.baseTextList, newXPos, newYPos)
                self.drawTextBox(screen)
        #Displays the original text afer temporary display.
        else:
            self.tempDisplayStart = None
            self.tempText = None
            self.updateTextBox(self.baseTextList, newXPos, newYPos)
            self.drawTextBox(screen)

#Text boxes to guide users on planting, harvesting and accessing the shop.
plantText = TextBox("Press E to plant", 20, (237, 147, 69), (240, 182, 132), 0, 0, None)
shopText = TextBox("Press G to access shop", 20, (237, 147, 69), (240, 182, 132), 1000, 200, None)
shopInfoTextBoxList = []

#This displays all the information of every plant the user can buy.
for index in range(len(plantInfoList)):
    #Information of seed price, fruit price, water expenses after planting, and time it takes for the plant to grow to harvesting stage.
    infoText1 = f"Time to grow: {plantInfoList[index][1]}              water cost to plant: {plantInfoList[index][4]}"
    infoText2 = f"seed price: ${plantInfoList[index][2]}               fruit sells for: ${plantInfoList[index][3]}"
    infoTextList = [infoText1, infoText2]
    #Creates a text box with the plant information, position of 0,0 as there is no starting position.
    shopInfoText = TextBox(infoTextList, 20, (241, 195, 145), (213, 126, 106), 0, 0, None)
    #Adds every shop info text into the list.
    shopInfoTextBoxList.append(shopInfoText)