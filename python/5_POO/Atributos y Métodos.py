#crear atributos y metodos 
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")
mi_perro = Perro("Max", "Labrador")
mi_perro.ladrar()
