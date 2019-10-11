import pygame, sys,time, random
from pygame.locals import *

def abra():
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()	
def random_color():
	return (random.randrange(1,254),random.randrange(1,254),random.randrange(1,254))
def square(x):
	return x*x
def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("Score: "+str(count), True, WHITE)
    windowSurface.blit(text,(0,0))
    text = font.render("Go Green ", True, WHITE)
    windowSurface.blit(text,(int(WINDOWWIDTH/2)-int(WINDOWWIDTH/9),0))

def display_hero(x,y):
    windowSurface.blit(Hero,(x-1,y-5))
def display_friend(x,y):
	windowSurface.blit(Friend,(x-1,y-5))
def display_monster(x,y):
	windowSurface.blit(Monster,(x+2,y))
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
y = [RED,GREEN]
# set up pygame
pygame.init()
mainClock = pygame.time.Clock()
#bulletSound = pygame.mixer.music.load('bullet.mp3')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

# set up the window
WINDOWWIDTH = 700
WINDOWHEIGHT = WINDOWWIDTH
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Brusting_the_Ballons')
windowSurface.fill(WHITE)
myfont = pygame.font.SysFont("monospace", 16)
Hero = pygame.image.load('character.png')
Friend = pygame.image.load('Friend.png')
Monster = pygame.image.load('monster.png')

NUMBER = 10
SPEED = 2
MARGIN = 20
MOVEMENT = 2
RAD = 30
RAD_BALL = RAD
SCORE = 0
KILL = 0
PREV_KILL = 1
SPEED_BALL = 5
MOVE_X = MOVE_Y = 0

ball = {'centre_x' : (int)(WINDOWWIDTH/2) , 'centre_y' : WINDOWHEIGHT-RAD_BALL, 'color' : WHITE }
items = []
for i in range(NUMBER):
	b = {'centre_x' : random.randrange(RAD,WINDOWWIDTH-RAD), 'centre_y' : random.randrange(RAD,WINDOWWIDTH/2*3), 'color' : random.choice(y),'num':i}
	items.append(b)
	
while SPEED_BALL:
	pygame.draw.circle(windowSurface,ball['color'], (ball['centre_x'],ball['centre_y']), RAD_BALL,0)
	display_hero(ball['centre_x']-RAD_BALL,ball['centre_y']-RAD)
	if KILL >= 5+ PREV_KILL:
		SPEED += 5
		PREV_KILL = KILL
	for b1 in items:
		for b2 in items:
			if b1['num'] < b2['num'] and b1['color'] != WHITE and b2['color'] != WHITE and (square(b1['centre_x'] - b2['centre_x']) + square(b1['centre_y']- b2['centre_y']) <= square(2*RAD)):
				b2['color'] = WHITE

	for b in items:
		if b['color'] != WHITE and square(ball['centre_x'] - b['centre_x']) + square(ball['centre_y']- b['centre_y']) <= square(RAD_BALL + RAD):
			if b['color'] == GREEN:
				SPEED_BALL += 1
				KILL += 1
				SCORE += 2
			if b['color'] == RED:
				SPEED_BALL -= 1
				SCORE -= 1
			b['color'] = WHITE

		if b['color'] != WHITE:
			pygame.draw.circle(windowSurface,b['color'],(b['centre_x'],b['centre_y']),RAD,0)
			if b['color'] == GREEN:
				display_friend(b['centre_x']-RAD,b['centre_y']-RAD)
			if b['color'] == RED:
				display_monster(b['centre_x']-RAD,b['centre_y']-RAD)
		b['centre_y'] += SPEED
		if b['centre_y'] - RAD >= WINDOWHEIGHT:
			b['centre_y'] = -RAD
			b['centre_x'] = random.randrange(RAD,WINDOWWIDTH-RAD)
			b['color'] = random.choice(y)
	abra()
	things_dodged(SCORE)
	pygame.display.update()
	time.sleep(0.02)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				MOVE_X = -1
			if event.key == K_RIGHT:
				MOVE_X = 1
			if event.key == K_UP:
				MOVE_Y = -1
			if event.key == K_DOWN:
				MOVE_Y = 1
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_LEFT:
				MOVE_X = 0
			if event.key == K_RIGHT:
				MOVE_X = 0
			if event.key == K_UP:
				MOVE_Y = 0
			if event.key == K_DOWN:
				MOVE_Y = 0
	ball['centre_x'] += MOVE_X*SPEED_BALL
	ball['centre_y'] += MOVE_Y*SPEED_BALL
	if ball['centre_x'] <= RAD:
		ball['centre_x'] = RAD
	if ball['centre_y'] <= RAD:
		ball['centre_y'] = RAD
	if ball['centre_x'] + RAD >= WINDOWWIDTH:
		ball['centre_x'] = WINDOWWIDTH-RAD
	if ball['centre_y'] + RAD >= WINDOWHEIGHT:
		ball['centre_y'] = WINDOWHEIGHT- RAD

	windowSurface.fill(BLACK)
	abra()

time.sleep(1)