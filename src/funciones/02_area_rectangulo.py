def calcular_area(base, altura):
    """Devuelve el area de un rectangulo."""
    return base * altura


base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))
area = calcular_area(base, altura)

print(f"El area del rectangulo es: {area}")
