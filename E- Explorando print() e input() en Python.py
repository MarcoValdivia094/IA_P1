#La función print() sirve para mostrar cosas en pantalla. Es como decirle a Python: "¡Ey, muéstrame esto!"
print("Hola mundo")  # Clásico.

# El parámetro *objects permite imprimir varios elementos a la vez, separados por comas.
nombre = "Marco"
edad = 99
print("Tu nombre es:", nombre, "y tu edad es:", edad)  # Aquí *objects está imprimiendo 4 cosas, el primer mensaje, el contenido de nombre, el segundo mensaje y por último el contenido de edad.

# El parámetro sep define qué separador usar entre los objetos.
print("Python", "es", "genial", sep="🔥")  # Resultado: Python🔥es🔥genial

# Por defecto, print() termina con un salto de línea (\n), pero podemos cambiar eso con el parámetro end.
print("Esto está en la misma línea", end=" ")  # No salta de línea
print("¿Ves?")  # Se imprime justo después

# La función input() sirve para pedirle al usuario que escriba algo. Es como abrirle la puerta al teclado.
nombre_usuario = input("¿Cómo te llamas? ")  # Lo que escribas se guarda como texto (str)
print("Hola", nombre_usuario)

# Tipos de datos en las entradas: todo lo que entra por input() es texto (string), aunque parezca número.
edad_usuario = input("¿Cuántos años tienes? ")  # Aunque pongas 25, sigue siendo un str
print("Tipo de dato:", type(edad_usuario))  # Esto mostrará: <class 'str'>

#Si quieres trabajar con números, hay que convertirlos.
edad_num = int(edad_usuario)  # Ahora sí, es un entero (int)
print("En 5 años tendrás:", edad_num + 5)

# Tip extra: también puedes usar float() para decimales, bool() para booleanos, etc.
altura = float(input("¿Cuánto mides en metros? "))  # Ejemplo: 1.75
print("Tu altura más 0.1m sería:", altura + 0.1)
