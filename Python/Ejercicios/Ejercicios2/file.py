#=========================================================================
#Librerias
#=========================================================================
import random
import sys

#=========================================================================
#Saludo personalizado con año de nacimiento
#=========================================================================
# nombre = input("Ingresa su nombre: ")
# anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
# anio_actual = 2025
# anios = anio_actual - anio_nacimiento

# print(f"Hola", nombre, ", naciste en", anio_nacimiento, " y ahora tienes ", anios, "años.")

#=========================================================================
#Número par, impar o múltiplo de 5
#=========================================================================
# num = int(input("Ingrese su numero: "))
# if num % 2 == 0:
#     if num % 5 == 0:
#         print("Su numero es par y es multiplo de 5")
#     else:
#         print("su numero es par, pero no es multiplo de 5")
# else:
#     if num % 5 == 0:
#         print("Su numero es impar y es multiplo de 5")
#     else:
#         print("su numero es impar, pero no es multiplo de 5")

#==========================================================================
#Serie de cuadrados
#==========================================================================
# num = int(input("Ingrese su numero: "))
# for i in range(1, num+1):
#     print(i**2)

#==========================================================================
#Promedio hasta cero
#==========================================================================
# suma = 0
# cont= 0

# while True:
#     num = int(input("Ingrese su numero, (Ingrese ""0"" para terminar): "))

#     if num > 0:
#         suma += num
#         cont += 1

#     if num == 0:
#         print(f"El promedio de los numeros que a ingresado es ", suma/cont)
#         break

#========================================================================
#Gestor de cuentas bancarias
#========================================================================
# monto = 500000

# while True:
#     print("====================")
#     print("Bienvenido a BancoEstado")
#     print("Ingrese la opcion que desea realizar.")
#     print("1) Ver monto total.")
#     print("2) Ingresar monto.")
#     print("3) Retirar monto.")
#     print("0) Salir.")
#     print("====================")

#     opcion = int(input("Ingrese una opcion: "))

#     if opcion == 0:
#         print("Gracias por elegirnos, !Vuelva pronto¡")
#         break

#     elif opcion == 1:
#         print(f"Su monto total es de $", monto)

#     elif opcion == 2:
#         sumonto = int(input("Ingrese el monto que quiera ingresar: $"))
#         monto = monto + sumonto
#         print(f"Su monto actual es de $", monto)

#     elif opcion == 3:
#         remonto = int(input("Ingrese el monto que quiera retirar: $"))
#         if remonto <= monto:
#             print(f"¿Desea retirar $", remonto, " de su cuenta?")
#             print("1) Si")
#             print("0) No")
#             eleccion = int(input("Ingrese su opcion: "))
#             if eleccion == 1:
#                 monto = monto - remonto
#                 print(f"Su monto actual es de $", monto)
#             else:
#                 print("Operacion cancelada.")
#         else:
#                 print("Su saldo es insuficiente.")