from abc import ABC, abstractmethod
from excepciones.excepciones import ServicioError 

class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if precio_base <= 0:
            raise ServicioError("El precio base debe ser mayor a cero")

        self.__nombre = nombre
        self.__precio_base = precio_base

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_precio_base(self):
        return self.__precio_base

    # Método abstracto
    @abstractmethod
    def calcular_costo(self, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def consultar_disponibilidad(self):
        pass