from vehiculo import Vehiculo, Coche, Camioneta, Bicicleta, Motocicleta

def catalogar(vehiculos, ruedas=None):
    print("CATALOGO DE VEHICULOS:")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Vehículo {i}:\n{vehiculo}\n")

    vehiculos_seleccionados = []

    if ruedas is not None:
        print("---------------------------------------------------------------")
        print(f"Filtro: {ruedas} ruedas")
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                vehiculos_seleccionados.append(vehiculo)

    if vehiculos_seleccionados:
        print(f"Se han encontrado {len(vehiculos_seleccionados)} vehículos\n")

        for i, vehiculo in enumerate(vehiculos_seleccionados, start=1):
            print(f"Vehículo {i}:\n{vehiculo}\n")

    else:
        if ruedas is not None:
            print(f"No se han encontrado vehículos con {ruedas} ruedas.")

            

coche1 = Coche("Rojo", 4, 180, 2000)
camioneta1 = Camioneta("Azul", 4, 150, 3000, 1000)
bicicleta1 = Bicicleta("Verde", 2, "Urbana")
motocicleta1 = Motocicleta("Negra", 2, "Deportiva", 250, 150)

vehiculos = [coche1, camioneta1, bicicleta1, motocicleta1]

# Prueba con diferentes valores de ruedas
#catalogar(vehiculos)
catalogar(vehiculos, ruedas=2)
#catalogar(vehiculos, ruedas=4)
#catalogar(vehiculos, ruedas=0)