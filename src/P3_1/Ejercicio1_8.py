# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


# Por alguna razón este ejercicio está en los ejercicios de listas así que lo voy a hacer con listas
def pedir_palabra() -> list:
    palabra = input("Introduce una palabra: ")
    palabra = list(letra for letra in palabra)
    return palabra


def crear_lista_reversa(lista: list) -> list:
    lista_reversa = list(lista[pos] for pos in range(len(lista) - 1, -1, -1))
    return lista_reversa


def comprobar_lista_palindromo(lista: list, lista_reversa: list) -> bool:
    if lista == lista_reversa:
        return True
    else:
        return False


def main():
    palabra = pedir_palabra()
    palabra_reversa = crear_lista_reversa(palabra)

    if comprobar_lista_palindromo(palabra, palabra_reversa):
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    main()
