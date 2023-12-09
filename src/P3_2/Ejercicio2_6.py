# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario.
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.


from os import system


def clean_screen():
    system("cls")


def pedir_cadena() -> str:
    return input("--> ")


def mostrar_contacto(contacto: dict):
    for clave in contacto.keys():
        print(f"{clave} = {contacto.get(clave)}")
    print("--------------------------------")


def actualizar_contacto(contacto: dict, clave: str):
    contacto[clave] = pedir_cadena()
    clean_screen()
    mostrar_contacto(contacto)


def main():
    contacto = {}

    print("Introduce el nombre del contacto", end=" ")
    actualizar_contacto(contacto, "nombre")

    print("Introduce el DNI del contacto", end=" ")
    actualizar_contacto(contacto, "DNI")

    print("Introduce el telefono del contacto", end=" ")
    actualizar_contacto(contacto, "telefono")

    print("Introduce el email del contacto", end=" ")
    actualizar_contacto(contacto, "email")


if __name__ == "__main__":
    main()
