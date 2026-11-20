# ==================================================================
# 32_dict_contador_palabras.py
# EJERCICIO: Contador de palabras
# ==================================================================
# QUÉ HACE:
#   Cuenta cuántas veces aparece cada palabra de una frase.
#
# LO MÁS IMPORTANTE:
#   - Diccionario donde clave = palabra y valor = frecuencia.
#   - Si la palabra ya existe se suma 1; si no, se crea con valor 1.
#   - Atajo: conteo[p] = conteo.get(p, 0) + 1 (get devuelve 0 si no existe).
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta la de input):
# frase = "hola mundo hola"

# VERSIÓN CON input():
frase = input("Frase: ")

# ---------- LÓGICA ----------
conteo = {}
for palabra in frase.split():
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
print(conteo)
