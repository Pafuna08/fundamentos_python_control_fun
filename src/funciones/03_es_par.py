def es_par(numero):
    """Devuelve True cuando el numero es divisible entre dos."""
    return numero % 2 == 0


numero = int(input("Ingresa un numero entero: "))

if es_par(numero):
    print(f"{numero} es un numero par.")
else:
    print(f"{numero} es un numero impar.")
