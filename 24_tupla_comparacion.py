# ==================================================================
# 24_tupla_comparacion.py
# EJERCICIO: Comparación de tuplas
# ==================================================================
# QUÉ HACE:
#   Dadas dos tuplas numéricas, determina cuál es mayor.
#
# LO MÁS IMPORTANTE:
#   - Python compara tuplas elemento a elemento (orden lexicográfico) y se detiene
#   - en el primer elemento distinto. (3,4,5) vs (3,4,2): 3=3, 4=4, 5>2 -> gana la primera.
#   - Se pueden usar directamente los operadores >, < e ==.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
# t1 = (3, 4, 5)
# t2 = (3, 4, 2)

# VERSIÓN CON input():
t1 = tuple(int(v) for v in input("Primera tupla (ej: 3 4 5): ").split())
t2 = tuple(int(v) for v in input("Segunda tupla (ej: 3 4 2): ").split())

# ---------- LÓGICA ----------
if t1 > t2:
    print("La primera tupla es mayor.")
elif t1 < t2:
    print("La segunda tupla es mayor.")
else:
    print("Las tuplas son iguales.")
