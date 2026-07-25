numero_1 = float(input("Ingresa el primer numero: "))
numero_2 = float(input("Ingresa el segundo numero: "))

if numero_1 > numero_2:
    print(f"El numero mayor es {numero_1}.")
elif numero_2 > numero_1:
    print(f"El numero mayor es {numero_2}.")
else:
    print("Los dos numeros son iguales.")
