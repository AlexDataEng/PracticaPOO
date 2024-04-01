# Clase Persona

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def guardar_db(self):
        print(f"El cliente {self.nombre} ha sido ingresado a la BBDD")

class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre

    def guardar_db(self):
        print(f"El Proveedor {self.nombre} ha sido ingresado a la BBDD")


def guardar_db(objetos):
    if isinstance(objetos, list):
        for objeto in objetos:
            objeto.guardar_db()
    else:
        objetos.guardar_db()


# Instancias
alex = Cliente('Alex')
caprile = Proveedor('Caprile')


# Guardamos usando la funcion
# -> guardar_db([caprile, alex])
guardar_db(alex)
