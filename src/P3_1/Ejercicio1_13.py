# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y
# muestre por pantalla su media y desviación típica.


def pedir_lista_nums() -> tuple:
    return tuple(input("Introduce numeros separados por coma: ").replace(" ", "").split(","))


def convertir_a_float(nums: tuple) -> tuple:
    return tuple(float(num) for num in nums)


def sumatorio_nums(nums: tuple) -> float:
    sumatorio = 0
    for num in nums:
        sumatorio += num

    return sumatorio


def calcular_media(nums: tuple) -> float:
    return sumatorio_nums(nums) / len(nums)


def distancia_entre_numeros(num: float, media: float) -> float:
    return abs(media - num)


def elevar_al_cuadrado(num: float) -> float:
    return num ** 2


def raiz_cuadrada(num: float) -> float:
    return num ** 0.5


def calcular_desviacion_tipica(nums, media):
    distancias = tuple(elevar_al_cuadrado(distancia_entre_numeros(num, media)) for num in nums)
    sum_distancias = sumatorio_nums(distancias)
    desviacion = raiz_cuadrada(sum_distancias / len(distancias))
    return desviacion


def mostrar_info(nums: tuple, media: float, desviacion: float):
    cadena_nums = ", ".join([str(i) for i in nums])
    print("Lista --> " + cadena_nums)
    print("MEDIA = {:.2f}".format(media))
    print("DESVIACIÓN TIPÍCA = {:.2f}".format(desviacion))


def main():
    nums = ()
    try:
        nums = convertir_a_float(pedir_lista_nums())
    except ValueError:
        print("***ERROR*** - no se pudo crear la lista de numeros")

    if nums:
        media = calcular_media(nums)
        desviacion_tipica = calcular_desviacion_tipica(nums, media)

        mostrar_info(nums, media, desviacion_tipica)


if __name__ == "__main__":
    main()
