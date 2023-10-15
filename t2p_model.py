from T2P import t2p_funciones as t2p

T1 = [0, 0]
T2 = [0, 0]


def results(data):
    T1[0] = float(data["constant_1"])
    T1[1] = float(data["slope_1"])
    T1[0] = float(data["constant_1"])
    T1[1] = float(data["slope_1"])
    proporcion = float(data["proporcion"])
    numero_clientes = int(data["numero_clientes"])
    cf = float(data["costo_fijo"])
    cmg = float(data["costo_marginal"])

    # Tarifas
    Pa = t2p.p_a(cmg)
    Pb = t2p.p_b(T1, T2, proporcion, cmg)
    CFa = t2p.cf_a(T1, T2, Pa, Pb)
    CFb = t2p.cf_b(T2, Pb)
    # Cantidades demandadas
    qa = t2p.q(T1, Pa)
    qb = t2p.q(T2, Pb)
    # Excedentes del conumidor
    ECa = t2p.ec(T1, Pa)
    ECb = t2p.ec(T2, Pb)
    # Beneficios
    beneficios = t2p.beneficios(numero_clientes, proporcion, T1, T2, Pa, Pb, cmg, cf)

    solution = {
        "CFa": CFa,
        "Pa": Pa,
        "CFb": CFb,
        "Pb": Pb,
        "qa": qa,
        "qb": qb,
        "ECa": ECa,
        "ECb": ECb,
        "beneficios": beneficios,
    }

    return solution
