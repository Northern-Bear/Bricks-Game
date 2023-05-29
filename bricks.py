import pygame, os, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((800, 600))

brick = None
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

def createBricks(pathToImg, rows, cols):
    global brick

    brick = pygame.image.load(pathToImg)
    bricks = []

    for y in range(rows):
        brickY = (y * 24) + 100
        for x in range(cols):
            brickX = (x * 31) + 245
            bricks.append(Rect(brickX, brickY, brick.get_width(), brick.get_height()))
    
    return bricks

bricks = createBricks('images/brick.png', 5, 10)

while True:

    mainSurface.fill(black)

    # brick draw

    for b in bricks:
        mainSurface.blit(brick, b)

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
        elif event.type == MOUSEBUTTONUP:
            if not ballServed:
                ballServed = True
    

    # main game logic
    if ballServed:
        bX += sX
        bY += sY
        ballRect.topleft = (bX, bY)

    # collision detection

    if (bY <= 0):
        bY = 0
        sY *= -1
    if (bY >= 600 - 8):
        ballServed = False
        bX, bY = (24, ballStartY)
        ballRect.topleft = (bX, bY)
    if (bX <= 0):
        bX = 0
        sX *= -1
    if (bX >= 800 - 8):
        bX = 800 -8
        sX *= -1

    if ballRect.colliderect(batRect):
        bY = playerY - 8
        sY *= -1

    brickHitIndex = ballRect.collidelist(bricks)
    if brickHitIndex >= 0:
        hb = bricks[brickHitIndex]

        mX = bX + 4
        mY = bY + 4
        if mX > hb.x + hb.width or mX < hb.x:
            sX *= -1
        else:
            sY *= -1
    
        del (bricks[brickHitIndex])

    pygame.display.update()
    fpsClock.tick(30)

