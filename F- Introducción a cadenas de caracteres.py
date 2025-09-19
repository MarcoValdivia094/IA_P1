# ¿Qué es la concatenación?
  # Es unir cadenas de texto. Como pegar palabras con pegamento digital.
  nombre = "Marco"
  saludo = "Hola " + nombre  # Concatenación con el operador +
  print(saludo) #Imprime "Hola Marco"

# Tipos de comillas en cadenas de caracteres
  cadena1 = 'Texto con comillas simples'
  cadena2 = "Texto con comillas dobles"
  cadena3 = '''Texto con triple comilla simple (ideal para textos largos)'''
  cadena4 = """Texto con triple comilla doble (también para textos largos)"""

# Alternar comillas
# Útil cuando quieres incluir comillas dentro de la cadena
print('Ella dijo: "Hola"')  # Comillas dobles dentro de simples
print("Él respondió: 'Adiós'")  # Comillas simples dentro de dobles

# Escape de caracteres
  # Para incluir comillas o caracteres especiales sin romper la cadena
  print("Ella dijo: \"Hola\" y se fue")  # \" escapa la comilla
  print("Primera línea\nSegunda línea")  # \n es salto de línea
  print("C:\\Users\\Marco")  # \\ para mostrar una barra invertida

# Formateo de cadenas
  # Hay varias formas de insertar valores en cadenas
  
  # 1. Concatenación (ya vista)
  # 2. Usando el método format()
  edad = 99
  print("Tu nombre es {} y tienes {} años".format(nombre, edad))
  
  # 3. Usando f-strings (desde Python 3.6)
  print(f"Tu nombre es {nombre} y tienes {edad} años")  # Más limpio y directo

"""
  Diferencia entre concatenación y formateo
    Concatenación: une cadenas, pero puede ser incómodo con tipos distintos
    Formateo: permite incrustar variables y expresiones fácilmente
"""

# Incrustando valores en las cadenas
  # Ya lo hicimos con f-strings. También se pueden hacer cálculos dentro
  print(f"En 5 años tendrás {edad + 5} años")  # Resolviendo expresiones dentro de la cadena

# Métodos de cadenas de caracteres
  # Son funciones que se aplican a cadenas para modificarlas o analizarlas
  
  # Cómo llamar a un método en Python
    #Sintaxis: variable.metodo()
    texto = "hola mundo"
    print(texto.capitalize())  # Capitaliza: "Hola mundo"
  
  # Entrada de datos con conversión de letra mayúscula
    entrada = input("Escribe algo: ")
    print("Versión capitalizada:", entrada.capitalize())  # Primera letra en mayúscula
  
  # El método upper()
    print("Todo en mayúsculas:", entrada.upper())  # Convierte todo a mayúsculas
  
  # El método lower()
    print("Todo en minúsculas:", entrada.lower())  # Convierte todo a minúsculas
