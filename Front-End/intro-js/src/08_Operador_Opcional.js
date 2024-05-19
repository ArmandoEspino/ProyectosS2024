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
    inventarios: [
        {
            id: 1,
            color: 'Rojo',
            cantidad: 3,
            precio: 1100000
        },
        {
            id: 1,
            color: 'Blanco',
            cantidad: 2,
            precio: 1120000
        },
        {
            id: 1,
            color: 'Amarillo',
            cantidad: 1,
            precio: 1150000
        },
    ],
    totalInventario: function () {
        let total = 0;
        this.inventarios.forEach(inventario => {
            total = total + inventario.precio*inventario.cantidad;
        });
        return total;
    },
    costo: 1000000,
    saludo: function () {
        return `Hola ${this.marca.nombre} ${this.nombre}`;
    }
}

// Operador opcional

if(carro.lugarProcedencia != undefined && carro.lugarProcedencia.name){
    console.log('Cumple');
}else{
    console.log('No existe lugar de procedencia');
}

console.log(carro.lugarProcedencia);
console.log(carro.marca?.municipio?.name);