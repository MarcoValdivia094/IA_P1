# Los operadores de comparación
# Se usan para comparar valores y devuelven True o False

# Operador de comparación igual que (==)
print(5 == 5)     # True
print("a" == "b") # False

# Tabla comparativa del operador igual que
"""
  x == y   → True si x es igual a y
  5 == 5   → True
  "a" == "a" → True
  3 == 4   → False
"""

# Operador de comparación diferente que (!=)
print(5 != 3)     # True
print("a" != "a") # False

# Tabla comparativa del operador diferente que
"""
  x != y   → True si x es distinto de y
  5 != 3   → True
  "a" != "b" → True
  4 != 4   → False
"""

# Operador de comparación mayor que (>)
print(10 > 5)     # True
print(3 > 7)      # False

# Tabla comparativa del operador mayor que
"""
  x > y    → True si x es mayor que y
  10 > 5   → True
  3 > 7    → False
"""

# Operador de comparación menor que (<)
print(2 < 8)      # True
print(9 < 1)      # False

# Tabla comparativa del operador menor que
"""
  x < y    → True si x es menor que y
  2 < 8    → True
  9 < 1    → False
"""

# Operador de comparación mayor o igual que (>=)
print(5 >= 5)     # True
print(6 >= 10)    # False

# Tabla comparativa del operador mayor o igual que
"""
  x >= y   → True si x es mayor o igual que y
  5 >= 5   → True
  6 >= 10  → False
"""

# Operador de comparación menor o igual que (<=)
print(4 <= 4)     # True
print(7 <= 3)     # False

# Tabla comparativa del operador menor o igual que
"""
  x <= y   → True si x es menor o igual que y
  4 <= 4   → True
  7 <= 3   → False
"""

# Los operadores lógicos
  # Se usan para combinar condiciones

# El operador lógico and
print(True and True)   # True
print(True and False)  # False

# Tabla comparativa del operador lógico and
"""
  x and y → True si ambos son True
  True and True   → True
  True and False  → False
  False and True  → False
  False and False → False
"""

# Ejemplo práctico con el operador and
edad = 25
tiene_licencia = True
print(edad >= 18 and tiene_licencia)  # True si es mayor de edad y tiene licencia

# El operador lógico or
print(True or False)   # True
print(False or False)  # False

# Tabla comparativa del operador lógico or
"""
  x or y → True si al menos uno es True
  True or False  → True
  False or True  → True
  False or False → False
"""

# Ejemplo práctico con el operador or
tiene_pasaporte = False
tiene_ine = True
print(tiene_pasaporte or tiene_ine)  # True si tiene al menos uno

# El operador lógico not
print(not True)   # False
print(not False)  # True

# Ejemplo práctico con el operador not
es_menor = False
print(not es_menor)  # True si no es menor

# Expresiones más complejas
  # Se pueden combinar operadores de comparación y lógicos

# ¿Puede votar?
edad = 20
ciudadania = "mexicana"
print(edad >= 18 and ciudadania == "mexicana")  # True

# ¿Acceso denegado?
usuario_activo = False
es_admin = False
print(not usuario_activo and not es_admin)  # True

# ¿Aprobado?
calificacion = 85
asistencia = 90
print(calificacion >= 70 and asistencia >= 80)  # True

# ¿Requiere verificación?
correo_verificado = False
telefono_verificado = False
print(not correo_verificado or not telefono_verificado)  # True
