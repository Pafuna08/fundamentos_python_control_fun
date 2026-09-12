"""Determina si un numero entero es par usando una funcion."""


def es_par(numero):
    """Devuelve True cuando el numero es divisible entre dos."""
    return numero % 2 == 0


def main():
    """Solicita un entero y muestra si es par o impar."""
    numero = int(input("Ingresa un numero entero: "))
    if es_par(numero):
        print(f"{numero} es un numero par.")
    else:
        print(f"{numero} es un numero impar.")


if __name__ == "__main__":
    main()
def es_par(numero):
    """Devuelve True cuando el numero es divisible entre dos."""
    return numero % 2 == 0


numero = int(input("Ingresa un numero entero: "))

if es_par(numero):
    print(f"{numero} es un numero par.")
else:
    print(f"{numero} es un numero impar.")
