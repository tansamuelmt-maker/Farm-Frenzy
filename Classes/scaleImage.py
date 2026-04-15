import pygame
def scaleImg(image, scale):
 width = image.get_width()
 height = image.get_height()
 return pygame.transform.scale(image, (int(width * scale), int(height*scale)))