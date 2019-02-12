import pygame,os
global screen,screensize
directory = str(os.path.dirname(os.path.abspath(__file__)))
fdir = directory+"\\Font.ttf"
def init(scrn,size):
    global screen,screensize
    screen = scrn
    screensize = size
def rFont (size):
    return pygame.font.Font(fdir,size)
def writeText(text,x,y,size,color,bgcolor):
    label = rFont(size).render(text,1,color)
    tsize = rFont(size).size(text)
    whd = [tsize[0],tsize[1]]
    re = pygame.Rect(x,y,whd[0],whd[1])
    pygame.draw.rect(screen,bgcolor,re)
    screen.blit(label,(x,y))
    return re
def getClicked(rect):
    return pygame.mouse.get_pressed()[0] & pygame.Rect(rect).collidepoint(pygame.mouse.get_pos()) == 1
def getDir():
    return directory
def getHovering(rect):
    return pygame.Rect(rect).collidepoint(pygame.mouse.get_pos()) == 1
def centerPx (fs,txt):
    font = rFont(fs)
    return [screensize[0]/2-font.size(txt)[0]/2,screensize[1]/2-font.size(txt)[1]]
def getScreen():
    return screen
def getScreenSize():
    return screensize