from flask_app import app #Importamos la app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.estudiante import Estudiante #Importamos desde models
from flask_app.models.curso import Curso #Importamos desde models

@app.route('/')
def index():
    return redirect(url_for('cursos'))

@app.route('/estudiante')
def estudiante():
    estudiantes = Estudiante.get_all()
    cursos = Curso.get_all()
    return render_template("index.html", todos_estudiantes = estudiantes, todos_cursos = cursos)

@app.route("/crear_estudiante", methods=['POST'])
def crear_estudiante():
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "edad": request.form['edad'],
        "curso_id": request.form['curso_id']
    }
    Estudiante.save(datos)
    return redirect('/')

@app.route('/cursos')
def cursos():
    cursos = Curso.get_all()
    return render_template('cursos.html', todos_cursos = cursos)

@app.route("/crear_curso", methods=['POST'])
def crear_curso():
    datos = {
        "nombre": request.form['nombre']
    }
    Curso.save(datos)
    return redirect('cursos')

@app.route('/ver_curso/<int:curso_id>')
def ver_curso(curso_id):
    estudiante_curso = Estudiante.get_by_curso(curso_id)
    return render_template("resultados.html", resultado = estudiante_curso)