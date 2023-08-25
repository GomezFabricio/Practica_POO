from persona import Persona

class Coordinador(Persona):
    def __init__(self, nombre, apellido, edad, cantidad_cursos):
        super().__init__(nombre, apellido, edad);
        self.cantidad_cursos = cantidad_cursos;

    def detalleCantidadCursos(self):
        return f"Cantidad de cursos a cargo: {self.cantidad_cursos}"