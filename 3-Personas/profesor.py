from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, cantidad_horas):
        super().__init__(nombre, apellido, edad);
        self.cantidad_horas = cantidad_horas;

    def detalleHorasAcumuladas(self):
        return f"Horas acumuladas: {self.cantidad_horas}"

