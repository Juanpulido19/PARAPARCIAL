# ==================================================================
# 29_set_diferencia_simetrica.py
# EJERCICIO: Diferencia simétrica de dos conjuntos
# ==================================================================
# QUÉ HACE:
#   Muestra los elementos que están en uno de los conjuntos pero no en ambos.
#
# LO MÁS IMPORTANTE:
#   - Operador ^ o método A.symmetric_difference(B).
#   - Equivale a (A | B) - (A & B).
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
# A = {1, 2, 3}
# B = {3, 4, 5}

# VERSIÓN CON input():
A = set(int(v) for v in input("Conjunto A (ej: 1 2 3): ").split())
B = set(int(v) for v in input("Conjunto B (ej: 3 4 5): ").split())

# ---------- LÓGICA ----------
print(A ^ B)
