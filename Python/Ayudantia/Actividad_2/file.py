# print("=====================================================")
# print("Imprimir la lista o arreglo creada/o")
# print("=====================================================")
# frutas = ["Manzana", "Platano", "Frutilla", "Toronja"]
# for i in frutas:
#     print(i)


# print("=====================================================")
# print("En reversa")
# print("=====================================================")
# for o in reversed(frutas):
#     print(o)

# print("=====================================================")
# print("Orden alfabetico")
# print("=====================================================")
# for u in sorted(frutas):
#     print(u)

# print("=====================================================")
# print("Contador del 1 al 10")
# print("=====================================================")
# cont=1
# while cont <= 10:
#     print(cont)
#     cont += 1
# else:
#     print("BOOOM!!!!!!!!")

# =====================================================
# Menu
# =====================================================
while True:
    print("===============================")
    print("Bienvenido al sistema NoSe")
    print("Ingrese la opcion que desea realizar")
    print("1) Imprimir un mensaje")
    print("0) Salir")
    print("===============================")

    opcion = int(input("Seleccion su opcion: "))

    if opcion == 1:
        msg = input("¿Que mensaje desea enviar?: ")
        print(msg)
    
    elif opcion == 0:
        print("Gracias por estar con nosotros. vuelva pronto.")
        break

    else:
        print("Opcion no encontrada, por favor intente de nuevo")