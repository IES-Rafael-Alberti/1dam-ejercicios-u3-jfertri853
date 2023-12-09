# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
# Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una
# de las asignaturas de la lista.


from src.P3_1.Ejercicio1_1 import *


def formatted_subject_printing(subjects: tuple):
    """ Prints a formatted string for every element of a tuple of subjects

    :param subjects: a tuple containing subjects
    :return: None
    """
    for subject in subjects:
        print("Yo estudio", subject)


def main():
    try:
        counter = convert_to_positive_integer(input("cuantas asignaturas tienes? "))
    except ValueError:
        counter = 0

    subjects = create_subject_tuple(counter)
    formatted_subject_printing(subjects)


if __name__ == "__main__":
    main()
