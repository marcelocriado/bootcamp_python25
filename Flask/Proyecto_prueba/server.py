from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return '¡Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/exito')
def exito(): #El nombre de la función puede ser el que tú quieras
    return "¡Éxito!"

@app.route('/saludo/<nombre>')
def saludo(nombre):
    print(nombre) #Imprime en la terminal el nombre enviado a través de la URL
    return (f'¡Hola {nombre}!') #Regresa al navegador '¡Hola ____!' con el nombre enviado a través de la URL

@app.route('/color/<nombre>/<color>')
def color_favorito(nombre, color):
    print(nombre)
    print(color)
    return f'Hola {nombre}, tu color favorito es el {color}'

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente   
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo