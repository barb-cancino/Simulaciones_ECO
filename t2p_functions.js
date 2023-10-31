
module.exports.precioA = (cmg) => {
    return cmg
}

module.exports.precioB = (dAlta, dBaja, proporcionA, costoMarginal) => {
    return ((proporcionA * (dBaja[0] - dAlta[0])) - ((1-proporcionA) * dBaja[1] * costoMarginal)) / (
        (proporcionA * (dBaja[1] - dAlta[1])) - ((1-proporcionA) * dBaja[1])
    )
}

module.exports.cantDem = (d, precio) => {
    return d[0] - d[1]*precio
}

module.exports.excedente = (d,precio) => {
    return (((d[0]/d[1])-precio)* cantDem(d,precio))/2
}

module.exports.cfB = (dB,pB) => {
    return excedente(dB,pB)
}

module.exports.cfA = (dA, dB, pA, pB) => {
    return excedente(dA,pA) - excedente(dA,pB) + cfB(dB,pB)
}

module.exports.beneficiosTotales = (numeroClientes, proporcionA, dA, dB, precioA, precioB, costoMarginal, costoFijo) => {
    return numeroClientes * ((proporcionA)*(cantDem(dA,precioA)*(precioA-costoMarginal)) + (1-proporcionA)*(cantDem(dB,precioB))*(precioB-costoMarginal)) - costoFijo
}





