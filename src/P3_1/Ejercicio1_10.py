# Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por
# pantalla el menor y el mayor de los precios.


def sacar_mayor(precios) -> int:
    mayor = precios[0]
    for precio in precios:
        if precio > mayor:
            mayor = precio
    return mayor


def sacar_menor(precios) -> int:
    menor = precios[0]
    for precio in precios:
        if precio < menor:
            menor = precio
    return menor


def imprimir_mayor_y_menor(precios):
    print("El precio menor es:", sacar_menor(precios))
    print("El precio mayor es:", sacar_mayor(precios))


def main():
    precios = (50, 75, 46, 22, 80, 65, 8)
    imprimir_mayor_y_menor(precios)


if __name__ == "__main__":
    main()
