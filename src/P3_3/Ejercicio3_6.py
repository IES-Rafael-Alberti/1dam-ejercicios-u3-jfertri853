# Dado el conjunto de letras:
#
# vocales = {'a', 'e', 'i', 'o', 'u'}
#
# Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
#
# Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto
# vocales como en el conjunto consonantes.


def main():
    alfabeto = {"a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                "r", "s", "t", "u", "v", "w", "x", "y", "z"}

    vocales = {"a", "e", "i", "o", "u"}

    consonantes = alfabeto - vocales
    print(consonantes, "\n")

    letras_comunes = consonantes & vocales
    print(letras_comunes)


if __name__ == "__main__":
    main()
