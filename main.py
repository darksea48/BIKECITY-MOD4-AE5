from Clases import Bike, Reservation, InvalidReservationError, BikeUnavailableError
from datetime import datetime

#Creación primera bicicleta
oxford1 = Bike("Oxford X1")
print(oxford1.modelo)
print(oxford1.estado)

#Intentar reservar
try:
    reserva1 = Reservation(oxford1, "Conan", estado = "Activa", inicio=datetime(2025, 8, 6, 20, 0), fin=datetime(2025, 8, 6, 22, 30))

except InvalidReservationError as e:
    print(f"Error: {e}")
except BikeUnavailableError as e:
    print(f"Error: {e}")
finally:
    print("Se intentó la reserva.")

#Intentar reservar la misma bicicleta
try:
    reserva2 = Reservation(oxford1, "Gokú", estado = "Activa", inicio=datetime(2025, 8, 6, 20, 0), fin=datetime(2025, 8, 6, 22, 30))

except InvalidReservationError as e:
    print(f"Error: {e}")
except BikeUnavailableError as e:
    print(f"Error: {e}")
finally:
    print("Se intentó la reserva.")


#Intentar reservar con horarios inválidos
oxford2 = Bike("Oxford X2")
try:
    reserva3 = Reservation(oxford2, "Mikasa", estado = "Activa", inicio=datetime(2025, 8, 6, 20, 0), fin=datetime(2025, 8, 6, 14, 30))

except InvalidReservationError as e:
    print(f"Error: {e}")
except BikeUnavailableError as e:
    print(f"Error: {e}")
finally:
    print("Se intentó la reserva.")

#Finalizar reserva 1
reserva1.finalizar()
print(f"Estado {oxford1.modelo}: {oxford1.estado}")

#Intentar reservar nuevamente la primera bicicleta
try:
    reserva3 = Reservation(oxford1, "Teemo", estado = "Activa", inicio=datetime(2025, 8, 7, 12, 0), fin=datetime(2025, 8, 7, 16, 30))

except InvalidReservationError as e:
    print(f"Error: {e}")
except BikeUnavailableError as e:
    print(f"Error: {e}")
finally:
    print("Se intentó la reserva.")
