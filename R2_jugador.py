from R1_personaje import Personaje

class Jugador(Personaje):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.victorias = 0 #Aspecto único de la clase Jugadpor

  #Aquí las victorias aumentan en 1, si es que el jugador gana un combate.
    def registrar_victoria(self):
        self.victorias += 1
        print(f"{self.nombre} lleva {self.victorias} victoria(s).")
