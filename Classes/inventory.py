#This is where the class of inventory is built
import pygame
from Classes.text import Text
#Class of a single inventory slot
class InventorySlot():
    '''
    Attributes contain the information on whether the slot is selected, the information of the item to be stored in the slot
    the quantity of the items in the slot, and the kay press to select the slot.
    '''
    
    def __init__(self, selected, invXPos, plantName,itemtype,quantity, itemImage, keyMapping):
        #Boolean value of whether the slot is selected.
        self.selected = selected
        #Takes in the unique position of every slot.
        self.invXPos = invXPos
        #Takes in the name of the plant which the slot is mapped to.
        self.plantName = plantName
        #Takes in the type of item the slot holds, whether it be fruit or seed.
        self.itemtype = itemtype
        #Stores the quantity of the items in the slot
        self.quantity = quantity
        #Takes in the item image of the item in the slot to be displayed.
        self.itemImage = itemImage
        #Takes in the keybind of the item slot that will be displayed.
        self.keyMapping = keyMapping
        #Fixed Y position as inventory slots are lined up side by side horizontally.
        self.invYPos = 40
        self.name = f'{plantName} {type}'
        #Texts regarding the information of the slot are instantiated as text objects.
        self.quantityText = Text(15, 'white', f'{self.quantity}', (self.invXPos + 5, self.invYPos))
        self.selectedText = Text(20, 'white', f'{self.quantity} {self.name}' , (200, 100))
        self.keyMappingText = Text(18, 'white', f'{self.keyMapping}', (self.invXPos +5 ,self.invYPos -20))
        #Rectangle of item is calculated to be in the center of slot so item is displayed in the center of the slot.
        self.itemrect = itemImage.get_rect(center = (self.invXPos+20, self.invYPos+20))
    
    #Draws the inventory slot, inventory image and the inventory texts.
    def drawInvSlot(self, screen):
        #Draws the name of the item and colors the slot yellow if the slot is selected and has items in it. 
        #This allows users to know more about the item they are selecting.
        if self.selected == True:
         if self.selected > 0:
            if self.quantity > 0:
                self.selectedText.displayDynamicText(screen, f'{self.quantity} {self.name}')
         pygame.draw.rect(screen, (242, 250, 7), (self.invXPos,self.invYPos, 40,40))
        elif self.selected == False:
         #Displays the item slot and the border around the itemslot.
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
