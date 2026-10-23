from cls_Stack import cls_Stack

class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.partida = cls_Stack()
        self.cartas_obtenidas = []


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nuevo_nombre


    





        
        

   