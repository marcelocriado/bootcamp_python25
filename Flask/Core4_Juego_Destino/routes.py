from flask import Flask, render_template, redirect, session, request, url_for  # Importa Flask para permitirnos crear nuestra aplicación
import random
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
app.secret_key = "Core4"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida'] = request.form['comida']
    session['profesion'] = request.form.getlist("profesion")
    return redirect(url_for('futuro'))

@app.route('/futuro')
def futuro():
    nombre = session['nombre']
    lugar = session['lugar']
    numero = session['numero']
    comida = session['comida']
    profesion = session['profesion'][0]
    if random.random() < 0.5:
        mensaje = f"""
        !Soy el adivino del Dojo! 
        {nombre} tendrás un viaje muy largo dentro de {numero} años
        a {lugar} y estarás el resto de tus días preparando {comida} 
        para todas las personas que quieres, conseguiras tu profesion
        soñada de {profesion}.
        """
        gif = "nat-20-baldur's-gate.gif"
    else:
        mensaje = f"""
        !Soy el adivino del Dojo! 
        {nombre} tendrás {numero} años de mala suerte, 
        nunca conocerás {lugar}, jamás volveras a comer {comida}
        y nunca podras ser {profesion}.
        """
        gif = "tenor.gif"
    return render_template('resultado.html', mensaje = mensaje, gif=gif)

@app.route('/logout', methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__=="__main__":   
    app.run(debug=True)  