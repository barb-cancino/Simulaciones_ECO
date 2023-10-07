import pygame
from math import *
from T2P_solucion import *


def drawgraph(TA, TB):
    pygame.init()
    screen = pygame.display.set_mode([800, 800])
    screen.fill([255, 255, 255])
    # Dibujamos los ejes del gráfico
    pygame.draw.line(
        screen, [0, 0, 0], start_pos=[100, 100], end_pos=[100, 700], width=4
    )
    pygame.draw.line(
        screen, [0, 0, 0], start_pos=[100, 700], end_pos=[700, 700], width=4
    )
    # Dibujamos las curvas de demanda

    # Modificamos las posiciones tal que quede a escala el gráfico
    TA_pos = [[100, 700 - (TA[0] / TA[1])], [100 + TA[0], 700]]
    TB_pos = [[100, 700 - (TB[0] / TB[1])], [100 + TB[0], 700]]

    max_disp_pagar_A = TA[0] / TA[1]
    max_disp_pagar_B = TB[0] / TB[1]

    if max_disp_pagar_A == max_disp_pagar_B:
        TA_pos[0][1] = 200
        TB_pos[0][1] = 200
    elif max_disp_pagar_A > max_disp_pagar_B:
        TA_pos[0][1] = 200
        TB_pos[0][1] = 700 - (max_disp_pagar_B / max_disp_pagar_A) * 600
    else:
        TB_pos[0][1] = 200
        TA_pos[0][1] = 700 - (max_disp_pagar_A / max_disp_pagar_B) * 600

    max_q_A = TA[0]
    max_q_B = TB[0]

    if max_q_A == max_q_B:
        TA_pos[1][0] = 600
        TB_pos[1][0] = 600
    elif max_q_A > max_q_B:
        TA_pos[1][0] = 600
        TB_pos[1][0] = 100 + ((max_q_B / max_q_A) * 600)
    else:
        TA_pos[1][0] = 100 + ((max_q_A / max_q_B) * 600)
        TB_pos[1][0] = 600

    # Función de demanda de clientes de demanda alta
    pygame.draw.line(
        screen, [255, 0, 0], start_pos=TA_pos[0], end_pos=TA_pos[1], width=4
    )
    # Función de demanda de clientes de demanda baja
    pygame.draw.line(
        screen, [0, 0, 255], start_pos=TB_pos[0], end_pos=TB_pos[1], width=4
    )

    # Dibujamos los precios de la solución

    # Precio cliente demanda baja
    PB = Pb(TA, TB, 0.5, 1)
    PB = 700 - (PB / max(max_disp_pagar_A, max_disp_pagar_B)) * 600
    pygame.draw.line(
        screen,
        [0, 123, 255],
        start_pos=[100, PB],
        end_pos=[700, PB],
        width=2,
    )
    # Costo Marginal
    PA = Pa(1)
    PA = 700 - (PA / max(max_disp_pagar_A, max_disp_pagar_B)) * 600
    pygame.draw.line(
        screen,
        [0, 0, 0],
        start_pos=[100, PA],
        end_pos=[700, PA],
        width=2,
    )

    pygame.display.flip()


def exitbutton():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
