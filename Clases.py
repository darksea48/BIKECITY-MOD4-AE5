from datetime import datetime, timedelta
import random
from math import *

class BikeUnavailableError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class InvalidReservationError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class Bike():
    def __init__(self, modelo, estado="Disponible"):
        self.modelo = modelo
        self.estado = estado
    
    def cambiar_estado(self, nuevo_estado: str):
        if nuevo_estado not in ("disponible", "ocupado"):
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
        self.bici.comprobar_estado("Ocupado")
        self.cliente = cliente
        self.inicio = inicio
        self.fin = fin
        self.duracion = self.calcular_duracion(inicio, fin)
        self.precio = self.duracion * self.tarifa_por_hora
        self.estado = "Activa"

    def finalizar(self):
        try:
            if self.estado == "Activa":
                self.estado = "Completada"
                self.bici.comprobar_estado("Disponible")
                print(f"Precio arriendo: {self.precio}")
            else:
                raise BikeUnavailableError("La reserva ya está completada.")
        except BikeUnavailableError as e:
            print(f"Error: {e}")
            
    @staticmethod
    def calcular_duracion(inicio, fin):   
        duracion_segundos = (fin - inicio).total_seconds()
        duracion_horas = duracion_segundos / 3600
        return round(duracion_horas)
       

class Cliente():
    def __init__(self, nombre, apellido, telefono, email, id=random.randint(1000, 9999)):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email