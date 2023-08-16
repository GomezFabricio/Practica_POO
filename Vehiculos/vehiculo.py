class Vehiculo():
    def __init__(self, marca, modelo, color):
        self.marca = marca;
        self.modelo = modelo;
        self.color = color;

# Clase hija que hereda de la clase padre vehículo y agrega dos atributos llamados puertas y baul.
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color, puertas, baul):
        super().__init__(marca, modelo, color) # Llamada al constructor del objeto padre (super).
        self.__puertas = puertas;  # Asignación a una variable privada el valor pasado por parámetro.
        self.__baul = baul;

    def descripcion(self):
        return f"\nDetalle del Automovil:\nMarca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nCantidad de puertas: {self.__puertas}\nBaul: {self.__baul}";

# Clase hija que hereda de la clase padre vehículo y agrega un atributo llamado acoplado.
class Camion(Vehiculo):
    def __init__(self, marca, modelo, color, acoplado):
        super().__init__(marca, modelo, color) # Llamada al constructor del objeto padre (super).
        self.__acoplado = acoplado;

    def descripcion(self):
        return f"\nDetalle del camion:\nMarca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nAcomplado: {self.__acoplado}";