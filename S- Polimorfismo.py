""" ===============================
    PROYECTO: POLIMORFISMO EN POO
==============================="""

"""Este programa simula un grupo de personajes con diferentes clases (Mago, Guerrero, Arquero),
todos heredan de una clase base llamada Personaje. Cada uno tiene su propia forma de atacar,
demostrando el concepto de polimorfismo: una misma acción (atacar) se comporta diferente
según el tipo de objeto que la ejecuta."""

#Clase base: Personaje
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    # Método genérico de ataque. Este será sobrescrito por las clases hijas.
    def atacar(self):
        print(f"{self.nombre} realiza un ataque básico.")  # Comportamiento por defecto


#Clase hija: Mago

class Mago(Personaje):
    # Sobrescribimos el método atacar para que el mago lance un hechizo
    def atacar(self):
        print(f"{self.nombre} lanza una bola de fuego 🔥.")  # Ataque mágico

# Clase hija: Guerrero
class Guerrero(Personaje):
    # Sobrescribimos el método atacar para que el guerrero use su espada
    def atacar(self):
        print(f"{self.nombre} ataca con su espada ⚔️.")  # Ataque físico

# Clase hija: Arquero
class Arquero(Personaje):
    # Sobrescribimos el método atacar para que el arquero dispare una flecha
    def atacar(self):
        print(f"{self.nombre} dispara una flecha 🏹.")  # Ataque a distancia

# -------------------------------
# Simulación de combate
# -------------------------------

"""
Se crea una lista de personajes de diferentes clases
Aunque todos son tratados como objetos de tipo Personaje,
cada uno ejecuta su propia versión del método atacar()
"""

personajes = [
    Mago("Merlín"),        # Instancia de Mago
    Guerrero("Thorgar"),   # Instancia de Guerrero
    Arquero("Lina")        # Instancia de Arquero
]

# Recorremos la lista y llamamos al método atacar()
  # Aquí ocurre el polimorfismo: misma llamada, diferentes comportamientos
print("=== COMBATE INICIADO ===\n")
for personaje in personajes:
    personaje.atacar()  # Cada clase ejecuta su propia versión del método
