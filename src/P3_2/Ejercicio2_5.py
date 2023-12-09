# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada
# asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de
# las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número
# total de créditos del curso.


def mostrar_creditos_por_separado(asignaturas: dict):
    for asignatura in asignaturas.keys():
        print(asignatura, "tiene", asignaturas.get(asignatura), "créditos")


def mostrar_creditos_totales(asignaturas: dict):
    creditos = 0
    for credito in asignaturas.values():
        creditos += credito

    print("Créditos totales =", creditos)
    

def main():
    asignaturas = {"matematicas": 6, "fisica": 4, "quimica": 5}
    mostrar_creditos_por_separado(asignaturas)
    mostrar_creditos_totales(asignaturas)


if __name__ == "__main__":
    main()
