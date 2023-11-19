class Animal:
    # Primer Principio: Abstracción = Es tomar las características mas generales de un objeto
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass # Método abstracto que será implementado por las clases derivadas

    def get_information(self):
        return f"{self.name} tiene {self.age} años."