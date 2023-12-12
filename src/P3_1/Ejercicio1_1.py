# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
# Lengua) en una lista y la muestre por pantalla.

# Pycharm ha cambiado la forma en la que genera automáticamente el formato de la documentación de funciones


def convert_to_positive_integer(value: str) -> int:
    """ Converts a string to an integer or raises an exception

    :param value: the string which is going to be converted
    :return: value: same value but as an integer

    """
    if not value.isnumeric():
        raise ValueError
    else:
        return int(value)


def request_subject(counter):
    """ Returns user's input

    :param counter: used to show which subject position is the program asking for
    :return: user's input
    """
    return input("{}. ".format(counter + 1))


def create_subject_tuple(counter):
    """ Asks the user to enter the same number of subjects that the counter has

    :return: subjects: a tuple containing a string of each subject introduced by the user
    """
    if counter > 0:
        print("Introduce las asignaturas: ")
        subjects = tuple(request_subject(i) for i in range(counter))
        return subjects
    else:
        return ()


def main():
    try:
        counter = convert_to_positive_integer(input("cuantas asignaturas tienes? "))
    except ValueError:
        counter = 0
    subjects = create_subject_tuple(counter)
    print(subjects)


if __name__ == "__main__":
    main()
