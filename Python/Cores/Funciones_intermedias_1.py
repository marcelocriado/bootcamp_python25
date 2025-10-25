#======================================
#   Parte 1
#======================================
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    #Se agregan mas datos segun los solicitado en el core
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#===================================================
#   Cambia el valor de 3 en matriz por 6
#===================================================
# def cambio():
#     for sublistas in matriz:
#         for i in range(len(sublistas)):
#             if sublistas[i] == 3:
#                 sublistas[i] = 6
#         print (sublistas)

# cambio()

#===================================================
#   Cambia el nombre
#===================================================
# def cambio_nom():
#     for nombre in cantantes:
#         if nombre["nombre"] == "Ricky Martin":
#             nombre["nombre"] = "Enrique Martin Morales"
#         print (nombre)

# cambio_nom()

#===================================================
#   Cambia la ciudad
#===================================================
# def cambio_ciudad():
#     for ciudad in ciudades["México"]:
#         if ciudad == "Cancún":
#             ciudad = "Monterrey"
#         print(ciudad)

# cambio_ciudad()

#===================================================
#   Cambio de coordenadas
#===================================================
# def cambio_coords():
#     for coord in coordenadas:
#         coord["latitud"] = 9.9355431
#         print(coord)

# cambio_coords()


#=============================================
#   Parte 2
#=============================================
# def iterarDiccionario(lista):
#     for dato in lista:
#         contador = 0
#         total = len(dato)
#         for clave, valor in dato.items():
#             contador += 1
#             if contador == total:
#                 print(f"{clave} - {valor}")
#             else:
#                 print(f"{clave} - {valor}, ", end="")   #End evita hacer un salto de linea, se utilizo para evitar separar los datos a la hora de hacer print

# iterarDiccionario(cantantes) #Se utilizo la lista "cantantes" creada anteriormente como prueba.


#=============================================
#   Parte 3
#=============================================
# def iterarDiccionario2(llave, lista):
#     clave = llave
#     for dato in lista:
#         print(dato[clave])


# iterarDiccionario2("pais", cantantes)


#=============================================
#   Parte 4
#=============================================
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

#=========================================
#   Imprimir informacion
#=========================================
# def imprimirInformacion(diccionario):
#     for clave, dato in diccionario.items():
#         print(f"{len(dato)} {clave.upper()}") #Se utilizo upper para hacer que las letras esten en mayusculas y parecerse mas al ejemplo del caso
#         for item in dato:
#             print(item)


# imprimirInformacion(costa_rica)