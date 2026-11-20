# ==================================================================
# 12_matriz_transpuesta_nxm.py
# EJERCICIO: Matriz transpuesta (n x m)
# ==================================================================
# QUÉ HACE:
#   Lee una matriz n x m (no tiene que ser cuadrada) e imprime la original
#   y su transpuesta (m x n).
#
# LO MÁS IMPORTANTE:
#   - Transponer = intercambiar filas por columnas: T[j][i] = M[i][j].
#   - Los bucles van 'invertidos': el externo recorre las COLUMNAS (j) y el
#   - interno las FILAS (i), tomando M[i][j].
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta TODO el bloque con input):
# M = [[1, 2, 3], [4, 5, 6]]

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
n = len(M)        # filas de la original
m = len(M[0])     # columnas de la original

T = []
for j in range(m):          # la transpuesta tiene m filas
    fila = []
    for i in range(n):      # y n columnas
        fila.append(M[i][j])
    T.append(fila)

print("Matriz original:")
for fila in M:
    for x in fila:
        print(f"{x:8.2f}", end="")
    print()

print("Matriz transpuesta:")
for fila in T:
    for x in fila:
        print(f"{x:8.2f}", end="")
    print()
