import pygame
from Classes.textbox import TextBox
from Classes.scaleImage import scaleImg
#This is a child class of the text box, its only difference is the standardized color scheme.
class Tutorial(TextBox):
    def __init__(self, textList, textSize, textBoxXPos, textBoxYPos, image, imagePos=None):
        super().__init__(textList, textSize, (45, 235, 149), (148, 247, 203), textBoxXPos, textBoxYPos, image, imagePos)

#Intro text is created to give users the basic premise of the game.
introTutorialText = ["Welcome to Farm-Frenzy!",
                     "In this game, your goal is to earn money from planting and growing crops",
                     "If you can earn $500 ($600 total) before the time turns 400 you win!",
                     "Press T to continue to next tutorial"]

#First movement text is created to give the user knowledge on how to move left.
movementTutorialText1 = ["In order to move left press A",
                         "Press T to continue to next tutorial"]

#Second movement text is created to give the user knowledge on how to move right.
movementTutorialText2 = ["In order to move right press D",
                         "Press T to continue to next tutorial"]

#Planting text gives the user an idea on how and where to plant.
plantTutorialText = ["Look under the red arrow now, those brown rectangles are plots",
                     "In order to plant a crop, you must have a plant seed, and be standing on an empty plot",
                     "Then, with enough water, you may plant the crop by pressing E",
                     "Press T to continue to next tutorial"]

#Harvest text gives the user an idea on how to harvest the plants.
harvTutorialText = ["When your plant is ready to harvest, press R to harvest it",
                    "That is how you collect your crops to earn money",
                    "Press T to continue to next tutorial"]

#Inventory text 1 gives the user information of how to access the inventory slot
inventoryTutorialText1 = ["Look at your inventory at the top left",
                           "Above the inventory slots are the keys to press that allow you to select the inventory slot below it",
                           "Press T to continue to next tutorial"]

#Inventory text 2 gives the user information about how he/she can identify the quantity of each item in the inventory slots.
inventoryTutorialText2 = ["Look at the zeroes to the top right of the inventory",
                           "This is the quantity of each item you have",
                           "Press T to continue to next tutorial"]

#Utilities text points out and explains the utilities of the user
utilitiesTutorialText = ["Look over at the top right",
                         "Those three texts allow you to see how much money and water you have,",
                         "as well as the game's time",
                         "Your water will be deducted every time you plant",
                         "However it resets back to 30 every season",
                         "Press T to continue to next tutorial"]

#Shop tutorial gives a lengthy explanation of the shop and its functionality.
shopTutorialText = ["Look under the arrow now, that's a shop",
                    "To access the shop, simply stand next to it and press G",
                    "This allows you to enter the shop menu to buy seeds to plant,",
                    "sell crops, and check out information about each plant you're buying",
                    "This is your final tutorial, press T to exit and start playing!"]

#Each tutorial is instantiated individually with a unique arrow to guide the user and point out areas of interest.
introTutorial      = Tutorial(introTutorialText,      24, 300, 100, None)
movementTutorial1  = Tutorial(movementTutorialText1,  24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_left.png'), 0.3),  (450, 260))
movementTutorial2  = Tutorial(movementTutorialText2,  24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_right.png'), 0.3),  (650, 260))
plantTutorial      = Tutorial(plantTutorialText,      24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_down.png'), 0.3),  (700, 230))
harvTutorial       = Tutorial(harvTutorialText,       24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_down.png'), 0.3),  (700, 230))
inventoryTutorial1 = Tutorial(inventoryTutorialText1, 24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_left.png'), 0.18), (525, 0))
inventoryTutorial2 = Tutorial(inventoryTutorialText2, 24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_left.png'), 0.2),  (525, 12))
utilitiesTutorial  = Tutorial(utilitiesTutorialText,  24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_right.png'), 0.3),  (1000, 30))
shopTutorial       = Tutorial(shopTutorialText,       24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_down.png'), 0.3),  (1050, 150))

#All these tutorials are added into a list for easy access and selection of tutorials.
gameTutorial = [introTutorial, movementTutorial1, movementTutorial2, plantTutorial,
                harvTutorial, inventoryTutorial1, inventoryTutorial2, utilitiesTutorial, shopTutorial]

#Edited by AI:
#Displaying the tutorial is a method which is only called at the start of the game, and allows for each tutorial to be displayed for however long the user wants.
def displayTutorial(gameState, screen, keyPress):
    index = gameState['tutorialIndex']
    #Uses an if statement to display tutorial for an indeterminant amount of time but with a determined number of tutorials.
    if index < len(gameTutorial):
        gameTutorial[index].drawTextBox(screen)
        if keyPress[pygame.K_t] and gameState['tKeyWasUp']: 
            # triggers the next tutorial by incrementing the index of tutorials that are displayed when user presses T
            gameState['tutorialIndex'] += 1
            gameState['tKeyWasUp'] = False
            #tKeyWas up allows for only one tutorial to be skipped at a time.
        if not keyPress[pygame.K_t]:
            gameState['tKeyWasUp'] = True
    #Stops displaying tutorials once all tutorials have been skipped.
    else:
        gameState['tutorialActive'] = False
