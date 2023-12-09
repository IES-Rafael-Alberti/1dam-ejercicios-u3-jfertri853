# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones
# múltiplos de 3, y muestre por pantalla la lista resultante.


from src.P3_1.Ejercicio1_6 import mostrar_lista


def eliminar_multiplos_de_3(abecedario: list):
    for pos in range(len(abecedario) - 1, -1, -1):
        if (pos + 1) % 3 == 0.0:
            del abecedario[pos]


def main():
    abecedario = ["a", "b", "c", "d", "e", "f", "g",
                  "h", "i", "j", "k", "l", "m", "n",
                  "ñ", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]

    eliminar_multiplos_de_3(abecedario)
    mostrar_lista(abecedario)


if __name__ == "__main__":
    main()
