"""Practica un ciclo while para contar de forma ascendente."""


def contar_hasta(limite):
    """Devuelve los numeros desde 1 hasta el limite usando while."""
    numeros = []
    contador = 1
    while contador <= limite:
        numeros.append(contador)
        contador += 1
    return numeros


def main():
    """Muestra un conteo sencillo del 1 al 5."""
    for numero in contar_hasta(5):
        print("Contador:", numero)


if __name__ == "__main__":
    main()
contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador = contador + 1
