# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso
# separados por comas.


def mostrar_lista_inversa(lista: list):
    for posicion in range(len(lista) - 1, -1, -1):
        if posicion != 0:
            print(str(lista[posicion]) + ", ", end="")
        else:
            print(str(lista[posicion]))


def main():
    mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mostrar_lista_inversa(mi_lista)


if __name__ == "__main__":
    main()
