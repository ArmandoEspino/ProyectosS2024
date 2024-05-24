
const carros = ['Model S', 'Model E', 'Model X', 'Model O'];

const carros2 = carros.concat('Model A', 'Model AN', 'Model L');

const motos = ['Yamaha', 'Italika', 'Ninja'];

const tienda = [...motos, ...carros, 'rin 18'];

const tienda2 = motos.concat(carros2).concat('rin 18');

console.log(carros2);
console.log(tienda2);