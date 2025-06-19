#clase 
class Persona:
    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
#objeto
persona1 = Persona("Luis", 25)
persona1.saludar()
