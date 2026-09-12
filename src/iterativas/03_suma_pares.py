"""Suma los puntos de actividades con numero par."""


def sumar_puntos_pares(inicio, fin):
    """Devuelve actividades pares y su puntaje total."""
    suma = 0
    pares = []
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            pares.append(numero)
            suma += numero
    return pares, suma


def main():
    """Muestra los puntos de las actividades pares del 2 al 10."""
    actividades, total = sumar_puntos_pares(2, 10)
    for actividad in actividades:
        print("Actividad par:", actividad)
    print("Puntos acumulados:", total)


if __name__ == "__main__":
    main()
