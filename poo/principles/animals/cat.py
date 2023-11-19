from .animal import Animal
# Segundo Principio: Herencia = Una clase hija puede heredar atributos y comportamientos de una clase padre.
class Cat(Animal):
    def __init__(self, name, age, color):
        # Cuarto Principio: Encapsulamiento = Los atributos de la clase están ocultos para otras clases
        super().__init__(name, age)
        self.color = color

    # Tercer Principio: Polimorfismo = Muchos comportamientos.
    def make_sound(self):
        return "¡Miau, miau!"

    """ Sin hacer polimorfismo
    def get_information(self):
    return super().get_information() """

    def get_information(self):
        return f"{self.name} es un gato de color {self.color} y tiene {self.age} años."