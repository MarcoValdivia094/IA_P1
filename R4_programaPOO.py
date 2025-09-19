#Este es el main del "Q- Ejercicio práctico RPG de herencia y args en POO (todo en uno).py", solo que ahora si modulado.

#Importamos las clases Jugador y Enemigo de sus respectivos .py. Y no llamamos a la clase padre: Personaje, ya que sus hijas tienen las caracteristicas totakles de esta.
from R2_jugador import Jugador
from R3_enemigo import Enemigo

# Crear al jugador
protagonista = Jugador("Marco, el caballero", 1)

# Crear enemigos
goblin = Enemigo("Goblin", 1, "bestia")
slime = Enemigo("Slime", 2, "gelatinoso")
esqueleto = Enemigo("Esqueleto", 3, "no-muerto")
dragon = Enemigo("Dragón", 5, "jefe final")

# Simulación de combate
protagonista.saludar()
protagonista.atacar(goblin, slime, esqueleto)

#Siempre va a aperder el protagonista contra el drágon, es simplemente un ejemplo de todo lo que hace el código.
print("\n¡Enfrentamiento final!")
dragon.rugir()
protagonista.atacar(dragon)
