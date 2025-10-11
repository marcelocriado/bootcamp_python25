/* Se utiliza el DomContenLoades para esperar a que el documento esté completamente cargado */
document.addEventListener("DOMContentLoaded", function() {
    const likebutton = document.querySelectorAll(".like-btn button") /* Se crea una variable inmutable, relacionada con la clase "like-btn", debido a que hay mas de un boton con el mismo funcionamiento y al asignarle una id igual a ambos solo se accionara el primero*/

        likebutton.forEach(function (button) { /* Se recorre todos los botenes que tengan la clase */
        button.addEventListener("click", function() {
            const contenedor = button.parentElement;
            const contador = contenedor.querySelector(".contador"); /* Se crea una constante inmutable que selecciona todos los span con la clase "contador" */
            let valor = parseInt(contador.textContent); /* Se crea un valor mutable, luego mediante "textContent" se obtiene el contenido del span, para luego ser transformado mediante "parseInt" en un entero para realizar la funcion matematica siguiente */
            contador.textContent = valor + 1; /* El contenido del span es cambiado por el resultado del valor obtenido anteriormente + 1 */
        })
    });
})