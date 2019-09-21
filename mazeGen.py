import pygame,os,sys,random
from pygame.locals import *


"""
1-TOP WALL
2-RIGHT WALL
3-BOTTOM WALL
4-LEFT WALL
"""

WALL_WIDTH = 2 			#WALL WIDTH IN PIXELS
GAP_WIDTH  = 10
noOfWalls  = 25

visited = [ [0 for i in range(noOfWalls-1)] for i in range(noOfWalls-1) ]
BLACK   = (  0,   0,   0)
WHITE	= (255, 255, 255)

DISPLAY_WIDTH = noOfWalls * WALL_WIDTH + (noOfWalls-1) * GAP_WIDTH
DISPLAY_HEIGHT = DISPLAY_WIDTH

mousex , mousey = 0 , 0
FPS = 20

def main():
	global FPSCLOCK,DISPLAYSURF,WALL,visited,DISPLAY_HEIGHT,DISPLAY_HEIGHT
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300, 50)


	pygame.init()
	pygame.display.set_caption('Maze Generator')

	print(DISPLAY_WIDTH,DISPLAY_HEIGHT)

	DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF.fill(WHITE)

	#DRAW THE GRID
	WALL=0
	while(WALL<=DISPLAY_WIDTH-1):
		pygame.draw.line(DISPLAYSURF,BLACK,(WALL,0),(WALL,DISPLAY_HEIGHT),1)
		pygame.draw.line(DISPLAYSURF,BLACK,(WALL+1,0),(WALL+1,DISPLAY_HEIGHT),1)
		pygame.draw.line(DISPLAYSURF,BLACK,(0,WALL),(DISPLAY_HEIGHT,WALL),1)
		pygame.draw.line(DISPLAYSURF,BLACK,(0,WALL+1),(DISPLAY_HEIGHT,WALL+1),1)
		WALL = WALL + 2 + GAP_WIDTH




	# print(visited)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.locals.QUIT: 	 # QUIT CONDITION
				pygame.image.save(DISPLAYSURF,'maze1.png')
				pygame.quit()
				sys.exit()
		recursiveBacktracker(0,0)
		pygame.display.update()
		FPSCLOCK.tick(FPS)


def waitwithCurrentScreen(timeInmilliSecs):
    '''A WAIT FUNCTION'''
    while timeInmilliSecs>=0:
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT CONDITION
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        timeInmilliSecs = timeInmilliSecs-1


def findWallCoordinates(xW,yW,code):
	"Returns the x,y starting co-ordinates of the wall with code passed "
	if code==1: #Upper Wall
		xU= 2 + xW*(GAP_WIDTH+WALL_WIDTH) 
		yU= 1 + yW*(GAP_WIDTH+WALL_WIDTH)
		return(xU,yU,xU,yU-1)
	elif code==2:#Right Wall
		xR= 2 + xW*(GAP_WIDTH+WALL_WIDTH) + GAP_WIDTH
		yR= 2 + yW*(GAP_WIDTH+WALL_WIDTH) 
		return(xR,yR,xR+1,yR)
	elif code==3: #Bottom Wall
		xB= 2 + xW*(GAP_WIDTH+WALL_WIDTH) 
		yB= 2 + yW*(GAP_WIDTH+WALL_WIDTH) + GAP_WIDTH
		return(xB,yB,xB,yB+1)
	elif code==4: #Left Wall
		xL= 1 + xW*(GAP_WIDTH+WALL_WIDTH) 
		yL= 2 + yW*(GAP_WIDTH+WALL_WIDTH) 
		return(xL,yL,xL-1,yL)

def colorCoordinates(xS,yS,code):
	if code==1 or code==3: #upper or bottom
		pygame.draw.line(DISPLAYSURF,WHITE,(xS,yS),(xS+GAP_WIDTH-1,yS),1)
	elif code==2 or code==4:	#left or right
		pygame.draw.line(DISPLAYSURF,WHITE,(xS,yS),(xS,yS+GAP_WIDTH-1),1)

def checkIfvisisted(x1,y1,code):
	"Checks if the upper/lower/right/left tile of x1,y1 is visited or not"
	global  visisted
	if code ==1:
		return visited[x1][y1-1]==0
	elif code ==2:
		return visited[x1+1][y1]==0
	elif code ==3:
		return visited[x1][y1+1]==0
	elif code ==4:
		return visited[x1-1][y1]==0

def nextCoordinates(x1,y1,code):
	"Returns the co-ordinates of the next tile to be visited depending on the code passed"
	if code ==1:
		return x1,y1-1
	elif code ==2:
		return x1+1,y1
	elif code ==3:
		return x1,y1+1
	elif code ==4:
		return x1-1,y1

def recursiveBacktracker(x1,y1):
	""" It is assumed that the current tile x1,y1 is unvisited when u enter the code"""
	global visited
	visited[x1][y1]=1 #mark it visisted


	l=[] #wallChoicesAvaliable
	#generate available choices
	if y1!=0:
		l.append(1)
	if x1!=23:
		l.append(2)
	if y1!=23:
		l.append(3)
	if x1!=0:
		l.append(4)


	print(l)
	wallCode=random.choice(l)

	#remove the wall corresponding to the wallCode obtained
	xtemp1,ytemp1,xtemp2,ytemp2 = findWallCoordinates(x1,y1,wallCode)
	colorCoordinates(xtemp1,ytemp1,wallCode)
	colorCoordinates(xtemp2,ytemp2,wallCode)

	for i in l:
		isNotVisited = checkIfvisisted(x1,y1,i)
		if not isNotVisited:
			l.remove(i)

	print(x1,y1,l)
	if l==[]:
		return

	random.shuffle(l)
	for j in l:
		newX ,newY = nextCoordinates(x1,y1,j)
		if visited[newX][newY]==1:
			return
		recursiveBacktracker(newX,newY)

if __name__ == '__main__':
    main()