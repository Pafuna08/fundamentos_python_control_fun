"""Calcula puntos acumulados para varias sesiones de practica."""


def generar_plan_puntos(puntos_por_sesion, cantidad_sesiones=5):
    """Devuelve los puntos acumulados usando un ciclo for."""
    plan = []
    for sesion in range(1, cantidad_sesiones + 1):
        puntos = puntos_por_sesion * sesion
        plan.append(f"Sesion {sesion}: {puntos} puntos acumulados")
    return plan


def main():
    """Solicita puntos por sesion y muestra el plan de avance."""
    puntos = int(input("Puntos obtenidos por sesion: "))
    for registro in generar_plan_puntos(puntos):
        print(registro)


if __name__ == "__main__":
    main()
