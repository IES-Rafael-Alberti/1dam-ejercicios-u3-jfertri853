# Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
# hasta que el usuario decida terminar.
# Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
#
# Lista de la compra
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# …	…
# Total	Coste


def pedir_articulo(contador) -> str:
    return input(f"Introduce el nombre del articulo {contador}: ")


def pedir_precio(articulo) -> float:
    return abs(float(input(f"Introduce el precio de {articulo}: ")))


def actualizar_lista(lista_compra: dict):
    contador = 1
    articulo = None
    while articulo != "":
        articulo = pedir_articulo(contador).replace(" ", "")
        if articulo:
            try:
                precio = pedir_precio(articulo)
                lista_compra[articulo] = precio
                contador += 1
            except ValueError:
                print("has introducido un precio inválido")


def calcular_coste_total(lista_compra: dict) -> float:
    coste_total = 0
    for precio in lista_compra.values():
        coste_total += precio

    return coste_total


def imprimir_ticket(lista_compra: dict, coste_total: float):
    print("Lista de la compra")
    for articulo in lista_compra.keys():
        print(f"{articulo}           {lista_compra.get(articulo)}")
    print(f"\nTotal Coste: {coste_total:.2f}")


def main():
    lista_compra = {}
    actualizar_lista(lista_compra)

    if lista_compra:
        coste_final = calcular_coste_total(lista_compra)
        imprimir_ticket(lista_compra, coste_final)
    else:
        print("No has comprado nada")


if __name__ == "__main__":
    main()
