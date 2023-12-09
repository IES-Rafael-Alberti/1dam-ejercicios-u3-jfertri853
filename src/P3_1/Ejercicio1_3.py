# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
# Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por
# pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la
# lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


from src.P3_1.Ejercicio1_1 import convert_to_positive_integer
from src.P3_1.Ejercicio1_1 import create_subject_tuple
from os import system


def clean_screen():
    """Clear terminal text

    :return: None
    """
    system("cls")


def request_subject(counter: int) -> str:
    """Asks the user for an input which is supposed to be a school subject and returns it as a string

    :param counter: an integer which will be shown in the input text
    :return: a string which is entered by the user
    """
    return input("{}. ".format(counter + 1))


def enter_grade():
    """Asks for an input, turns it into float and returns it if the number is between 0 and 10

    :return: a grade
    """
    grade = float(input())
    if grade < 0 or grade > 10:
        raise ValueError
    else:
        return grade


def evaluate_single_subject(subject):
    print("Introduce la nota de {}: ".format(subject), end="")
    try:
        grade = enter_grade()
    except ValueError:
        grade = "No Evaluado"
    return grade


def evaluate_subjects(subjects: tuple) -> tuple:
    return tuple(evaluate_single_subject(i) for i in subjects)


def show_subject_grades(subjects, grades):
    for i in range(0, len(subjects)):
        print("En", subjects[i], "has sacado", grades[i])


def main():
    try:
        counter = convert_to_positive_integer(input("cuantas asignaturas tienes? "))
    except ValueError:
        counter = 0
    clean_screen()

    subjects = create_subject_tuple(counter)
    clean_screen()
    grades = evaluate_subjects(subjects)
    clean_screen()
    show_subject_grades(subjects, grades)


if __name__ == "__main__":
    main()
