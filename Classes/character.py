#Imports all necessary classes such as the plant class for planting, the plant info list for inventory information of the plants, text to display warning texts, scale image functions to scale the character image, and guiding text boxes.
#Also imports all necessary mapping from key press to list index so that user can access inventory based on his/her key press.
import pygame
from Classes.plant import Apple, Pear, Banana, Watermelon, Corn, Wheat, plantInfoList
from Classes.text import Text
from Classes.inventory import createInventory, InvMappingPlainText, InvMapping, InvKeys
from Classes.scaleImage import scaleImg
from Classes.textbox import plantText, shopText

pygame.init()
#This is the character class that contains all the attributes of the character such as the image and the rectangle of the character, the starting utilities of money and water, the warning text to guide the character's actions.
#This also contains all the actions the character can do like move around, plant and harvest crops, buy and sell crops, access inventory, access shop, etc.
class Character():
    #No attributes need to be passed into the character
    def __init__(self):
        #Character position is always initialized at the middle of the game, and ensures the character is standing on the floor.
        self.characterXPos = 600
        self.characterYPos = 350
        #The starting utilities are initialized according to problem description, as the starting utilities that the user has to use to win the game.
        self.money = 100
        self.water = 30
        #This creates the starting and empty inventory of the character, the parameter's give information for the item's in the inventory and the key binds to access each inventory slot.
        self.inventory = createInventory(plantInfoList, InvMappingPlainText)
        #This determines which slot is selected by the user, ensuring only 1 slot can be selected at a time. The selected slot displays the information of the slot and allows the user to use the items in the slot for planting.
        self.selectedSlot = None #Used AI's idea for an attribute of selected slot instead of a local variable in a function.
        #This sets the character's movement images when the character moves left and right, the default image of the character and the rectangle of the character which needs to be updated when the character moves.
        self.characterLeft = scaleImg(pygame.image.load('images/farmer_sprite_left.png').convert_alpha(), 0.3)
        self.characterRight = scaleImg(pygame.image.load('images/farmer_sprite_right.png').convert_alpha(), 0.3)
        self.characterImage = self.characterRight
        self.characterRect = None
        # Created by the AI to display warnings when the user lacks the criteria to execute certain actions.
        #This will display a singular warning text always at fixed position and orients the text to be centered, ensuring only one warning is displayed at a time.
        # Warning text: persists across frames so the 2-second timer works correctly
        self.warningMessage = ""
        self.warningTimer = 0
        #Red text to capture the user's attention more easily.
        self.warningTextObj = Text(20, 'red', " ", (600, 150))
        self.warningTextObj.centerPosText()
        # Brief feedback shown in the plot textbox after planting or harvesting
        self.feedbackMessage = ""
        self.feedbackTimer = 0
        #This attributes determines when the shop of the game is displayed based on character's location and the user's key presses.
        self.shopToggled = False

    def _triggerWarning(self, message):
        #This allows for any message to be displayed in the warning.
        self.warningMessage = message
        #This sets the initial time when the warnin was issued:
        self.warningTimer = pygame.time.get_ticks()

    def _drawWarning(self, screen):
        #This draws the warning if there is a warning message and will display the message for the 1 second of elapsed time since the warning has been issued.
        if self.warningMessage and (pygame.time.get_ticks() - self.warningTimer) < 1000:
            self.warningTextObj.displayDynamicText(screen, self.warningMessage)

    #This loads the character at the character's position.
    def displayCharacter(self, screen):
        #Initiates the character's rectangle so that the game can register the character's collision with other objects based on the character's position.
        self.characterRect = self.characterImage.get_rect(midbottom=(self.characterXPos, self.characterYPos))
        screen.blit(self.characterImage, self.characterRect)

    def walkCharacter(self, keyPress):
        #Changes the character's image to face the direction of movement as well as changing the position of the character.
        if keyPress[pygame.K_a]:
            self.characterImage = self.characterLeft
            self.characterXPos -= 3
        elif keyPress[pygame.K_d]:
            self.characterImage = self.characterRight
            self.characterXPos += 3
    def plantSeed(self, keyPress, screen, plotArray):
        # Find first plot the character is standing on
        collidingPlot = None
        for plot in plotArray:
            if self.characterRect.colliderect(plot.plotRect):
                collidingPlot = plot
                break
        if collidingPlot:
            if collidingPlot.isEmpty:
                if self.selectedSlot in range(0, 6) and self.inventory[self.selectedSlot].quantity > 0:
                    if self.water >= plantInfoList[self.selectedSlot][4]:
                        if keyPress[pygame.K_e] and pygame.KEYDOWN:
                            plant_name = self.inventory[self.selectedSlot].plantName
                            match self.selectedSlot:
                                case 0:
                                    collidingPlot.plantedSeed(Apple(collidingPlot.plotXPos, collidingPlot.plotYPos))
                                case 1:
                                    collidingPlot.plantedSeed(Pear(collidingPlot.plotXPos, collidingPlot.plotYPos))
                                case 2:
                                    collidingPlot.plantedSeed(Banana(collidingPlot.plotXPos, collidingPlot.plotYPos))
                                case 3:
                                    collidingPlot.plantedSeed(Watermelon(collidingPlot.plotXPos, collidingPlot.plotYPos))
                                case 4:
                                    collidingPlot.plantedSeed(Corn(collidingPlot.plotXPos, collidingPlot.plotYPos))
                                case 5:
                                    collidingPlot.plantedSeed(Wheat(collidingPlot.plotXPos, collidingPlot.plotYPos))
                            self.inventory[self.selectedSlot].updateQuantity(-1)
                            self.water -= plantInfoList[self.selectedSlot][4]
                            self.feedbackMessage = f"Planted {plant_name}!"
                            self.feedbackTimer = pygame.time.get_ticks()
                    else:
                        if keyPress[pygame.K_e] and pygame.KEYDOWN:
                            self._triggerWarning(f"Cannot plant {self.inventory[self.selectedSlot].plantName}, not enough water!")
                else:
                    if keyPress[pygame.K_e] and pygame.KEYDOWN:
                        self._triggerWarning("Please select an inventory slot with a seed")
            else:
                if keyPress[pygame.K_e] and pygame.KEYDOWN and not (self.feedbackMessage and (pygame.time.get_ticks() - self.feedbackTimer) < 1000):
                    self._triggerWarning("This plot is occupied, plant at another plot")
        else:
            if keyPress[pygame.K_e] and pygame.KEYDOWN:
                self._triggerWarning("Go to an appropriate empty plot to plant")
        self._drawWarning(screen)
    def HarvestFruit(self, keyPress, screen, plotArray):
        # Find first plot the character is standing on
        collidingPlot = None
        for plot in plotArray:
            if self.characterRect.colliderect(plot.plotRect):
                collidingPlot = plot
                break

        if collidingPlot:
            # Priority 1: brief feedback after planting or harvesting
            if self.feedbackMessage and (pygame.time.get_ticks() - self.feedbackTimer) < 1000:
                displayText = self.feedbackMessage
            # Priority 2: empty plot — invite the user to plant
            elif collidingPlot.isEmpty:
                displayText = "Press E to plant"
            # Priority 3: plant is ready to harvest
            elif collidingPlot.plant.isFruiting:
                if keyPress[pygame.K_r] and pygame.KEYDOWN:
                    plant_name = collidingPlot.plant.name
                    match plant_name:
                        case "Apple":
                            self.inventory[6].updateQuantity(1)
                        case "Pear":
                            self.inventory[7].updateQuantity(1)
                        case "Banana":
                            self.inventory[8].updateQuantity(1)
                        case "Watermelon":
                            self.inventory[9].updateQuantity(1)
                        case "Corn":
                            self.inventory[10].updateQuantity(1)
                        case "Wheat":
                            self.inventory[11].updateQuantity(1)
                    collidingPlot.harvestedPlant()
                    self.feedbackMessage = f"Harvested {plant_name}!"
                    self.feedbackTimer = pygame.time.get_ticks()
                    displayText = self.feedbackMessage
                else:
                    displayText = "Press R to harvest"
            # Priority 4: plant is still growing
            else:
                remainingTime = collidingPlot.plant.growthTime - (int(pygame.time.get_ticks() / 1000) - collidingPlot.plant.plantedTime)
                displayText = f"{remainingTime}s until harvest"
                if keyPress[pygame.K_r] and pygame.KEYDOWN:
                    self._triggerWarning(f"Cannot harvest yet! Wait {remainingTime} seconds")

            plantText.updateTextBox(displayText, collidingPlot.plotXPos - 10, collidingPlot.plotYPos - 100)
            plantText.drawTextBox(screen)
        else:
            self.feedbackMessage = ""
            if keyPress[pygame.K_r] and pygame.KEYDOWN:
                self._triggerWarning("Go to a plot with fruiting plants to harvest")
        self._drawWarning(screen)
    #A method tp control what the user can buy based on his/her money.
    #Since the plant info list is mapped on to the inventory, we can use the index of the plant and the inventory slot of the user with just the index of the plant in the plant info list.
    def buySeed(self, plantIndex):
        #Finds the price of the plant
        seedCost = plantInfoList[plantIndex][2]
        #Compares the money of the user and the cost of the plant seed.
        if self.money >= seedCost:
            #Updates the user's money.
            self.money -= seedCost
            self.inventory[plantIndex].updateQuantity(1)
            #Alerts the user of the seed they have bought.
            self._triggerWarning(f"Bought 1 {plantInfoList[plantIndex][0]} seed for ${seedCost}!")
        else:
            #Alerts the user if the user has not enough money to buy the plant seed.
            self._triggerWarning(f"Not enough money! Need ${seedCost}, have ${self.money}")
    #Calculates the value of all the fruits of the user, adds them to the user's money, and removes all fruits of the user.
    def sellFruits(self):
        #Initiates the value of the user's fruits
        sumValue = 0 
        #Since all the fruits are stored between item slots 6 to 12, we can use it as the number of loops for our iteration.
        for index in range(6,12):
            #Totals the value of the items by adding the number of items multiplied by the fruit price of the item into sum value.
            sumValue += self.inventory[index].quantity*plantInfoList[index-6][3]
            self.inventory[index].updateQuantity(-self.inventory[index].quantity)
        #Alerts the user of how much money he/she has earned.
        if sumValue > 0:
            self._triggerWarning(f"You have earned {sumValue} dollars")
            self.money += sumValue
        #Alerts the user if the user has nothing to sell.
        else: 
            self._triggerWarning("You do not have anything to sell")

    #Allows for the user to access the shop through key press when the user's character is colliding with the shop graphic.    
    def accessShop(self, keyPress, screen, shopGraphic, shopMenu):
        if self.characterRect.colliderect(shopGraphic):
            shopText.drawTextBox(screen)
            #Toggles the shop when the user is presses the key G.
            if keyPress[pygame.K_g] and pygame.KEYDOWN:
                self.shopToggled = True
        #If the shop is not near the user, a warning is displayed.
        if self.shopToggled == True:
            shopMenu.displayMenu(screen)
            self._drawWarning(screen)
    #Allows for the user to exit shop when this method is called.
    def exitShop(self):
        self.shopToggled = False

    #Modified by AI to use the for key in Inv Keys.
    def accessInv(self, keyPress):
        """
        Added by AI: Selects an inventory slot based on the player's key press.

        Each key in InvKeys maps to a slot index via InvMapping (e.g. pressing '1'
        selects slot 0). When a mapped key is detected:
          1. self.selectedSlot is updated to the corresponding slot index.
          2. That slot's .selected flag is set to True so it renders as highlighted.
          3. All other slots have their .selected flag cleared, ensuring only one
             slot is active at a time.
          4. The loop breaks immediately — only the first matched key is processed
             per frame, preventing conflicting selections if multiple keys are held.

        Args:
            keyPress: The pygame key state (from pygame.key.get_pressed()), used to
                      check which keys are currently held down.
        """
        for key in InvKeys:
            if keyPress[key]:
                self.selectedSlot = InvMapping[key]
                self.inventory[self.selectedSlot].selected = True
                for inventorySlot in self.inventory:
                    if inventorySlot.selected == True and self.inventory.index(inventorySlot) != self.selectedSlot:
                        inventorySlot.selected = False
                break
    #Updates the water back to thirty at the end of each season. Doesn't need to update for spring since the game ends at that point.
    def updateWater(self, summerRange, autumnRange, winterRange, currentTime):
        if currentTime == summerRange[-1] or currentTime == autumnRange[-1] or currentTime == winterRange[-1]:
            self.water = 30
