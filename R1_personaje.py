#Este código es lo mismo que "Q- Ejercicio práctico RPG de herencia y args en POO (todo en uno).py" solo que dividido en 4 .py.
  #Está es la clase padre "Personaje"
class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre #Nombre del personaje
        self.nivel = nivel #Nivel usado en combate

    def saludar(self):
        print(f"Soy {self.nombre}, nivel {self.nivel}.") #Un mero saludo al inicio de la aventura

  # Simulador de ataque: acepta múltiples enemigos con *args
    def atacar(self, *enemigos):
        for enemigo in enemigos:
            enemigo.rugir()
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
