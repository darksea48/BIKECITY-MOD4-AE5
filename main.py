from Clases import Bike, Reservation, InvalidReservationError, BikeUnavailableError
from datetime import datetime

#Creación primera bicicleta
print("----Bicicleta----")
oxford1 = Bike("Oxford X1")
print(oxford1.modelo)
print(oxford1.estado)

print("\n----Reserva 1----")
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
print("\n----Reserva 2----")
try:
    reserva2 = Reservation(oxford1, "Gokú", estado = "Activa", inicio=datetime(2025, 8, 6, 20, 0), fin=datetime(2025, 8, 6, 22, 30))

except InvalidReservationError as e:
    print(f"Error: {e}")
except BikeUnavailableError as e:
    print(f"Error: {e}")
finally:
    print("Se intentó la reserva.")


#Intentar reservar con horarios inválidos
print("\n----Reserva 3----")
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
print("\n----Reserva 1 finalizada----")
reserva1.finalizar()
print(f"Estado {oxford1.modelo}: {oxford1.estado}")

#Intentar reservar nuevamente la primera bicicleta
print("\n----Reintento en reserva 3----")
try:
    reserva3 = Reservation(oxford1, "Teemo", estado = "Activa", inicio=datetime(2025, 8, 7, 12, 0), fin=datetime(2025, 8, 7, 16, 30))

except InvalidReservationError as e:
    print(f"Error: {e}")
except BikeUnavailableError as e:
    print(f"Error: {e}")
finally:
    print("Se intentó la reserva.")
