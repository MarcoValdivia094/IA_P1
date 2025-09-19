from R1_personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, nombre, nivel, tipo):
        super().__init__(nombre, nivel)
        self.tipo = tipo  #Aspecto único de la clase enemigo.

  #Acción simplemente para saber la caracteristica especial de cada enemigo, es decir, su "Tipo".
    def rugir(self):
        print(f"{self.nombre} ({self.tipo}) ruge ferozmente!")
