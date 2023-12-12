# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato
# dd de <mes> de aaaa donde <mes> es el nombre del mes.


MESES = {"01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo", "06": "Junio", "07": "Julio",
         "08": "Agosto", "09": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"}


def pedir_fecha() -> str:
    return input("Introduce la fecha en formato dd/mm/aaaa: ")


def validar_dia(day: str, month: str) -> bool:
    meses30 = ["Abril", "Junio", "Septiembre", "Noviembre"]

    if len(day) != 2:
        return False

    if day.isnumeric():
        day = int(day)
        if month in meses30:
            if 0 <= day <= 30:
                return True
        elif month == "Febrero":
            if 0 <= day <= 28:
                return True
        else:
            if 0 <= day <= 31:
                return True

    return False


def validar_mes(month: str) -> bool:
    if len(month) != 2:
        return False

    if month.isnumeric():
        if 1 <= int(month) <= 12:
            return True
    return False


def validar_year(year: str) -> bool:
    if len(year) == 4:
        return True
    else:
        return False


def validar_fecha(fecha: str) -> bool:
    fecha = fecha.split("/")
    if len(fecha) == 3:
        day = fecha[0]
        month = fecha[1]
        year = fecha[2]
        if validar_dia(day, MESES.get(month)) and validar_mes(month) and validar_year(year):
            return True
    return False


def mostrar_fecha(fecha):
    day = fecha[0]
    month = fecha[1]
    year = fecha[2]
    print(f"{day} de {MESES.get(month)} de {year}")


def main():
    fecha = pedir_fecha()
    if validar_fecha(fecha):
        fecha = fecha.split("/")
        mostrar_fecha(fecha)
    else:
        print("Algo no ha ido bien")


if __name__ == "__main__":
    main()
