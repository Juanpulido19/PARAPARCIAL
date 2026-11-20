# ==================================================================
# 19_suma_matrices_listas.py
# EJERCICIO: Suma de dos matrices (listas de listas)
# ==================================================================
# QUÉ HACE:
#   Dadas dos matrices del mismo tamaño, calcula su suma elemento a elemento.
#
# LO MÁS IMPORTANTE:
#   - Cada posición (i, j) de la resultante es A[i][j] + B[i][j].
#   - Las matrices se ingresan escritas como en Python: [[1, 2], [3, 4]]
#   - (ast.literal_eval las convierte de texto a lista de listas).
# ==================================================================

import ast

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# VERSIÓN CON input():
A = ast.literal_eval(input("Matriz A (ej: [[1, 2], [3, 4]]): "))
B = ast.literal_eval(input("Matriz B (ej: [[5, 6], [7, 8]]): "))

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
    print(C)
