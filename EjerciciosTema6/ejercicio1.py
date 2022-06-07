class Vehiculo:
    color = "blanco"
    ruedas = 4
    puertas = 4


class Coche(Vehiculo):
    velocidad = 90
    cilindrada = 1200

    def cambiarColor(self, color):
        self.color = color

    def cambiarRuedas(self, ruedas):
        self.ruedas = ruedas

    def cambiarPuertas(self, puertas):
        self.puertas = puertas

    def cambiarVelocidad(self, velocidad):
        self.velocidad = velocidad

    def cambiarCilindrada(self, cilindrada):
        self.cilindrada = cilindrada


coche = Coche()
print(coche.color, coche.ruedas, coche.puertas, coche.velocidad, coche.cilindrada)
coche.cambiarColor("Verde")
coche.cambiarRuedas(6)
coche.cambiarPuertas(3)
coche.cambiarVelocidad(60)
coche.cambiarCilindrada(2500)
print(coche.color, coche.ruedas, coche.puertas, coche.velocidad, coche.cilindrada)

