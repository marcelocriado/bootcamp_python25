from flask import Flask, render_template, redirect, url_for, session, request  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
app.secret_key = "Core3"
contVisitas = 0
contReset = 0

@app.route('/')
def index():
    if 'email_usuario' in session:
        return redirect(url_for("visitas"))
    return render_template('login.html')

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    session['nombre_usuario'] = request.form['nombre']
    session['email_usuario'] = request.form['email']
    return redirect('visitas')

@app.route('/destruir_sesion', methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/visitas')
def visitas():
    if 'email_usuario' not in session:
        return redirect(url_for('index'))
    global contVisitas
    global contReset
    if session.get("skip_next", False):
        session["skip_next"] = False
    else:
        contVisitas += 1
    return render_template('index.html', contVisitas = contVisitas, contReset = contReset)

@app.route("/sumar2", methods=["POST"])
def sumar2():
    global contVisitas
    contVisitas += 2
    session["skip_next"] = True
    return redirect(url_for("visitas"))

@app.route("/reset", methods=["POST"])
def reset():
    global contVisitas
    global contReset
    contVisitas = 0
    contReset += 1
    session["skip_next"] = True
    return redirect(url_for("visitas"))

@app.route("/sumar", methods=["POST"])
def sumar():
    global contVisitas
    try:
        n = int(request.form.get("visitas", 0))
    except ValueError:
        n = 0
    contVisitas += n
    session["skip_next"] = True
    return redirect(url_for("visitas"))

if __name__=="__main__":   
    app.run(debug=True)  