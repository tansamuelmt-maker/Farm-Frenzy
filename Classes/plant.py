#This is where the class of plants is built
import pygame
from Classes.scaleImage import scaleImg

#Base plant class
class Plant():
    #Attributes allow for a unique x and y position, as well as marking down the time the plant has been planted.
    def __init__(self, plantXPos, plantYPos):
        self.plantXPos = plantXPos
        self.plantYPos = plantYPos
        #Marks the time when the plant class was instantiated
        self.plantedTime = int(pygame.time.get_ticks() / 1000)
        #non-functional attributes but are used to give new programmer the meaning of each attributes.
        self.growthImage1 = "Seedling stage"
        self.growthImage2 = "Stem stage"
        self.growthImage3= "Fruiting stage"
        #Shows new programmers all important attributes each plant class will have.
        self.isFruiting = False
        self.plantImage = "image of fruit"
        self.seedImage = "image of seed"
        self.plantRect = None
        self.fruitPrice = "Price that fruit is sold"
        self.seedCost = "Price to buy the seed"
        self.waterCost = "water that is consumed when seed is planted."
        self.growthTime = "Time it takes for plant to grow from seedling to fruiting"
    #Displays the stages of the plant as it grows, and determines when plant can be harvested.

    def growPlant(self):
        #This tracks the time elapsed since the plant has been planted
        elapsedTime = (pygame.time.get_ticks() / 1000) - self.plantedTime
        #This displays a unique stage of the plant based on the time it has been growing.
        if elapsedTime > self.growthTime:
            self.plantImage = self.growthImage3
            #Allows for plant to be harvested when plant is fully grown.
            self.isFruiting = True
        elif elapsedTime > (0.5*self.growthTime):
            self.plantImage = self.growthImage2
        elif elapsedTime < (0.5*self.growthTime):
            self.plantImage = self.growthImage1
        #Changes the rectangle of the plant based on the image to keep the plant at the same position always.
        self.plantRect = self.plantImage.get_rect(midbottom = (self.plantXPos, self.plantYPos))

    #Displays the plant and the stage of its growth.
    def displayPlant(self, screen):
        screen.blit(self.plantImage, self.plantRect)

#Child classes of the plant, each with their unique costs, prices, images, and names
class Apple(Plant):
    #Apple class is a plant that takes longer to grow, more water to grow but yields more money.
    def __init__(self, plantXPos, plantYPos):
        super().__init__(plantXPos, plantYPos)
        #Defines its own unique growth stages to be displayed
        self.growthImage1 = scaleImg(pygame.image.load('images/apple_stage1_seedling.png').convert_alpha(), 0.2)
        self.growthImage2 = scaleImg(pygame.image.load('images/apple_stage2_sapling.png').convert_alpha(), 0.2)
        self.growthImage3 = scaleImg(pygame.image.load('images/apple_stage4_fruiting.png').convert_alpha(), 0.2)
        #Defines its own name for reference in inventory/shop
        self.name = "Apple"
        #Has unique stats that differ from other plants.
        self.growthTime = 45
        self.fruitPrice = 45
        self.seedCost = 24
        self.waterCost = 4
        #Fruit image and seed image for display on shops and inventory
        self.fruitImage = scaleImg(pygame.image.load('images/apple_fruit.png').convert_alpha(), 0.05)
        self.seedImage = scaleImg(pygame.image.load('images/apple_seed.png').convert_alpha(), 0.05)

class Pear(Plant):
    #Pear class is a plant similiar to apple, but is quicker and less costly to grow however it returns less money.
    def __init__(self, plantXPos, plantYPos):
        super().__init__(plantXPos, plantYPos)
        self.growthImage1 = scaleImg(pygame.image.load('images/pear_stage1_seedling.png').convert_alpha(), 0.2)
        self.growthImage2 = scaleImg(pygame.image.load('images/pear_stage2_sapling.png').convert_alpha(), 0.2)
        self.growthImage3 = scaleImg(pygame.image.load('images/pear_stage4_fruiting.png').convert_alpha(), 0.2)
        self.name = "Pear"
        self.growthTime = 35
        self.fruitPrice = 33
        self.seedCost = 20
        self.waterCost = 3
        self.fruitImage = scaleImg(pygame.image.load('images/pear_fruit.png').convert_alpha(),0.05)
        self.seedImage = scaleImg(pygame.image.load('images/pear_seed.png').convert_alpha(),0.05)

