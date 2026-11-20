# ==================================================================
# 20_transposicion_matriz_listas.py
# EJERCICIO: Transposición de una matriz (listas de listas)
# ==================================================================
# QUÉ HACE:
#   Genera la matriz transpuesta de una matriz ingresada por el usuario.
#
# LO MÁS IMPORTANTE:
#   - A[i][j] pasa a T[j][i]: las columnas de A son las filas de T.
#   - Bucle externo sobre columnas (j), interno sobre filas (i).
#   - Se ingresa como texto de Python: [[1, 2, 3], [4, 5, 6]].
# ==================================================================

import ast

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta la de input):
# A = [[1, 2, 3], [4, 5, 6]]

# VERSIÓN CON input():
A = ast.literal_eval(input("Matriz (ej: [[1, 2, 3], [4, 5, 6]]): "))

# ---------- LÓGICA ----------
T = []
for j in range(len(A[0])):
    fila = []
    for i in range(len(A)):
        fila.append(A[i][j])
    T.append(fila)
print(T)
