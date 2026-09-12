"""Interpreta el resultado de una actividad del curso."""


def interpretar_resultado(porcentaje):
    """Devuelve el nivel de avance para un porcentaje entre 0 y 100."""
    if porcentaje < 0 or porcentaje > 100:
        return "El porcentaje debe estar entre 0 y 100."
    elif porcentaje >= 90:
        return "Avance sobresaliente"
    elif porcentaje >= 70:
        return "Avance esperado"
    elif porcentaje >= 60:
        return "Avance en construccion"
    else:
        return "Necesita refuerzo"


def main():
    """Solicita un porcentaje y muestra el nivel de avance."""
    porcentaje = float(input("Ingresa el porcentaje de avance (0 a 100): "))
    print(interpretar_resultado(porcentaje))


if __name__ == "__main__":
    main()
