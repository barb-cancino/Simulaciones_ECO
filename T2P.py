caso = input("¿Qué caso?: ")

T1 = [11,1]
T2 = [11,0.5]

if caso == "1":
    TA = T1
    TB = T2
else:
    TA = T2
    TB = T1

N=200
alpha = 0.5
Proporcion = [alpha,1-alpha]
CMg = 1

Pa = CMg
Pb = (Proporcion[0]*(TB[0]-TA[0]) - Proporcion[1]*TB[1]*CMg) / (Proporcion[0]*(TB[1]-TA[1])-Proporcion[1]*TB[1])

def qa(Pa):
    return TA[0] - TA[1]*Pa

def qb(Pb):
    return TB[0] - TB[1]*Pb

def ECa(p):
    return (((TA[0]/TA[1])-p)*qa(p))/2

CF_B = (((TB[0]/TB[1])-Pb)*qb(Pb))/2
CF_A = ECa(Pa) - ECa(Pb) + CF_B

beneficios = N*((Proporcion[0]*(qa(Pa)*(Pa-CMg) +CF_A)) + (Proporcion[1]*(qb(Pb)*(Pb-CMg) +CF_B)))

print(f"Beneficios: {beneficios}")
print(f"Tarifa cliente de alta demanda: \n CF = {CF_A} \n CV = {Pa}")
print(f"Cantidad demandada cliente de demanda alta: {qa(Pa)}")
print(f"Tarifa cliente de demanda baja: \n CF = {CF_B} \n CV = {Pb}")
print(f"Cantidad demandada cliente de demanda baja: {qb(Pb)}")
