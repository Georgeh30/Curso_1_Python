
class Animal:
    def __init__(self,nombre="", ataque=0):
        self.nombre = nombre
        self.vida = 100
        self.ataque = ataque

    def gano(self):
        return "El Animal " + self.nombre + " con ataque: " + str(self.ataque) \
               + " y vida actual de: " + str(self.vida) + " ha ganado el encuentro"
