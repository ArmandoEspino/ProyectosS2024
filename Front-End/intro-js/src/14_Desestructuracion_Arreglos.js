const alumnos = ['monse', 'mau', 'guzzi', 'jose', 'barbara', 'juan'];

const [nom1, nom2, nom3, ...nombres] = alumnos;

console.log(nom1, nom2, nom3, ...nombres);