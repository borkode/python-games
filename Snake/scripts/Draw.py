import pygame, math, time
from scripts import pg_functions as func
colors = [(0,0,0),(255,0,0),(0,255,0)]
pygame.init()
global Map,sz,screen,screensize
screen = func.getScreen()
screensize = func.getScreenSize()
def setMap(m,s):
    global Map,sz
    Map = m
    sz = s
    global ps
    ps = [math.floor(screensize[0]/sz[0]),math.floor(screensize[1]/sz[1])]
def retXY(x,y):
  return Map[y*sz[0]+x]
def retID(x,y):
  return y*sz[0]+x
def printMap():
    for i in range(sz[1]):
        st=""
        for x in range(sz[0]):
            st += str(Map[x+i*sz[0]])
        print(st)
def drawMap():
    for y in range(sz[1]):
        for x in range(sz[0]):
            pygame.draw.rect(screen,colors[retXY(x,y)],pygame.Rect(x*ps[0],y*ps[1],ps[0],ps[1]))
    for x in range(sz[0]):
        pygame.draw.line(screen,(0,0,0),(x*ps[0],0),(x*ps[0],screensize[1]),2)
    for y in range(sz[1]):
        pygame.draw.line(screen,(0,0,0),(0,y*ps[1]),(screensize[0],y*ps[1]),2)
    pygame.display.flip()