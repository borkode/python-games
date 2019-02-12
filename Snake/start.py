import pygame,ctypes,time
from scripts import pg_functions as func
from scripts import PiControl
user32 = ctypes.windll.user32
onStartScreen=True
size = [800,480] # adjust for monitor
pygame.init()
pygame.mouse.set_visible(False)
directory = func.getDir()
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
func.init(screen,size)
pygame.display.set_caption("PI ZERO GAME")
done = False
clock = pygame.time.Clock()
global ptext
ptext = "PRESS A TO PLAY"
i = 0
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    if i == 120:
        ptext = ""
    elif i >= 200:
        ptext = "PRESS A TO PLAY"
        i=0
    screen.fill((0,0,0))
    func.writeText("PySnake",func.centerPx(35,"PySnake")[0],func.centerPx(35,"PySnake")[1]-35/2,35,(255,255,255),(0,0,0))
    play_button = func.writeText(ptext,func.centerPx(15,ptext)[0],func.centerPx(15,ptext)[1]+25+15/2,15,(255,255,255),(0,0,0))
    pygame.display.flip()
    i+=1
    if PiControl.buttonChecked("A"):
        break
screen.fill((0,0,0))
pygame.display.flip()
from scripts import Map