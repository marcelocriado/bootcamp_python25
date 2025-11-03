from flask import Flask, render_template, redirect, url_for  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')
def index():
    return redirect(url_for('lista'))

@app.route('/lista')
def lista():
    paises = [
    {'pais': 'Argentina' , 'capital': 'Buenos Aires'},
    {'pais': 'Brasil' , 'capital': 'Brasilia'},
    {'pais': 'Chile' , 'capital': 'Santiago de Chile'},
    {'pais': 'Colombia' , 'capital': 'Bogotá'},
    {'pais': 'Costa Rica' , 'capital': 'San José'},
    {'pais': 'Paraguay' , 'capital': 'Asunción'},
    {'pais': 'Perú' , 'capital': 'Lima'}
    ]
    return render_template('index.html', paises = paises)

if __name__=="__main__":   
    app.run(debug=True)  
