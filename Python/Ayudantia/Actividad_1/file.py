#1.- Imprimir el nombre completo
nombre = "Marcelo Criado Collao"
print(nombre)

print("============================================")
#2.- Operaciones
num1 = 25
num2 = 30

suma = (num1 + num2)
resta = (num2 - num1)
mult = (num1 * num2)
div = (num2 / num1)

print(f"Total suma:", suma)
print(f"Total resta:", resta)
print(f"Total multiplicacion:", mult)
print(f"Total division:", div)

print("============================================")
#2.5.- bonus total de la division
rest = (num2 % num1)

print(f"El resto de la division:", rest)

print("============================================")
#3.- Comparacion de numeros
num3 = 80
num4 = 80

def comparacion(num3, num4):
    if num3 > num4:
        print(f"El numero", num3, "es mayor que el numero", num4)
    elif num3 < num4:
        print (f"El numero", num3, "es menor que el numero", num4)
    else:
        print ("Los numeros son iguales")

comparacion(num3, num4)

print("============================================")
#5.- Calcular Celcius a Fahrenheit
tem = float(input("Ingresa los grados a calcular: (solo el numero)"))

cal_tem = (tem * 9 / 5) + 32

print(f"La temperatura en grados Fahrenheit es:", cal_tem,"°F")