import pygame
from math import *


def drawgraph(TA, TB):
    """
    plotPoints_A = []
    plotPoints_B = []

    for x in range(0, TA[0] + 1):
        y = TA[0] - TA[1] * x  # equation goes here
        y = -y + 100
        plotPoints_A.append([x, y])

    for x in range(0, TB[0] + 1):
        y = TB[0] - TB[1] * x  # equation goes here
        y = -y + 100
        plotPoints_B.append([x, y])
    """
    pygame.init()
    screen = pygame.display.set_mode([800, 800])
    screen.fill([255, 255, 255])
    # Dibujamos los ejes del gráfico
    pygame.draw.line(
        screen, [0, 0, 0], start_pos=[100, 100], end_pos=[100, 700], width=2
    )
    pygame.draw.line(
        screen, [0, 0, 0], start_pos=[100, 700], end_pos=[700, 700], width=2
    )
    # Dibujamos las curvas de demanda
    pygame.draw.line(
        screen,
        [255, 0, 0],
        start_pos=[100, 700 - (TA[0] / TA[1])],
        end_pos=[100 + TA[0], 700],
    )
    pygame.draw.line(
        screen,
        [0, 0, 255],
        start_pos=[100, 700 - (TB[0] / TB[1])],
        end_pos=[100 + TB[0], 700],
    )
    # pygame.draw.lines(screen, [255, 0, 0], False, plotPoints_A, 2)
    # pygame.draw.lines(screen, [0, 0, 255], False, plotPoints_B, 2)
    pygame.display.flip()


def exitbutton():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
