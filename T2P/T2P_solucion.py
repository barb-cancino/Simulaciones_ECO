def Proporcion(a):
    return [a, 1 - a]


def Pa(CMg):
    return CMg


def Pb(TA, TB, a, CMg):
    Prop = Proporcion(a)

    return ((Prop[0] * (TB[0] - TA[0])) - (Prop[1] * TB[1] * CMg)) / (
        (Prop[0] * (TB[1] - TA[1])) - (Prop[1] * TB[1])
    )


def q(T, P):
    return T[0] - T[1] * P


def EC(T, P):
    return (((T[0] / T[1]) - P) * q(T, P)) / 2


def CF_B(TB, Pb):
    return (((TB[0] / TB[1]) - Pb) * q(TB, Pb)) / 2


def CF_A(TA, TB, Pa, Pb):
    return EC(TA, Pa) - EC(TA, Pb) + CF_B(TB, Pb)
