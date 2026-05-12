from modelos.servicio import Servicio

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, dias):

        super().__init__(nombre, precio_base)

        self.__dias = dias

    def get_dias(self):
        return self.__dias

    # Sobrecarga con descuento opcional
    def calcular_costo(self, descuento=0):

        costo = self.get_precio_base() * self.__dias

        if descuento > 0:
            costo -= costo * (descuento / 100)

        return costo

    def descripcion(self):

        return "Alquiler de equipos tecnológicos"

    # Disponibilidad simulada
    def consultar_disponibilidad(self):

        return True 