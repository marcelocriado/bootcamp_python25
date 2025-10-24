import random
import time

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    def pagar_tarjeta(self):
        if self.saldo_pagar <= self.limite_credito:
            print("================================")
            print("¿Desea continuar la operacion?")
            print("1) Si")
            print("0) No")
            eleccion = int(input("Ingrese su opcion: "))
            if eleccion == 1:
                self.limite_credito = self.limite_credito - self.saldo_pagar
                self.saldo_pagar = self.saldo_pagar - self.saldo_pagar
                print("El pago se a realizado correctamente")
            else:
                print("Operacion cancelada.")
        elif self.saldo_pagar == 0:
            print("Usted no tiene ningun monto a pagar")
        else:
            print("Su saldo es insuficiente.")

    def transferir_deuda(self, otro_usuario):
            while True:
                print("  ===========================================")
                print("|| Bienvenido al sistema de transferencia ||")
                print("")
                print("|| ¿Que funcion desea realizar?")
                print("1) Transferir a otro usuario")
                print("0) Salir")
                print("")

                opcion = int(input("Ingrese el numero de la opcion a realizar: "))
                if opcion == 0:
                    print("Saliendo. . .")
                    time.sleep(3)
                    break
                elif opcion == 1:
                    time.sleep(2)
                    monto = int(input("Ingrese el monto a transferir: $"))
                    if monto <= 0:
                        print("El monto debe ser mayor que cero.")
                        time.sleep(2)
                    elif monto > self.limite_credito:
                        print("No cuenta con el suficiente credito para realizar dicha transferencia")
                        time.sleep(2)
                    else:
                        print(f"¿Desea transferir ${monto} del limite de credito?")
                        print("1) Sí")
                        print("0) No")
                        print("")

                        eleccion = int(input("Ingrese su opción: "))
                        if eleccion == 1:
                            self.limite_credito -= monto
                            otro_usuario.limite_credito += monto
                            print("Transferencia realizada correctamente.")
                            time.sleep(2)
                            print("=======================================================")
                            print(f"Su nuevo limite de credito es: {self.limite_credito}")
                            print("=======================================================")
                            time.sleep(3)
                        else:
                            print("Operación cancelada.")
                            time.sleep(2)
                else:
                    print("La opcion no existe.")
                    time.sleep(2)

    def mostrar_saldo_usuario(self):
        while True:
            print("=======================")
            print(" ||   Bienvenido  ||")
            print(f" || {self.nombre} {self.apellido} ||")
            print("")
            print("")
            print(f" || Su limite de credito actual es: ${self.limite_credito} ||")
            print(f" || Tiene un monto a pagar de: ${self.saldo_pagar} ||")
            print("")
            print("")
            print(" || ¿Que funcion desea realizar?")
            print("")
            print("1) Comprar")
            print("2) Pagar monto")
            print("3) Transferir")
            print("0) Salir")
            print("")

            opcion = int(input("Ingrese el numero de la opcion a realizar: "))
            if opcion == 0:
                print("Saliendo. . .")
                time.sleep(3)
                break
            elif opcion == 1:
                time.sleep(2)
                compra = random.randint(5000, 40000)
                self.hacer_compra(compra)
                print(f"Ha realizado una compra por ${compra}")
                time.sleep(3)
            elif opcion == 2:
                time.sleep(2)
                self.pagar_tarjeta()
            elif opcion == 3:
                time.sleep(2)
                print("=============================")
                print("|| Usuarios disponibles para transferir")
                for id, i in usuarios_sistema.items():
                    if i != self:
                        print(f"{id}) {i.nombre} {i.apellido}")
                print("0) Salir")
                print("")

                trans = int(input("Ingrese el numero de la opcion a realizar: "))
                if trans == 0:
                    print("Saliendo. . .")
                    time.sleep(3)
                    break
                elif trans in usuarios_sistema and usuarios_sistema[trans] != self:
                    time.sleep(2)
                    self.transferir_deuda(usuarios_sistema[trans])
            else:
                print("La opcion no existe.")

def main_menu():
    while True:
        print("=======================")
        print("1) Usuarios")
        print("0) Salir")
        print("")

        opcion = int(input("Ingrese el numero de la opcion a realizar: "))

        if opcion == 0:
            print("Saliendo del sistema")
            time.sleep(3)
            break
        elif opcion == 1:
            time.sleep(2)
            usuarios()
        else:
            print("La opcion no existe.")

usuarios_sistema = {
    1: Usuario("Jose", "Florecio", "j.flore@gmail.com"),
    2: Usuario("Daniel", "Collao", "d.colla@gmail.com")
}

def usuarios():
    while True:
        print("")
        print("")
        print("=======================")
        print("Elige el usuario con el cual quieras interactuar")
        print("1) Usuario [Jose]")
        print("2) Usuario [Daniel]")
        print("0) Salir")
        print("")

        opcion = int(input("Ingrese el numero de la opcion a realizar: "))
        if opcion == 0:
            print("Saliendo. . .")
            time.sleep(3)
            break
        elif opcion in usuarios_sistema:
            usuario = usuarios_sistema[opcion]
            time.sleep(2)
            usuario.mostrar_saldo_usuario()
        else:
            print("La opcion no existe.")

main_menu()