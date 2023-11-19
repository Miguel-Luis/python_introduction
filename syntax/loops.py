# ----------------------- Bucles -----------------
# En Python, se pueden usar dos tipos principales de bucles: for y while

# * El bucle for se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena, o rango).
frutas = ["manzana", "plátano", "uva", "cereza"]

for fruta in frutas:
    print(fruta)

# ! El bucle while se ejecuta mientras una condición sea verdadera.
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# ? La sentencia break se utiliza para salir de un bucle antes de que se complete su ejecución normal.
for fruta in frutas:
    if fruta == "plátano":
        break

    #print(fruta)

# TODO La sentencia continue se utiliza para omitir el resto del código en la iteración actual y pasar a la siguiente iteración.
for fruta in frutas:
    if fruta == "manzana":
        continue

    print(fruta)