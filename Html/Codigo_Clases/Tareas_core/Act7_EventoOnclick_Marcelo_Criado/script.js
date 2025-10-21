/* Se utiliza el DomContenLoades para esperar a que el documento esté completamente cargado */
document.addEventListener("DOMContentLoaded", function() {
    const loginButton = document.getElementById("login"); /* Se crea una variable inmutable, relacionada con el id del boton  de "Iniciar Sesion" */
    const defbutton = document.getElementById("def"); /* Se crea una variable inmutable, relacionada con el id del boton de "agregar definicion" */
    const likebutton = document.querySelectorAll(".like-btn button") /* Se crea una variable inmutable, relacionada con la clase "like-btn", debido a que hay mas de un boton con el mismo funcionamiento y al asignarle una id igual a ambos solo se accionara el primero*/

    loginButton.addEventListener("click", function() { /* Se utiliza la variable antes creada, relacionadola con un activador, este se activa siempre que un evento de "click" se haga presente en el boton*/
        if (loginButton.textContent === "Iniciar Sesion") { /* Se compara su el contenido de texto del boton es "Iniciar Sesion" */
            loginButton.textContent = "Cerrar Sesion"; /* Si es igual el texto cambia a "Cerrar Sesion" */ 
        } else {
            loginButton.textContent = "Iniciar Sesion"; /* Si es distinto vuelve a "Iniciar Sesion" */
        }
    });

    defbutton.addEventListener("click", function() {
        defbutton.style.display = "none"; /* Se altera el estilo del boton, "eliminando" su estilo visual */
    })

    likebutton.forEach(function (button) { /* Se recorre todos los botenes que tengan la clase */
        button.addEventListener("click", function() {

            const mensaje = button.getAttribute("data-msg"); /* Se crea una constante inmutable que "absorve" los atributos del button, en este caso el "data-msg" */
            alert(mensaje); /* Se envia la alerta del navegador */

            const contador = button.querySelector(".contador"); /* Se crea una constante inmutable que selecciona todos los span con la clase "contador" */
            let valor = parseInt(contador.textContent); /* Se crea un valor mutable, luego mediante "textContent" se obtiene el contenido del span, para luego ser transformado mediante "parseInt" en un entero para realizar la funcion matematica siguiente */
            contador.textContent = valor + 1; /* El contenido del span es cambiado por el resultado del valor obtenido anteriormente + 1 */
        })
    });
});
