def isBisiesto(year):
    es_bisiesto = (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)
    return True if es_bisiesto else False


year = 2022
es_bisiesto = "si es bisiesto." if isBisiesto(year) else "no es bisiesto."
print("El año", year, es_bisiesto)