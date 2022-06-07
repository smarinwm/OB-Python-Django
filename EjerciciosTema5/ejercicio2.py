def isPrimo(numero):
    for i in range(2, numero):
        return False if numero % i == 0 else True


numero = 7
es_primo = "SI es primo." if isPrimo(numero) else "NO es primo."
print("El numero", numero, es_primo)