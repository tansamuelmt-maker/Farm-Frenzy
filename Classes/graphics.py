#This where the classes of graphics is built
class Graphics:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = image.get_rect(midbottom=(position))
    
    def displayGraphic(self, screen):
        screen.blit(self.image,self.rect)