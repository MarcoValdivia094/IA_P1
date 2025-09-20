# Declaración de funciones
# Se usa la palabra clave 'def' seguida del nombre y paréntesis
def saludar():
  print("Hola, Shadow")

# Ejemplo práctico de función
saludar()  # Llama a la función y ejecuta su contenido

# Parámetros de las funciones
# Son variables que se definen dentro de los paréntesis al declarar la función

# Ejemplo de uso de un parámetro en una función
def saludar_persona(nombre):
  print("Hola,", nombre)

saludar_persona("Marco")  # Pasa un argumento a la función

# Funciones con varios parámetros
def presentar(nombre, edad):
    print("Nombre:", nombre)
    print("Edad:", edad)

presentar("Marco", 23)

# Parámetros obligatorios
  # Si no se pasan, la función lanza un error
      # presentar("Marco")  # TypeError: falta el segundo argumento

# El orden de los argumentos
  # Los argumentos se asignan en el orden en que aparecen
presentar("Ana", 30)  # nombre = "Ana", edad = 30

# Diferencia entre parámetro y argumento
"""
  Parámetro: variable definida en la función (ej. nombre, edad)
  Argumento: valor que se pasa al llamar la función (ej. "Ana", 30)
"""

# Argumentos de clave (keyword arguments)
  # Se pueden pasar usando nombre=valor
presentar(edad=25, nombre="Luis")  # El orden ya no importa

# Devolver valores con las funciones
  # Se usa la palabra clave 'return'

# El uso de return en las funciones
def sumar(a, b):
    return a + b

resultado = sumar(5, 3) #Aquí a vale 5 y b vale 3, además resultado recibe el valor de a+b, es decir, 5+3.
print("Resultado:", resultado) #8

# print() y return en la misma función
def operacion(a, b):
    print("Sumando", a, "y", b)
    return a + b

total = operacion(10, 20)
print("Total:", total)

# ¿Qué son las funciones predefinidas?
"""
  Son funciones que ya vienen con Python, listas para usarse.
  Ejemplos: print(), len(), type(), input(), max(), min(), sum(), etc.
  No necesitas definirlas, solo llamarlas.
"""

# Ejemplo de funciones predefinidas
texto = "Python"
print(len(texto))       # Devuelve la longitud
print(type(texto))      # Devuelve el tipo de dato
print(texto.upper())    # Convierte a mayúsculas
