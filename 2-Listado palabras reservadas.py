#Con este pequeño código podemos observar las palabras reservadas en lista
import keyword
print(keyword.kwlist)


#A continuación una pequeña explicación de que hace o para que sirve cada una.
"""
and
Operador lógico que evalúa dos expresiones y devuelve True solo si ambas son verdaderas.

as
Palabra reservada utilizada para asignar un alias a un módulo o recurso importado, facilitando su uso dentro del código

assert
Comprueba si una expresión es verdadera; si no lo es, lanza una excepción, generalmente utilizada para depuración.

async
Declara una función como asíncrona, lo que permite que su ejecución no bloquee el hilo principal del programa.

await
Pausa la ejecución de una función asíncrona hasta que una operación asíncrona previamente iniciada se complete.

break
Interrumpe un bucle antes de que se complete, terminando la ejecución de la estructura que lo contiene.

class
Palabra clave que define una nueva clase, proporcionando una plantilla para crear objetos en programación orientada a objetos.

continue
Hace que el programa salte a la siguiente iteración de un bucle, omitiendo el resto del código en la iteración actual.

def
Se utiliza para declarar una nueva función, especificando su nombre, parámetros y el bloque de código que ejecutará.

del
Elimina objetos o sus referencias, como claves en un diccionario o variables, liberando así recursos.

else
Parte de una estructura condicional que ejecuta un bloque de código si las condiciones anteriores no se cumplen.

finally
Bloque de código que se ejecuta siempre al final de una estructura try-except, sin importar si hubo una excepción.

for
Inicia un bucle que itera sobre una secuencia, como una lista o un rango, ejecutando el código interno en cada iteración.

global
Declara una variable como global, permitiendo que se acceda y modifique fuera del alcance local de una función.

elif
Parte de una estructura condicional que permite evaluar múltiples condiciones si las anteriores no se cumplen.

except
Captura y maneja excepciones en un bloque try, permitiendo que el programa continúe sin interrumpirse.

False
Valor booleano que representa la falsedad lógica en Python.

from
Se usa para importar elementos específicos de un módulo, como funciones o clases, sin necesidad de importar todo el módulo.

if
Inicia una estructura condicional que evalúa una expresión, ejecutando el bloque de código correspondiente si es verdadera.

import
Incorpora módulos o bibliotecas externas en el código, habilitando el uso de sus funciones, clases u objetos.

in
Comprueba si un elemento está presente dentro de una secuencia, como una lista, tupla o cadena de caracteres.

is
Compara la identidad de dos objetos, verificando si son exactamente el mismo objeto en memoria.

lambda
Define funciones anónimas y de una sola línea, que pueden ser utilizadas en cualquier parte del código donde se necesite una función simple.

nonlocal
Permite modificar variables dentro de funciones anidadas que no pertenecen a la función local, pero tampoco son globales.

None
Representa la ausencia de valor o un valor nulo en Python.

not
Operador lógico de negación, que invierte el valor de una expresión booleana.

or
Operador lógico que evalúa dos expresiones y devuelve True si al menos una de ellas es verdadera.

pass
Permite dejar bloques de código vacíos sin generar errores, útil como marcador de posición en funciones o bucles.

raise
Genera una excepción manualmente, permitiendo que el programador indique situaciones de error específicas.

return
Finaliza la ejecución de una función y devuelve un valor al llamador de la función.

True
Valor booleano que representa la verdad lógica en Python.

try
Bloque de código que intenta ejecutar operaciones que podrían generar excepciones, permitiendo el manejo adecuado de errores.

while
Inicia un bucle que se ejecuta mientras una condición dada sea verdadera.

with
Palabra clave que facilita la gestión de recursos, como archivos, asegurando que se cierren o liberen adecuadamente después de su uso.

yield
Se utiliza dentro de funciones generadoras para devolver valores de manera pausada, permitiendo que se reanude su ejecución posteriormente.
"""
