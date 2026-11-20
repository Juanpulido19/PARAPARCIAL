# ==================================================================
# 28_set_pares_comunes.py
# EJERCICIO: Intersección de números pares
# ==================================================================
# QUÉ HACE:
#   Dadas dos listas de números, muestra los pares que están en ambas.
#
# LO MÁS IMPORTANTE:
#   - Se convierten a set y se usa & (intersección) para los comunes.
#   - Luego se filtran los pares con x % 2 == 0.
# ==================================================================

import ast

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
# A = [2, 4, 6, 8]
# B = [4, 5, 6, 9]

# VERSIÓN CON input():
A = [ast.literal_eval(v) for v in input("Lista A (ej: 2 4 6 8): ").split()]
B = [ast.literal_eval(v) for v in input("Lista B (ej: 4 5 6 9): ").split()]

# ---------- LÓGICA ----------
comunes = set(A) & set(B)
pares_comunes = {x for x in comunes if x % 2 == 0}
print(pares_comunes)
