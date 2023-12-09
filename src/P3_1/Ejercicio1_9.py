# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada
# vocal.


from src.P3_1.Ejercicio1_8 import pedir_palabra


VOCALES = ("a", "e", "i", "o", "u")


def mostrar_repeticion_de_vocal(palabra: list):
    for vocal in VOCALES:
        print(vocal, "se repite", palabra.count(vocal), "veces")


def main():
    palabra = pedir_palabra()
    mostrar_repeticion_de_vocal(palabra)


if __name__ == "__main__":
    main()
