"""
Sintaxis de una tupla
  Las tuplas usan paréntesis y pueden contener múltiples elementos
"""
mi_tupla = ("manzana", "banana", "cereza")

# Acceder a los elementos de una tupla
  print(mi_tupla[0])  # manzana
  print(mi_tupla[2])  # cereza

# Métodos para tuplas
  # Las tuplas tienen pocos métodos porque son inmutables (no se pueden modificar)

  # El método index() con tuplas
    # Devuelve el índice del primer elemento que coincida
    pos = mi_tupla.index("banana")
    print("Índice de 'banana':", pos) #1

  # El método count()
    # Cuenta cuántas veces aparece un valor
    cantidad = mi_tupla.count("manzana")
    print("Cantidad de 'manzana':", cantidad)

# ¿Cuándo utilizar tuplas en lugar de listas?
"""
Usa tuplas cuando:
- Los datos no deben cambiar (por ejemplo, coordenadas, días de la semana)
- Quieres proteger la integridad de la información
- Buscas eficiencia: las tuplas ocupan menos memoria que las listas
"""

# Desempaquetado de tuplas y listas
  # Puedes extraer los valores directamente en variables
  fruta1, fruta2, fruta3 = mi_tupla
  print(fruta1)  # manzana
  print(fruta2)  # banana
  print(fruta3)  # cereza

  # También funciona con listas
  mi_lista = [10, 20, 30]
  a, b, c = mi_lista
  print(a, b, c)  # 10 20 30

  #Para recoger el exceso de valores se usa el operador *
  fruta1, *resto = mi_tupla
  print(fruta1)  # manzana
  print(resto) #[banana, cereza]
