import pygame, os, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((800, 600))

black = pygame.Color(0, 0, 0) # cornflower blue

# bat init

bat = pygame.image.load('images/bat.png')
playerY = 540
batRect = bat.get_rect()
mouseX, mouseY = (0, playerY)

# ball init

ball = pygame.image.load('images/ball.png')
ballRect = ball.get_rect()
ballStartY = 200
ballSpeed = 3
ballServed = False

bX, bY = (24, ballStartY)
sX, sY = (ballSpeed, ballSpeed)
ballRect.topleft = (bX, bY)

# brick init

while True:

    mainSurface.fill(black)

    # brick draw

    # bat and ball draw

    mainSurface.blit(bat, batRect)

    mainSurface.blit(ball, ballRect)

    # events

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
            if (mouseX < 800 - 55):
                batRect.topleft = (mouseX, playerY)
            else:
                batRect.topleft = (800 - 55, playerY)
    

    # main game logic

    bX += sX
    bY += sY
    ballRect.topleft = (bX, bY)

    # collision detection

    if (bY <= 0):
        bY = 0
        sY *= -1
    if (bY >= 600 - 8):
        bY = 600 - 8
        sY *= -1
    if (bX <= 0):
        bX = 0
        sX *= -1
    if (bX >= 800 - 8):
        bX = 800 -8
        sX *= -1

    if ballRect.colliderect(batRect):
        bY = playerY - 8
        sY *= -1

    pygame.display.update()
    fpsClock.tick(30)

