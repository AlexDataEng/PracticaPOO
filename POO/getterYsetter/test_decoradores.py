class Perro:
    def __init__(self, nombre):
        self.nombre = nombre # Primero llama para saber si existe un Getter dentro de la clase.
        print("Pasando por constructor")


    #El decorador @property crea un método getter para el atributo nombre,
    # permitiendo acceder a él como si fuera un atributo de solo lectura.
    @property
    def nombre(self):
        print("Pasando por Getter")
        return self.__nombre
    

    # El decorador @nombre.setter crea un método setter
    # para el atributo nombre, permitiendo establecer su valor.
    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por Setter")
        if nombre.strip():
            self.__nombre = nombre
        else:
            return

perro = Perro("Roca")
print(perro.nombre)
