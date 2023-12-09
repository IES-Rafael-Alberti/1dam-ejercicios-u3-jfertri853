# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su
# producto escalar.


def multiplicacion(num1: float, num2: float) -> float:
    return num1 * num2


def calcular_sumatorio(vector: tuple) -> float:
    sumatorio = 0
    for num in vector:
        sumatorio += num
    return sumatorio


def mostrar_resultado(vector1: tuple, vector2: tuple, resultado: float):
    print("El producto escalar de", vector1, "y", vector2, "es", resultado)


def producto_escalar_2_vectores(vector1: tuple, vector2: tuple) -> float:
    if len(vector1) == len(vector2):
        vector_producto_escalar = tuple(multiplicacion(vector1[pos], vector2[pos]) for pos in range(len(vector1)))
    else:
        raise ValueError("No se puede calcular el producto escalar de 2 vectores de diferentes dimensiones")

    producto_escalar = calcular_sumatorio(vector_producto_escalar)

    return producto_escalar


def main():
    vector1 = (1, 2, 3)
    vector2 = (-1, 0, 2)
    try:
        resultado = producto_escalar_2_vectores(vector1, vector2)
    except ValueError as e:
        print("***ERROR*** - ", e)
    else:
        mostrar_resultado(vector1, vector2, resultado)


if __name__ == "__main__":
    main()
