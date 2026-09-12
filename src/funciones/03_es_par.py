"""Determina si el numero de una actividad es par."""


def es_actividad_par(numero_actividad):
    """Devuelve True si el numero de actividad es divisible entre dos."""
    return numero_actividad % 2 == 0


def main():
    """Solicita un numero de actividad y muestra su tipo."""
    numero_actividad = int(input("Numero de la actividad: "))
    if es_actividad_par(numero_actividad):
        print(f"La actividad {numero_actividad} tiene numero par.")
    else:
        print(f"La actividad {numero_actividad} tiene numero impar.")


if __name__ == "__main__":
    main()
