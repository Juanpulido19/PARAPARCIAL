# ==================================================================
# 11_matrices_suma_con_validacion.py
# EJERCICIO: Suma de dos matrices (valida dimensiones)
# ==================================================================
# QUÉ HACE:
#   Lee dos matrices, verifica que tengan las mismas dimensiones y,
#   si coinciden, imprime la suma elemento a elemento (A[i][j] + B[i][j]).
#   Sin funciones propias ni numpy (regla del enunciado).
#
# LO MÁS IMPORTANTE:
#   - Una matriz es una lista de listas: matriz[fila][columna].
#   - Para leer: un for externo crea cada fila y uno interno llena sus columnas.
#   - Validación: len(A) = filas, len(A[0]) = columnas. Si difieren, mensaje de error.
#   - f'{x:8.2f}' reserva 8 espacios por número: las columnas quedan alineadas.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta TODO el bloque con input):
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# VERSIÓN CON input():
print("Matriz A")
filas_a = int(input("Número de filas de A: "))
columnas_a = int(input("Número de columnas de A: "))
A = []
for i in range(filas_a):
    fila = []
    for j in range(columnas_a):
        fila.append(float(input(f"A[{i}][{j}]: ")))
    A.append(fila)

print("Matriz B")
filas_b = int(input("Número de filas de B: "))
columnas_b = int(input("Número de columnas de B: "))
B = []
for i in range(filas_b):
    fila = []
    for j in range(columnas_b):
        fila.append(float(input(f"B[{i}][{j}]: ")))
    B.append(fila)

# ---------- LÓGICA ----------
if len(A) != len(B) or len(A[0]) != len(B[0]):
    print("Error: las dimensiones no coinciden")
else:
    C = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)

    print("Matriz resultante A + B:")
    for fila in C:
        for x in fila:
            print(f"{x:8.2f}", end="")
        print()
