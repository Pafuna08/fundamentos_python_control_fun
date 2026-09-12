"""Compara dos numeros con if, elif y else."""


def comparar_numeros(numero_1, numero_2):
    """Devuelve el resultado de comparar dos numeros."""
    if numero_1 > numero_2:
        return f"El numero mayor es {numero_1}."
    elif numero_2 > numero_1:
        return f"El numero mayor es {numero_2}."
    else:
        return "Los dos numeros son iguales."


def main():
    """Solicita dos numeros y muestra cual es mayor."""
    numero_1 = float(input("Ingresa el primer numero: "))
    numero_2 = float(input("Ingresa el segundo numero: "))
    print(comparar_numeros(numero_1, numero_2))


if __name__ == "__main__":
    main()
numero_1 = float(input("Ingresa el primer numero: "))
numero_2 = float(input("Ingresa el segundo numero: "))

if numero_1 > numero_2:
    print(f"El numero mayor es {numero_1}.")
elif numero_2 > numero_1:
    print(f"El numero mayor es {numero_2}.")
else:
    print("Los dos numeros son iguales.")
