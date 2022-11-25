import pygame
import sys
import threading
from suduko import solve, isValidEntry
from pygame import sprite
from suduko import printGrid
from Accessories import Button

grid = [
    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],

    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],

    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0]
]
boolGrid = [
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],

    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],

    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
]

FPS_CLOCK = pygame.time.Clock()
FPS = 60
SOLVING = False
START = -1
TEXT = 'Get Your Solution Here'

ROW = None
COL = None
RECT = [0,0,0,0]

BLACK = (0,0,0)
RED = (200,0,0)
GOLD = (255,215,0)
GRAY = (30,30,30)
CYAN = (0,200,200)
WHITE = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('        SUDUKO SOLVER')
pygame.display.set_icon(pygame.image.load('images/logo.bmp'))
screen.fill((0,90,0))

# INTIALIZING FONT

font = pygame.font.SysFont('Calibri',30)
logoFont = pygame.font.SysFont('Parchment',500)
font1 = pygame.font.SysFont('Monotype Corsiva',30,italic=True)
buttonFont = pygame.font.SysFont('times new roman',20,bold=True)

def clearGrid():
    for i in range(0,9):
        for j in range(0,9):
            grid[i][j]=0
            boolGrid[i][j]=False

def printText(text):
    img = font1.render(text,True,WHITE)
    rect = img.get_rect()
    rect.center = (275,70)
    screen.blit(img,rect)

def drawGrid():
    screen.fill((0, 90, 0))
    img = logoFont.render('R',True,GRAY)
    rect = img.get_rect()
    rect.center = (325,325)
    screen.blit(img,rect)
    pygame.draw.rect(screen,BLACK,(100,100,450,450),3)
    for i in range(1,9):
        width = 1
        if i in [3,6]:
            width = 3
        pygame.draw.line(screen,BLACK,(100, 100+i*50),(550, 100+i*50),width)
        pygame.draw.line(screen,BLACK,(100+i*50, 100),(100+i*50, 550),width)
    submitButton = Button(screen,(275,560),100,30,RED,BLACK,'SOLVE',BLACK,buttonFont)
    clearButton = Button(screen,(100,560),100,30,WHITE,BLACK,'CLEAR',BLACK,buttonFont)
    printText(TEXT)
    printNumbers()
    return submitButton, clearButton

def GET_IMAGE(ch,i,j,color):
    img = font.render(str(ch),True,color)
    img_rect = img.get_rect()
    img_rect.center = (125 + j*50, 125 + i*50)
    return img, img_rect

def ckeckClick(pos):
    row = -1
    col = -1
    rect = [0,0,0,0]
    for i in range(0,9):
        if pos[0] in list(range(100 + i*50, 150 + i*50)):
            col = i
            for j in range(0,9):
                if pos[1] in list(range(100 + j * 50, 150 + j * 50)):
                    row = j
    if row >= 0 and col >= 0:
        rect = [100+col*50,100+row*50,51,51]
    # print(pos,' ',row,' ',col,'   ',rect)
    return rect, col, row

def printNumbers():
    color = RED
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j]:
                if boolGrid[i][j]:
                    color = RED
                else:
                    color = WHITE
                img, rect = GET_IMAGE(grid[i][j],i,j,color)
                screen.blit(img, rect)

solveButton, clearButton = drawGrid()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            RECT, COL, ROW = ckeckClick(event.pos)
            if solveButton.isCollide(event.pos) and not SOLVING:
                SOLVING = True
                TEXT = 'Solving...'
                T = threading.Thread(target=solve,args=[grid])
                T.start()

            if clearButton.isCollide(event.pos) and not SOLVING:
                clearGrid()
                TEXT = 'Get Your Solution Here'
                drawGrid()

            drawGrid()
            pygame.draw.rect(screen,RED,RECT,2)
        elif event.type == pygame.KEYDOWN and not SOLVING:
            if TEXT == 'SUDUKO Solved':
                TEXT = 'Get Solution Here'
            try:
                if int(event.unicode) in [0,1,2,3,4,5,6,7,8,9]:
                    if ROW >= 0 and COL >= 0:
                        if isValidEntry(grid,int(event.unicode),ROW,COL) or event.unicode == '0':
                            grid[ROW][COL] = int(event.unicode)
                            boolGrid[ROW][COL] = True
                            drawGrid()
                            pygame.draw.rect(screen, RED, RECT, 2)
            except:
                pass
    if SOLVING:
        drawGrid()
    if threading.active_count() == 1 and SOLVING:
        SOLVING = False
        TEXT = 'SUDUKO Solved'
        drawGrid()


    pygame.display.update()
    FPS_CLOCK.tick(FPS)