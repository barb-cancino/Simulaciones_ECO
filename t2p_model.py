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
            "Q": str(0),
            "ECa": str(0),
            "ECb": str(0),
            "CT": str(0),
            "CF": str(0),
            "CV": str(0),
            "Cme": str(0),
            "beneficios": str(0),
            "beneficios_a": str(0),
            "beneficios_b": str(0),
        }

    else:
        T1[0] = float(parameters["constant_1"])
        T1[1] = float(parameters["slope_1"])
        T2[0] = float(parameters["constant_2"])
        T2[1] = float(parameters["slope_2"])
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
        Q = numero_clientes * (proporcion * qa + (1 - proporcion) * qb)
        # Costos
        CT = cf + cmg * Q
        CV = cmg * Q
        CMe = CT / Q
        # Excedentes del conumidor
        ECa = t2p.ec(T1, Pa)
        ECb = t2p.ec(T2, Pb)
        # Beneficios
        beneficios = t2p.beneficios(
            numero_clientes, proporcion, T1, T2, Pa, Pb, cmg, cf
        )
        beneficios_a = (qa * (Pa - cmg) + CFa) * proporcion * numero_clientes
        beneficios_b = (qb * (Pb - cmg) + CFb) * (1 - proporcion) * numero_clientes

        solution = {
            "CFa": str(CFa),
            "Pa": str(Pa),
            "CFb": str(CFb),
            "Pb": str(Pb),
            "qa": str(qa),
            "qb": str(qb),
            "Q": str(Q),
            "CT": str(CT),
            "CF": str(cf),
            "CV": str(CV),
            "Cme": str(CMe),
            "ECa": str(ECa),
            "ECb": str(ECb),
            "beneficios": str(beneficios),
            "beneficios_a": str(beneficios_a),
            "beneficios_b": str(beneficios_b),
        }
        return solution
