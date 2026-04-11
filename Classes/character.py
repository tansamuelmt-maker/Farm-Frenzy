#Where class of character is built
import pygame
from Classes.plant import Plant
pygame.init()
class Character():
 
 def __init__(self, characterImage = pygame.Surface((60,30)), characterXPos = 600, characterYPos = 350, characterCol = 'red', money = 30, water = 30, characterRect = "Not initialized yet"):
  self.characterImage = characterImage
  self.characterXPos = characterXPos
  self.characterYPos = characterYPos
  self.characterCol = characterCol
  self.money = money
  self.water = water
  self.characterRect = characterRect

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

 def plantSeed(self, keyPress, plantList):
  if keyPress[pygame.K_e] and pygame.KEYDOWN:
    newPlant = Plant((self.characterXPos, self.characterYPos), 10)
    plantList.append(newPlant)

 def HarvestSeed(self,)