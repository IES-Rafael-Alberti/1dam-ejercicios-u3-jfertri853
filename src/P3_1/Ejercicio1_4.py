# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.


from os import system


def clean_screen():
    system("cls")


def introducir_numero_loteria(boleto: list) -> int:
    num = int(input("Introduce un numero de loteria(1-49): "))
    if num < 1:
        raise ValueError("El numero de loteria no puede ser menor que 1")
    elif num > 49:
        raise ValueError("El numero de loteria no puede ser mayor que 49")
    elif num in boleto:
        raise ValueError("Un mismo boleto no puede tener numeros repetidos")
    return num


def introducir_numero_reintegro() -> int:
    num = int(input("Introduce el numero de reintegro(0-9): "))
    if num < 0:
        raise ValueError("El numero de reintegro no puede ser menos que 0")
    elif num > 9:
        raise ValueError("El numero de reintegro no puede ser mayor que 9")
    return num


def crear_boleto() -> list:
    boleto = []
    contador = 0
    while contador < 6:
        try:
            boleto.append(introducir_numero_loteria(boleto))
        except ValueError as e:
            print("***ERROR*** - ", e)
        else:
            contador += 1

    reintegro = False
    while not reintegro:
        try:
            boleto.append(introducir_numero_reintegro())
        except ValueError as e:
            print("***ERROR*** - ", e)
        else:
            reintegro = True

    return boleto


def ordenar_boleto(boleto: list) -> list:
    total = len(boleto) - 2
    intercambios = None
    contador = 0

    while contador != len(boleto) and intercambios != 0:
        intercambios = 0

        for i in range(0, total):
            if boleto[i] > boleto[i + 1]:
                mayor = boleto[i]
                boleto[i] = boleto[i + 1]
                boleto[i + 1] = mayor
                intercambios += 1

        total -= 1
        contador += 1
    return boleto


def mostrar_boleto(boleto: list):
    clean_screen()
    print("Tu boleto:")
    for posicion in range(len(boleto) - 1):
        if posicion < 5:
            print(boleto[posicion], "-", end=" ")
        else:
            print(boleto[posicion])
    print("Reintegro:", boleto[6])


def main():
    boleto_ganador = crear_boleto()
    ordenar_boleto(boleto_ganador)
    mostrar_boleto(boleto_ganador)


if __name__ == "__main__":
    main()
