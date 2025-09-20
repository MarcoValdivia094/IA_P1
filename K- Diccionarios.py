# Sintaxis de un diccionario
# Los diccionarios usan llaves {} y pares clave:valor
mi_diccionario = {"nombre": "Marco", "edad": 23, "profesion": "estudiante"}

# Crear un diccionario
# Ya lo hicimos arriba. También puedes usar dict()
otro_diccionario = dict(pais="México", idioma="Español")

# Claves y valores
# Las claves son únicas y apuntan a un valor
# Ejemplo: "nombre" es la clave, "Marco" es el valor

# Claves del diccionario
print(mi_diccionario.keys())  # dict_keys(['nombre', 'edad', 'profesion'])

# Valores del diccionario
print(mi_diccionario.values())  # dict_values(['Marco', 23, 'estudiante'])

# Llamar a valores de diccionario
print(mi_diccionario["nombre"])  # Marco

# Error por clave inexistente
# print(mi_diccionario["altura"])  # KeyError: 'altura'

# Para evitar el error, puedes usar get()
print(mi_diccionario.get("altura"))  # None

# Asignar nuevos valores a un diccionario
mi_diccionario["edad"] = 100  # Cambia el valor de la clave 'edad'
print(mi_diccionario)

# Crear claves y valores nuevos
mi_diccionario["altura"] = 1.75  # Agrega nueva clave
print(mi_diccionario)

# Eliminar claves y valores en diccionarios
del mi_diccionario["profesion"]  # Elimina la clave 'profesion'
print(mi_diccionario)

# Eliminar un diccionario entero
del mi_diccionario  # Elimina el diccionario completo
# print(mi_diccionario)  # NameError: name 'mi_diccionario' is not defined