class Banana(Plant):
    #Banana is a plant that returns high profit in a short amount of time yet consumes lots of water
    def __init__(self, plantXPos, plantYPos):
        super().__init__(plantXPos, plantYPos)
        self.growthImage1 = scaleImg(pygame.image.load('images/banana_stage1_seedling.png').convert_alpha(), 0.15)
        self.growthImage2 = scaleImg(pygame.image.load('images/banana_stage2_stem.png').convert_alpha(), 0.1)
        self.growthImage3 = scaleImg(pygame.image.load('images/banana_stage3_fruiting.png').convert_alpha(), 0.1)
        self.name = "Banana"
        self.growthTime = 20
        self.fruitPrice = 38
        self.seedCost = 15
        self.waterCost = 5
        self.fruitImage = scaleImg(pygame.image.load('images/banana_fruit.png').convert_alpha(), 0.05)
        self.seedImage = scaleImg(pygame.image.load('images/banana_seed.png').convert_alpha(), 0.05)

class Watermelon(Plant):
    #Similiar to banana class, but more costly and takes longer to grow.
    def __init__(self, plantXPos, plantYPos):
        super().__init__(plantXPos, plantYPos)
        self.growthImage1 = scaleImg(pygame.image.load('images/watermelon_stage1_seedling.png').convert_alpha(), 0.15)
        self.growthImage2 = scaleImg(pygame.image.load('images/watermelon_stage2_vine.png').convert_alpha(), 0.1)
        self.growthImage3 = scaleImg(pygame.image.load('images/watermelon_stage3_fruiting.png').convert_alpha(), 0.1)
        self.name = "Watermelon"
        self.growthTime = 25
        self.fruitPrice = 43
        self.seedCost = 17
        self.waterCost = 5
        self.fruitImage = scaleImg(pygame.image.load('images/watermelon_fruit.png').convert_alpha(), 0.05)
        self.seedImage = scaleImg(pygame.image.load('images/watermelon_seed.png').convert_alpha(), 0.05)

class Corn(Plant):
    #Corn grows extremely fast for cheap but returns little money.
    def __init__(self, plantXPos, plantYPos):
        super().__init__(plantXPos, plantYPos)
        self.growthImage1 = scaleImg(pygame.image.load('images/corn_stage1_seedling.png').convert_alpha(), 0.15)
        self.growthImage2 = scaleImg(pygame.image.load('images/corn_stage2_stem.png').convert_alpha(), 0.1)
        self.growthImage3 = scaleImg(pygame.image.load('images/corn_stage3_mature.png').convert_alpha(), 0.1)
        self.name = "Corn"
        self.growthTime = 13
        self.fruitPrice = 15
        self.seedCost = 7
        self.waterCost = 1
        self.fruitImage = scaleImg(pygame.image.load('images/corn_fruit.png').convert_alpha(), 0.05)
        self.seedImage = scaleImg(pygame.image.load('images/corn_seed.png').convert_alpha(), 0.05)

class Wheat(Plant):
    #Wheat is similiar to corn but even cheaper and returns even less money.
    def __init__(self, plantXPos, plantYPos):
        super().__init__(plantXPos, plantYPos)
        self.growthImage1 = scaleImg(pygame.image.load('images/wheat_stage1_seedling.png').convert_alpha(), 0.15)
        self.growthImage2 = scaleImg(pygame.image.load('images/wheat_stage2_stem.png').convert_alpha(), 0.1)
        self.growthImage3 = scaleImg(pygame.image.load('images/wheat_stage3_mature.png').convert_alpha(), 0.1)
        self.name = "Wheat"
        self.growthTime = 9
        self.fruitPrice = 14
        self.seedCost = 7
        self.waterCost = 1
        self.fruitImage = scaleImg(pygame.image.load('images/wheat_fruit.png').convert_alpha(), 0.05)
        self.seedImage = scaleImg(pygame.image.load('images/wheat_seed.png').convert_alpha(), 0.05)
     
#Creates a reference for plant information of all plants.
def createPlantInfoList():
    #Instantiates each plant to get all information, does not give coordinates as they are not needed.
    #Uses list instead of abstracting from the plant class since list are easier to iterate and unpack.
    allPlants = [Apple(None,None), Pear(None,None), Banana(None,None), Watermelon(None, None), Corn(None, None), Wheat(None,None)]
    #Define an empty list to put all information in.
    plantInfoList = []
    #Iterates for every plant in the game
    for plant in allPlants:
        #Collects all the information in meaningful names before appending them to list
        plantName = plant.name
        plantGrowthTime = plant.growthTime
        plantSeedCost = plant.seedCost
        plantFruitPrice = plant.fruitPrice
        plantWaterCost = plant.waterCost
        plantSeedImage = plant.seedImage
        plantFruitImage = plant.fruitImage
        #Appending a sublist into the list creates a 2D array for fast and easy access, decreasing latency and complexity of the game.
        plantInfoList.append([plantName, plantGrowthTime, plantSeedCost, plantFruitPrice, plantWaterCost, plantSeedImage, plantFruitImage])
    return tuple(plantInfoList)
#Calls createPlantInfoList before game starts so that other classes can retrieve information.
plantInfoList = createPlantInfoList()

