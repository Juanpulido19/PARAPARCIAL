# ==================================================================
# 21_tupla_sin_duplicados.py
# EJERCICIO: Lista a tupla sin duplicados
# ==================================================================
# QUÉ HACE:
#   Convierte una lista de elementos en una tupla sin repetidos.
#
# LO MÁS IMPORTANTE:
#   - set() elimina duplicados y tuple() lo vuelve tupla.
#   - CUIDADO: un set NO conserva el orden. Si piden mantener el orden usa
#   - tuple(dict.fromkeys(lista)).
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta la de input):
# lista = ["rojo", "azul", "rojo", "verde"]

# VERSIÓN CON input():
lista = input("Elementos separados por espacio: ").split()

# ---------- LÓGICA ----------
sin_duplicados = tuple(set(lista))
print(sin_duplicados)

# Versión que conserva el orden original:
# print(tuple(dict.fromkeys(lista)))
