# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono
# es <teléfono>.


def pedir_cadena() -> str:
    cadena = input(" --> ")
    return cadena


def validar_telefono(telefono: str) -> bool:
    if len(telefono) == 9 and telefono.isnumeric():
        return True
    else:
        return False


def convertir_a_entero(edad: str) -> int:
    edad = int(edad)
    return edad


def crear_contacto(nombre: str, edad: int, direccion: str, telefono: str) -> dict:
    contacto = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
    return contacto


def mostrar_contacto(contacto: dict):
    print("{} tiene {} años, vive en {} y su número de teléfono es {}".format(contacto.get("nombre"),
                                                                              contacto.get("edad"),
                                                                              contacto.get("direccion"),
                                                                              contacto.get("telefono")))


def main():
    print("NOMBRE", end="")
    nombre = pedir_cadena()

    edad_correcta = False
    while not edad_correcta:
        try:
            print("EDAD", end="")
            edad = convertir_a_entero(pedir_cadena())
        except ValueError:
            print("***ERROR*** - eso no es un numero")
        else:
            edad_correcta = True

    print("DIRECCIÓN", end="")
    direccion = pedir_cadena()

    telefono_correcto = False
    while not telefono_correcto:
        print("TELÉFONO", end="")
        telefono = pedir_cadena()
        telefono_correcto = validar_telefono(telefono)
        if not telefono_correcto:
            print("El telefono que has introducido no es válido")

    contacto = crear_contacto(nombre, edad, direccion, telefono)
    mostrar_contacto(contacto)


if __name__ == "__main__":
    main()
