#This is where the class of menu is built
from Classes.textbox import TextBox
from Classes.button import Button
from Classes.text import Text
#This is the menu class, it allows for easy creation of unique menus such as the start, shop and end menu.
class Menu():
    #It's attributes allow for custom title, custom background, and custom buttons.
    def __init__(self, menuText, menuTextColor, menuTextPos, menuBackgroundImg, menuButtonList, menuBackgroundPos):
        #Allows for customizeable text, color, and position of the title
        self.menuText = menuText
        self.menuTextColor = menuTextColor
        self.menuTextPos = menuTextPos
        #Takes in the background image with its position to be displayed behind as well as the button list of all the buttons.
        self.menuBackground = menuBackgroundImg
        self.menuBackgroundPos = menuBackgroundPos
        #Uses a list to store all buttons so an indeterminate amount of buttons can be stored, displayed as well as accessed very easily
        self.menuButtonList = menuButtonList
        #Instantiates a new text for the title so title can be easily created and displayed
        self.menuTitle = Text(40, menuTextColor, menuText, menuTextPos)
    def displayMenu(self,screen):
        #Orients menu title
        self.menuTitle.centerPosText()
        #Displays background first so it renders behind everything
        screen.blit(self.menuBackground, self.menuBackgroundPos)
        self.menuTitle.displayStaticText(screen)
        #Unpacks the button list for easy display of all buttons regardless of amount of buttons.
        #Displays button and hover text of button 
        for button in self.menuButtonList:
            button.displayButton(screen)
        #Hover text drawn after all buttons so it renders on top of them.
        for button in self.menuButtonList:
            button.drawHoverText(screen)
    #Added by AI, takes a new text to be displayed on the menu. This is used to create a customized end game menu based on the game's condition.
    def updateMenuText(self, newText):
        self.menuText = newText
        #Changes the text attribute of the menu title into the new text.
        self.menuTitle.text = newText
        #Re-renders the title with the new text.
        self.menuTitle.textSurf = self.menuTitle.font.render(newText, False, self.menuTextColor)

            