"""Creción de funciones para obtener la soulción del problema de T2P"""


def proporcion(a):
    """Entrega la proporción de los dos tipos de clientes"""
    return [a, 1 - a]


def p_a(cmg):
    """Entrega el precio variable para el consumidor de demanda alta"""
    return cmg


def p_b(ta, tb, a, cmg):
    """Entrega la solución del precio variable para consumidor de demanda baja"""
    prop = proporcion(a)

    return ((prop[0] * (tb[0] - ta[0])) - (prop[1] * tb[1] * cmg)) / (
        (prop[0] * (tb[1] - ta[1])) - (prop[1] * tb[1])
    )


def q(t, p):
    """
    Entrega la cantidad demandada para un consumidor cuya función de demanda está descrita por t
    """
    return t[0] - t[1] * p


def ec(t, p):
    """
    Entrega el excedente de un consumidor cuya función de denamda está dada por t y paga un precio p
    """
    return (((t[0] / t[1]) - p) * q(t, p)) / 2


def cf_a(ta, tb, pa, pb):
    """Entrega el valor del cargo fijo para un consumidor de demanda alta
    que soluciona el problema de tarifa en dos partes
    """
    return ec(ta, pa) - ec(ta, pb) + cf_b(tb, pb)


def cf_b(tb, pb):
    """Entrega el valor del cargo fijo para un consumidor de demanda baja
    que soluciona el problema de tarifa en dos partes
    """
    return (((tb[0] / tb[1]) - pb) * q(tb, pb)) / 2
