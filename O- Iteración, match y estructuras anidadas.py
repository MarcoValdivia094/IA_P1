# Condicional match
# match permite comparar un valor contra múltiples patrones
comando = "iniciar"

match comando:
    case "iniciar":
        print("Sistema encendido")
    case "detener":
        print("Sistema apagado")
    case _:
        print("Comando no reconocido")

# Patrones múltiples en bloques case
# Se pueden agrupar varias opciones con el operador |
match comando:
    case "iniciar" | "arrancar":
        print("Encendido por comando alternativo")

# match con estructuras de datos
# También se puede usar para extraer valores de listas, tuplas o diccionarios
datos = [1, 2, 3]

match datos:
    case [1, x, 3]:
        print("El valor central es:", x)
    case _:
        print("No coincide con el patrón esperado")

# Comparación: match vs if
# match es más limpio cuando hay muchas condiciones con patrones
# if es más flexible para expresiones lógicas complejas

# Operador in con cadenas
# Verifica si un carácter o subcadena está dentro de otra cadena
texto = "python"
print("y" in texto)     # True
print("z" in texto)     # False

# Operador in con listas
numeros = [10, 20, 30]
print(20 in numeros)    # True
print(99 in numeros)    # False

# Operador in con tuplas y conjuntos
colores = ("rojo", "verde", "azul")
print("verde" in colores)  # True

conjunto = {"a", "b", "c"}
print("b" in conjunto)     # True

# Iterar lista con for
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print("Fruta:", fruta)

# Iterar diccionario
persona = {"nombre": "Marco", "edad": 23}
for clave, valor in persona.items():
    print(clave, "→", valor)

# Acceder a una posición concreta de una cadena
mensaje = "Hola mundo"
print("Primera letra:", mensaje[0])   # H
print("Última letra:", mensaje[-1])  # o

# Estructuras de control anidadas
# Puedes colocar condicionales dentro de bucles, o bucles dentro de condicionales

# If anidado dentro de for
usuarios = ["Ana", "Luis", "Shadow"]
for usuario in usuarios:
    if usuario == "Shadow":
        print("¡Bienvenido, Shadow!")
    else:
        print("Usuario:", usuario)

# Bucle for dentro de un if
activo = True
if activo:
    for i in range(3):
        print("Iteración activa:", i)

# Bucle while con condicional interno
contador = 0
while contador < 5:
    if contador % 2 == 0:
        print("Par:", contador)
    contador += 1  # Mover fuera del if para evitar bucle infinito

# Bucle con continue
# Salta una iteración cuando se cumple una condición
for letra in "python":
    if letra == "h":
        continue
    print("Letra:", letra)  # Ahora sí se imprime correctamente

# Bucle con break
# Rompe el ciclo cuando se cumple una condición
for letra in "python":
    if letra == "o":
        break
    print("Letra antes de romper:", letra)  # Se imprime hasta antes de 'o'

# Bucle while True (infinito controlado)
intentos = 0
while True:
    print("Intento:", intentos)
    intentos += 1
    if intentos == 3:
        print("Fin del ciclo")
        break

# Bucle con else
# El bloque else se ejecuta si el bucle termina sin usar break
for numero in [1, 2, 3]:
    print("Número:", numero)
else:
    print("Bucle completado sin interrupciones")

# Iterar múltiples secuencias
# Puedes combinar listas, tuplas o diccionarios en una sola iteración
nombres = ["Ana", "Luis", "Marco"]
edades = [25, 30, 23]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

