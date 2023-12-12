# El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.
# Por ejemplo, el conjunto potencia de {1,2,3} es:
# {∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
# Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s
# y retorne su «lista potencia» (la lista de todos sus subconjuntos):
# >>> conjunto_potencia({6, 1, 4})
# [set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]


def conjunto_potencia(conjunto_inicial: set) -> list:
    potencia = [set()]

    for i in conjunto_inicial:
        conjuntos = []
        for j in potencia:
            conjunto = set(j)
            conjunto.add(i)
            conjuntos.append(conjunto)
        potencia.extend(conjuntos)

    return potencia


def main():
    s = {6, 1, 4}
    potencia = conjunto_potencia(s)
    print(potencia)


if __name__ == "__main__":
    main()
