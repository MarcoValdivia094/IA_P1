# Bucle for con range()
  # Recorre una secuencia de números desde 0 hasta 2 (sin incluir el 3)
  for i in range(3):
      print("Iteración:", i)  # Imprime 0, 1, 2

# Modificar incremento
  # range(inicio, fin, paso) → aquí va de 1 a 9, saltando de 2 en 2
  for i in range(1, 10, 2):
      print("Paso:", i)  # Imprime 1, 3, 5, 7, 9

# Bucle while
  # Ejecuta mientras la condición sea verdadera
  contador = 0
  while contador < 3:
      print("Contador:", contador)  # Imprime 0, 1, 2
      contador += 1  # Incrementa en cada vuelta

# Bucle infinito con break
  # Este ciclo se repetiría para siempre, pero lo rompemos con break
  while True:
      print("Ciclo único")  # Se ejecuta una vez
      break  # Rompe el ciclo inmediatamente

# Bucle con continue
  # Salta la iteración cuando i es igual a 2
  for i in range(5):
      if i == 2:
          continue  # Salta el print cuando i es 2
      print("Valor:", i)  # Imprime 0, 1, 3, 4

# Bucle con else
  # El bloque else se ejecuta si el bucle termina sin usar break
  for i in range(3):
      print("Número:", i)  # Imprime 0, 1, 2
  else:
      print("Fin del bucle")  # Se ejecuta al final del ciclo

# If anidado
  # Se puede colocar un condicional dentro de otro
  x = 10
  if x > 0:  # Primera condición: ¿x es positivo?
      if x < 20:  # Segunda condición: ¿x es menor que 20?
          print("Entre 1 y 19")  # Ambas condiciones se cumplen

