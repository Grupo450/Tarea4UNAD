from modelos.servicio import Servicio

class Asesoria(Servicio):

    def __init__(self, nombre, precio_base, horas):

        super().__init__(nombre, precio_base)

        self.__horas = horas

    def get_horas(self):
        return self.__horas

    # Sobrecarga con descuento opcional
    def calcular_costo(self, descuento=0):

        costo = self.get_precio_base() * self.__horas

        if descuento > 0:
            costo -= costo * (descuento / 100)

        return costo

    def descripcion(self):

        return "Asesoría especializada"

    # Disponibilidad simulada
    def consultar_disponibilidad(self):

        return True 