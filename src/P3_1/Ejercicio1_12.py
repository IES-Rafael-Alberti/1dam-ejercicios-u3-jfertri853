# Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre
# por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas,
# representando cada vector fila en una lista.

# NO SE PUEDEN MULTIPLICAR MATRICES si el número de filas de una matriz es diferente al número de columnas de la otra
# Tendría más sentido si A = ((1, 2, 3), (4, 5, 6)) y B = ((-1, 0), (0, 1), (1, 1))
# Para poder realizar el ejercicio voy a hacer que las matrices sean introducidas por el usuario


from src.P3_1.Ejercicio1_3 import clean_screen


# Es una excepción personalizada, me apetecía buscar como se hacían
class MatricesNoOperablesError(Exception):
    def __init__(self, mensaje="Estas matrices no pueden realizar la operación"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def pedir_num() -> int:
    num = int(input(" -> "))
    return num


def multiplicacion(num1: int, num2: int) -> float:
    return num1 * num2


def pedir_filas_columnas() -> tuple:
    print("FILAS", end="")
    try:
        num_filas = pedir_num()
    except ValueError:
        print("***ERROR*** - El numero introducido no es válido, la matriz se creará con 1 FILA por defecto")
        num_filas = 1

    print("COLUMNAS", end="")
    try:
        num_columnas = pedir_num()
    except ValueError:
        print("***ERROR*** - El numero introducido no es válido, la matriz se creará con 1 COLUMNA por defecto")
        num_columnas = 1

    clean_screen()
    return num_filas, num_columnas


def crear_matriz(numfilascolumnas: tuple) -> list:
    matriz = []
    num_filas = numfilascolumnas[0]
    num_columnas = numfilascolumnas[1]
    for i in range(num_filas):
        print("Introduce los números de la FILA", i + 1)
        fila = tuple(pedir_num() for _ in range(num_columnas))
        matriz.append(fila)
        clean_screen()

    return matriz


def trasponer_matriz(matriz: list) -> list:
    matriz_traspuesta = []
    for i in range(len(matriz[0])):
        linea = tuple(matriz[j][i] for j in range(len(matriz)))
        matriz_traspuesta.append(linea)

    return matriz_traspuesta


# De qué otras formas se puede hacer esto sin usar 3 bucles anidados?
def multiplicar_matrices(matriz1: list, matriz2: list) -> list:
    if len(matriz1[0]) != len(matriz2):
        raise MatricesNoOperablesError("No puedes multiplicar matrices si la cantidad de filas de una es diferente a la"
                                       " cantidad de columnas de la otra")

    # Es más fácil multiplicar una matriz por la traspuesta de otra,
    # que multiplicar las líneas de una matriz por las columnas de otra
    # (o a lo mejor no y me lo he inventado)
    resultado = []
    matriz2_trasp = trasponer_matriz(matriz2)
    for p in range(len(matriz1)):
        linea = []
        for q in range(len(matriz2_trasp)):
            sumatorio = 0
            for r in range(len(matriz1[0])):
                sumatorio += multiplicacion(matriz1[p][r], matriz2_trasp[q][r])
            linea.append(sumatorio)
        linea = tuple(linea)
        resultado.append(linea)

    return resultado


def mostrar_matriz(matriz: list):
    for linea in matriz:
        for numero in linea:
            print(numero, end="   ")
        print()


def main():
    try:
        print("Crea la primera matriz")
        a = crear_matriz(pedir_filas_columnas())

        print("Crea la segunda matriz")
        b = crear_matriz(pedir_filas_columnas())
    except ValueError:
        print("***ERROR*** - Has introducido un valor inválido, no se pudo crear la matriz")
    else:

        try:
            resultado = multiplicar_matrices(a, b)
        except MatricesNoOperablesError as e:
            print("***ERROR*** - ", e)
        else:
            print("MATRIZ RESULTADO")
            mostrar_matriz(resultado)


# Este ejercicio se me ha hecho muy difícil por intentar que las matrices fuesen una lista con tuplas dentro.
if __name__ == "__main__":
    main()
