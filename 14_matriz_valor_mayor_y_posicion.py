# ==================================================================
# 14_matriz_valor_mayor_y_posicion.py
# EJERCICIO: Mayor valor de una matriz y su posición
# ==================================================================
# QUÉ HACE:
#   Lee una matriz n x m, imprime la matriz, el valor máximo y la posición
#   (fila X, columna Y) donde aparece por primera vez.
#
# LO MÁS IMPORTANTE:
#   - Patrón 'mayor hasta ahora': se parte de M[0][0] y se recorre todo con doble for.
#   - Se usa > ESTRICTO (no >=): así, si el máximo se repite, se conserva la PRIMERA posición.
#   - Las posiciones se cuentan desde 0 (fila 0, columna 0 es la esquina superior izquierda).
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta TODO el bloque con input):
# M = [[1, 9, 3], [9, 2, 4]]

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
mayor = M[0][0]
pos_fila = 0
pos_columna = 0
for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] > mayor:
            mayor = M[i][j]
            pos_fila = i
            pos_columna = j

print("Matriz:")
for fila in M:
    for x in fila:
        print(f"{x:8.2f}", end="")
    print()
print("Valor máximo:", mayor)
print(f"Posición: fila {pos_fila}, columna {pos_columna}")
