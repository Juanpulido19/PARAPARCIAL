# ==================================================================
# 15_matriz_multiplicar_por_escalar.py
# EJERCICIO: Multiplicar una matriz por un escalar
# ==================================================================
# QUÉ HACE:
#   Lee una matriz n x m (validando que cada valor sea numérico) y un escalar,
#   e imprime la matriz original y el resultado de multiplicar cada elemento.
#
# LO MÁS IMPORTANTE:
#   - Cada elemento se multiplica por el escalar y se guarda en una matriz NUEVA.
#   - El escalar puede ser positivo, negativo, cero o decimal.
#   - try/except ValueError + while True: si float() falla, se vuelve a pedir el dato.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta TODO el bloque con input):
# M = [[1, 2], [3, 4]]
# escalar = 2

# VERSIÓN CON input():
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))
M = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        while True:
            try:
                valor = float(input(f"M[{i}][{j}]: "))
                break
            except ValueError:
                print("Debe ser un número, intente de nuevo")
        fila.append(valor)
    M.append(fila)

while True:
    try:
        escalar = float(input("Escalar: "))
        break
    except ValueError:
        print("Debe ser un número, intente de nuevo")

# ---------- LÓGICA ----------
R = []
for i in range(len(M)):
    fila = []
    for j in range(len(M[0])):
        fila.append(M[i][j] * escalar)
    R.append(fila)

print("Matriz original:")
for fila in M:
    for x in fila:
        print(f"{x:8.2f}", end="")
    print()

print("Matriz resultante:")
for fila in R:
    for x in fila:
        print(f"{x:8.2f}", end="")
    print()
