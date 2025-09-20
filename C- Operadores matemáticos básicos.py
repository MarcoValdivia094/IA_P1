#Suma directa
print(20 + 50)

#Suma guardada en una variable
# Calcula y guarda el resultado
operacion = 20 + 50  
# Imprime el resultado
print(operacion)

#Resta guardada en una variable (también se puede hacer directa)
# Calcula y guarda el resultado
operacion = 10 - 4
# Imprime el resultado
print(operacion)

#Multiplicación
# Calcula y guarda el resultado
operacion = 10 * 4
# Imprime el resultado
print(operacion)

#División 
# Calcula y guarda el resultado
operacion = 10 / 3
# Imprime el resultado
print(operacion)

#Ejemplo de una operación mixta (que tiene más de una operación diferente)
# Calcula y guarda el resultado
operacion = 100 * 98 + 65 * 2 - 10 / 5
# Imprime el resultado
print(operacion)

#Operación con 2 variables, aunque pueden sea con más de 2.
# Declaración de dos variables numéricas
numero1 = 100
numero2 = 500
# Calcula el resultado de la suma de los dos valores
resultado = numero1 + numero2
# Imprime el resultado
print(resultado)

#Módulo %, este realiza una división entre dos números, y en lugar de devolvernos el resultado como hace el operador de división (/), nos devuelve el resto.
# Declaramos dos variables numéricas
numero1 = 10 # Dividendo
numero2 = 3 # Divisor
# Calculamos el cociente y el resto de la división
cociente = numero1 / numero2 # División normal
resto = numero1 % numero2 # División módulo
# Imprimimos el cociente y el resto
print("Cociente:", cociente)
print("Resto:", resto)

#División entera (//), este sirve para realizar una división, devolviendo siempre un resultado de tipo int.
# Declaramos dos variables numéricas
numero1 = 10 # Dividendo
numero2 = 3 # Divisor
# Calculamos la división
division = numero1 / numero2
division_entera = numero1 / numero2
# Imprimimos los resultados
print(division)
print(division_entera)

#Potencia (**)
# Cálculo de 2 elevado a 10
operacion = 2 ** 10
print(operacion)

#Cálculos con paréntesis, con os parémntesis podrás establecer prioridades diferentes en las operaciones de cálculo, al igual que haces con las matemáticas corrientes.
operacion = (10 + 6) * 2 #En este caso, la prioridad es la suma (10 + 6). Entonces, la operación que se está realizando es 10 + 6 = 16 * 2 = 32
print(operacion)

"""
El orden de preferencia de las operaciones matemáticas que se usan (al menos hasta este archivo), es el siguiente (ordenado de mayor a menor):
Paréntesis
Exponentes
Multiplicación y división
Suma y resta
"""
#Guiones bajos para números grandes
#En Python podemos representar números grandes de una forma más legible, con un guion bajo(_).
numero_largo = 56_404_357_843_987 #Esto es lo mismo que: 56404357843987 solo que de forma más "legible"
print(numero_largo)

#También podemos utilizar estos guiones con números que tienen decimales:
numero_largo_con_decimal = 56_404_357_843_987.78 #Lo mismo que 56404357843987.78, e incluso podemos agregar más (_) después del punto como 56_404_357_843_987.7_234_543
print(numero_largo_con_decimal)

