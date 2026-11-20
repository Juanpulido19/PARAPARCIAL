# ==================================================================
# 25_tupla_suma_y_promedio.py
# EJERCICIO: Suma y promedio de una tupla
# ==================================================================
# QUÉ HACE:
#   Dada una tupla de números, calcula su suma y su promedio.
#
# LO MÁS IMPORTANTE:
#   - sum(tupla) suma todos los elementos y len(tupla) los cuenta.
#   - promedio = sum / len.
# ==================================================================

import ast

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta la de input):
# t = (10, 20, 30, 40)

# VERSIÓN CON input():
t = tuple(ast.literal_eval(v) for v in input("Números separados por espacio: ").split())

# ---------- LÓGICA ----------
print("Suma =", sum(t))
print("Promedio =", sum(t) / len(t))
