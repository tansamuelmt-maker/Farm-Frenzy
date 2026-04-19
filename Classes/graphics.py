#This where the classes of graphics is built
#This allows for simple, non-functional, non-dynamic images to be displayed easily, without increasing the complexity and amount of lines the game has.
class Graphics:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        #Calculates the rectangle of the image for precise positioning and collision detection.
        self.rect = image.get_rect(midbottom=(position))
    #Displays the image at the intended position.
    def displayGraphic(self, screen):
        screen.blit(self.image,self.rect)