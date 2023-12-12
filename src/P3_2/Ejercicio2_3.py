# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio
# de ese número de kilos de fruta.
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
#
# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70


from src.P3_2.Ejercicio2_2 import pedir_cadena


FRUTA = {"platano": 1.35, "manzana": 0.8, "pera": 0.85, "naranja": 0.7}


def calcular_precio(fruta: str, kilos: float):
    if fruta in FRUTA:
        return FRUTA.get(fruta) * kilos
    else:
        return FRUTA.get(fruta, f"No tenemos {fruta} en esta fruteria")


def main():
    print("¿Qué fruta quieres?", end="")
    fruta = pedir_cadena().lower()

    print(f"¿Cuántos kilos de {fruta} quieres?", end="")
    try:
        kilos = float(pedir_cadena())
    except ValueError:
        print(f"***ERROR*** - eso no es un numero")
    else:
        precio = calcular_precio(fruta, kilos)
        if type(precio) is float:
            print(f"{kilos:.2f}kg de {fruta} te saldrán a {precio:.2f}€")
        else:
            print(precio)


if __name__ == "__main__":
    main()
