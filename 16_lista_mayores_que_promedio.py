# ==================================================================
# 16_lista_mayores_que_promedio.py
# EJERCICIO: Números mayores que el promedio
# ==================================================================
# QUÉ HACE:
#   Lee una lista de números y muestra el promedio y los que lo superan.
#
# LO MÁS IMPORTANTE:
#   - promedio = sum(lista) / len(lista).
#   - Comprensión de listas: [x for x in lista if x > promedio] filtra.
#   - ast.literal_eval convierte '10' en int y '2.5' en float según corresponda.
#   - sorted() solo sirve para igualar la salida del enunciado; si no piden orden, quítalo.
# ==================================================================

import ast

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta la de input):
# numeros = [10, 5, 8, 3, 9]

# VERSIÓN CON input():
numeros = [ast.literal_eval(x) for x in input("Números separados por espacio: ").split()]

# ---------- LÓGICA ----------
promedio = sum(numeros) / len(numeros)
mayores = sorted([x for x in numeros if x > promedio])
print("Promedio:", promedio)
print("Mayores que el promedio:", mayores)
