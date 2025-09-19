"""
¿Por qué los conjuntos (sets) solo aceptan objetos inmutables?

  Porque los conjuntos usan funciones hash para organizar sus elementos internamente.
  Si un objeto cambia, su hash también podría cambiar, rompiendo la estructura del conjunto.
  Por eso, solo se permiten objetos inmutables como strings, números, tuplas sin listas, etc.
"""

# Sintaxis de un conjunto
  mi_conjunto = {1, 2, 3, 4}

# Ejemplo de uso de un conjunto
  print(mi_conjunto)  # {2, 1, 4, 3}  En los sets o conjuntos sus elementos no tienen un orden especifico, por lo que al llamarlos pueden salir en posiciones diferentes.

# Métodos para sets de Python
  # Los sets tienen métodos como add(), remove(), discard(), pop(), clear(), union(), intersection(), etc.

# Añadir valores a un conjunto con el método add()
  mi_conjunto.add(5)
  print(mi_conjunto)  # {1, 2, 3, 4, 5}

# Eliminar valores de un conjunto con el método remove()
  mi_conjunto.remove(2)
  print(mi_conjunto)  # {1, 3, 4, 5}

    # Error por elemento inexistente
      # mi_conjunto.remove(99)  # ValueError: el elemento no existe

# Eliminar elementos con el método discard()
  mi_conjunto.discard(99)  # No lanza error si el elemento no existe
  print(mi_conjunto)  # {1, 3, 4, 5}

# Elementos duplicados en los conjuntos
  # Los sets eliminan duplicados automáticamente
  duplicados = {1, 2, 2, 3, 3, 3}
  print(duplicados)  # {1, 2, 3}

    # Error por elemento mutable
      # conjunto = {[1, 2]}  # TypeError: unhashable type: 'list'

# Ver el total de elementos que tiene un conjunto
  print("Total de elementos:", len(mi_conjunto))  # 4

# Ver los valores mayores y menores de un conjunto
  print("Máximo:", max(mi_conjunto))  # 5
  print("Mínimo:", min(mi_conjunto))  # 1

# Inmutabilidad con frozensets
  # Un frozenset es un conjunto inmutable: no se puede modificar después de crearlo

# Sintaxis de un frozenset
  mi_frozen = frozenset([10, 20, 30])
  print(mi_frozen)  # frozenset({10, 20, 30})

    # mi_frozen.add(40)  # AttributeError: 'frozenset' object has no attribute 'add'
