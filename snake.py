#!/usr/bin/env python

# Raspberry Snake
# Written by Gareth Halfacree for the Raspberry Pi User Guide
# rewritten by Aniket patel 
# make snake that eat raspberry itself :)

import pygame, sys, time, random
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('SnakeAI')
outberry=0
outberrydir='right'
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
snakePosition = [100,100]
snakeSegments = [[100,100],[80,100],[60,100]]
raspberryPosition = [300,300]
raspberrySpawned = 1
direction = 'right'
changeDirection = direction
input='right'

def gameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

def checkdir():
    if direction == 'right':
        if snakePosition[0] > raspberryPosition[0]:
		changeDirection='down'
		return 1
     	   	
    if direction == 'left':
        if snakePosition[0] < raspberryPosition[0]:
		changeDirection='up'
		return 1
     
    if direction == 'up':
        if snakePosition[1] < raspberryPosition[1]:
		changeDirection='right'
		return 1
     	   	
    if direction == 'down':
        if snakePosition[1] > raspberryPosition[1]:
		changeDirection='left'
		return 1
		
     	   	
def  whatinput():
    if direction == 'right':
        if snakePosition[0] == raspberryPosition[0]:
		if snakePosition[1] < raspberryPosition[1]:
	         	return 'down'
     	   	else:
      	      		return 'up'
        else:
        	return 'right'
    if direction == 'left':
        if snakePosition[0] == raspberryPosition[0]:
		if snakePosition[1] < raspberryPosition[1]:
	         	return 'down'
     	   	else:
      	      		return 'up'
        else:
        	return 'left'
    if direction == 'up':
        if snakePosition[1] == raspberryPosition[1]:
		if snakePosition[0] < raspberryPosition[0]:
	         	return 'right'
     	   	else:
      	      		return 'left'
        else:
        	return 'up'
    if direction == 'down':
        if snakePosition[1] == raspberryPosition[1]:
		if snakePosition[0] < raspberryPosition[0]:
	         	return 'right'
     	   	else:
      	      		return 'left'
        else:
        	return 'down'
    
while True:
  
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
 
            if event.key == K_RIGHT or event.key == ord('d'):
	        changeDirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    if (snakePosition[0]<=40 or snakePosition[1]<=620):
	if(direction=='left'):
		changeDirection='down'
	else:
		changeDirection='right'	
    elif (snakePosition[0]<=620 or snakePosition[1]<=40):
	if(direction=='right'):
		changeDirection='down'
	else:
		changeDirection='left'
    elif (snakePosition[0]<=620 or snakePosition[1]<=460):
	if(direction=='down'):
		changeDirection='left'
	else:
		changeDirection='up'
    elif (snakePosition[0]<=40 or snakePosition[1]<=460):
	if(direction=='left'):
		changeDirection='up'
	else:
		changeDirection='right'
    else:
        changeDirection = whatinput()
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection
    if direction == 'right':
        snakePosition[0] += 20
    if direction == 'left':
        snakePosition[0] -= 20
    if direction == 'up':
        snakePosition[1] -= 20
    if direction == 'down':
        snakePosition[1] += 20
    snakeSegments.insert(0,list(snakePosition))
    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
        raspberrySpawned = 0
    else:
        snakeSegments.pop()
    if raspberrySpawned == 0:
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        raspberryPosition = [int(x*20),int(y*20)]
    raspberrySpawned = 1
    playSurface.fill(blackColour)
    for position in snakeSegments:
        pygame.draw.rect(playSurface,whiteColour,Rect(position[0], position[1], 20, 20))
    pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
    pygame.display.flip()
    if snakePosition[0] > 620 or snakePosition[0] < 0:
        gameOver()
    if snakePosition[1] > 460 or snakePosition[1] < 0:
        gameOver()
    for snakeBody in snakeSegments[1:]:
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            gameOver()
    fpsClock.tick(5)

