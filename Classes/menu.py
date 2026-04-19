#This is where the class of menu is built
from Classes.textbox import TextBox
from Classes.button import Button
from Classes.text import Text
class Menu():
    def __init__(self, menuText, menuTextColor, menuTextPos, menuBackgroundImg, menuButtonList, menuBackgroundPos):
        self.menuText = menuText
        self.menuTextColor = menuTextColor
        self.menuTextPos = menuTextPos
        self.menuBackground = menuBackgroundImg
        self.menuButtonList = menuButtonList
        self.menuBackgroundPos = menuBackgroundPos
        self.menuTitle = Text(40, menuTextColor, menuText, menuTextPos)
    def displayMenu(self,screen):
        self.menuTitle.centerPosText()
        screen.blit(self.menuBackground, self.menuBackgroundPos)
        self.menuTitle.displayStaticText(screen)
        for button in self.menuButtonList:
            button.displayButton(screen)
        for button in self.menuButtonList:
            button.drawHoverText(screen)
    def updateMenuText(self, newText):
        self.menuText = newText
        self.menuTitle.text = newText
        self.menuTitle.textSurf = self.menuTitle.font.render(newText, False, self.menuTextColor)

            