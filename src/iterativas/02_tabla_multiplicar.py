"""Genera una tabla de multiplicar con un ciclo for."""


def generar_tabla(numero):
    """Devuelve las operaciones del 1 al 10 para un numero."""
    tabla = []
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        tabla.append(f"{numero} x {multiplicador} = {resultado}")
    return tabla


def main():
    """Solicita un numero y muestra su tabla de multiplicar."""
    numero = int(input("Ingresa un numero para ver su tabla: "))
    for operacion in generar_tabla(numero):
        print(operacion)


if __name__ == "__main__":
    main()
numero = int(input("Ingresa un numero para ver su tabla: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
