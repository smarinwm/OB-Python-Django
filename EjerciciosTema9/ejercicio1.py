def pedirPaises():
    return input('Paises separados por "," :_ ')


def main():
    paises = pedirPaises().split(',')
    paises = set(paises)
    paises = sorted(paises)

    print(paises)

    res = ''
    for it in paises:
        res += f'{it},'
    print(res)


if __name__ == '__main__':
    main()
