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
