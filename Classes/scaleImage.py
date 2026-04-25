import pygame

#This command allows for efficient and easy dimension change of images
#Takes in image and scale that image should be adjusted to.
def scaleImg(image, scale):
    #Height and width of current image is taken
    width = image.get_width()
    height = image.get_height()
    #Returns the image but with the height and width scaled by a certain amount so image is still proportional.
    return pygame.transform.scale(image, (int(width * scale), int(height*scale)))