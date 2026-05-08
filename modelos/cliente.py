from modelos.entidad import Entidad
from excepciones.excepciones import ClienteError

class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        if not nombre:
            raise ClienteError("Nombre vacío")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        if len(telefono) < 10:
            raise ClienteError("Teléfono inválido")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}" 