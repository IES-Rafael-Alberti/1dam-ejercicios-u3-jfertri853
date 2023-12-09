# Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente.
# El programa debe preguntar al usuario por una opción del siguiente menú:
# (1) Añadir cliente,
# (2) Eliminar cliente,
# (3) Mostrar cliente,
# (4) Listar todos los clientes,
# (5) Listar clientes preferentes,
# (6) Terminar.
# En función de la opción elegida el programa tendrá que hacer lo siguiente:
#
# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# Terminar el programa.


OPCIONES_MENU = ("ADD CLIENT", "DELETE CLIENT", "SHOW CLIENT", "SHOW ALL CLIENTS", "SHOW PREFERRED CLIENTS", "END")


def mostrar_menu():
    print("Menu de opciones\n1. Añadir cliente\n2. Eliminar cliente"
          "\n3. Mostrar cliente\n4. Listar todos los clientes"
          "\n5. Listar clientes preferentes\n6. Terminar\n")


def elegir_opcion():
    opcion = input("Elige una opción: ")
    match opcion:
        case "1":
            opcion = OPCIONES_MENU[0]
        case "2":
            opcion = OPCIONES_MENU[1]
        case "3":
            opcion = OPCIONES_MENU[2]
        case "4":
            opcion = OPCIONES_MENU[3]
        case "5":
            opcion = OPCIONES_MENU[4]
        case "6":
            opcion = OPCIONES_MENU[5]

    if opcion not in OPCIONES_MENU:
        raise ValueError("opcion inexistente")
    else:
        return opcion


def add_cliente(clientes: dict):
    dni = input("Introduce el dni: ")
    nombre = input("Introduce el nombre: ")
    direccion = input("Introduce la dirección: ")
    telefono = input("Introduce el número de teléfono: ")
    correo = input("Introduce el email: ")

    preferencia = None
    while preferencia != "y" and preferencia != "n":
        preferencia = input("es preferente? (y/n)").lower()

    if preferencia == "y":
        preferencia = True
    else:
        preferencia = False

    cliente = {dni: {"nombre": nombre, "direccion": direccion, "telefono": telefono,
               "correo": correo, "preferencia": preferencia}}

    clientes.update(cliente)


def pedir_dni() -> str:
    return input("Introduce el DNI: ")


def delete_client(clientes: dict, dni: str):
    if dni in clientes:
        del clientes[dni]
    else:
        print("No se pudo eliminar el cliente..")


def show_client(clientes: dict, dni: str):
    if dni in clientes:
        print("DNI:", dni, "\nNombre:", clientes[dni]["nombre"], "\nDirección:", clientes[dni]["direccion"],
              "\nTeléfono:", clientes[dni]["telefono"], "\nCorreo", clientes[dni]["correo"])

        if clientes[dni]["preferencia"]:
            print("Cliente preferente")
        else:
            print("Cliente NO preferente")
        print("----------------------------\n")


def show_all(clientes: dict):
    for clave in clientes.keys():
        show_client(clientes, clave)


def show_preferred(clientes: dict):
    for clave in clientes.keys():
        if clientes[clave]["preferencia"]:
            show_client(clientes, clave)


# Las funciones de este ejercicio se pueden dividir más, pero tardaría mucho más tiempo
def main():
    clientes = {"12345678A": {"nombre": "Pepe Pepsi", "direccion": "Avd Caballo 12",
                              "telefono": "999112233", "correo": "pepepsi@jmail.es",
                              "preferencia": False}}

    opcion = None
    while opcion != "END":
        mostrar_menu()
        try:
            opcion = elegir_opcion()
        except ValueError as e:
            print("***ERROR*** - ", e)
        else:
            if opcion == "ADD CLIENT":
                add_cliente(clientes)
            elif opcion == "DELETE CLIENT":
                nif = pedir_dni()
                delete_client(clientes, nif)
            elif opcion == "SHOW CLIENT":
                nif = pedir_dni()
                show_client(clientes, nif)
            elif opcion == "SHOW ALL CLIENTS":
                show_all(clientes)
            else:
                show_preferred(clientes)


if __name__ == "__main__":
    main()
