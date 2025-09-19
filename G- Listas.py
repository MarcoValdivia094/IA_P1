# ¿Array y lista son lo mismo?
"""
En Python, usamos listas como si fueran arrays. Pero técnicamente, los arrays vienen del módulo 'array'.
Las listas son más flexibles y se usan mucho más.

¿Para qué queremos listas en Python?
Para almacenar múltiples valores en una sola variable. Como una caja con compartimentos.
"""

#Sintaxis de una lista Python
  mi_lista = [10, 20, 30, 40]  # Corchetes, elementos separados por comas

# Creando una lista de Python
  frutas = ["manzana", "banana", "cereza"]

# ¿Cómo se muestra una lista en la consola?
  print(frutas)  # Muestra todos los elementos: ['manzana', 'banana', 'cereza']

# Índice de posiciones en las listas
  # Los índices empiezan en 0
  print(frutas[0])  # manzana
  print(frutas[2])  # cereza

# Sintaxis de asignación en listas
  frutas[1] = "kiwi"  # Cambia 'banana' por 'kiwi'
  print(frutas)  # ['manzana', 'kiwi', 'cereza']

    # Error por número de índice inexistente
      # print(frutas[5])  # IndexError: list index out of range   Es decir, esa posición no existe en la lista.

# Métodos para añadir elementos en listas

# El método append() para listas de Python
  # Añade al final
  frutas.append("naranja")
  print(frutas)  # ['manzana', 'kiwi', 'cereza', 'naranja']

""" 
Sintaxis del método append()
  # lista.append(valor_a_agregar)
"""

# El método insert() para listas de Python
  # Inserta en una posición específica
  frutas.insert(1, "sandía")  # Inserta en índice 1
  print(frutas)  # ['manzana', 'sandía', 'kiwi', 'cereza', 'naranja']


    #Índice inexistente en insert()
      #Si el índice es mayor que la longitud, se añade al final


# El método extend() para listas Python
  # Añade múltiples elementos
  frutas.extend(["pera", "uva"])
  print(frutas)  # ['manzana', 'sandía', 'kiwi', 'cereza', 'naranja', 'pera', 'uva']

"""
  Sintaxis del método extend()
    lista.extend([valores])
"""

# Métodos para eliminar elementos en listas Python

# El método pop() para listas
  # Elimina y devuelve el último elemento
  ultimo = frutas.pop()
  print("Eliminado:", ultimo) #Eliminado: uva
  print(frutas) # ['manzana', 'sandía', 'kiwi', 'cereza', 'naranja', 'pera']

# Eliminar un elemento concreto con pop()
  eliminado = frutas.pop(2)  # Elimina el índice 2
  print("Eliminado:", eliminado) #Eliminado: kiwi
  print(frutas) # ['manzana', 'sandía', 'cereza', 'naranja', 'pera']

    # Error con pop()
      # frutas.pop(100)  # IndexError si el índice no existe

# El método remove()
  # Elimina el primer elemento que coincida con el valor
  frutas.remove("sandía")
  print(frutas) # ['manzana', 'cereza', 'naranja', 'pera']

"""
  Sintaxis del método remove()
    lista.remove(valor)
"""

# El método remove() no elimina duplicados
  frutas.extend(["pera", "pera"])
  frutas.remove("pera")  # Solo elimina la primera
  print(frutas) # ['manzana', 'cereza', 'naranja', 'pera', 'pera']

    # Error con remove()
      # frutas.remove("mango")  # ValueError si no existe

# Métodos para buscar elementos en listas de Python

# El método index()
  # Devuelve el índice del primer elemento que coincida
  pos = frutas.index("manzana")
  print("Índice de 'manzana':", pos) #Índice de 'manzana': 0

"""
  Sintaxis del método index()
    lista.index(valor)
"""

    # Error con index()
      # frutas.index("mango")  # ValueError si no existe

# El método count()
  # Cuenta cuántas veces aparece un valor
  cantidad = frutas.count("pera")
  print("Cantidad de 'pera':", cantidad) #Cantidad de 'pera': 2

"""
  Sintaxis del método count()
    lista.count(valor)
"""


