# ==================================================================
# 23_tupla_empaquetar_desempaquetar.py
# EJERCICIO: Empaquetar y desempaquetar datos en una tupla
# ==================================================================
# QUÉ HACE:
#   Guarda (nombre, edad, país) en una tupla y muestra cada dato por separado.
#
# LO MÁS IMPORTANTE:
#   - Empaquetar: datos = (a, b, c).
#   - Desempaquetar: nombre, edad, pais = datos (el orden importa y la cantidad
#   - de variables debe coincidir con la de elementos).
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea y comenta TODO el bloque con input):
# datos = ("Ana", 23, "Colombia")

# VERSIÓN CON input():
nombre_in = input("Nombre: ")
edad_in = int(input("Edad: "))
pais_in = input("País: ")
datos = (nombre_in, edad_in, pais_in)      # empaquetar

# ---------- LÓGICA ----------
nombre, edad, pais = datos                 # desempaquetar
print("Nombre:", nombre)
print("Edad:", edad)
print("País:", pais)
