# Mutabilidad
  # Un objeto mutable puede cambiar su contenido después de ser creado
  lista_mutable = [1, 2, 3]
  lista_mutable[0] = 99  # Se modifica el primer elemento
  print("Lista mutable:", lista_mutable)  # [99, 2, 3]

# Inmutabilidad
  # Un objeto inmutable no puede cambiar su contenido una vez creado
  tupla_inmutable = (1, 2, 3)
  # tupla_inmutable[0] = 99  # Esto lanza TypeError: 'tuple' object does not support item assignment

"""
 Hashabilidad
    Un objeto hashable tiene un valor hash fijo y puede usarse como clave en un diccionario
    Los objetos inmutables como strings, enteros y tuplas (sin listas dentro) son hashables

¿Por qué la necesidad de un hash?
    El hash permite identificar objetos rápidamente en estructuras como diccionarios y conjuntos
    Es como un "ID digital" que resume el contenido del objeto

¿Por qué no se pueden utilizar objetos mutables como hash?
    Porque si el contenido cambia, el hash también cambiaría, rompiendo la integridad de estructuras como dict
      Ejemplo:
        diccionario = {[1, 2, 3]: "valor"}  # TypeError: unhashable type: 'list'
"""

# Ver el número hash de un objeto
  texto = "Marco"
  print("Hash de texto:", hash(texto))  # Devuelve un número entero único

  numero = 42
  print("Hash de número:", hash(numero))  # También funciona con enteros

# Iterabilidad
  # Un objeto iterable puede ser recorrido elemento por elemento (por ejemplo, en un bucle for)
  mi_lista = ["a", "b", "c"]
  for letra in mi_lista:
      print("Letra:", letra) #Ciclo 0= a, Ciclo 1= b y Ciclo 2= c

# También se puede convertir en iterador manualmente
  iterador = iter(mi_lista)
  print(next(iterador))  # 'a'
  print(next(iterador))  # 'b'
  print(next(iterador))  # 'c'
  # print(next(iterador))  # StopIteration si se acaba

# Puedes verificar si un objeto es iterable
  from collections.abc import Iterable
  print("¿Es iterable?", isinstance(mi_lista, Iterable))  # True
