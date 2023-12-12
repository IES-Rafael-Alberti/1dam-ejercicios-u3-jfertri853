# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas.
# El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.


def pedir_traducciones() -> str:
    print("Introduce las traducciones siguiendo este formato: "
          "<<palabra_español>>:<<traducción_inglés>>, <<palabra_español>>:<<traducción_inglés>>, ...")

    return input("--> ")


def introducir_frase() -> str:
    return input("Introduce una frase: ")


# ¿Cómo se podría pasar un iterable al constructor de un diccionario???
def crear_diccionario(cadena: str) -> dict:
    diccionario = {}
    cadena = cadena.replace(" ", "")
    lista_traducciones = cadena.split(",")
    for elemento in lista_traducciones:
        elemento = elemento.split(":")
        diccionario[elemento[0]] = elemento[1]

    return diccionario


def traducir_frase(frase: str, diccionario: dict):
    lista_frase = frase.split(" ")
    traducido = ""
    for palabra in lista_frase:
        if palabra in diccionario:
            traducido += diccionario.get(palabra) + " "
        elif palabra != "":
            traducido += palabra + " "

    print(traducido)


def main():
    try:
        diccionario = crear_diccionario(pedir_traducciones())
    except IndexError:
        print("Algo has hecho mal al crear el diccionario")
    except Exception:
        print("Algo ha ido mal pero no sé el qué")
    else:
        frase = introducir_frase()
        traducir_frase(frase, diccionario)


if __name__ == "__main__":
    main()
