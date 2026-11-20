# ==================================================================
# 31_dict_agenda_telefonica.py
# EJERCICIO: Agenda telefónica
# ==================================================================
# QUÉ HACE:
#   Pide nombres y teléfonos y los guarda en un diccionario hasta escribir 'fin'.
#
# LO MÁS IMPORTANTE:
#   - Clave = nombre, valor = teléfono.
#   - while True + break cuando el usuario escribe 'fin'.
#   - partition('-') separa 'Juan - 123' en nombre y teléfono; strip() quita espacios.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea, comenta TODO el bloque con input y salta a LÓGICA):
# agenda = {"Juan": "123", "Ana": "456"}

# VERSIÓN CON input():
agenda = {}
while True:
    entrada = input("Nombre - teléfono (o 'fin'): ")
    if entrada.strip().lower() == "fin":
        break
    nombre, _, telefono = entrada.partition("-")
    agenda[nombre.strip()] = telefono.strip()

# ---------- LÓGICA ----------
print(agenda)
