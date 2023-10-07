T1 = [11, 1]
T2 = [11, 0.5]

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
Proporcion = [alpha, 1 - alpha]
CMg = 1

Pa = CMg
Pb = ((Proporcion[0] * (TB[0] - TA[0])) - (Proporcion[1] * TB[1] * CMg)) / (
    (Proporcion[0] * (TB[1] - TA[1])) - (Proporcion[1] * TB[1])
)


def qa(Pa):
    return TA[0] - TA[1] * Pa


def qb(Pb):
    return TB[0] - TB[1] * Pb


def ECa(p):
    return (((TA[0] / TA[1]) - p) * qa(p)) / 2


def CF_B():
    return (((TB[0] / TB[1]) - Pb) * qb(Pb)) / 2


def CF_A():
    return ECa(Pa) - ECa(Pb) + CF_B()


def beneficios():
    return N * (
        (Proporcion[0] * (qa(Pa) * (Pa - CMg) + CF_A()))
        + (Proporcion[1] * (qb(Pb) * (Pb - CMg) + CF_B()))
    )


print(f"\n Beneficios: {beneficios()}")
print(f"Tarifa cliente de alta demanda: \n CF = {CF_A()} \n CV = {Pa}")
print(f"Cantidad demandada cliente de demanda alta: {qa(Pa)}")
print(f"Tarifa cliente de demanda baja: \n CF = {CF_B()} \n CV = {Pb}")
print(f"Cantidad demandada cliente de demanda baja: {qb(Pb)}")
