from T2P_solucion import *
from graphic_calculator import *

T1 = [11, 1]
T2 = [8.5, 0.5]

print("Datos del problema:")
print(f"q1 = {T1[0]} - {T1[1]}*p1")
print(f"q2 = {T2[0]} - {T2[1]}*p2")

caso = 0
while (caso < 1) or (caso > 2):
    caso = int(
        input("¿Cuál de los dos consumidores es de damanda alta? Seleccione 1 o 2: ")
    )

if caso == 1:
    TA = T1
    TB = T2
else:
    TA = T2
    TB = T1

N = 200
alpha = 0.5
Prop = Proporcion(alpha)
CMg = 1

PA = Pa(CMg)

PB = Pb(TA, TB, alpha, CMg)


def beneficios():
    return N * (
        (Prop[0] * (q(TA, PA) * (PA - CMg) + CF_A(TA, TB, PA, PB)))
        + (Prop[1] * (q(TB, PB) * (PB - CMg) + CF_B(TB, PB)))
    )


print(f"\n Beneficios: {beneficios()}")
print(f"Tarifa cliente de alta demanda: \n CF = {CF_A(TA, TB, PA, PB)} \n CV = {PA}")
print(f"Cantidad demandada cliente de demanda alta: {q(TA, PA)}")
print(f"Tarifa cliente de demanda baja: \n CF = {CF_B(TB,PB)} \n CV = {PB}")
print(f"Cantidad demandada cliente de demanda baja: {q(TB, PB)}")

drawgraph(TA, TB)
exitbutton()
