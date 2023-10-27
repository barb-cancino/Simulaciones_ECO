import * as t2p from "./t2p_functions.js"

D1 = [0, 0]
D2 = [0, 0]

function t2pSolucion(parametros) {
    let solucion = {
        cargoFijoA : 0,
        precioA : 0,
        cargoFijoB : 0,
        precioB : 0,
        cantidadA : 0,
        cantidadB : 0,
        cantidadTotal : 0,
        excedenteConsumidorA: 0,
        excedenteConsumidorB: 0,
        costoTotal: 0,
        costosFijos: 0,
        costosVariables: 0,
        costoMedio: 0,
        beneficiosTotales : 0,
        beneficiosConsumidoresA: 0,
        beneficiosConsumidoresB: 0,
        restriccionParticipacionA: false,
        restriccionParticipacionB: false,
        restriccionCompIncentivosA: false,
        restriccionCompIncentivosB: false,
    }

    if (parametros !== 0) {
        // Guardamos los parámetros necesarios para el cálculo de los resultados
        DA[0] = parametros.constanteA
        DA[1] = parametros.pendienteA
        DB[0] = parametros.constanteB
        DB[1] = parametros.pendienteB
        propA = parametros.proporcionA
        numeroClientes = parametros.numeroClientes
        cf = parametros.costoFijo
        cmg = parametros.costoMarginal

        // Cálculo de tarifas
        pA = t2p.precioA(cmg)
        solucion.precioA = pA

        pB = t2p.precioB(DA, DB, propA, cmg)
        solucion.precioB = pB

        cargoFijoA = t2p.cfA(DA, DB, pA, pB)
        solucion.cargoFijoA = cargoFijoA

        cargoFijoB = t2p.cfB(DB, pB)
        solucion.cargoFijoB = cargoFijoB

        // cantidades demandadas
        qa = t2p.cantDem(DA, pA)
        solucion.cantidadA = qa
        qb = t2p.cantDem(DB, pB)
        solucion.cantidadB = qb
        Q = numeroClientes * (porpA * qa - (1 - propA) * qb)
        solucion.cantidadTotal = Q

        // Costos
        CT = cf + cmg * Q
        solucion.costoTotal = CT

        solucion.costosFijos = cf

        CV = cmg * Q
        solucion.costosVariables = CV

        CMe = CT / Q
        solucion.costoMedio = CMe

        // Excedentes del consumidor
        ecA = t2p.excedente(DA, pA)
        solucion.excedenteConsumidorA = ecA
        ecB = t2p.excedente(DB, pB)
        solucion.excedenteConsumidorB = ecB

        // Beneficios
        solucion.beneficiosTotales = t2p.beneficiosTotales(numeroClientes, propA, DA, DB, pA, pB, cmg, cf)
        
        // Restricción de compatibilidad de incentivos

        if (ecA >= cargoFijoA) {
            solucion.restriccionParticipacionA = true
        }

        if (ecB >= cargoFijoB) {
            solucion.restriccionParticipacionB = true
        }

        // Restricción de compatibilidad de incentivos
        if ((ecA - cargoFijoA) >= (t2p.excedente(DA,pB)-cargoFijoB)) {
            solucion.restriccionCompIncentivosA = true
        }
        if ((ecB - cargoFijoB) >= (t2p.excedente(DB,pA)-cargoFijoA)) {
            solucion.restriccionCompIncentivosB = true
        }
    }
    
    return solucion
}



