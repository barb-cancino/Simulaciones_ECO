import pygame
from math import *

def drawgraph():

    plotPoints = []

    for x in range(-500, 500):
        x = x + 500
        y = sin(50*x)*50 #equation goes here
        y = -y + 300
        plotPoints.append([x, y])

    pygame.init()
    screen = pygame.display.set_mode([1000,600])
    screen.fill([255, 255, 255])
    pygame.draw.rect(screen, [0, 0, 0], [499, 0, 3, 600], 0)
    pygame.draw.rect(screen, [0, 0, 0], [0, 299, 1000, 3], 0)
    pygame.draw.lines(screen, [255,0,0],False, plotPoints, 2)
    pygame.display.flip()

def exitbutton():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
    pygame.quit()

drawgraph()
exitbutton()