#=============================================================
#   Se crea la clase usuario y tarjeta de credito
#=============================================================
class tarjetaCredito:
    def __init__(self, banco, monto = 0, limiteCredito = 20000, intereses = 15): #Se deja por defecto el valor del monto, limite de credito e intereses para todas las tarjetas de credito
        self.banco = banco
        if monto > 0:
            self.saldoPagar = monto
        else:
            self.saldoPagar = 0
        self.limiteCredito = limiteCredito
        self.intereses = (intereses/100)
    
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = {}
    
    def agregarTarjeta(self, banco, monto = 0, limiteCredito = 20000, intereses = 15):
        if banco in self.tarjetas: #Se asegura que el nombre de la tarjeta a crear no este duplicado
            print(f"Ya existe una tarjeta de este banco: {banco}")
        else:
            nuevaTarjeta = tarjetaCredito(banco, monto, limiteCredito, intereses) #Si la tarjeta no esta duplicada, se agrega a la lista del usuario con los valores por defectos definidos tanto en los valores de esta funcion como en la clase de tarjeta de credito
            self.tarjetas[banco] = nuevaTarjeta
            print(f"Ha registrado una nueva tarjeta en el siguiente banco: {banco}")
        return self

    def obtenerTarjeta(self, banco): #Se crean una funcion para "buscar" el nombre de la tarjeta, esto se ocupara en cada funcion siguiente para asegurar que el usuario si cuente con una tarjeta con ese nombre
        tarjeta = self.tarjetas.get(banco)
        if not tarjeta:
            print(f"No existe una tarjeta de este banco: '{banco}'")
        return tarjeta
    
    def compra(self, banco, monto):
        tarjeta = self.obtenerTarjeta(banco) #Se utiliza la funcion para "buscar" una tarjeta con el nombre ingresado
        if not tarjeta:
            return self

        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        elif tarjeta.saldoPagar + monto > tarjeta.limiteCredito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            tarjeta.saldoPagar += monto
        return self
    
    def pago(self, banco, monto):
        tarjeta = self.obtenerTarjeta(banco)
        if not tarjeta:
            return self

        if monto <= 0:
            print("El monto a pagar debe ser mayor que cero.")
        else:
            tarjeta.saldoPagar -= monto
            if tarjeta.saldoPagar < 0:
                tarjeta.saldoPagar = 0
                return self
        return self
    
    def mostrar_info_tarjeta(self, banco = None): #Si al llamar la funcion mostrar_info_tarjeta no se indica el nombre de una tarjeta, se hara print a todas las tarjetas que el usuario tenga en su poder
        print("==========================================================")
        if banco is None:
            print(f"Información de todas las tarjetas de {self.nombre}:")
            for i in self.tarjetas.values():
                print(f"{i.banco}: Límite ${i.limiteCredito}, Saldo a pagar ${i.saldoPagar}")
        else:
            tarjeta = self.obtener_tarjeta(banco) #En caso contrario si se expecifica una tarjeta solo devolvera los datos de dicha tarjeta
            if tarjeta:
                print(f"Tarjeta {banco} de {self.nombre}")
                print(f"Crédito total: ${tarjeta.limiteCredito}")
                print(f"Saldo a pagar actual: ${tarjeta.saldoPagar}")
        print("==========================================================")
        print("")
        print("")
        return self

    def cobrar_interes(self, banco):
        tarjeta = self.obtenerTarjeta(banco)
        if not tarjeta:
            return self
    
        tarjeta.saldoPagar += (tarjeta.saldoPagar * tarjeta.intereses)
        return self
    
#==========================================================
#   Creacion de usuarios
#==========================================================
usuario1 = Usuario("john", "Marston", "john@hotmail.com")
usuario2 = Usuario("Mariana", "Centolla", "mariaC@gmail.com")

#==========================================================
#   Acciones usuario 1
#==========================================================
usuario1.agregarTarjeta("Banco Chile")
usuario1.agregarTarjeta("BancoEstado")
usuario1.compra("Banco Chile", 200).compra("BancoEstado", 800).pago("BancoEstado", 600).cobrar_interes("BancoEstado").mostrar_info_tarjeta()

#==========================================================
#   Acciones usuario 2
#==========================================================
usuario2.agregarTarjeta("BCI")
usuario2.compra("BCI", 300).compra("BCI", 100).compra("BCI", 1000).pago("BCI", 600).pago("BCI", 8000).cobrar_interes("BCI").mostrar_info_tarjeta()

