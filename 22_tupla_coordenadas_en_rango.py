# ==================================================================
# 22_tupla_coordenadas_en_rango.py
# EJERCICIO: Coordenadas dentro de un rango
# ==================================================================
# QUÉ HACE:
#   Dada una coordenada (x, y) en una tupla, verifica si está dentro de un rango.
#
# LO MÁS IMPORTANTE:
#   - Se desempaqueta la tupla: x, y = coordenada.
#   - Comparación encadenada: minimo <= x <= maximo (válida en Python).
#   - Ambas coordenadas deben cumplir el rango (and).
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
# coordenada = (4, 6)
# minimo, maximo = 0, 10

# VERSIÓN CON input():
coordenada = tuple(int(v) for v in input("Coordenada x y (ej: 4 6): ").split())
minimo, maximo = (int(v) for v in input("Rango mínimo y máximo (ej: 0 10): ").split())

# ---------- LÓGICA ----------
x, y = coordenada
if minimo <= x <= maximo and minimo <= y <= maximo:
    print("Dentro del rango")
else:
    print("Fuera del rango")
