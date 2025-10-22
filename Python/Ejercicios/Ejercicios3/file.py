# estudiantes = [ 
#     {"Nombre": "Juan", "Edad": 17, "Calificaciones": [85, 90, 88]},
#     {"Nombre": "Maria", "Edad": 19, "Calificaciones": [92, 89, 30]},
#     {"Nombre": "Pedro", "Edad": 21, "Calificaciones": [85, 95, 80]},
#     {"Nombre": "Ana", "Edad": 18, "Calificaciones": [90, 92, 87]},
#     {"Nombre": "Luis", "Edad": 20, "Calificaciones": [88, 85, 92]},
# ]

# def filtro1():
#     for estudiante in estudiantes:
#         notas = estudiante["Calificaciones"]
#         prom = sum(notas)/len(notas)
        
#         if estudiante["Edad"] >= 18:
#             if prom >= 85.0:
#                 print (f"El estudiante {estudiante["Nombre"]}, tiene un promedio de {prom:.2f}")
#         else:
#             print("No se han encontrado estudiantes con esas caracteristicas")

# def filtro2():
#     suma = 0
#     for estudiante in estudiantes:
#         notas = estudiante["Calificaciones"]
#         suma += notas
#         prom = suma/len(notas)

#         if estudiante["Edad"] % 2 == 0:
#             print (f"El estudiante {estudiante["Nombre"]}, con edad {estudiante["Edad"]}, tiene un promedio de {prom:.2f}")

# while True:
#     print("====================")
#     print("Bienvenido al centro de notas")
#     print("Ingrese la opcion que desea realizar.")
#     print("1) Ver estudiantes mayores de 18 años y promedio superior a 85.")
#     print("2) Ver promedio de estudiantes con edad prima.")
#     print("0) Salir.")
#     print("====================")

#     opcion = int(input("Ingrese una opcion: "))

#     if opcion == 0:
#         print("Gracias por elegirnos, !Vuelva pronto¡")
#         break

#     elif opcion == 1:
#         filtro1()

#     elif opcion == 2:
#         filtro2()

#===========================================================================
#
#===========================================================================
num = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
lista = []
def filtro():
    for numeros in num:
        if numeros[0] == 0:
            continue
        print(numeros)
filtro()