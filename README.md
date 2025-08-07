# BIKECITY - Sistema de Reservas de Bicicletas

**BIKECITY** es un sistema educativo desarrollado en Python que simula la reserva de bicicletas mediante programación orientada a objetos, manejo de fechas y control de errores y está diseñado para enseñar buenas prácticas en el uso de clases, excepciones personalizadas y validaciones.

## Estructura del Proyecto

- `Clases.py`: Contiene las clases principales del sistema:
  - `Bike`: Representa una bicicleta con estado (`Disponible` u `Ocupado`).
  - `Reservation`: Gestiona reservas con cálculo de duración y precio.
  - `Cliente`: Representa al usuario que realiza la reserva.
  - Excepciones personalizadas:
    - `BikeUnavailableError`
    - `InvalidReservationError`

- `main.py`: Script de ejecución que simula distintos escenarios de reserva.

## Funcionalidades

- Crear bicicletas con estado inicial.
- Reservar bicicletas disponibles.
- Validar fechas de inicio y fin.
- Calcular duración y precio de la reserva.
- Finalizar reservas y liberar bicicletas.
- Manejo de errores con `try/except/finally`.

## Ejecución

python main.py



