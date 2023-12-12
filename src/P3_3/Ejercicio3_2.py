# Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela,
# finalizando cuando se introduzca “x”.
# A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.
#
# Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
# Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
# Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
# Mostrar si todos los nombres de primaria están incluidos en secundaria.


def crear_nombres() -> set:
    nombres = []

    nombre = None
    while nombre != "x" and nombre != "X":
        nombre = input("--> ")
        if nombre != "x" and nombre != "X":
            nombres.append(nombre)

    return set(nombres)


def mostrar_nombres(nombres: set):
    print()

    nombres = tuple(nombres)
    for i in range(len(nombres)):
        if i != len(nombres) - 1:
            print(nombres[i], end=", ")
        else:
            print(nombres[i], "\n")


def main():
    print("Introduce los nombres de los alumnos de primaria")
    primaria = crear_nombres()

    print("\nIntroduce los nombres de los alumnos de secundaria")
    secundaria = crear_nombres()

    print("Todos los nombres:", end=" ")
    todos = primaria | secundaria
    mostrar_nombres(todos)

    print("Nombres repetidos en ambos cursos:", end=" ")
    comunes = primaria & secundaria
    mostrar_nombres(comunes)

    print("Nombres que solo están en primaria:", end=" ")
    solo_primaria = primaria - secundaria
    mostrar_nombres(solo_primaria)

    print("Están todos los nombres de primaria en secundaria:", end=" ")
    inclusion = primaria <= secundaria
    print(inclusion)


if __name__ == "__main__":
    main()
