# Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor
# el coste de la factura.
# El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
# Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
# Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento
# y la cantidad pendiente de cobro.


def pedir_cadena() -> str:
    return input(" -> ")


def mostrar_menu():
    print("Menu de opciones\n1. Añadir una factura\n2. Pagar una factura\n3. Salir\n")


def validar_codigo(codigo: str) -> bool:
    if len(codigo) < 3:
        return False
    elif len(codigo) > 7:
        return False
    return True


def validar_coste(coste: float) -> bool:
    if coste <= 0:
        return False
    return True


def add_factura(facturas: dict):
    print("Introduce el código de la factura")
    codigo = pedir_cadena()
    if not validar_codigo(codigo):
        raise NameError("se ha introducido un código inválido")

    print("Introduce el coste de la factura")
    coste = float(pedir_cadena())
    if not validar_coste(coste):
        raise NameError("el coste de la factura no puede ser cero ni negativo")

    facturas[codigo] = coste


def eliminar_factura(facturas: dict) -> float:
    print("Introduce el codigo de la factura que quieres eliminar")
    codigo = pedir_cadena()
    if codigo in facturas:
        return facturas.pop(codigo)
    else:
        print("no se ha encontrado la factura")


def calcular_cobros_pendientes(facturas: dict) -> float:
    total = 0
    for coste in facturas.values():
        total += coste

    return total


def mostrar_info(total: float, facturas: dict):
    pendiente = calcular_cobros_pendientes(facturas)
    print(f"COBRADO: {total:.2f}\nPENDIENTE: {pendiente:.2f}")


def menu(facturas: dict):
    total_cobrado = 0
    opcion = None

    while opcion != "3":
        mostrar_menu()
        print("Introduce una opción", end="")
        opcion = pedir_cadena()

        if opcion == "1":
            try:
                add_factura(facturas)
            except NameError as e:
                print("***ERROR*** -", e)
            except ValueError:
                print("***ERROR*** - has introducido un valor erróneo para el coste de la factura")
            finally:
                mostrar_info(total_cobrado, facturas)

        if opcion == "2":
            cobrado = eliminar_factura(facturas)
            if type(cobrado) is float:
                total_cobrado += cobrado
            mostrar_info(total_cobrado, facturas)

        if opcion == "3":
            mostrar_info(total_cobrado, facturas)
            print("\ncerrando el programa...")

        else:
            print("La opcion introducida no existe")


def main():
    libro_facturas = {"034AG": 19.75, "1KFC9": 32.0}
    menu(libro_facturas)


if __name__ == "__main__":
    main()
