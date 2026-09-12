"""Clasifica una edad usando una estructura condicional."""


def clasificar_edad(edad):
    """Devuelve el mensaje correspondiente a la edad recibida."""
    if edad < 0:
        return "La edad no puede ser negativa."
    elif edad < 18:
        return "Eres menor de edad."
    else:
        return "Eres mayor de edad."


def main():
    """Solicita una edad y muestra su clasificacion."""
    edad = int(input("Ingresa tu edad: "))
    print(clasificar_edad(edad))


if __name__ == "__main__":
    main()
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("La edad no puede ser negativa.")
elif edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
