import time


def main():
    def isHoraSalida(hora):
        return True if hora >= hora_salida else False

    def queFaltaParaSalir(hora, minutos):
        faltan_horas = str(hora_salida - hora)
        faltan_minutos = str(60 - minutos)
        cuanto_falta = 'Faltan ' + faltan_horas + ' horas y ' + faltan_minutos + ' minutos.'
        return cuanto_falta

    def mirarHoraMinutos():
        localtime = time.localtime()
        hora = localtime[3]
        minutos = localtime[4]
        return hora, minutos

    hora_salida = 19
    que_hora_es = mirarHoraMinutos()
    hora_actual = que_hora_es[0]
    minutos_actuales = que_hora_es[1]

    es_hora_de_salir = "Ya es la hora de Salir." if isHoraSalida(hora_actual) else queFaltaParaSalir(hora_actual, minutos_actuales)

    print(es_hora_de_salir)


if __name__ == '__main__':
    main()
