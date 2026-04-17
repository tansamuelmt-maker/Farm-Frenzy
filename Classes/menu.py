#This is where the class of menu is built
class Menu():
    def __init__(self, menuTitle, menuBackgroundImg, menuButtonList, menuBackgroundPos):
        self.menuTitle = menuTitle
        self.menuBackground = menuBackgroundImg
        self.menuButtonList = menuButtonList
        self.menuBackgroundPos = menuBackgroundPos
    def displayMenu(self,screen):
        self.menuTitle.createFont()
        self.menuTitle.centerPosText()
        self.menuTitle.displayStaticText()
        screen.blit(self.menuBackground, self.menuBackgroundPos)
        for button in self.menuButtonList:
            button.displayButton()
            