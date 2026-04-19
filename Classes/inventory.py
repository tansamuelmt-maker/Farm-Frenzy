#This is where the class of inventory is built
import pygame
from Classes.text import Text
class InventorySlot():
    def __init__(self, selected, invXPos, plantName,type,quantity, itemImage, keyMapping):
        self.selected = selected
        self.invXPos = invXPos
        self.plantName = plantName
        self.type = type
        self.quantity = quantity
        self.itemImage = itemImage
        self.keyMapping = keyMapping
        self.invYPos = 40
        self.name = f'{plantName} {type}'
        self.quantityText = Text(15, 'white', f'{self.quantity}', (self.invXPos + 5, self.invYPos))
        self.selectedText = Text(20, 'white', f'{self.quantity} {self.name}' , (200, 100))
        self.keyMappingText = Text(18, 'white', f'{self.keyMapping}', (self.invXPos +5 ,self.invYPos -20))
        self.itemrect = itemImage.get_rect(center = (self.invXPos+20, self.invYPos+20))
        
    def drawInvSlot(self, screen):
        if self.selected == True:
         if self.selected > 0:
            if self.quantity > 0:
                self.selectedText.displayDynamicText(screen, f'{self.quantity} {self.name}')
         pygame.draw.rect(screen, (242, 250, 7), (self.invXPos,self.invYPos, 40,40))
        elif self.selected == False:
         pygame.draw.rect(screen, (102, 95, 95), (self.invXPos,self.invYPos, 40,40))
        pygame.draw.rect(screen, (199, 187, 187), (self.invXPos,self.invYPos,40,40),3)
        if self.quantity > 0:
           screen.blit(self.itemImage, self.itemrect)
        self.quantityText.displayDynamicText(screen, f'{self.quantity}')
        self.keyMappingText.displayStaticText(screen)

    def updateQuantity(self, changeInQuantity):
       self.quantity += changeInQuantity
       
def createInventory(plantInfoList,KeyMapping):
    inventorySlots = []
    startingInvXPos = 43
    for x in range(6):
        newSlot = InventorySlot(False, startingInvXPos,plantInfoList[x][0], "Seed", 0, plantInfoList[x][5], KeyMapping[x])
        inventorySlots.append(newSlot)
        startingInvXPos += 43
    for x in range(6):
       newSlot = InventorySlot(False, startingInvXPos,plantInfoList[x][0], "Fruit", 0, plantInfoList[x][6], KeyMapping[x+6])
       inventorySlots.append(newSlot)
       startingInvXPos += 43
    return inventorySlots

InvMapping = {
    pygame.K_1: 0,
    pygame.K_2: 1,
    pygame.K_3: 2,
    pygame.K_4: 3,
    pygame.K_5: 4,
    pygame.K_6: 5,
    pygame.K_7: 6,
    pygame.K_8: 7,
    pygame.K_9: 8,
    pygame.K_0 : 9,
    pygame.K_MINUS: 10,
    pygame.K_EQUALS: 11 #Used AI as I was unfamiliar with the keyboard mappings
}

InvKeys = InvMapping.keys()
InvMappingPlainText = ["1","2","3","4","5","6","7","8","9","0","-","="]
