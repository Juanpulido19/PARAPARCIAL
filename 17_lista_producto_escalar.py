# ==================================================================
# 17_lista_producto_escalar.py
# EJERCICIO: Producto escalar de dos listas
# ==================================================================
# QUÉ HACE:
#   Dadas dos listas del mismo tamaño, calcula su producto escalar.
#
# LO MÁS IMPORTANTE:
#   - Se multiplica posición por posición y se acumulan los resultados.
#   - Ejemplo: [1,2,3] . [4,5,6] = 1*4 + 2*5 + 3*6 = 32.
#   - Validar que tengan la misma longitud antes de calcular.
# ==================================================================

import ast

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
# A = [1, 2, 3]
# B = [4, 5, 6]

# VERSIÓN CON input():
A = [ast.literal_eval(x) for x in input("Lista A: ").split()]
B = [ast.literal_eval(x) for x in input("Lista B: ").split()]

# ---------- LÓGICA ----------
if len(A) != len(B):
    print("Error: las listas deben tener el mismo tamaño")
else:
    total = 0
    for i in range(len(A)):
        total += A[i] * B[i]
    print("Producto escalar =", total)
