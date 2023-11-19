# ----------------------------- Estructuras de Datos --------------------

""" ---------- Listas ---------
* Sintaxis: [elemento1, elemento2, ..., elementoN]
* Las listas son colecciones ordenadas y mutables de elementos.
* Puedes agregar, eliminar y modificar elementos después de haber creado la lista.
* Se accede a los elementos mediante índices (que comienzan desde 0).
"""

lista = [1, 2, 'tres', 4.0, True]
lista.append(5) # Agrega un elemento al final
lista[2] = "nuevo" # Modifica un elemento
del lista[1] # Elimina un elemento por índice
lista[4] # Acceder a la posición 4 de la lista

print("Lista:")
print(lista)
print(lista[4])

""" ---------- Tuplas --------
* Sintaxis: (elemento1, elemento2, ..., elementoN)
* Las tuplas son colecciones ordenadas e inmutables de elementos.
* No puedes cambiar el contenido de una tupla después de haberla creado.
* Se accede a los elementos mediante índices (que comienzan desde 0)
"""

tupla = (1, 2, 'tres', 4.0, True)
valor = tupla[2] # Accede a un elemento por índice

""" ----------- Diccionarios -----------
* Sintaxis: {
    clave1: valor1,
    clave2: valor2,
    ...,
    claveN: valorN
}

* Los diccionarios son colecciones no ordenadas de pares clave-valor.
* Puedes agregar, eliminar y modificar elementos.
* Se accede a los valores mediante claves, no índices.
"""

diccionario = {
    'clave1': 'valor1',
    'clave2': 42,
    'clave3': [1, 2, 3]
}

print("Diccionario:")
print(diccionario)

diccionario['clave4'] = 'nuevo valor' # Agrega un nuevo par clave-valor.
del diccionario['clave1'] # Elimina un par clave-valor por clave