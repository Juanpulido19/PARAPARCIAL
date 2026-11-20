# ==================================================================
# 34_dict_invertido.py
# EJERCICIO: Diccionario invertido (valor -> clave)
# ==================================================================
# QUÉ HACE:
#   Invierte un diccionario clave -> valor a valor -> clave.
#
# LO MÁS IMPORTANTE:
#   - Comprensión de diccionarios: {v: k for k, v in dic.items()}.
#   - items() entrega pares (clave, valor).
#   - CUIDADO: si hay valores repetidos se pierden claves (las claves no se duplican).
# ==================================================================

import ast

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta la de input):
# dic = {"a": 1, "b": 2, "c": 3}

# VERSIÓN CON input():
dic = ast.literal_eval(input("Diccionario (ej: {'a': 1, 'b': 2}): "))

# ---------- LÓGICA ----------
invertido = {v: k for k, v in dic.items()}
print(invertido)
