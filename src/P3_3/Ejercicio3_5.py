# Dado el conjunto de números enteros:
#
# numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Crea un conjunto pares que contenga los números pares del conjunto numeros.

# Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
# Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado
# pares_y_multiplos_de_tres.


def pares(conjunto: set) -> set:
    lista_par = []
    for i in conjunto:
        if i % 2 == 0:
            lista_par.append(i)
    return set(lista_par)


def multiplos_tres(conjunto: set) -> set:
    lista_multip_tres = []
    for i in conjunto:
        if i % 3 == 0:
            lista_multip_tres.append(i)
    return set(lista_multip_tres)


def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    numeros_par = pares(numeros)

    numeros_multip_tres = multiplos_tres(numeros)

    pares_y_multiplos_de_tres = numeros_par | numeros_multip_tres

    print(numeros, "\n")
    print(numeros_par, "\n")
    print(numeros_multip_tres, "\n")
    print(pares_y_multiplos_de_tres)


if __name__ == "__main__":
    main()
