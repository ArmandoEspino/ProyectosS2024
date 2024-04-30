// Creacion de un objeto

const carro = {
    id: 1,
    nombre: 'Model Y',
    date: new Date(),
    marca: {
        id: 1,
        nombre: 'Tesla',
        ubicacion: 'Europa',
        age: 100
    },
    costo: 1000000,
    saludo: function () {
        return `Hola ${this.marca.nombre} ${this.nombre}`;
    }
}

// Sets
carro.nombre = 'Model X';
carro.costo = 1200000;

// Impresion
console.log(`${carro.saludo()}`);