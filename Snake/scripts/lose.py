import time,pygame,os
from scripts import pg_functions as func
from scripts import PiControl
pygame.init()
screen = func.getScreen()
screensize = func.getScreenSize
def Lose(score):
    sct = "SCORE: "+str(score)+"."
    screen.fill((0,0,0))
    func.writeText("GAME OVER",func.centerPx(32,"GAME OVER")[0],50,32,(255,255,255),(0,0,0))
    func.writeText(sct,func.centerPx(16,sct)[0],90,16,(255,255,255),(0,0,0))
    func.writeText("PRESS B TO EXIT",func.centerPx(16,"PRESS B TO EXIT")[0],110,16,(255,255,255),(0,0,0))
    pygame.display.flip()
    while True:
        time.sleep(0.1)
        if PiControl.buttonChecked("B")==True:
            pygame.quit()
            break