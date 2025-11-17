from flask_app.config.mysqlconnection import connectToMySQL #importamos desde config

class Curso:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, datos):
        query = "INSERT INTO cursos (nombre, created_at, updated_at) VALUES(%(nombre)s, NOW(), NOW());"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, datos)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        cursos_en_bd = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
        cursos = []
        for curso in cursos_en_bd:
            cursos.append(cls(curso))
        return cursos