import armas

class cazador:
    def __init__(self):
        self.vida = 30 #restar con la vida del jugador
        self.arma = armas.arco()

class mago:
    def __init__(self, arma):
        self.vida = 50 #restar con la vida del jugador
        self.arma = armas.baston()

class guerrero:
    def __init__(self, arma):
        self.vida = 50 #sumar con la vida del jugador
        self.armadura = 10 #sumar con la vida del jugador
        self.arma = armas.mandoble()

class ladron:
    def __init__(self, arma):
        self.vida = 30 #restar con la vida del jugador
        self.armadura = 5 #sumar con la vida del jugador
        self.arma = armas.daga()

