import time
#===========================================================================
#Filtros de estudiantes
#===========================================================================
# estudiantes = [ 
#     {"Nombre": "Juan", "Edad": 17, "Calificaciones": [85, 90, 88]},
#     {"Nombre": "Maria", "Edad": 19, "Calificaciones": [92, 89, 30]},
#     {"Nombre": "Pedro", "Edad": 21, "Calificaciones": [85, 95, 80]},
#     {"Nombre": "Ana", "Edad": 18, "Calificaciones": [90, 92, 87]},
#     {"Nombre": "Luis", "Edad": 20, "Calificaciones": [88, 85, 92]},
# ]
# def primo(edad):
#     if edad <= 1:
#         return False
#     for i in range(2, int(edad**0.5) + 1):
#         if edad % i == 0:
#             return False
#     return True

# def filtro1():
#     for estudiante in estudiantes:
#         suma = 0
#         for nota in estudiante["Calificaciones"]:
#             suma += nota
#             prom = suma/len(estudiante["Calificaciones"])
#             if estudiante["Edad"] >= 18:
#                 if prom >= 85.0:
#                     print (f"El estudiante {estudiante["Nombre"]}, tiene un promedio de {prom:.2f}")
#             else:
#                 print("No se han encontrado estudiantes con esas caracteristicas")

# def filtro2():
#     for estudiante in estudiantes:
#         suma = 0
#         for nota in estudiante["Calificaciones"]:
#             suma += nota
#             prom = suma/len(estudiante["Calificaciones"])
#         if not primo(estudiante["Edad"]):
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
#Listas sin 0
#===========================================================================
# num = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
# lista = []
# lista_final = []
# letras = "ABCDEFGHIJKLMNOPQRS"

# def filtro():
#     #Eliminar la sublista con 0 al inicio
#     for numeros in num:
#         if numeros[0] == 0:
#             continue
#     #Eliminar los 0 de la sub lista
#         while 0 in numeros:
#             numeros.remove(0)
#         lista.append(numeros)
#         for i, lista_nueva in enumerate(lista):
#             etiqueta = letras[i]
#         lista_final.append(f"{etiqueta}: {lista_nueva}")
#     print("================================")
#     print("La lista final es:")
#     print(lista_final)
#     print("================================")
# filtro()

#===========================================================================
#Operaciones
#===========================================================================
def suma(num1, num2):
    suma = num1 + num2
    return(suma)

def resta(num1, num2):
    resta = num1 - num2
    return(resta)

def mult(num1, num2):
    mult = num1 * num2
    return(mult)

def div(num1, num2):
    div = num1 / num2
    return(div)

tupla = []
while True:
    print("====================")
    print("Bienvenido a calcular Z")
    print("Ingrese los numeros a calcular")
    print("====================")

    num1 = float(input("Ingrese el primer numero a calcular: "))
    num2 = float(input("Ingrese el segundo numero a calcular: "))
    time.sleep(3)
    print("El resultado final es el siguiente.")
    print(f"Suma: {suma(num1,num2)}")
    print(f"Resta: {resta(num1,num2)}")
    print(f"Multiplicacion: {mult(num1,num2)}")
    print(f"Division: {div(num1,num2)}")
    time.sleep(2)
    print("Los resultados han sido almacenados")

    tupla.append(f"Suma: {suma(num1,num2)}, Resta: {resta(num1,num2)}, Multiplicacion: {mult(num1,num2)}, Division: {div(num1,num2)}")