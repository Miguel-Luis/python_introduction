class Dog:
    '''
    Método constructor es un método que sirve para
    dar un estado inicial a un objeto cuando este es instanciado
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "¡Guau, guau!"
    
    def get_information(self):
        return f"{self.name} tiene {self.age} años"