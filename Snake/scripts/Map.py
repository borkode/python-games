import time,random,os,math
from scripts import Draw, PiControl
global yp,xp,screen,foodBeingEaten
yp=0
xp=0
foodBeingEaten = True
sz = [40,20]
global snakex,snakey,sheadp,blockInFront,snakelength
snakex = []
snakey = []
sheadp = [round(sz[0]/2),round(sz[1]/2)]
blockInFront = 0
snakelength = 0
displaylen = 0
def createBlankGraph(size,filler):
  width = size[0]
  height = size[1]
  blank = []
  for i in range(width*height):
    blank.append(filler)
  return blank
Map = createBlankGraph(sz,0)
def placeFood(filler):
  for i in range(len(Map)):
    if Map[i]==filler:
      Map[i]=0
      break
  rndm = round(random.random()*len(Map))
  while True:
    rndm = round(random.random()*len(Map))
    try:
      if Map[rndm]!=2:
        Map[rndm]=filler
        break
    except:
      continue
  return rndm
def setXY(x,y,setTo):
  Map[y*sz[0]+x] = setTo
  return y*sz[0]+x
def retXY(x,y):
  return Map[y*sz[0]+x]
def retID(x,y):
  return y*sz[0]+x
def checkSnakeCollide(headp):
  headx = headp[0]
  heady = headp[1]
  Colliding = False
  for i in range(len(snakex)):
    if snakex[i] == headx and snakey[i] == heady and i!=snakelength-1:
        Colliding = True
  return Colliding
z = 0
MoveNotUsed = True
while True:
  try:
    if PiControl.buttonChecked('w') and yp!=1 and MoveNotUsed:
      yp=-1
      xp=0
      MoveNotUsed = False
    elif PiControl.buttonChecked('a') and xp!=1 and MoveNotUsed:
      yp=0
      xp=-1
      MoveNotUsed = False
    elif PiControl.buttonChecked('s') and yp!=-1 and MoveNotUsed:
      yp=1
      xp=0
      MoveNotUsed = False
    elif PiControl.buttonChecked('d') and xp!=-1 and MoveNotUsed:
      yp=0
      xp=1
      MoveNotUsed = False
    if z == 30:
      os.system('cls' if os.name == 'nt' else 'clear')
      Map = createBlankGraph(sz,0)
      Draw.setMap(Map,sz)
      if foodBeingEaten:
        food = placeFood(1)
        foodBeingEaten = False
      try:
        setXY(sheadp[0],sheadp[1],2)
      except:
        break
      Map[food] = 1
      if displaylen > snakelength:
        snakelength+=1
      sheadp[0]=sheadp[0]+xp
      sheadp[1]=sheadp[1]+yp
      snakex.append(sheadp[0])
      snakey.append(sheadp[1])
      if len(snakex)>snakelength and len(snakey)>snakelength:
        del snakex[0]
        del snakey[0]
      for i in range(len(snakex)):
        try:
          setXY(snakex[i],snakey[i],2)
        except:
          break
      if sheadp[0]<=-1 or sheadp[0]>sz[0] or sheadp[1]<=-1 or sheadp[1]>sz[1] or checkSnakeCollide(sheadp):
        break
      if retID(sheadp[0],sheadp[1]) == food:
        foodBeingEaten = True
        displaylen+=4
      Draw.drawMap()
      z=0
      MoveNotUsed = True
    time.sleep(1/300)
    z+=1
  except:
    continue
from scripts import lose
lose.Lose(snakelength)