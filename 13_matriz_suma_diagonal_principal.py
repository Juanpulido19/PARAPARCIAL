# ==================================================================
# 13_matriz_suma_diagonal_principal.py
# EJERCICIO: Suma de la diagonal principal
# ==================================================================
# QUÉ HACE:
#   Lee una matriz cuadrada, la imprime y calcula la suma de su diagonal principal.
#   Si no es cuadrada, muestra un mensaje de error.
#
# LO MÁS IMPORTANTE:
#   - La diagonal principal son los elementos donde fila == columna: M[i][i].
#   - Por eso basta UN solo for (no hace falta doble for).
#   - Validación: número de filas == número de columnas.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta TODO el bloque con input):
# M = [[1, 2], [3, 4]]

# VERSIÓN CON input():
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))
M = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(float(input(f"M[{i}][{j}]: ")))
    M.append(fila)

# ---------- LÓGICA ----------
if len(M) != len(M[0]):
    print("Error: la matriz no es cuadrada")
else:
    suma = 0
    for i in range(len(M)):
        suma += M[i][i]

    print("Matriz:")
    for fila in M:
        for x in fila:
            print(f"{x:8.2f}", end="")
        print()
    print("Suma de la diagonal principal:", suma)
