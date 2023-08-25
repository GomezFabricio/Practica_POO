class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre;
        self.apellido = apellido;
        self.edad = edad; 
    
    def nombreCompleto(self):
        return f"Nombre Completo: {self.nombre} {self.apellido}"

    def mayorEdad(self):
        if self.edad >= 0:
            if self.edad >= 18:
                return "Es mayor de edad";
            else:
                return "No es mayor de edad";
        else:
            return "Edad Inválida"
