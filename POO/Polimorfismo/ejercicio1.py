from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def sonido():
        pass

# Clase de Perros
class Perro(Animal):
    def __init__(self, nombre):
        self.nombre = nombre
    #Este método es obligatorio por ser Abstrancto en la clase Animal
    def sonido(self):
        print({f"El Perro {self.nombre} dice GUAU!"})
    
    def nombre_animal(self):
        print(f"El nombre del perro es {self.nombre}")


# Clase de Pollos
class Pollo(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        print({f"El Gallo {self.nombre} dice Pío!"})


# Funcion con Polimorfismo
def hacer_sonar(objeto):
    objeto.sonido()

#roca = Perro('Roca')

#hacer_sonar(roca)