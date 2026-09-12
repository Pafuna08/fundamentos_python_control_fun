"""Calcula el area de un rectangulo mediante una funcion."""


def calcular_area(base, altura):
    """Devuelve el area de un rectangulo."""
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura no pueden ser negativas.")
    return base * altura


def main():
    """Solicita las medidas y muestra el area calculada."""
    base = float(input("Ingresa la base del rectangulo: "))
    altura = float(input("Ingresa la altura del rectangulo: "))
    area = calcular_area(base, altura)
    print(f"El area del rectangulo es: {area}")


if __name__ == "__main__":
    main()
def calcular_area(base, altura):
    """Devuelve el area de un rectangulo."""
    return base * altura


base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))
area = calcular_area(base, altura)

print(f"El area del rectangulo es: {area}")
