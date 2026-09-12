"""Calcula el espacio disponible en una mesa de estudio."""


def calcular_area_mesa(largo, ancho):
    """Devuelve el area de una mesa rectangular en centimetros cuadrados."""
    if largo <= 0 or ancho <= 0:
        raise ValueError("El largo y el ancho deben ser positivos.")
    return largo * ancho


def main():
    """Solicita las medidas de la mesa y muestra el area."""
    largo = float(input("Largo de la mesa en centimetros: "))
    ancho = float(input("Ancho de la mesa en centimetros: "))
    area = calcular_area_mesa(largo, ancho)
    print(f"El espacio de estudio disponible es: {area} cm2")


if __name__ == "__main__":
    main()
