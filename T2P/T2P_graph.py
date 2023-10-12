"""Creación de funciones para graficar el problema de tarifa en dos partes con pygame"""


import pygame
from t2p_funciones import *
from t2p_parametros import *


def drawgraph(ta, tb):
    """Creación de gráfico a partir de los parámetros de dos funciones de demanda"""
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

    CMG = cmg()
    # Modificamos las posiciones tal que quede a escala el gráfico
    ta_pos = [[100, 700 - (ta[0] / ta[1])], [100 + ta[0], 700]]
    tb_pos = [[100, 700 - (tb[0] / tb[1])], [100 + tb[0], 700]]

    max_disp_pagar_A = ta[0] / ta[1]
    max_disp_pagar_B = tb[0] / tb[1]

    if max_disp_pagar_A == max_disp_pagar_B:
        ta_pos[0][1] = 200
        tb_pos[0][1] = 200
    elif max_disp_pagar_A > max_disp_pagar_B:
        ta_pos[0][1] = 200
        tb_pos[0][1] = 700 - (max_disp_pagar_B / max_disp_pagar_A) * 600
    else:
        tb_pos[0][1] = 200
        ta_pos[0][1] = 700 - (max_disp_pagar_A / max_disp_pagar_B) * 600

    max_q_A = ta[0]
    max_q_B = tb[0]

    if max_q_A == max_q_B:
        ta_pos[1][0] = 600
        tb_pos[1][0] = 600
    elif max_q_A > max_q_B:
        ta_pos[1][0] = 600
        tb_pos[1][0] = 100 + ((max_q_B / max_q_A) * 600)
    else:
        ta_pos[1][0] = 100 + ((max_q_A / max_q_B) * 600)
        tb_pos[1][0] = 600

    # Función de demanda de clientes de demanda alta
    pygame.draw.line(
        screen, [255, 0, 0], start_pos=ta_pos[0], end_pos=ta_pos[1], width=4
    )
    # Función de demanda de clientes de demanda baja
    pygame.draw.line(
        screen, [0, 0, 255], start_pos=tb_pos[0], end_pos=tb_pos[1], width=4
    )
    ##########################################################################
    # Dibujamos los precios de la solución

    # Costo Marginal
    PA = p_a(CMG)
    PA = 700 - (PA / max(max_disp_pagar_A, max_disp_pagar_B)) * 600
    pygame.draw.line(
        screen,
        [0, 0, 0],
        start_pos=[100, PA],
        end_pos=[700, PA],
        width=4,
    )

    # Precio cliente demanda baja
    PB = p_b(ta, tb, alpha(), CMG)
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
    text_CMg_y = font.render(str(float(p_a(CMG))), True, [0, 0, 0])
    text_Pb = font.render("Pb", True, [0, 123, 255])
    text_Pb_y = font.render(str(p_b(ta, tb, alpha(), CMG)), True, [0, 0, 0])
    text_ta_y = font.render(str(max_disp_pagar_A), True, [0, 0, 0])
    text_tb_y = font.render(str(max_disp_pagar_B), True, [0, 0, 0])
    text_ta_x = font.render(str(max_q_A), True, [0, 0, 0])
    text_tb_x = font.render(str(max_q_B), True, [0, 0, 0])

    textRect_P = text_P.get_rect()
    textRect_Q = text_Q.get_rect()

    textRect_Cmg = text_CMg.get_rect()
    textRect_Cmg_y = text_CMg_y.get_rect()
    textRect_Pb = text_Pb.get_rect()
    textRect_Pb_y = text_Pb_y.get_rect()
    textRect_ta_y = text_ta_y.get_rect()
    textRect_tb_y = text_tb_y.get_rect()
    textRect_ta_x = text_ta_x.get_rect()
    textRect_tb_x = text_ta_x.get_rect()

    textRect_P.center = (70, 100)
    textRect_Q.center = (720, 730)

    textRect_Cmg.center = (740, PA)
    textRect_Cmg_y.midright = (90, PA)
    textRect_Pb.center = (740, PB)
    textRect_Pb_y.midright = (90, PB)
    textRect_ta_y.midright = (90, ta_pos[0][1])
    textRect_tb_y.midright = (90, tb_pos[0][1])
    textRect_ta_x.center = (ta_pos[1][0], 720)
    textRect_tb_x.center = (tb_pos[1][0], 720)

    screen.blit(text_P, textRect_P)
    screen.blit(text_Q, textRect_Q)

    screen.blit(text_CMg, textRect_Cmg)
    screen.blit(text_CMg_y, textRect_Cmg_y)
    screen.blit(text_Pb, textRect_Pb)
    screen.blit(text_Pb_y, textRect_Pb_y)
    screen.blit(text_ta_y, textRect_ta_y)
    screen.blit(text_tb_y, textRect_tb_y)
    screen.blit(text_ta_x, textRect_ta_x)
    screen.blit(text_tb_x, textRect_tb_x)

    pygame.display.flip()


def exitbutton():
    """Boton de cierre de ventana con gráfico"""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
