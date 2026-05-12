from excepciones.excepciones import ReservaError
from excepciones.excepciones import ServicioError

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a cero")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    # Getters
    def get_cliente(self):
        return self.__cliente

    def get_servicio(self):
        return self.__servicio

    def get_duracion(self):
        return self.__duracion

    def get_estado(self):
        return self.__estado

    def confirmar(self):

        self.__estado = "Confirmada"

    def cancelar(self):

        self.__estado = "Cancelada"

    def procesar(self):

        try:

            if not self.__servicio.consultar_disponibilidad():
                raise ServicioError("El servicio no está disponible")

            costo = self.__servicio.calcular_costo()

            self.confirmar()

            return f"Reserva procesada correctamente. Total: {costo}"

        except ServicioError as e:

            raise ReservaError(
                f"Error al procesar la reserva: {e}"
            ) from e