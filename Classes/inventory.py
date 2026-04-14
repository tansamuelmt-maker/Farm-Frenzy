#This is where the class of inventory is built
import pygame
class InventorySlot():
    def __init__(self, selected, invXPos, plantName,type,quantity, invYPos = 40,):
        self.selected = selected
        self.invXPos = invXPos
        self.plantName = plantName
        self.type = type
        self.quantity = quantity
        self.invYPos = invYPos
        self.name = f'{plantName} {type}'
    def drawInvSlot(self, screen):
        if self.selected == True:
         pygame.draw.rect(screen, (242, 250, 7), (self.invXPos,self.invYPos, 40,40))
        elif self.selected == False:
         pygame.draw.rect(screen, (102, 95, 95), (self.invXPos,self.invYPos, 40,40))
        pygame.draw.rect(screen, (199, 187, 187), (self.invXPos,self.invYPos,40,40),3)

def createInventory():
    inventorySlots = []
    startingInvXPos = 43
    for x in range(12):
        newSlot = InventorySlot(False, startingInvXPos, "None", "None", 0)
        inventorySlots.append(newSlot)
        startingInvXPos += 43
    return inventorySlots
