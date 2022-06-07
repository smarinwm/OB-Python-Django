import operaciones.calculadora as calcula


def main():
    num_a = 2
    num_b = 0
    res_sumar = calcula.suma(num_a, num_b)
    res_restar = calcula.resta(num_a, num_b)
    res_multiplicar = calcula.multiplicacion(num_a, num_b)
    res_dividir = calcula.division(num_a, num_b)

    print(" la suma de", num_a, "+", num_b, "=", res_sumar)
    print(" la resta de", num_a, "-", num_b, "=", res_restar)
    print(" la multiplicación de", num_a, "*", num_b, "=", res_multiplicar)
    print(" la división de", num_a, "/", num_b, "=", res_dividir)


if __name__ == '__main__':
    main()
