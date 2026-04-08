#Where class of character is built
import pygame
class Character():
 def __init__(self, characterImage = pygame.Surface((60,30)), characterXPos = 600, characterYPos = 320, characterCol = 'red'):
  self.characterImage = characterImage
  self.characterXPos = characterXPos
  self.characterYPos = characterYPos
  self.characterCol = characterCol
 def displayCharacter(self, screen):
  self.characterImage.fill(self.characterCol)
  screen.blit(self.characterImage, (self.characterXPos,self.characterYPos))
 def walkCharacter(self, keyPress):
  self.characterCol = 'red'
  if keyPress[pygame.K_a]:
   self.characterCol = 'white'
   self.characterXPos -= 3
  elif keyPress[pygame.K_d]:
   self.characterCol = 'white'
   self.characterXPos += 3