from persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, cantidad_materias):
        super().__init__(nombre, apellido, edad);
        self.cantidad_materias = cantidad_materias;

    def detalleMaterias(self):
        return f"Cantidad Materias: {self.cantidad_materias}"