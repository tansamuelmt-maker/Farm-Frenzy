#Where class of character is built
import pygame
from Classes.plant import Plant
from Classes.text import Text
from Classes.inventory import createInventory
pygame.init()
class Character():
 
 def __init__(self, characterImage = pygame.Surface((20,30)), characterXPos = 600, characterYPos = 350, characterCol = 'red', money = 30, water = 30, characterRect = "Not initialized yet"):
  self.characterImage = characterImage
  self.characterXPos = characterXPos
  self.characterYPos = characterYPos
  self.characterCol = characterCol
  self.money = money
  self.water = water
  self.characterRect = characterRect
  self.inventory = createInventory()

 def displayCharacter(self, screen):
  self.characterImage.fill(self.characterCol)
  self.characterRect = self.characterImage.get_rect(midbottom= (self.characterXPos,self.characterYPos ))
  screen.blit(self.characterImage, self.characterRect)
  
 def walkCharacter(self, keyPress):
  self.characterCol = 'red'
  if keyPress[pygame.K_a]:
   self.characterCol = 'white'
   self.characterXPos -= 3
  elif keyPress[pygame.K_d]:
   self.characterCol = 'white'
   self.characterXPos += 3

 def plantSeed(self, keyPress, plot):
   if keyPress[pygame.K_e] and pygame.KEYDOWN and self.characterRect.colliderect(plot.plotRect) and plot.isEmpty == True:
    newPlant = Plant(plot.plotXPos, plot.plotYPos, 10)
    plot.plantedSeed()

 def HarvestSeed(self, keyPress,textList, plot):
   if not plot.isEmpty and keyPress[pygame.K_r] and pygame.KEYDOWN and self.characterRect.colliderect(plot.plant.plantRect):
     if plot.plant.isFruiting == True:
      plot.harvestedPlant()
     else: 
      remainingTime = plot.plant.growthTime - (int(pygame.time.get_ticks() / 1000) - plot.plant.plantedTime)
      cantHarvText = Text(20, 'black', f'wait {remainingTime} seconds until you may harvest this', (plot.plant.plantXPos, plot.plant.plantYPos - 50))
      cantHarvText.createFont()
      textList.append(cantHarvText)
 def accessInv(self, keyPress, keyPressMapping, keyPressMappingKeys):
    if keyPress in keyPressMappingKeys:
     selectedSlot = keyPressMapping[keyPress]
     self.inventory[selectedSlot].selected = True
     for inventorySlot in self.inventory:
      if inventorySlot.selected == True and self.inventory.index(inventorySlot) != selectedSlot:
       inventorySlot.selected = False #Minor aid from AI to edit syntax errors and logical errors
