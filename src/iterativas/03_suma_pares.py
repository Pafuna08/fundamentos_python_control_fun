"""Suma los numeros pares de un rango usando for."""


def sumar_pares(inicio, fin):
    """Suma los valores pares incluidos entre inicio y fin."""
    suma = 0
    pares = []
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            pares.append(numero)
            suma += numero
    return pares, suma


def main():
    """Muestra los pares del 2 al 10 y su suma."""
    pares, suma = sumar_pares(2, 10)
    for numero in pares:
        print("Numero par:", numero)
    print("Suma de pares:", suma)


if __name__ == "__main__":
    main()
suma = 0

for numero in range(2, 11, 2):
    suma = suma + numero
    print("Numero par:", numero)

print("Suma de pares:", suma)
