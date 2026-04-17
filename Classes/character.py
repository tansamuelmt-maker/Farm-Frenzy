#Where class of character is built
import pygame
from Classes.plant import Plant, Apple, Pear, Banana, Watermelon, Corn, Wheat, plantInfoList
from Classes.text import Text
from Classes.inventory import createInventory, InvMappingPlainText, InvMapping, InvKeys
from Classes.scaleImage import scaleImg
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
  self.characterRect = self.characterImage.get_rect(midbottom= (self.characterXPos,self.characterYPos ))
  screen.blit(self.characterImage, self.characterRect)
 def walkCharacter(self, keyPress):
  if keyPress[pygame.K_a]:
   self.characterImage = self.characterLeft
   self.characterXPos -= 3
  elif keyPress[pygame.K_d]:
   self.characterImage = self.characterRight
   self.characterXPos += 3

 def plantSeed(self, keyPress, plot):
   if keyPress[pygame.K_e] and pygame.KEYDOWN and self.characterRect.colliderect(plot.plotRect) and plot.isEmpty == True and self.selectedSlot != None:
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
    plot.plantedSeed(newPlant)

 def HarvestSeed(self, keyPress,textList, plot):
   if not plot.isEmpty and keyPress[pygame.K_r] and pygame.KEYDOWN and self.characterRect.colliderect(plot.plant.plantRect):
     if plot.plant.isFruiting == True:
      plot.harvestedPlant()
     else: 
      remainingTime = plot.plant.growthTime - (int(pygame.time.get_ticks() / 1000) - plot.plant.plantedTime)
      cantHarvText = Text(20, 'black', f'wait {remainingTime} seconds until you may harvest this', (plot.plant.plantXPos, plot.plant.plantYPos - 100))
      cantHarvText.createFont()
      cantHarvText.centerPosText()
      textList.append(cantHarvText)
 def accessInv(self, keyPress):
    if keyPress in InvKeys:
     self.selectedSlot = InvMapping[keyPress]
     self.inventory[self.selectedSlot].selected = True
     for inventorySlot in self.inventory:
      if inventorySlot.selected == True and self.inventory.index(inventorySlot) != self.selectedSlot:
       inventorySlot.selected = False #Minor aid from AI to edit syntax errors and logical errors
       '''
 def buySeed(self, buyOrder, PlantInfoList):
    if self.money >
    '''
