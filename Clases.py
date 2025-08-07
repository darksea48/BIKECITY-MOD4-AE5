from datetime import datetime, timedelta
import random
from math import *

class BikeUnavailableError(Exception):
    pass
class InvalidReservationError(Exception):
    pass
class Bike():
    bikes = []
    
    def __init__(self, modelo, estado="Disponible"):
        self.modelo = modelo
        self.estado = estado
        self.bikes.append(self)
    
    def cambiar_estado(self, nuevo_estado: str):
        if nuevo_estado not in ("Disponible", "Ocupado"):
            raise ValueError(f"Estado inválido: {nuevo_estado}. Se esperan sólo los valores 'disponible' u 'ocupado'.")
        self.estado = nuevo_estado
        return self
    
    def consulta_estado(self):
        print(f"Modelo de la bicicleta: {self.modelo}")
        print(f"Estado de la bicicleta: {self.estado}")
        return self
    
    def __str__(self):
        return f"Bicicleta nueva agregada: modelo={self.modelo} estado={self.estado}"
    
class Reservation():
    tarifa_por_hora = 10
    
    def __init__(self, bici, cliente, inicio=datetime.now(), fin=datetime.now()):
        
        if fin < inicio:
            raise InvalidReservationError("Las horas de inicio y fin no pueden ser iguales o fin sea anterior a inicio.")
        
        if bici.estado != "Disponible":
            raise BikeUnavailableError(f"La bicicleta {bici.modelo} está ocupada. No se puede reservar esta bicicleta.")
        
        self.bici = bici
        self.bici.cambiar_estado("Ocupado")
        self.cliente = cliente
        self.inicio = inicio
        self.fin = fin
        self.duracion = self.calcular_duracion(inicio, fin)
        self.precio = ceil(self.duracion) * self.tarifa_por_hora
        self.estado = "Activa"

    def finalizar(self):
        try:
            if self.estado == "Activa":
                self.estado = "Completada"
                self.bici.cambiar_estado("Disponible")
                print(f"Precio arriendo: {self.precio}")
            else:
                raise BikeUnavailableError("La reserva ya está completada.")
        except BikeUnavailableError as e:
            print(f"Error: {e}")
        return self
            
    @staticmethod
    def calcular_duracion(inicio, fin):   
        duracion_segundos = (fin - inicio).total_seconds()
        duracion_horas = duracion_segundos / 3600
        return duracion_horas
       

class Cliente():
    def __init__(self, nombre, apellido, telefono, email, id=random.randint(1000, 9999)):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email