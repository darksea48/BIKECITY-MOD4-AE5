from datetime import datetime
import random

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
    
    def cambiar_estado(self, nuevo_estado):
        try:
            if nuevo_estado != self.estado:
                self.estado = nuevo_estado
            else:
                if self.estado == "Ocupado":
                    mensaje ="El artículo se encuentra Ocupado"
                else:
                    mensaje ="El artículo ya se encuentra Disponible"
                raise BikeUnavailableError(mensaje)
        except BikeUnavailableError as e:
            print(f"Error: {e}")
            
    def comprobar_estado(self, nuevo_estado):
        try:
            if nuevo_estado == "Ocupado" or nuevo_estado == "Disponible":
                self.cambiar_estado(nuevo_estado)
            else:
                raise ValueError("El estado debe ser 'Ocupado' o 'Disponible'")
        except ValueError as e:
            print(f"Error: {e}")

class Reservation():
    tarifa_por_hora = 10
    
    def __init__(self, bici, cliente, estado="Activa", inicio=datetime.now(), fin=datetime.now()):
        self.bici = bici
        self.cliente = cliente
        self.inicio = inicio
        self.fin = fin
        self.duracion = self.calcular_duracion(inicio, fin)
        self.precio = self.duracion * self.tarifa_por_hora
        self.estado = estado

    def finalizar(self):
        try:
            if self.estado == "Activa":
                self.estado = "Finalizada"
                self.bici.comprobar_estado("Disponible")
            else:
                raise BikeUnavailableError("La bicicleta no está ocupada")
        except BikeUnavailableError as e:
            print(f"Error: {e}")
            
    @staticmethod
    def calcular_duracion(inicio, fin):
        try: 
            if fin < inicio:
                raise InvalidReservationError     
        
            duracion_segundos = (fin - inicio).total_seconds()
            duracion_horas = duracion_segundos / 3600
            return round(duracion_horas)
        except InvalidReservationError as e:
            raise InvalidReservationError(f"Error en la duracion: {e}")

class Cliente():
    def __init__(self, nombre, apellido, telefono, email, id=random.randint(1000, 9999)):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email