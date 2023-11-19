# ---------------------------------- Funciones -------------------------
'''
En Python, se puede definir funciones utilizando la palabra clave def.
'''

def saludar(nombre):
    mensaje = f"Hola, {nombre}!"
    return mensaje

# Llamada a la función
nombre = input("¿Cómo te llamas bebé?\n") # Pedir información por consola
resultado_saludo = saludar(nombre)
print(resultado_saludo)