// Creacion de un objeto

const carro = {
    id: 1,
    nombre: 'Model Y',
    date: new Date(),
    marca: 'Tesla',
    costo: 1000000
}

carro.nombre = 'Model X';
carro.costo = 1200000;

console.log(`Auto: ${carro.nombre}
Costo: ${carro.costo}`);