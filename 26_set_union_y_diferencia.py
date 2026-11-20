# ==================================================================
# 26_set_union_y_diferencia.py
# EJERCICIO: Unión y diferencia entre conjuntos
# ==================================================================
# QUÉ HACE:
#   Dados dos conjuntos A y B, muestra su unión y la diferencia A - B.
#
# LO MÁS IMPORTANTE:
#   - Unión: A | B (todos los elementos, sin repetir).
#   - Diferencia: A - B (lo que está en A pero NO en B). Importa el orden: A-B != B-A.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
# A = {1, 2, 3}
# B = {3, 4, 5}

# VERSIÓN CON input():
A = set(int(v) for v in input("Conjunto A (ej: 1 2 3): ").split())
B = set(int(v) for v in input("Conjunto B (ej: 3 4 5): ").split())

# ---------- LÓGICA ----------
print("Unión:", A | B)
print("Diferencia:", A - B)
