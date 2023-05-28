import pygame, os, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((800, 600))

black = pygame.Color(0, 0, 0) # cornflower blue

# bat init

# ball init

# brick init

while True:

    mainSurface.fill(black)

    # brick draw

    # bat and ball draw

    # events

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # main game logic

    # collision detection
    pygame.display.update()
    fpsClock.tick(30)

