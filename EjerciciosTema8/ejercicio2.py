import pickle


class Vehiculo:
    color = 'Verde'
    velocidad = 50

    def __init__(self, color, velocidad):
        self.color = color
        self.velocidad = velocidad


def main():
    v1 = Vehiculo('Azul', 120)
    print(v1.color, v1.velocidad)

    f = open("myvehiculo.bin", "wb")
    pickle.dump(v1, f)
    f.close()

    file = open("myvehiculo.bin", "rb")
    new_vehiculo = pickle.load(file)
    file.close()

    print(new_vehiculo.color, new_vehiculo.velocidad)


if __name__ == '__main__':
    main()
