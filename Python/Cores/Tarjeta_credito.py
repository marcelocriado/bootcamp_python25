#==========================================================
#   Creacion de clase tarjeta
#==========================================================
class tarjetaCredito:
    def __init__(self, monto, limiteCredito, intereses):
        if monto > 0:
            self.saldoPagar = monto
        else:
            self.saldoPagar = 0
        self.limiteCredito = limiteCredito
        self.intereses = (intereses/100)
    
    def compra(self, monto):
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        elif self.saldoPagar + monto > self.limiteCredito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldoPagar += monto
        return self
    
    def pago(self, monto):
        if monto <= 0:
            print("El monto a pagar debe ser mayor que cero.")
        else:
            self.saldoPagar -= monto
        return self
    
    def mostrar_info_tarjeta(self):
        print("==========================================================")
        print(f"Usted cuenta con un credito de: ${self.limiteCredito}")
        print(f"Su saldo a pagar actual es: ${self.saldoPagar}")
        print("==========================================================")
        print("")
        print("")
        return self

    def cobrar_interes(self):
        self.saldoPagar += (self.saldoPagar * self.intereses)
        return self
    
#==========================================================
#   Creacion de tarjetas
#==========================================================
tarjeta1 = tarjetaCredito(4000, 500000, 2)
tarjeta2 = tarjetaCredito(60000, 600000, 10)
tarjeta3 = tarjetaCredito(200, 8000, 1)

#==========================================================
#   Acciones tarjeta 1
#==========================================================
tarjeta1.compra(2000).compra(80000).pago(6000).cobrar_interes().mostrar_info_tarjeta()

#==========================================================
#   Acciones tarjeta 2
#==========================================================
tarjeta2.compra(3000).compra(100).compra(1000).pago(600).pago(8000).cobrar_interes().mostrar_info_tarjeta()

#==========================================================
#   Acciones tarjeta 3
#==========================================================
tarjeta3.compra(30000).compra(1000).compra(10000).compra(40000).compra(1000).mostrar_info_tarjeta()