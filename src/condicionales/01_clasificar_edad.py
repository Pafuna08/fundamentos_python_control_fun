"""Clasifica la etapa de un participante de la actividad."""


def clasificar_participante(edad):
    """Devuelve una categoria de participacion segun la edad."""
    if edad < 0:
        return "Edad invalida"
    elif edad < 18:
        return "Participante menor de edad"
    else:
        return "Participante mayor de edad"


def main():
    """Solicita la edad del participante y muestra su categoria."""
    edad = int(input("Ingresa la edad del participante: "))
    print(clasificar_participante(edad))


if __name__ == "__main__":
    main()
