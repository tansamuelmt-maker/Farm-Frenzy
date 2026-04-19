#Where class of character is built
import pygame
from Classes.plant import Plant, Apple, Pear, Banana, Watermelon, Corn, Wheat, plantInfoList
from Classes.text import Text
from Classes.inventory import createInventory, InvMappingPlainText, InvMapping, InvKeys
from Classes.scaleImage import scaleImg
from Classes.textbox import plantText, HarvText, shopText

pygame.init()

class Character():

    def __init__(self):
        self.characterImage = scaleImg(pygame.image.load('images/farmer_sprite_right.png').convert_alpha(), 0.3)
        self.characterXPos = 600
        self.characterYPos = 350
        self.money = 100
        self.water = 30
        self.characterRect = None
        self.inventory = createInventory(plantInfoList, InvMappingPlainText)
        self.selectedSlot = None
        self.characterLeft = scaleImg(pygame.image.load('images/farmer_sprite_left.png').convert_alpha(), 0.3)
        self.characterRight = scaleImg(pygame.image.load('images/farmer_sprite_right.png').convert_alpha(), 0.3)
        # Warning text: persists across frames so the 2-second timer works correctly
        self.warningMessage = ""
        self.warningTimer = 0
        self.warningTextObj = Text(20, 'red', " ", (600, 150))
        self.warningTextObj.centerPosText()
        # Feedback messages shown in the plot textbox for 2 seconds after an action
        self.plantedMessage = ""
        self.plantedTimer = 0
        self.harvestedMessage = ""
        self.harvestedTimer = 0
        self.shopToggled = False

    def _triggerWarning(self, message):
        self.warningMessage = message
        self.warningTimer = pygame.time.get_ticks()

    def _drawWarning(self, screen):
        if self.warningMessage and (pygame.time.get_ticks() - self.warningTimer) < 2000:
            self.warningTextObj.displayDynamicText(screen, self.warningMessage)

    def displayCharacter(self, screen):
        self.characterRect = self.characterImage.get_rect(midbottom=(self.characterXPos, self.characterYPos))
        screen.blit(self.characterImage, self.characterRect)

    def walkCharacter(self, keyPress):
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
            # Show "just planted" feedback for 2 seconds, regardless of current plot state
            if self.plantedMessage and (pygame.time.get_ticks() - self.plantedTimer) < 2000:
                displayText = self.plantedMessage
            elif collidingPlot.isEmpty:
                if self.selectedSlot in range(0, 6) and self.inventory[self.selectedSlot].quantity > 0:
                    if self.water >= plantInfoList[self.selectedSlot][4]:
                        if keyPress[pygame.K_e]:
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
                            self.plantedMessage = f"Planted {plant_name}!"
                            self.plantedTimer = pygame.time.get_ticks()
                            displayText = self.plantedMessage
                        else:
                            displayText = plantText.baseTextList
                    else:
                        displayText = "Not enough water!"
                        if keyPress[pygame.K_e]:
                            self._triggerWarning(f"Cannot plant {self.inventory[self.selectedSlot].plantName}, not enough water!")
                else:
                    displayText = plantText.baseTextList
                    if keyPress[pygame.K_e]:
                        self._triggerWarning("Please select an inventory slot with a seed")
            else:
                displayText = "Plot is occupied!"
                if keyPress[pygame.K_e]:
                    self._triggerWarning("This plot is occupied, plant at another plot")

            plantText.updateTextBox(displayText, collidingPlot.plotXPos - 10, collidingPlot.plotYPos - 100)
            plantText.drawTextBox(screen)
        else:
            self.plantedMessage = ""
            if keyPress[pygame.K_e]:
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
            # Show "just harvested" feedback for 2 seconds, regardless of current plot state
            if self.harvestedMessage and (pygame.time.get_ticks() - self.harvestedTimer) < 2000:
                displayText = self.harvestedMessage
            elif not collidingPlot.isEmpty:
                if collidingPlot.plant.isFruiting:
                    if keyPress[pygame.K_r]:
                        plant_name = collidingPlot.plant.name  # Capture before harvesting
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
                        self.harvestedMessage = f"Harvested {plant_name}!"
                        self.harvestedTimer = pygame.time.get_ticks()
                        displayText = self.harvestedMessage
                    else:
                        displayText = HarvText.baseTextList
                else:
                    remainingTime = collidingPlot.plant.growthTime - (int(pygame.time.get_ticks() / 1000) - collidingPlot.plant.plantedTime)
                    displayText = f"{remainingTime}s until harvest"
                    if keyPress[pygame.K_r]:
                        self._triggerWarning(f"Cannot harvest yet! Wait {remainingTime} seconds")
            else:
                if keyPress[pygame.K_r]:
                    self._triggerWarning("Nothing to harvest in this plot")
                self._drawWarning(screen)
                return

            HarvText.updateTextBox(displayText, collidingPlot.plotXPos - 10, collidingPlot.plotYPos - 100)
            HarvText.drawTextBox(screen)
        else:
            self.harvestedMessage = ""
            if keyPress[pygame.K_r]:
                self._triggerWarning("Go to a plot with fruiting plants to harvest")

        self._drawWarning(screen)

    def buySeed(self, plantIndex):
        seedCost = plantInfoList[plantIndex][2]
        if self.money >= seedCost:
            self.money -= seedCost
            self.inventory[plantIndex].updateQuantity(1)
            self._triggerWarning(f"Bought 1 {plantInfoList[plantIndex][0]} seed for ${seedCost}!")
        else:
            self._triggerWarning(f"Not enough money! Need ${seedCost}, have ${self.money}")
    
    def sellFruits(self):
        sumValue = 0 
        for index in range(6,12):
            sumValue += self.inventory[index].quantity*plantInfoList[index-6][3]
            self.inventory[index].updateQuantity(-self.inventory[index].quantity)
        if sumValue > 0:
            self._triggerWarning(f"You have earned {sumValue} dollars")
            self.money += sumValue
        else: 
            self._triggerWarning("You do not have anything to sell")
        
    def accessShop(self, keyPress, screen, shopGraphic, shopMenu):
        if self.characterRect.colliderect(shopGraphic):
            shopText.drawTextBox(screen)
            if keyPress[pygame.K_g] and pygame.KEYDOWN:
                self.shopToggled = True
        if self.shopToggled == True:
            shopMenu.displayMenu(screen)
            self._drawWarning(screen)
    
    def exitShop(self):
        self.shopToggled = False



    def accessInv(self, keyPress):
        for key in InvKeys:
            if keyPress[key]:
                self.selectedSlot = InvMapping[key]
                self.inventory[self.selectedSlot].selected = True
                for inventorySlot in self.inventory:
                    if inventorySlot.selected == True and self.inventory.index(inventorySlot) != self.selectedSlot:
                        inventorySlot.selected = False
                break

    def updateWater(self, summerRange, autumnRange, winterRange, springRange, currentTime):
        if currentTime == summerRange[-1] or currentTime == autumnRange[-1] or currentTime == winterRange[-1] or currentTime == springRange[-1]:
            self.water = 30
