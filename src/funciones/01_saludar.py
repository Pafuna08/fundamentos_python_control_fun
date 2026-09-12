"""Define y utiliza una funcion con un parametro de texto."""


def saludar(nombre):
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}. Bienvenido a Python."


def main():
    """Solicita un nombre y muestra el saludo."""
    nombre_aprendiz = input("Ingresa tu nombre: ")
    print(saludar(nombre_aprendiz))


if __name__ == "__main__":
    main()
def saludar(nombre):
    """Muestra un saludo personalizado."""
    print(f"Hola, {nombre}. Bienvenido a Python.")


nombre_aprendiz = input("Ingresa tu nombre: ")
saludar(nombre_aprendiz)
