"""Compara el tiempo dedicado a dos sesiones de estudio."""


def comparar_sesiones(minutos_sesion_1, minutos_sesion_2):
    """Indica cual sesion tuvo mayor duracion o si empataron."""
    if minutos_sesion_1 > minutos_sesion_2:
        return f"La sesion 1 tuvo mas tiempo: {minutos_sesion_1} minutos."
    elif minutos_sesion_2 > minutos_sesion_1:
        return f"La sesion 2 tuvo mas tiempo: {minutos_sesion_2} minutos."
    else:
        return "Las dos sesiones tuvieron la misma duracion."


def main():
    """Solicita dos duraciones y muestra cual sesion fue mas larga."""
    sesion_1 = float(input("Minutos de la sesion 1: "))
    sesion_2 = float(input("Minutos de la sesion 2: "))
    print(comparar_sesiones(sesion_1, sesion_2))


if __name__ == "__main__":
    main()
