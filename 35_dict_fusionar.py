# ==================================================================
# 35_dict_fusionar.py
# EJERCICIO: Fusionar dos diccionarios
# ==================================================================
# QUÉ HACE:
#   Combina dos diccionarios en uno. Si hay claves repetidas, el segundo
#   sobrescribe al primero.
#
# LO MÁS IMPORTANTE:
#   - Operador A | B (Python 3.9+) crea uno NUEVO; el de la derecha gana en repetidas.
#   - A.update(B) hace lo mismo pero MODIFICA A (no crea uno nuevo).
#   - Alternativa para versiones viejas: {**A, **B}.
# ==================================================================

import ast

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
# A = {"x": 1, "y": 2}
# B = {"y": 10, "z": 3}

# VERSIÓN CON input():
A = ast.literal_eval(input("Diccionario A (ej: {'x': 1, 'y': 2}): "))
B = ast.literal_eval(input("Diccionario B (ej: {'y': 10, 'z': 3}): "))

# ---------- LÓGICA ----------
fusion = A | B          # alternativa: {**A, **B}
print(fusion)
