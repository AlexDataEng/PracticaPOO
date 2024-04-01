# Clase Clientes
class Cliente:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

    # Getter
    @property
    def nombre(self):
         print(f"El nombre del cliente es {self.__nombre}")    
    
    @property
    def contrasena(self):
         print(f"El nombre del cliente es {self.__contrasena}") 


    #Setter (Validadores)
    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
        else:
            print("Debe ingresar un nombre")

    @contrasena.setter
    def contrasena(self, contrasena):
        if contrasena.strip():
            self.__contrasena = contrasena
        else:
            print("Debe ingresar una contraseña")


alex = Cliente("Alex", "74187418")
