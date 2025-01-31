class Cine:
    maximo_boletos = 7
    precio_boletos = 12

    def __init__(self):
        self.compradores = []

    def boletos_compradores(self, nombre, cantidad_boletos):
        while cantidad_boletos > Cine.maximo_boletos:
            try:
                decision = int(input("No puedes comprar más de 7 boletos, quieres cambiar el numero de boletos o el numero de compradores? 0 = Cambiar boletos / 1 = Cambiar compradores: "))
            except ValueError:
                print("Ingresa solo letras")
                continue

            if decision == 0:
                try:
                    cantidad_boletos = int(input("Cuantos boletos quieres comprar?: "))
                except ValueError:
                    print("Ingresa solo numeros")
                    continue
            elif decision == 1:
                try:
                    cantidad_compradores = int(input("Cuantas personas van a comprar boletos?: "))
                except ValueError:
                    print("Ingresa solo numeros")
                    continue

                for i in range(cantidad_compradores):
                    nombre_comprador = input(f"Ingresa el nombre del comprador #{i + 1}: ")
                    while True:
                        try:
                            boletos_comprador = int(input(f"Cuantos boletos va a comprar {nombre_comprador}?: "))
                            if boletos_comprador > Cine.maximo_boletos:
                                print("Cada persona no puede comprar más de 7 boletos")
                                continue
                            break
                        except ValueError:
                            print("Ingresa solo numeros")

                    self.compradores.append((nombre_comprador, boletos_comprador))
                return True
            else:
                print("Esa opcion no esta disponible")

        self.compradores.append((nombre, cantidad_boletos))
        return True

    def total(self):
        total_precio = 0
        detalles_compra = []

        for nombre, cantidad_boletos in self.compradores:
            if cantidad_boletos > 5:
                total = (cantidad_boletos * Cine.precio_boletos) * 0.85
            elif cantidad_boletos >= 3:
                total = (cantidad_boletos * Cine.precio_boletos) * 0.90
            else:
                total = (cantidad_boletos * Cine.precio_boletos)

            detalles_compra.append(f"{nombre} compro {cantidad_boletos} boletos, el total es de {total:.2f}")
            total_precio += total

        return detalles_compra, total_precio


def main():
    cine = Cine()

    while True:
        nombre = input("Cual es tu nombre?: ")
        while True:
            try:
                cantidad_boletos = int(input("Cuantos boletos quieres comprar?: "))
                break
            except ValueError:
                print("Ingresa solo numeros")

        if not cine.boletos_compradores(nombre, cantidad_boletos):
            continue

        detalles_finales, total_precio = cine.total()

        print("---------------------")
        print(f"El total de la compra es de: {total_precio:.2f}")

        while True:
            try:
                pago = int(input("\nDesea pagar con efectivo o tarjeta CINECO? Al pagar con tarjeta obtendrá un descuento del 10% 0 = Efectivo / 1 = Tarjeta: "))
                if pago == 1:
                    descuento_final = total_precio * 0.10
                    total_precio -= descuento_final
                    print(f"El total es de {total_precio:.2f}")
                    detalles_finales.append(f"Total: {total_precio:.2f}")
                elif pago == 0:
                    print(f"Total {total_precio:.2f}")
                    detalles_finales.append(f"Total {total_precio:.2f}")
                else:
                    print("Esa opción no esta disponible")
                    continue
                break
            except ValueError:
                print("Ingresa solo numeros")

        while True:
            try:
                continuar = int(input("\nDesea finalizar la compra o volver a comprar? 0 = Finalizar / 1 = Volver: "))
                if continuar == 0:
                    print("\nTicket")
                    print("\n".join(detalles_finales))

                    with open('ticket_compra.txt', 'w') as archivo:
                        archivo.write("\n".join(detalles_finales))
                    return
                elif continuar == 1:
                    print("Volver a comprar\n")
                    break
                else:
                    print("Esa opcion no esta disponible")
            except ValueError:
                print("Ingresa solo numeros")


if __name__ == "__main__":
    main()
