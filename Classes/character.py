#Where class of character is built
import pygame
from Classes.plant import Plant, Apple, Pear, Banana, Watermelon, Corn, Wheat, plantInfoList
from Classes.text import Text
from Classes.inventory import createInventory, InvMappingPlainText, InvMapping, InvKeys
from Classes.scaleImage import scaleImg
from Classes.textbox import plantText, HarvText

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

    def _addTempText(self, textList, newText):
        textList[:] = [t for t in textList if t.tag is None or t.tag != newText.tag]
        textList.append(newText)

    def plantSeed(self, keyPress, textList, plotArray):
        if not (keyPress[pygame.K_e] and pygame.KEYDOWN):
            return
        collidingPlots = [p for p in plotArray if self.characterRect.colliderect(p.plotRect)]
        if not collidingPlots:
            return
        for plot in collidingPlots:
            if plot.isEmpty:
                if not (self.selectedSlot in range(0, 6) and self.inventory[self.selectedSlot].quantity):
                    msg = Text(30, 'red', 'Please select an inventory slot with at least 1 seed', (600, 150), tag='plant_error')
                    msg.centerPosText()
                    self._addTempText(textList, msg)
                elif self.water <= plantInfoList[self.selectedSlot][4]:
                    msg = Text(30, 'red', 'Not enough water to plant, wait until next season', (600, 150), tag='plant_error')
                    msg.centerPosText()
                    self._addTempText(textList, msg)
                else:
                    match self.selectedSlot:
                        case 0:
                            newPlant = Apple(plot.plotXPos, plot.plotYPos)
                        case 1:
                            newPlant = Pear(plot.plotXPos, plot.plotYPos)
                        case 2:
                            newPlant = Banana(plot.plotXPos, plot.plotYPos)
                        case 3:
                            newPlant = Watermelon(plot.plotXPos, plot.plotYPos)
                        case 4:
                            newPlant = Wheat(plot.plotXPos, plot.plotYPos)
                        case 5:
                            newPlant = Corn(plot.plotXPos, plot.plotYPos)
                    self.inventory[self.selectedSlot].updateQuantity(-1)
                    plot.plantedSeed(newPlant)
                    self.water -= plantInfoList[self.selectedSlot][4]
                return

    def HarvestSeed(self, keyPress, textList, plotArray):
        if not (keyPress[pygame.K_r] and pygame.KEYDOWN):
            return
        for plot in plotArray:
            if not plot.isEmpty and self.characterRect.colliderect(plot.plant.plantRect):
                if plot.plant.isFruiting == True:
                    plot.harvestedPlant()
                else:
                    remainingTime = plot.plant.growthTime - (int(pygame.time.get_ticks() / 1000) - plot.plant.plantedTime)
                    msg = Text(30, 'red', f'wait {remainingTime} seconds until you may harvest this', (600, 150), tag='harvest_error')
                    msg.centerPosText()
                    self._addTempText(textList, msg)
                return

    def accessInv(self, keyPress):
        if keyPress in InvKeys:
            self.selectedSlot = InvMapping[keyPress]
            self.inventory[self.selectedSlot].selected = True
            for inventorySlot in self.inventory:
                if inventorySlot.selected == True and self.inventory.index(inventorySlot) != self.selectedSlot:
                    inventorySlot.selected = False  #Minor aid from AI to edit syntax errors and logical errors
    
   

    def updateWater(self, summerRange, autumnRange, winterRange, springRange, currentTime):
        if currentTime == summerRange[-1] or currentTime == autumnRange[-1] or currentTime == winterRange[-1] or currentTime == springRange[-1]:
            self.Water = 30
