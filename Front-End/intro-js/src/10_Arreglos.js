
const carros = ['Model S', 'Model E', 'Model X', 'Model O'];

carros.push('Model A', 'Model AN','Model L');

//console.log(carros);

const num = [10, 5, 6, 12, 22];

num.push(332, 532, 545);

//console.log(num);

carros.forEach(carro => console.log(carro));

for( const car of carros){
    console.log(car);
}

for( let i = 0; i < carros.length; i++){
    const elem = carros[i];
    console.log('i ' + carros[i]);
}