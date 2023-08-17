from vehiculo import Automovil, Camion

def atributosGenerales():
    print("\nPor favor, rellene los siguentes datos: ")
    while True:
        try:
            marca = input("\nMarca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")

            if marca and modelo and color:
                return marca, modelo, color
            else:
                print("Debe ingresar valores en todos los campos.")

        except Exception as e:
            print("Ha ocurrido un error:", e)

def main():
    while True:
        try:
            tipo_vehiculo = int(input("\n\nIngrese el tipo de vehiculo\n\n1- Automovil\n2- Camion\n\nRespuesta: "))

            if tipo_vehiculo == 1:
                marca_resultado, modelo_resultado, color_resultado = atributosGenerales()
                while True:
                    try:
                        puertas = int(input("Cantidad de puertas: "))
                        baul = input("Tipo de baul: ")

                        automovil1 = Automovil(marca_resultado, modelo_resultado, color_resultado, puertas, baul)
                        print(automovil1.descripcion())
                        break
                    except ValueError:
                        print("Error en la entrada de datos.")
                break
            elif tipo_vehiculo == 2:
                marca_resultado, modelo_resultado, color_resultado = atributosGenerales()
                acoplado = input("Acoplado: ")

                camion1 = Camion(marca_resultado, modelo_resultado, color_resultado, acoplado)
                print(camion1.descripcion())
                break
            else:
                print("Opción inválida.")
            break
        except ValueError:
            print("Error en la entrada de datos.")

if __name__ == "__main__":
    main()
