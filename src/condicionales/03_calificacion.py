"""Asigna un nivel de desempeno a una calificacion."""


def clasificar_calificacion(calificacion):
    """Devuelve el nivel para una calificacion entre 0 y 100."""
    if calificacion < 0 or calificacion > 100:
        return "La calificacion debe estar entre 0 y 100."
    elif calificacion >= 90:
        return "Desempeno superior."
    elif calificacion >= 70:
        return "Desempeno alto."
    elif calificacion >= 60:
        return "Desempeno basico."
    else:
        return "Desempeno bajo."


def main():
    """Solicita una calificacion y muestra el desempeno."""
    calificacion = float(input("Ingresa una calificacion entre 0 y 100: "))
    print(clasificar_calificacion(calificacion))


if __name__ == "__main__":
    main()
calificacion = float(input("Ingresa una calificacion entre 0 y 100: "))

if calificacion < 0 or calificacion > 100:
    print("La calificacion debe estar entre 0 y 100.")
elif calificacion >= 90:
    print("Desempeno superior.")
elif calificacion >= 70:
    print("Desempeno alto.")
elif calificacion >= 60:
    print("Desempeno basico.")
else:
    print("Desempeno bajo.")
