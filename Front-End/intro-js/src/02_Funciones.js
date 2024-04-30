//  Funciones

function ObtenerInfo(name, lastname){
    const info = `Hola ${name} ${lastname}`;

    return info
}

const info = ObtenerInfo('Yesse','Armando');

console.log(info);


//  Funcion anonima

const ObtenerInfo = (name, lastname) => `${name} ${lastname}`;

const Sum = (a, b) => a + b;

console.log(ObtenerInfo('Jesse','Espino'));
console.log(Sum(20,4));