"""Personaliza el saludo de bienvenida al espacio de estudio."""


def preparar_bienvenida(nombre, curso="Fundamentos de Python"):
    """Devuelve un saludo con el nombre del aprendiz y el curso."""
    return f"Hola, {nombre}. Bienvenido a {curso}."


def main():
    """Solicita el nombre del aprendiz y muestra la bienvenida."""
    nombre_aprendiz = input("Ingresa tu nombre: ")
    print(preparar_bienvenida(nombre_aprendiz))


if __name__ == "__main__":
    main()
