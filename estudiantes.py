
def leer_calificacion(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 100:
                return nota
            print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Ingresa un número válido.")


print(" SISTEMA DE CALIFICACIONES ")

estudiantes = int(input("Cantidad de estudiantes: "))
materias = int(input("Cantidad de materias: "))

matriz = []

for i in range(estudiantes):
    fila = []
    print(f"\nEstudiante {i + 1}")

    for j in range(materias):
        nota = leer_calificacion(
            f"Calificación de materia {j + 1}: "
        )
        fila.append(nota)

    matriz.append(fila)

print("\nPROMEDIO POR ESTUDIANTE")

for i in range(estudiantes):
    promedio = sum(matriz[i]) / materias
    print(f"Estudiante {i + 1}: {promedio:.2f}")

print("\nPROMEDIO POR MATERIA")

for j in range(materias):
    promedio = sum(matriz[i][j] for i in range(estudiantes)) / estudiantes
    print(f"Materia {j + 1}: {promedio:.2f}")

todas = [nota for fila in matriz for nota in fila]

print("\nRESULTADOS GENERALES")
print("Calificación más alta:", max(todas))
print("Calificación más baja:", min(todas))
