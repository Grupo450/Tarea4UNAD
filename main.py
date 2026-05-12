from modelos.cliente import Cliente
from modelos.sala import ReservaSala
from modelos.equipo import AlquilerEquipo
from modelos.asesoria import Asesoria
from modelos.reserva import Reserva
import logging

from excepciones.excepciones import (
    ClienteError,
    ServicioError,
    ReservaError
) 

# CONFIGURACION DE LOGS

logging.basicConfig(
    filename='logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

print("===== SISTEMA SOFTWARE FJ =====")
# OPERACION 1

try:

    cliente1 = Cliente(
        "Juan",
        "juan@gmail.com",
        "1234567890"
    )

    print(cliente1.mostrar_info())

    logging.info("Cliente creado correctamente")

except ClienteError as e:

    logging.error(f"Error al crear cliente: {e}") 



# OPERACION 2 INVALIDA

try:

    cliente2 = Cliente(
        "",
        "correoMALO",
        "123"
    )

except ClienteError as e:

    print("Error en cliente inválido")
    logging.error(f"Error al crear cliente inválido: {e}")


# OPERACION 3

try:

    sala1 = ReservaSala(
        "Sala VIP",
        100,
        3
    )

    print(sala1.descripcion())
    print(sala1.calcular_costo())

    logging.info("Reserva de sala creada correctamente")

except ServicioError as e:

    logging.error(f"Error en reserva de sala: {e}") 

# OPERACION 4

try:

    equipo1 = AlquilerEquipo(
        "Laptop",
        80,
        2
    )

    print(equipo1.descripcion())
    print(equipo1.calcular_costo())
    logging.info("Alquiler de equipo creado correctamente") 

except ServicioError as e:

    logging.error(f"Error en alquiler de equipo: {e}") 

# OPERACION 5

try:

    asesoria1 = Asesoria(
        "Python",
        120,
        2
    )

    print(asesoria1.descripcion())
    print(asesoria1.calcular_costo())  
    logging.info("Asesoría creada correctamente") 

except ServicioError as e:

    logging.error(f"Error en asesoría: {e}") 

# OPERACION 6

try:

    reserva1 = Reserva(
        cliente1,
        sala1,
        3
    )

    print(reserva1.procesar())

except ReservaError as e:

    logging.error(f"Error al procesar reserva: {e}") 


# OPERACION 7 INVALIDA

try:

    reserva2 = Reserva(
        cliente1,
        sala1,
        -5
    )

except ReservaError as e:

    print("Error en reserva inválida")
    logging.error(f"Error en reserva inválida: {e}") 

# OPERACION 8

try:

    reserva1.cancelar()

    print("Estado:", reserva1.get_estado())

    logging.info("Reserva cancelada correctamente")

except ReservaError as e:

    logging.error(f"Error al cancelar reserva: {e}") 

# OPERACION 9

try:

    servicios = [sala1, equipo1, asesoria1]

    for servicio in servicios:

        print(servicio.descripcion())

except ServicioError as e: 

    logging.error(f"Error general del sistema: {e}") 

# OPERACION 10

try:

    print("Sistema funcionando correctamente")

except Exception as e:

    logging.error(f"Error general del sistema: {e}") 

else:

    print("Operaciones ejecutadas")

finally:

    print("Programa finalizado") 