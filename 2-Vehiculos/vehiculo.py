class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"\nDetalle del Coche:\nColor: {self.color}\nRuedas: {self.ruedas}\nVelocidad: {self.velocidad}km/h\nCilindrada: {self.cilindrada}cc"

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"\nDetalle de la Camioneta:\nColor: {self.color}\nRuedas: {self.ruedas}\nVelocidad: {self.velocidad}km/h\nCilindrada: {self.cilindrada}cc\nCarga: {self.carga}"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"\nDetalle de la Bicicleta:\nColor: {self.color}\nRuedas: {self.ruedas}\nTipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"\nDetalle de la Motocicleta:\nColor: {self.color}\nRuedas: {self.ruedas}\nTipo: {self.tipo}\nVelocidad: {self.velocidad}km/h\nCilindrada: {self.cilindrada}cc"


