/* Variable mutable */
let edad = 12;
let calificaciones = [5.5, 6.5, 3.2, 5.6, 6.6];
let frutas_favoritas = ["Manzana", "Platano", "Frutilla"]

/* Variable inmutable */
const nombre = "Jhon";

/* Sprint de la primera parte */
console.log(nombre)
console.log(edad)
console.log(calificaciones)
console.log(frutas_favoritas)

/* Se agregan dos valores mas a frutas_favoritas */
frutas_favoritas.push("Mandarina", "Damasco")
console.log(frutas_favoritas)

/* Se accede a la primera fruta y se hace sprint */
console.log(frutas_favoritas[0]);

/* Ciclo for y sprint de cada elemento de frutas_favoritas*/
for (let i = 0; i < frutas_favoritas.length; i++){
    console.log(frutas_favoritas[i])
}