# Clase base: Personaje
class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    # Un simple saludo al iniciar la aventura
    def saludar(self):
        print(f"Soy {self.nombre}, nivel {self.nivel}.")

    # Simulador de ataque: acepta múltiples enemigos con *args
    def atacar(self, *enemigos):
        for enemigo in enemigos:
            print(f"{self.nombre} ataca a {enemigo.nombre} (nivel {enemigo.nivel})...")
            if self.nivel >= enemigo.nivel:
                print(f"{self.nombre} ha derrotado a {enemigo.nombre}!")
                self.subir_nivel()
                self.registrar_victoria()
            else:
                print(f"{self.nombre} fue derrotado por {enemigo.nombre}...")

    # Subida de nivel tras cada victoria
    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nombre} ha subido al nivel {self.nivel}!")

# Clase hija: Jugador (hereda de Personaje)
class Jugador(Personaje):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.victorias = 0  # Atributo exclusivo del jugador

    # Contamos las victorias del protagonista
    def registrar_victoria(self):
        self.victorias += 1
        print(f"{self.nombre} lleva {self.victorias} victoria(s).")

# Clase hija: Enemigo (hereda de Personaje)
class Enemigo(Personaje):
    def __init__(self, nombre, nivel, tipo):
        super().__init__(nombre, nivel)
        self.tipo = tipo  # Tipo de enemigo (bestia, jefe, etc.)

    def rugir(self):
        print(f"{self.nombre} ({self.tipo}) ruge ferozmente!")

# Crear al jugador
protagonista = Jugador("Marco, el caballero", 1)

# Crear enemigos con clase Enemigo
goblin = Enemigo("Goblin", 1, "bestia")
slime = Enemigo("Slime", 2, "gelatinoso")
esqueleto = Enemigo("Esqueleto", 3, "no-muerto")
dragon = Enemigo("Dragón", 5, "jefe final")

# Simulación de combate
protagonista.saludar()
protagonista.atacar(goblin, slime, esqueleto)  # Ataca a todos los enemigos "a la vez" usando *args

"""
La línea anterior equivale a:
  protagonista.atacar(goblin)
  protagonista.atacar(slime)
  protagonista.atacar(esqueleto)
Pero usando *args, lo hacemos en una sola llamada.
"""

# Enfrentamiento final
print("\n¡Enfrentamiento final!")
dragon.rugir()
protagonista.atacar(dragon)




