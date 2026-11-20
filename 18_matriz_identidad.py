# ==================================================================
# 18_matriz_identidad.py
# EJERCICIO: Matriz identidad de tamaño n x n
# ==================================================================
# QUÉ HACE:
#   Dado n, construye la matriz identidad: 1 en la diagonal y 0 en el resto.
#
# LO MÁS IMPORTANTE:
#   - La diagonal es donde fila == columna (i == j).
#   - Expresión condicional: 1 if i == j else 0.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta la de input):
# n = 3

# VERSIÓN CON input():
n = int(input("n = "))

# ---------- LÓGICA ----------
identidad = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(1 if i == j else 0)
    identidad.append(fila)

for fila in identidad:
    print(fila)
