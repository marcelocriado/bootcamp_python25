import time

def suma(num1, num2):
    sum = num1 + num2
    print("======================")
    print(f"El resultado de la suma es: {sum}")
    print("======================")
    return(sum)

def rest(num1, num2):
    res = num1 - num2
    print("======================")
    print(f"El resultado de la suma es: {res}")
    print("======================")
    return(res)

def mostrar_menu():
    print("======================")
    print("1) Sumar")
    print("2) Restar")
    print("0) Salir")
    print("======================")

def main ():
    while True:
        mostrar_menu()

        opcion = int(input("Eliga una opcion: "))
        if opcion == 0:
            print("Saliendo del programa")
            time.sleep(3)
            break
        elif opcion == 1:
            num1 = float(input("Ingrese el primer numero a sumar: "))
            num2 = float(input("Ingrese el segundo numero a sumar: "))
            time.sleep(3)
            suma(num1, num2)
        elif opcion == 2:
            num1 = float(input("Ingrese el primer numero a restar: "))
            num2 = float(input("Ingrese el segundo numero a restar: "))
            time.sleep(3)
            rest(num1, num2)
        else:
            print("La opcion no existe")

main()