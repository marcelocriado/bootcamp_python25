from flask_app.config.mysqlconnection import connectToMySQL #importamos desde config

class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.curso_id = data['curso_id']

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO estudiantes (nombre, apellido, edad, created_at, updated_at, curso_id) VALUES(%(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW(), %(curso_id)s);"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, datos)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM estudiantes;"
        estudiantes_en_bd = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
        estudiantes = []
        for estudiante in estudiantes_en_bd:
            estudiantes.append(cls(estudiante))
        return estudiantes
    
    @classmethod
    def get_by_curso(cls,curso_id):
        query = "SELECT e.*, c.nombre FROM estudiantes e join cursos c on e.curso_id = c.id WHERE e.curso_id = %(curso_id)s;"
        datos = {"curso_id": curso_id}
        resultados = connectToMySQL('esquema_estudiantes_cursos').query_db(query,datos)
        estudiantes_curso = []
        print(estudiantes_curso)
        for i in resultados:
            estudiantes_curso.append(cls(i))
        return estudiantes_curso
    
    # @classmethod
    # def update(cls, datos):
    #     query = "UPDATE tacos SET tortilla=%(tortilla)s, guiso=%(guiso)s, salsa=%(salsa)s WHERE id = %(id)s;"
    #     return connectToMySQL('esquema_tacos').query_db(query, datos)
    
    # @classmethod
    # def delete(cls, datos):
    #     query = "DELETE FROM tacos WHERE id = %(id)s;"
    #     return connectToMySQL('esquema_tacos').query_db(query, datos)
