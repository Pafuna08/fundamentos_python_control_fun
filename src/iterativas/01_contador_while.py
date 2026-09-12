"""Registra sesiones de estudio hasta completar una meta."""


def registrar_sesiones(meta):
    """Devuelve los numeros de sesion hasta la meta usando while."""
    sesiones = []
    sesion_actual = 1
    while sesion_actual <= meta:
        sesiones.append(sesion_actual)
        sesion_actual += 1
    return sesiones


def main():
    """Muestra las cinco sesiones planeadas para la actividad."""
    for sesion in registrar_sesiones(5):
        print("Sesion de estudio:", sesion)


if __name__ == "__main__":
    main()
