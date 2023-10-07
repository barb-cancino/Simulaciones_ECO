import pygame
from math import *
from T2P_solucion import *
from T2P_parametros import *


def drawgraph(TA, TB):
    pygame.init()
    screen = pygame.display.set_mode([800, 800])
    screen.fill([255, 255, 255])

    pygame.display.set_caption("Tarifa en dos partes")
    # Dibujamos los ejes del gráfico
    pygame.draw.line(
        screen, [0, 0, 0], start_pos=[100, 100], end_pos=[100, 700], width=4
    )
    pygame.draw.line(
        screen, [0, 0, 0], start_pos=[100, 700], end_pos=[700, 700], width=4
    )

    pygame.draw.polygon(
        screen, [0, 0, 0], [[100, 80], [90, 100], [110, 100]], width=0
    )  # flecha eje y
    pygame.draw.polygon(
        screen, [0, 0, 0], [[720, 700], [700, 690], [700, 710]], width=0
    )  # felcha eje x
    ##########################################################################
    # Dibujamos las curvas de demanda

    CMG = CMg()
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
    ##########################################################################
    # Dibujamos los precios de la solución

    # Costo Marginal
    PA = Pa(CMG)
    PA = 700 - (PA / max(max_disp_pagar_A, max_disp_pagar_B)) * 600
    pygame.draw.line(
        screen,
        [0, 0, 0],
        start_pos=[100, PA],
        end_pos=[700, PA],
        width=4,
    )

    # Precio cliente demanda baja
    PB = Pb(TA, TB, alpha(), CMG)
    PB = 700 - (PB / max(max_disp_pagar_A, max_disp_pagar_B)) * 600
    pygame.draw.line(
        screen,
        [0, 123, 255],
        start_pos=[100, PB],
        end_pos=[700, PB],
        width=2,
    )

    #################################################################
    # Texto
    font = pygame.font.Font("freesansbold.ttf", 16)
    font_big = pygame.font.Font("freesansbold.ttf", 24)

    text_P = font_big.render("P", True, [0, 0, 0])
    text_Q = font_big.render("Q", True, [0, 0, 0])

    text_CMg = font.render("Pa = CMg", True, [0, 0, 0])
    text_CMg_y = font.render(str(float(Pa(CMG))), True, [0, 0, 0])
    text_Pb = font.render("Pb", True, [0, 123, 255])
    text_Pb_y = font.render(str(Pb(TA, TB, alpha(), CMG)), True, [0, 0, 0])
    text_TA_y = font.render(str(max_disp_pagar_A), True, [0, 0, 0])
    text_TB_y = font.render(str(max_disp_pagar_B), True, [0, 0, 0])
    text_TA_x = font.render(str(max_q_A), True, [0, 0, 0])
    text_TB_x = font.render(str(max_q_B), True, [0, 0, 0])

    textRect_P = text_P.get_rect()
    textRect_Q = text_Q.get_rect()

    textRect_Cmg = text_CMg.get_rect()
    textRect_Cmg_y = text_CMg_y.get_rect()
    textRect_Pb = text_Pb.get_rect()
    textRect_Pb_y = text_Pb_y.get_rect()
    textRect_TA_y = text_TA_y.get_rect()
    textRect_TB_y = text_TB_y.get_rect()
    textRect_TA_x = text_TA_x.get_rect()
    textRect_TB_x = text_TA_x.get_rect()

    textRect_P.center = (70, 100)
    textRect_Q.center = (720, 730)

    textRect_Cmg.center = (740, PA)
    textRect_Cmg_y.midright = (90, PA)
    textRect_Pb.center = (740, PB)
    textRect_Pb_y.midright = (90, PB)
    textRect_TA_y.midright = (90, TA_pos[0][1])
    textRect_TB_y.midright = (90, TB_pos[0][1])
    textRect_TA_x.center = (TA_pos[1][0], 720)
    textRect_TB_x.center = (TB_pos[1][0], 720)

    screen.blit(text_P, textRect_P)
    screen.blit(text_Q, textRect_Q)

    screen.blit(text_CMg, textRect_Cmg)
    screen.blit(text_CMg_y, textRect_Cmg_y)
    screen.blit(text_Pb, textRect_Pb)
    screen.blit(text_Pb_y, textRect_Pb_y)
    screen.blit(text_TA_y, textRect_TA_y)
    screen.blit(text_TB_y, textRect_TB_y)
    screen.blit(text_TA_x, textRect_TA_x)
    screen.blit(text_TB_x, textRect_TB_x)

    pygame.display.flip()


def exitbutton():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
