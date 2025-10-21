
const loginButton = document.getElementById("login");
const regButton = document.getElementById("registro");

loginButton.addEventListener("click", function() { 
        if (loginButton.textContent === "Iniciar Sesion") { /* Se compara su el contenido de texto del boton es "Iniciar Sesion" */
            loginButton.textContent = "Cerrar Sesion"; /* Si es igual el texto cambia a "Cerrar Sesion" */
            alert("Inicio de sesión exitoso"); /* Envia un mensaje mediante al navegador comprobando el inicio de sesion */
        } else {
            loginButton.textContent = "Iniciar Sesion"; /* Si es distinto vuelve a "Iniciar Sesion" */
            alert("Se ha cerrado sesión correctamente"); /* Envia un mensaje mediante al navegador alertando el cierre de sesion */
        }
});

regButton.addEventListener("click", function() {
    alert("Pagina no encontrada"); /* Envia un mensaje mediante al navegador alertando que la pagina no fue encontrada */
});

const titulo = document.getElementById("titulo");
const generos = document.querySelectorAll(".genero"); /* Se seleciona todos los elementos con la clase ".genero" */

generos.forEach(function(genero) { /* Se llama un "forEach" para recorrer todos los elementos seleccionados, en este caso todos los que tenga la clase "genero" */
    genero.addEventListener("click", function(event){
        event.preventDefault(); /* Evita que la pagina se actualize, debido a que se utilizo "a href" en vez de "button" para la creacion de esta seccion */
        titulo.textContent = genero.textContent; /* Cambia el contenido del titulo por el contenido del genero clickeado */
    })
})

const rentabutton = document.querySelectorAll(".ren-btn button");

rentabutton.forEach(function(button){ /* Se llama un "forEach" para recorrer todos los elementos seleccionados, en este caso los "buttons" de la clase "ren-btn" */
    button.addEventListener("click", function() {
        if (button.textContent === "Rentar") { /* Se compara su el contenido de texto del boton es "Rentar" */
            button.textContent = "No disponible"; /* Si es igual el texto cambia a "No disponible" */
            button.style.backgroundColor = "red"; /* Si el texto cambia el color de fondo cambia rojo*/
            button.style.width = "16vh"; /* Se ajusta el tamaño del boton para que el texto se ajuste mejor */
            button.style.color = "white"; /* Se cambia el color de letra a blanco */
        }
    })
})
