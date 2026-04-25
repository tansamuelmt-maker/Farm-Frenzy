#Where class of button is built
from Classes.plant import plantInfoList
from Classes.text import Text
import pygame
#This is the Button class. It creates unique buttons for all purposes. Through this class, customizing the button's text, background, color and the function it calls when it is clicked it possible and easy.
class Button(): 
    def __init__(self, text, textColor, textSize, buttonBGDimension, buttonBGColor, buttonEdgeColor, buttonPos, funct, functArgs, functKwargs, hoverText, image, imagePos = None): 
        #Basic details of the button's text that will be displayed. This allows the program to specify the content, color and font size of the text.
        self.text = text
        self.textColor = textColor
        self.textSize = textSize
        #This allows for the body and border color of the button to be altered and customized as well as the size of the button.
        self.buttonBGDimension = buttonBGDimension
        self.buttonBGColor = buttonBGColor
        self.buttonEdgeColor = buttonEdgeColor
        #This allows the program to specify the position of where the button will be placed
        self.buttonPos = buttonPos
        #Through funct, args and kwargs, the program can take in any function as well as all the parameters necessary to execute the function.
        #These functions will be executed when the user clicks the button, thus adding functionality to the button.
        self.funct = funct
        self.functArgs = functArgs #Used AI for args and kwargs
        self.functKwargs = functKwargs
        #Optional attributes of hover text and images to be displayed. Hover text is a text box that appears when the user hovers over the button.
        #Hover text is used to give more information to the user.
        self.hoverText = hoverText
        self.image = image
        #Using this if statement, the program does not need to enter an image position if there is no image for the button, increasing its efficiency and decreasing complexity.
        self.imagePos = None if image is None else imagePos
        #Creates a text class using the information of the text and the position of the button, eliminating several lines of code and removing the need of an initialization of text, through the use of a single line.
        self.buttonText = Text(textSize, textColor, text, (buttonPos[0]+(buttonBGDimension[0]/2), buttonPos[1]+(buttonBGDimension[1]/2)))
        #Create a pygame surface that is only used to get the rectangle of the button.
        #Through checking the user's mouse position and the rectangle, we can decide if the user is hovering or clicking the button.
        self.buttonSurf = pygame.Surface(buttonBGDimension)
        self.buttonRect = self.buttonSurf.get_rect(topleft=buttonPos)
        #Created by AI, these attributes allow for the button to only call a function once for one click, instead of calling the function for every tick/millisecond that the user had clicked the button.
        self.clicked = False
        self.mouseWasUp = False

    # This method allows for the button to be displayed with its functional parts included. This renders the background, text, hover text and image of the button, in their correct position.
    # The functional part (clicking) has been enabled through the detection of the mouse position, and whether the mouse is clicked.
    # This function has been edited by AI to include the mouseWasUp and mouseClicked attributes.
    def displayButton(self,screen):
        #Renders the body and border of the button, with thecorrect color and position it is rendered in.
        pygame.draw.rect(screen, self.buttonBGColor, (self.buttonPos[0],self.buttonPos[1], self.buttonBGDimension[0],self.buttonBGDimension[1]))
        pygame.draw.rect(screen, self.buttonEdgeColor, (self.buttonPos[0],self.buttonPos[1],self.buttonBGDimension[0],self.buttonBGDimension[1]),3)
        #Mouse position is converted into a variable to store the mouse position instead of repeatedly calling for it.
        mousePos = pygame.mouse.get_pos()
        #Text is oriented, and then displayed on the screen.
        self.buttonText.centerPosText()
        self.buttonText.displayStaticText(screen)
        #Optional image displayed if image is passed into button class.
        if self.image != None:
            screen.blit(self.image,self.imagePos)
        #First if statement determines whether user's mouse is on the button
        if self.buttonRect.collidepoint(mousePos):
            #If the mouse is not pressed, then we know the user has not pressed down on his/her mouse and the user has not clicked the button. Therefore the attributes have been set as such.
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                self.mouseWasUp = True
            #If user clicks his/her mouse, while hovering over the text, we know that the button has been pressed, and since that the user mouse has been clicked, the mouse is definitely not up.
            elif pygame.mouse.get_pressed()[0] == 1 and not self.clicked and self.mouseWasUp:
                self.funct(*self.functArgs, **self.functKwargs)
                self.clicked = True
                self.mouseWasUp = False #The reason mouseWasUp is used is to prevent multiple calls of the function every time the button is clicked. When the button gets clicked, these variables change so that the conditions for executing the button
                # are no longer true and therefore the button's function can only be called once a click.
        else:
            #This ensures that the button class does not register the mouse's click on another surface as a click to the button.
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
    
    #A function that calls the method of the text box in the hover text attribute to display the hover text.
    def drawHoverText(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        #If the user's mouse is hovering over the button, and the button has hovertext, the button's hover text's top left position will be at the user's mouse position.
        if self.hoverText is not None and self.buttonRect.collidepoint(mouse_pos):
            #This uses the hover text's class of text box to display the hover text instead of manually writing the code to display the hover text.
            self.hoverText.displayDynamicTextBox(None, screen, mouse_pos[0], mouse_pos[1])
