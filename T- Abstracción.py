"""Este programa simula un sistema de combate entre personajes de distintas clases.
Utiliza herencia para compartir atributos comunes, polimorfismo para que cada clase
ataque de forma distinta, y abstracción para obligar a que todas las clases hijas
implementen el método atacar().
"""

from abc import ABC, abstractmethod  # Importamos herramientas para abstracción

# Clase base abstracta: Personaje
class Personaje(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    # Método abstracto: todas las clases hijas deben implementar su propia versión
    @abstractmethod
    def atacar(self):
        pass  # No se define aquí, solo se declara como obligatorio

# Clase hija: Mago
class Mago(Personaje):
    def atacar(self):
        # El mago lanza un hechizo como ataque
        print(f"{self.nombre} lanza una bola de fuego 🔥.")

# Clase hija: Guerrero
class Guerrero(Personaje):
    def atacar(self):
        # El guerrero ataca con su espada
        print(f"{self.nombre} ataca con su espada ⚔️.")

# Clase hija: Arquero
class Arquero(Personaje):
    def atacar(self):
        # El arquero dispara una flecha
        print(f"{self.nombre} dispara una flecha 🏹.")

# Simulación de combate
personajes = [
    Mago("Merlín"),        # Instancia de Mago
    Guerrero("Thorgar"),   # Instancia de Guerrero
    Arquero("Lina")        # Instancia de Arquero
]

# Iniciamos el combate
print("=== COMBATE INICIADO ===\n")
for personaje in personajes:
    personaje.atacar()  # Cada clase ejecuta su propia versión del método atacar(), sin tener definido nada, es decir, todas las clases hijas deben diseñar su propia versión sin exepción.
