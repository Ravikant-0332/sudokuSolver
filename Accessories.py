import pygame

class Button:
    def __init__(self,screen,pos,width,height,color,borderColor,text,textColor,font):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.borderColor = borderColor
        self.text = text
        self.textColor = textColor
        self.font = font
        self.surface = pygame.surface.Surface((width,height))
        self.surface.fill(color)

        pygame.draw.rect(self.surface,borderColor,(0,0,width-1,height-1),2)
        self.img = font.render(text,True,textColor)
        self.rect = self.img.get_rect()
        self.rect.center = self.surface.get_rect().center
        self.surface.blit(self.img,self.rect)

        screen.blit(self.surface,self.pos)

    def isCollide(self,point):
        if point[0] in list(range(self.pos[0], self.pos[0]+self.width)):
            if point[1] in list(range(self.pos[1], self.pos[1]+self.height)):
                return True
        return False

class Colors:
    BLACK = (0, 0, 0)
    GRAY = (50, 50, 50)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    LIME = (0, 255, 0)
    BLUE = (0, 0, 205)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    YELLOW_GREEN = (154, 205, 50)
    PINK = (255, 20, 147)
    ORANGE = (255, 165, 0)
    GOLDEN_BROWN = (153, 101, 21)
    SILVER = (192, 192, 192)
    MAROON = (128, 0, 0)
    OLIVE = (128, 128, 0)
    GREEN = (0, 128, 0)
    PURPLE = (120, 0, 128)
    TEAL = (0, 128, 128)
    NAVY = (0, 0, 128)
    CORAL = (225, 127, 80)
    GOLD = (255, 215, 0)
    OLIVE_DRAB = (107, 142, 35)

class CheackerBoard:

    """ DEAFAULT COLORS """
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    BOX_COLOR = (0,255,0)
    colors = [BOX_COLOR,BLACK,WHITE]

    """ PRIVATE VARIABLES """
    __COLOR = None
    __CELL_HEIGHT = None
    __CELL_WIDTH = None
    __NO_OF_COLUMN = None
    __NO_OF_ROW = None
    __POSITION = None
    __SURFACE = None
    __WIDTH = None
    __HEIGHT = None
    __SCREEN = None

    def __init__(self, cellHeight = 100, cellWidth = 100, no_of_column = 4, no_of_row = 4, color1 = BLACK, color2 = WHITE, pos = (0,0)):
        self.__COLOR = ['',color1,color2]
        self.__CELL_HEIGHT = cellHeight
        self.__CELL_WIDTH = cellWidth
        self.__NO_OF_COLUMN = no_of_column
        self.__NO_OF_ROW = no_of_row
        self.__POSITION = pos
        self.__WIDTH = no_of_column*cellWidth
        self.__HEIGHT = no_of_row*cellHeight

        for x in self.colors:
            if x != color1 and x != color2:
                self.BOX_COLOR = x
                break

        self.__SURFACE = pygame.surface.Surface((self.__WIDTH, self.__HEIGHT))

    def DrawBoard(self, screen):
        self.__SCREEN = screen
        pointer = 1
        changer = -1
        for i in range(0, self.__HEIGHT, self.__CELL_HEIGHT):
            for j in range(0, self.__WIDTH, self.__CELL_WIDTH):
                pygame.draw.rect(self.__SURFACE,self.__COLOR[pointer],(j,i,self.__CELL_WIDTH,self.__CELL_HEIGHT))
                pointer *= changer

            if self.__NO_OF_COLUMN % 2 == 0:
                pointer *= changer

        screen.blit(self.__SURFACE,self.__POSITION)

    def clickPosition(self,pos):
        X = None
        Y = None
        pos = list(pos)
        self.DrawBoard(self.__SCREEN)
        pos[0] -= self.__POSITION[0]
        pos[1] -= self.__POSITION[1]
        if self.__SCREEN != None:
            for i in range(0, self.__HEIGHT, self.__CELL_HEIGHT):
                if pos[1] in list(range(i,i+self.__CELL_HEIGHT)):
                    for j in range(0, self.__WIDTH, self.__CELL_WIDTH):
                        if pos[0] in list(range(j, j+self.__CELL_WIDTH)):
                            pygame.draw.rect(self.__SURFACE, self.BOX_COLOR,
                                             (j, i, self.__CELL_WIDTH, self.__CELL_HEIGHT),2)
                            self.__SCREEN.blit(self.__SURFACE, self.__POSITION)
                            return (j//self.__CELL_WIDTH),(i//self.__CELL_HEIGHT)
        return X,Y