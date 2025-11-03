from flask import Flask, render_template, redirect, url_for  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')
def index():
    return redirect(url_for('loteria'))

@app.route('/loteria', defaults={'filas': 4, 'columnas': 4})
@app.route('/loteria/<int:filas>', defaults={'columnas': 4})
@app.route('/loteria/<int:filas>/<int:columnas>')
def loteria(filas, columnas):
    return render_template('index.html', filas = filas, columnas = columnas)

if __name__=="__main__":   
    app.run(debug=True)  