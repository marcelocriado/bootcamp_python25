from flask_app.config.mysqlconnection import connectToMySQL #importamos desde config
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.contrasenia = data['contrasenia']
        self.f_nacimiento = data['f_nacimiento']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        users_en_bd = connectToMySQL('esquema_eventos').query_db(query)
        users = []
        for user in users_en_bd:
            users.append(cls(user))
        return users
    
    @staticmethod
    def validar_registro(user):
        es_valido = True #Asumimos que la información en válida

        # Normalizar el nombre y apellido
        user['nombre'] = user['nombre'].strip().title()
        user['apellido'] = user['apellido'].strip().title()

        # Normalizar email
        user['email'] = user['email'].lower()

        if len(user['nombre']) < 2:
            flash("El nombre debe tener al menos 2 caracteres", "datos") #Generamos el mensaje
            es_valido = False #El formulario deja de ser válido

        if len(user['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres", "datos")
            es_valido = False  
        
        if not EMAIL_REGEX.match(user['email']):
            flash("E-mail inválido", "email")
            es_valido = False
        
        # Evitar correos repetidos
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultado = connectToMySQL('esquema_eventos').query_db(query, {"email": user['email']})

        if len(resultado) >= 1:   # Si existe al menos 1 registro
            flash("El email ya está registrado", "email")
            es_valido = False

        if len(user['contrasenia']) < 8:
            flash("la contraseña debe tener al menos 8 caracteres", "pass")
        
        # Confirmar contraseña
        if user['contrasenia'] != user['contrasenia_conf']:
            flash("Las contraseñas no coinciden", "pass")
            es_valido = False
        
        return es_valido #Regresamos si es válido o no
    
    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, contrasenia, f_nacimiento, created_at, updated_at) VALUES(%(nombre)s, %(apellido)s, %(email)s, %(contrasenia)s, %(f_nacimiento)s, NOW(), NOW());"
        return connectToMySQL('esquema_eventos').query_db(query, datos)
    
    @classmethod
    def buscar_por_email(cls, datos):
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        resultados = connectToMySQL('esquema_eventos').query_db(query, datos)
        if len(resultados) == 1:
            #Si existe el usuario
            usuario = cls(resultados[0])
            return usuario #Regreso la instancia del usuario con ese correo
        else:
            return False
    
    @classmethod
    def buscar_por_id(cls, datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL('esquema_eventos').query_db(query, datos)

        if len(resultado) < 1:
            return False
        return cls(resultado[0])