# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al
# usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.


DIVISAS = {"Euro": "€", "Dollar": "$", "Yen": "¥"}


def pedir_cadena() -> str:
    nombre_divisa = input("Introduce el nombre de la divisa: ")
    return nombre_divisa


def buscar_divisa(nombre_divisa: str) -> str:
    return DIVISAS.get(nombre_divisa, f"La divisa {nombre_divisa} no existe")


def main():
    nombre_divisa = pedir_cadena()
    simbolo = buscar_divisa(nombre_divisa)
    if nombre_divisa in DIVISAS:
        print(nombre_divisa, "->", simbolo)
    else:
        print(simbolo)


if __name__ == "__main__":
    main()
