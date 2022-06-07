def main():
    def crearFichero():
        f = open('myfichero.txt', "w")
        f.close()

    def escribirFichero(texto):
        file = open('myfichero.txt', 'a')
        for i in range(1, 5):
            file.write(f'soy la linea {i} de {texto} \n')
        file.close()

    crearFichero()
    escribirFichero('banana')


if __name__ == '__main__':
    main()
