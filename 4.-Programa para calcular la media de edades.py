# Lista con edades
edades = [15, 26, 54, 22, 17, 50, 33, 32]  #Primero tenemos una lista llamada edades, con valores de edades diferentes.

# Obtener la suma de las edades
suma_edades = sum(edades) #Utilizamos una función predefinida de Python, llamada sum(). Esta función suma todos los valores de un elemento, como puede ser una lista.

# Obtener el número total de edades
numero_edades = len(edades) #Utilizamos otra función predefinida de Python, llamada len(), que es capaz de contar el total de elementos que hay en un elemento concreto, como puede ser una lista.

# Calcular la media
media = suma_edades / numero_edades #Aquí el resultado puede salir en decimal, por lo cual si quieres que siempre sea un número entero simplemente debes cambiar el operador (/) por (//)

# Imprimir los resultados
print("En total hay:", numero_edades, "edades en la media.")
print("La edad media de todas ellas es:", media)

