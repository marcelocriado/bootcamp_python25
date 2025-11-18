from flask_app import app #Importamos la app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.usuario import Usuario #Importamos desde models
from flask_bcrypt import Bcrypt #Importamos Bcrypt
# from flask_app.models.curso import Curso #Importamos desde models

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect(url_for("pagina_principal"))
    return redirect(url_for('inicio'))

@app.route('/inicio')
def inicio():
    if 'usuario_id' in session:
        return redirect(url_for("pagina_principal"))
    return render_template("inicio_sesion.html")

@app.route('/registro')
def registro():
    if 'usuario_id' in session:
        return redirect(url_for("pagina_principal"))
    return render_template("registro.html")

@app.route('/pagina_principal')
def pagina_principal():
    if 'usuario_id' not in session:
        return redirect(url_for('index'))
    
    datos = {"id": session['usuario_id']}
    usuario = Usuario.buscar_por_id(datos)

    return render_template("index.html", user = usuario)

@app.route('/registrar_usuario',methods=['POST'])
def registrar_usuario():
    datos = {
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "contrasenia": request.form['contrasenia'],
        "contrasenia_conf": request.form['contrasenia_conf'],
        "f_nacimiento": request.form['f_nacimiento']
    }
    #Llamamos al método para validar
    if not Usuario.validar_registro(datos):
        return redirect(url_for('registro')) #Si NO es valida la información, redirigimos al formulario
    
    pass_hasheado = bcrypt.generate_password_hash(request.form['contrasenia'])
    #Generamos un diccionario con toda la info contraseña hasheada
    formulario = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "contrasenia": pass_hasheado,
        "f_nacimiento": request.form['f_nacimiento']
    }

    #Invocamos el método para guardar el usuario
    nuevo_id = Usuario.save(formulario) #Recibiendo el ID del nuevo Usuario
    session['usuario_id'] = nuevo_id #Guardamos en sesión el id del usuario
    return redirect('/inicio')

@app.route("/login", methods=['POST'])
def login():
    #Verificamos que el email exista en BD
    usuario = Usuario.buscar_por_email(request.form)
    if not usuario: #En caso de no estar registrado mandamos mensaje de error
        flash("Contraseña o email incorrecto", "login")
        return redirect("/inicio")
    
    #Comparamos las contraseñas
    if not bcrypt.check_password_hash(usuario.contrasenia, request.form['contrasenia']):
        flash("Contraseña o email incorrecto", "login") #Si no coinciden mandamos mensaje error
        return redirect("/inicio")
    
    session['usuario_id'] = usuario.id #Guardamos en sesión el id del usuario

    return redirect("/pagina_principal")

@app.route('/destruir_sesion', methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for('inicio'))