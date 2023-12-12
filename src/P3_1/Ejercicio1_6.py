# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


def pedir_nota(asignatura) -> float:
    nota = float(input("Introduce la nota de " + str(asignatura) + ": "))
    return nota


def validar_nota(nota: float) -> bool:
    if nota < 0 or nota > 10:
        return False
    else:
        return True


def eliminar_asignatura(lista: list, posicion: int):
    del lista[posicion]


def poner_notas(asignaturas: list) -> list:
    notas = []
    for pos in range(len(asignaturas)):
        nota = pedir_nota(asignaturas[pos])
        if validar_nota(nota):
            notas.append(nota)
        else:
            raise ValueError("Alguna de las notas introducidas no son válidas")
    return notas


def mostrar_lista(asignaturas: list):
    for pos in range(len(asignaturas)):
        if pos != len(asignaturas) - 1:
            print(asignaturas[pos] + ",", end=" ")
        else:
            print(asignaturas[pos])


def eliminar_aprobadas(asignaturas: list, notas: list):
    for pos in range(len(asignaturas) - 1, -1, -1):
        if notas[pos] >= 5:
            eliminar_asignatura(asignaturas, pos)


def main():
    asignaturas = ["Matemáticas", "Química", "Historia", "Lengua"]
    notas = []

    notas_evaluadas = False
    while not notas_evaluadas:
        try:
            notas = poner_notas(asignaturas)
        except ValueError as e:
            print("***ERROR*** - ", e)
        else:
            notas_evaluadas = True

    eliminar_aprobadas(asignaturas, notas)

    print("Tienes que recuperar:")
    mostrar_lista(asignaturas)


if __name__ == "__main__":
    main()
