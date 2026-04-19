import pygame
from Classes.textbox import TextBox
from Classes.scaleImage import scaleImg

class Tutorial(TextBox):
    def __init__(self, textList, textSize, textBoxXPos, textBoxYPos, image, imagePos=None):
        super().__init__(textList, textSize, (45, 235, 149), (148, 247, 203), textBoxXPos, textBoxYPos, image, imagePos)

introTutorialText = ["Welcome to Farm-Frenzy!",
                     "In this game, your goal is to earn money from planting and growing crops",
                     "If you can earn $500 before the time turns 400 you win!",
                     "Press T to continue to next tutorial"]
movementTutorialText1 = ["In order to move left press A",
                         "Press T to continue to next tutorial"]
movementTutorialText2 = ["In order to move right press D",
                         "Press T to continue to next tutorial"]
plantTutorialText = ["Look under the red arrow now, those brown rectangles are plots",
                     "In order to plant a crop, you must have a plant seed, and be standing on an empty plot",
                     "Then, with enough water, you may plant the crop by pressing E",
                     "Press T to continue to next tutorial"]
harvTutorialText = ["When your plant is ready to harvest, press R to harvest it",
                    "That is how you collect your crops to earn money",
                    "Press T to continue to next tutorial"]
inventoryTutorialText1 = ["Look at your inventory at the top left",
                           "Above the inventory slots are the keys to press that allow you to select the inventory slot below it",
                           "Press T to continue to next tutorial"]
inventoryTutorialText2 = ["Look at the zeroes to the top right of the inventory",
                           "This is the quantity of each item you have",
                           "Press T to continue to next tutorial"]
utilitiesTutorialText = ["Look over at the top right",
                         "Those three texts allow you to see how much money and water you have,",
                         "as well as the game's time",
                         "Press T to continue to next tutorial"]
shopTutorialText = ["Look under the arrow now, that's a shop",
                    "To access the shop, simply stand next to it and press G",
                    "This allows you to enter the shop menu to buy seeds to plant,",
                    "sell crops, and check out information about each plant you're buying",
                    "This is your final tutorial, press T to exit and start playing!"]

introTutorial      = Tutorial(introTutorialText,      24, 300, 100, None)
movementTutorial1  = Tutorial(movementTutorialText1,  24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_left.png'), 0.3),  (450, 260))
movementTutorial2  = Tutorial(movementTutorialText2,  24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_right.png'), 0.3),  (650, 260))
plantTutorial      = Tutorial(plantTutorialText,      24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_down.png'), 0.3),  (700, 230))
harvTutorial       = Tutorial(harvTutorialText,       24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_down.png'), 0.3),  (700, 230))
inventoryTutorial1 = Tutorial(inventoryTutorialText1, 24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_left.png'), 0.18), (525, 0))
inventoryTutorial2 = Tutorial(inventoryTutorialText2, 24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_left.png'), 0.2),  (525, 12))
utilitiesTutorial  = Tutorial(utilitiesTutorialText,  24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_right.png'), 0.3),  (1000, 30))
shopTutorial       = Tutorial(shopTutorialText,       24, 300, 100, scaleImg(pygame.image.load('images/red_arrow_down.png'), 0.3),  (1050, 150))

gameTutorial = [introTutorial, movementTutorial1, movementTutorial2, plantTutorial,
                harvTutorial, inventoryTutorial1, inventoryTutorial2, utilitiesTutorial, shopTutorial]

def displayTutorial(gameState, screen, keyPress):
    index = gameState['tutorialIndex']
    if index < len(gameTutorial):
        gameTutorial[index].drawTextBox(screen)
        if keyPress[pygame.K_t] and gameState['tKeyWasUp']:
            gameState['tutorialIndex'] += 1
            gameState['tKeyWasUp'] = False
        if not keyPress[pygame.K_t]:
            gameState['tKeyWasUp'] = True
    else:
        gameState['tutorialActive'] = False
