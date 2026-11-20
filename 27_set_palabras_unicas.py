# ==================================================================
# 27_set_palabras_unicas.py
# EJERCICIO: Palabras únicas de una frase
# ==================================================================
# QUÉ HACE:
#   Dada una frase, muestra sus palabras sin repetir.
#
# LO MÁS IMPORTANTE:
#   - split() separa la frase en palabras y set() elimina las repetidas.
#   - El set no garantiza orden.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta la de input):
# frase = "hola mundo hola python"

# VERSIÓN CON input():
frase = input("Frase: ")

# ---------- LÓGICA ----------
print(set(frase.split()))
