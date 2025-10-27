import random

class jugador:
    def __init__(self, clase, inventario):
        self.vida = 100
        self.clase = clase
        self.inventario = inventario
    
    def objetos(self):
        inventario = []
        for i in range(3):
            objeto = random.randint(1,10)
            if objeto == 1 or objeto == 6:
                objeto = "Cuerda"
            elif objeto == 2 or objeto == 8:
                objeto = "Ganzua"
            elif objeto == 3 or objeto == 9:
                objeto = "Aceite"
            elif objeto == 4:
                objeto = "Mapa"
            else:
                objeto = "Pocion de salud"
            inventario.append(objeto)
        return(inventario)


