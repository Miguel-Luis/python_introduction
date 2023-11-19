edad = 18

"""
Podemos usar operadores lógicos:
* and = &&
* or = ||
* not = !
"""

if edad < 18:
    print("Eres menor de edad. Mocoso.")
elif edad >= 18 and edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
