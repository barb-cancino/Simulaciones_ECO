
const canvas = document.getElementById("t2p_graph");

const heigthUnit= canvas.clientHeight/8
const widthUnit = canvas.clientWidth / 8
const heigthSubUnit = heigthUnit/8
const widthSubUnit = widthUnit/8

if (canvas.getContext) {
    const ctx = canvas.getContext("2d");
    // Ejes
    ctx.lineWidth = 2
    ctx.beginPath();
    ctx.moveTo(widthUnit, heigthUnit);
    ctx.lineTo(widthUnit, heigthUnit * 7);
    ctx.lineTo(widthUnit * 7, heigthUnit * 7);
    ctx.stroke();

    // flechas ejes
    ctx.beginPath();
    ctx.moveTo(widthUnit - widthSubUnit, heigthUnit);
    ctx.lineTo(widthUnit + widthSubUnit, heigthUnit);
    ctx.lineTo(widthUnit, heigthUnit - widthSubUnit*2);
    ctx.closePath();
    ctx.fill();

    ctx.beginPath();
    ctx.moveTo(widthUnit * 7, heigthUnit * 7 - heigthUnit / 8);
    ctx.lineTo(widthUnit * 7, heigthUnit * 7 + heigthUnit / 8);
    ctx.lineTo(widthUnit * 7 + widthSubUnit * 2, heigthUnit * 7);
    ctx.closePath();
    ctx.fill();

    // Nombres ejes
    ctx.font = `${widthSubUnit*3}px sans-serif`;
    ctx.fillText("P", widthUnit - widthSubUnit*4, heigthUnit - heigthSubUnit);
    ctx.fillText("Q", widthUnit*7 + widthSubUnit, heigthUnit*7 + heigthSubUnit*4);

    // Curvas de demanda
    ctx.strokeStyle = "rgb(229, 45, 35)";
    ctx.beginPath();
    ctx.moveTo(widthUnit, heigthUnit * 2);
    ctx.lineTo(widthUnit * 6, heigthUnit * 7);
    ctx.stroke();

    ctx.strokeStyle = "rgb(0, 130, 252)";
    ctx.beginPath();
    ctx.moveTo(widthUnit, heigthUnit * 3);
    ctx.lineTo(widthUnit * 5, heigthUnit * 7);
    ctx.stroke();

    // Intersección con ejes

    // --------------  Solución  --------------- //
    // Costo Marginal

    // Precio Cliente Demanda Baja

    // Intersección con eje Y




}


