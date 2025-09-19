# Condicional simple
edad = 20
if edad >= 18:
    print("Mayor de edad")

# Condicional if-else
if edad >= 18:
    print("Adulto")
else:
    print("Menor")

# Condicional if-elif-else
if edad >= 65:
    print("Adulto mayor")
elif edad >= 18:
    print("Adulto")
else:
    print("Menor")

# Condicional con is y type()
dato = "texto"
if type(dato) is str:
    print("Es una cadena")

# Combinación con is not
if type(dato) is not int:
    print("No es un entero")

# Operador ternario
resultado = "Aprobado" if edad >= 18 else "Reprobado"
print(resultado)

# Operadores lógicos
activo = True
admin = False

print(activo and admin)  # False
print(activo or admin)   # True
print(not activo)        # False
