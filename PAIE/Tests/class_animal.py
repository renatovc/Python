class animal:
    numAnimales = 0
    def __init__(self, age = "1", name = "dog"):
        self.age = age
        self.name = name
        animal.numAnimales += 1

    def mostrarNombre(self):
        print("El animal es:", str(self.name))

    def mostrarEdad(self):
        print("La edad es:", str(self.age))

class Math:
    @staticmethod
    def cuadrado(i):
        return i*i
    
    @staticmethod
    def mitad(i):
        return i/2

animal2 = animal("10","gato")
animal2.mostrarNombre()
animal2.mostrarEdad()
animal2.numAnimales