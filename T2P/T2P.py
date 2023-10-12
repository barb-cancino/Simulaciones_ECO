from t2p_funciones import *
from t2p_graph import drawgraph, exitbutton
from t2p_parametros import *

T1 = t1()
T2 = t2()

print("Datos del problema:")
print(f"q1 = {T1[0]} - {T1[1]}*p1")
print(f"q2 = {T2[0]} - {T2[1]}*p2")

CASO = 0
while (CASO < 1) or (CASO > 2):
    CASO = int(
        input("¿Cuál de los dos consumidores es de damanda alta? Seleccione 1 o 2: ")
    )

if CASO == 1:
    TA = T1
    TB = T2
else:
    TA = T2
    TB = T1

N = n()
ALPHA = alpha()
Prop = proporcion(ALPHA)
CMG = cmg()

PA = p_a(CMG)

PB = p_b(TA, TB, ALPHA, CMG)


def beneficios():
    return N * (
        (Prop[0] * (q(TA, PA) * (PA - CMG) + cf_a(TA, TB, PA, PB)))
        + (Prop[1] * (q(TB, PB) * (PB - CMG) + cf_b(TB, PB)))
    )


print("")
print(f"Excente del consumidor: {ec(TA,p_a(CMG))}")
print(f"Tarifa cliente de alta demanda: \n CF = {cf_a(TA, TB, PA, PB)} \n CV = {PA}")
print(f"Cantidad demandada cliente de demanda alta: {q(TA, PA)}")
print(f"\n Excente del consumidor: {ec(TB,p_b(TA,TB,ALPHA,CMG))}")
print(f"Tarifa cliente de demanda baja: \n CF = {cf_b(TB,PB)} \n CV = {PB}")
print(f"Cantidad demandada cliente de demanda baja: {q(TB, PB)}")

print(f"\n Beneficios: {beneficios()}")

drawgraph(TA, TB)
exitbutton()
