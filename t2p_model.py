from T2P import t2p_funciones as t2p


def results(parameters):
    T1 = [0, 0]
    T2 = [0, 0]
    if parameters == 0:
        return {
            "CFa": str(0),
            "Pa": str(0),
            "CFb": str(0),
            "Pb": str(0),
            "qa": str(0),
            "qb": str(0),
            "ECa": str(0),
            "ECb": str(0),
            "beneficios": str(0),
        }

    else:
        T1[0] = float(parameters["constant_1"])
        T1[1] = float(parameters["slope_1"])
        T1[0] = float(parameters["constant_1"])
        T1[1] = float(parameters["slope_1"])
        proporcion = float(parameters["proporcion"])
        numero_clientes = int(parameters["numero_clientes"])
        cf = float(parameters["costo_fijo"])
        cmg = float(parameters["costo_marginal"])

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
        beneficios = t2p.beneficios(
            numero_clientes, proporcion, T1, T2, Pa, Pb, cmg, cf
        )

        solution = {
            "CFa": str(CFa),
            "Pa": str(Pa),
            "CFb": str(CFb),
            "Pb": str(Pb),
            "qa": str(qa),
            "qb": str(qb),
            "ECa": str(ECa),
            "ECb": str(ECb),
            "beneficios": str(beneficios),
        }
        return solution
