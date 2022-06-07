from functools import reduce


def pedirLista():
    return input('Introduce una lista de números separados por "," :_ ')


def cambiaStrAInt(lista):
    for i in range(0, len(lista)):
        lista[i] = int(lista[i])
    return lista


def main():
    lista = pedirLista().split(',')
    lista_int = cambiaStrAInt(lista)
    solo_impares = filter(lambda x: x % 2 != 0, lista_int)
    resultado = reduce(lambda a, b: a + b, solo_impares)
    print(resultado)


if __name__ == '__main__':
    main()
