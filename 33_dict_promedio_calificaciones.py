# ==================================================================
# 33_dict_promedio_calificaciones.py
# EJERCICIO: Promedio de calificaciones
# ==================================================================
# QUÉ HACE:
#   Guarda nombre -> nota y calcula el promedio general.
#
# LO MÁS IMPORTANTE:
#   - notas.values() da solo las notas; promedio = sum(...) / len(...).
#   - Se guarda float(nota) para poder calcular.
#   - Se controla el caso de diccionario vacío para evitar división por cero.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta esta línea, comenta TODO el bloque con input y salta a LÓGICA):
# notas = {"Ana": 4.0, "Luis": 3.5, "Sofía": 4.5}

# VERSIÓN CON input():
notas = {}
while True:
    entrada = input("Nombre: nota (o 'fin'): ")
    if entrada.strip().lower() == "fin":
        break
    nombre, _, nota = entrada.partition(":")
    notas[nombre.strip()] = float(nota)

# ---------- LÓGICA ----------
if len(notas) == 0:
    print("No se ingresaron notas")
else:
    print("Promedio general:", sum(notas.values()) / len(notas))
